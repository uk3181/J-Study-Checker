# 학습 분석 기능과 관련된 각종 함수가 포함된 모듈

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import datetime as dt
from user import *
from math import ceil
from numpy import linspace

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

def getStudyingTimePerDaysList(user: User, dayCount: int) -> list[float]: # 하루 당 총 학습 시간 리스트를 반환해주는 함수
    studyDataList: list[StudyData] = user.getStudyDataList()
    studyingTimePerDaysList: list[float] = [0.0 for _ in range(dayCount)] # 하루 당 총 학습 시간 리스트
    breakLoop: bool = False
    for i in range(len(studyDataList) - 1, -1, -1):
        studyingTimeList: list[list[dt.datetime]] = studyDataList[i].getStudyingTimeList()
        for j in range(len(studyingTimeList)):
            startStudyingTime: dt.datetime = studyingTimeList[j][0] # 학습 시작 시간
            endStudyingTime: dt.datetime = studyingTimeList[j][1] # 학습 종료 시간

            dayGap: int = (dt.datetime.now().date() - startStudyingTime.date()).days
            if startStudyingTime.weekday() == endStudyingTime.weekday():
                if dayGap > dayCount - 1:
                    breakLoop = True
                    break
                studyingTimePerDaysList[dayGap] += (endStudyingTime - startStudyingTime).total_seconds() / 3600
            else:
                if dayGap > dayCount:
                    breakLoop = True
                    break
                studyingTimePerDaysList[dayGap - 1] += (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second) / 3600
                if dayGap < dayCount:
                    studyingTimePerDaysList[dayGap] += ((endStudyingTime - startStudyingTime).total_seconds()\
                            - (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second)) / 3600
        if breakLoop:
            break
    studyingTimePerDaysList.reverse()
    return studyingTimePerDaysList

def getStudyingTimePerSubjectsDict(user: User, dayCount: int) -> dict: # 과목 당 총 학습 시간 딕셔너리를 반환해주는 함수
    def addStudyingTimePerSubjects(studyingTimePerSubjectsDict: dict, subject: str, studyingTime: int) -> None:
        try:
            studyingTimePerSubjectsDict[subject] += studyingTime
        except KeyError:
            studyingTimePerSubjectsDict[subject] = studyingTime

    studyDataList: list[StudyData] = user.getStudyDataList()
    studyingTimePerSubjectsDict: dict = dict()
    breakLoop: bool = False
    for i in range(len(studyDataList) - 1, -1, -1):
        subject: str = studyDataList[i].getSubject()
        studyingTimeList: list[list[dt.datetime]] = studyDataList[i].getStudyingTimeList()
        for j in range(len(studyingTimeList)):
            startStudyingTime: dt.datetime = studyingTimeList[j][0] # 학습 시작 시간
            endStudyingTime: dt.datetime = studyingTimeList[j][1] # 학습 종료 시간

            dayGap: int = (dt.datetime.now().date() - startStudyingTime.date()).days
            if startStudyingTime.weekday() == endStudyingTime.weekday():
                if dayGap > dayCount - 1:
                    breakLoop = True
                    break
                studyingTime: int = (endStudyingTime - startStudyingTime).total_seconds() / 3600
                addStudyingTimePerSubjects(studyingTimePerSubjectsDict, subject, studyingTime)
            else:
                if dayGap > dayCount:
                    breakLoop = True
                    break
                studyingTime: int = (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second) / 3600
                if dayGap < dayCount:
                    studyingTime += ((endStudyingTime - startStudyingTime).total_seconds()\
                            - (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second)) / 3600
                addStudyingTimePerSubjects(studyingTimePerSubjectsDict, subject, studyingTime)
        if breakLoop:
            break
    return studyingTimePerSubjectsDict

def getBreakTimePerDaysList(user: User, dayCount: int) -> list[float]: # 하루 당 총 휴식 시간 리스트를 반환해주는 함수
    breakTimePerDaysList: list[float] = [0.0 for _ in range(dayCount)]
    studyDataList: list[StudyData] = user.getStudyDataList()
    breakLoop: bool = False
    for i in range(len(studyDataList) - 1, -1, -1):
        studyingTimeList: list[list[dt.datetime]] = studyDataList[i].getStudyingTimeList()
        if len(studyingTimeList) >= 2:
            for j in range(1, len(studyingTimeList), 1):
                previousEndStudyingTime: dt.datetime = studyingTimeList[j - 1][1] # 휴식 전 학습 종료 시간
                nextStartStudyingTime: dt.datetime = studyingTimeList[j][0] # 휴식 후 학습 시작 시간

                dayGap: int = (dt.datetime.now().date() - previousEndStudyingTime.date()).days
                if previousEndStudyingTime.weekday() == nextStartStudyingTime.weekday():
                    if dayGap > dayCount - 1:
                        breakLoop = True
                        break
                    breakTimePerDaysList[dayGap] += (nextStartStudyingTime - previousEndStudyingTime).total_seconds() / 3600
                else:
                    if dayGap > dayCount:
                        breakLoop = True
                        break
                    breakTimePerDaysList[dayGap - 1] += (nextStartStudyingTime.hour * 3600 + nextStartStudyingTime.minute * 60 + nextStartStudyingTime.second) / 3600
                    if dayGap < dayCount:
                        breakTimePerDaysList[dayGap] += ((nextStartStudyingTime - previousEndStudyingTime).total_seconds()\
                                - (nextStartStudyingTime.hour * 3600 + nextStartStudyingTime.minute * 60 + nextStartStudyingTime.second)) / 3600
        if breakLoop:
            break
    breakTimePerDaysList.reverse()
    return breakTimePerDaysList

def getBreakTimePerSubjectsDict(user: User, dayCount: int) -> dict: # 과목 당 총 학습 시간 딕셔너리를 반환해주는 함수
    def addBreakTimePerSubjects(breakTimePerSubjectsDict: dict, subject: str, breakTime: int) -> None:
        try:
            breakTimePerSubjectsDict[subject] += breakTime
        except KeyError:
            breakTimePerSubjectsDict[subject] = breakTime

    studyTimePerSubjectsDict: dict = getStudyingTimePerSubjectsDict(user, dayCount)
    breakTimePerSubjectsDict: dict = dict()
    studyDataList: list[StudyData] = user.getStudyDataList()
    breakLoop: bool = False
    for i in range(len(studyDataList) - 1, -1, -1):
        subject: str = studyDataList[i].getSubject()
        studyingTimeList: list[list[dt.datetime]] = studyDataList[i].getStudyingTimeList()
        if len(studyingTimeList) >= 2:
            for j in range(1, len(studyingTimeList), 1):
                previousEndStudyingTime: dt.datetime = studyingTimeList[j - 1][1] # 휴식 전 학습 종료 시간
                nextStartStudyingTime: dt.datetime = studyingTimeList[j][0] # 휴식 후 학습 시작 시간

                dayGap: int = (dt.datetime.now().date() - previousEndStudyingTime.date()).days
                if previousEndStudyingTime.weekday() == nextStartStudyingTime.weekday():
                    if dayGap > dayCount - 1:
                        breakLoop = True
                        break
                    breakTime: int = (nextStartStudyingTime - previousEndStudyingTime).total_seconds() / 3600
                    addBreakTimePerSubjects(breakTimePerSubjectsDict, subject, breakTime)
                else:
                    if dayGap > dayCount:
                        breakLoop = True
                        break
                    breakTime: int = (nextStartStudyingTime.hour * 3600 + nextStartStudyingTime.minute * 60 + nextStartStudyingTime.second) / 3600
                    if dayGap < dayCount:
                        breakTime += ((nextStartStudyingTime - previousEndStudyingTime).total_seconds()\
                                - (nextStartStudyingTime.hour * 3600 + nextStartStudyingTime.minute * 60 + nextStartStudyingTime.second)) / 3600
                    addBreakTimePerSubjects(breakTimePerSubjectsDict, subject, breakTime)
        if breakLoop:
            break
    for subject in studyTimePerSubjectsDict:
        if not (subject in breakTimePerSubjectsDict):
            addBreakTimePerSubjects(breakTimePerSubjectsDict, subject, 0)
    return breakTimePerSubjectsDict

def getFocusRatePerDaysList(user: User, dayCount: int) -> list[float]: # 하루 당 평균 집중도 리스트를 반환해주는 함수
    studyingTimePerDaysList: list[float] = getStudyingTimePerDaysList(user, dayCount)
    breakTimePerDaysList: list[float] = getBreakTimePerDaysList(user, dayCount)
    focusRatePerDaysList: list[float] = [0.0 for _ in range(dayCount)]
    for i in range(len(studyingTimePerDaysList)):
        if studyingTimePerDaysList[i] + breakTimePerDaysList[i] == 0:
            focusRatePerDaysList[i] = 0
        else:
            focusRatePerDaysList[i] = studyingTimePerDaysList[i] / (studyingTimePerDaysList[i] + breakTimePerDaysList[i]) * 100
    return focusRatePerDaysList

def getFocusRatePerSubjectsDict(user: User, dayCount: int) -> dict: # 과목 당 평균 집중도 리스트를 반환해주는 함수
    studyingTimePerSubjectsDict: dict = getStudyingTimePerSubjectsDict(user, dayCount)
    breakTimePerSubjectsDict: dict = getBreakTimePerSubjectsDict(user, dayCount)
    focusRatePerSubjectsDict: dict = dict()
    for subject in studyingTimePerSubjectsDict:
        if subject in breakTimePerSubjectsDict:
            if studyingTimePerSubjectsDict[subject] + breakTimePerSubjectsDict[subject] == 0:
                focusRatePerSubjectsDict[subject] = 0
            else:
                focusRatePerSubjectsDict[subject] = studyingTimePerSubjectsDict[subject]\
                        / (studyingTimePerSubjectsDict[subject] + breakTimePerSubjectsDict[subject]) * 100
        else:
            focusRatePerSubjectsDict[subject] = 100
    for subject in breakTimePerSubjectsDict:
        if not (subject in studyingTimePerSubjectsDict):
            focusRatePerSubjectsDict[subject] = 0
    return focusRatePerSubjectsDict

def makeGraphOfStudyingTimePerDays(user: User, graphFigSize: tuple[float], graphDpi: int,\
        dayCount: int = 7, shape: str = 'normal') -> None: # 지정 날짜동안 학습 시간 그래프를 그려주는 함수
    fontPath: str = '{}/Fonts/NanumGothic/NanumGothicBold.ttf'.format(path)
    fm.fontManager.addfont(fontPath)
    plt.rcParams['font.family'] = (fm.FontProperties(fname = fontPath)).get_name()
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = graphFigSize, dpi = graphDpi, facecolor = '#F0F7FF')
    plt.gca().set_facecolor('#FAFCFF')

    plt.title('{}일간 학습 시간'.format(dayCount), fontsize = 13)

    studyingTimePerDaysList: list[float] = getStudyingTimePerDaysList(user, dayCount) # 하루 당 총 학습 시간 리스트

    xTicks: list[int] = []; xLabels: list[str] = []
    if dayCount <= 7:
        xTicks: list[int] = [i for i in range(dayCount)]
    elif dayCount <= 20:
        xTicks: list[int] = linspace(0, dayCount - 1, 3, dtype = int)
    elif dayCount <= 30:
        xTicks: list[int] = linspace(0, dayCount - 1, 4, dtype = int)
    else:
        xTicks: list[int] = linspace(0, dayCount - 1, 5, dtype = int)
    xLabels: list[str] = ['{}일 전'.format(dayCount - xTick - 1) for xTick in xTicks]
    xLabels[len(xLabels) - 1] = '오늘'
    plt.xticks(ticks = xTicks, labels = xLabels, fontsize = 8)

    yTicks: list[int] = []; yLabels: list[str] = []
    start = 0; stop = 0; step = 0
    if max(studyingTimePerDaysList) <= 1:
        stop = 2; step = 1
    elif max(studyingTimePerDaysList) <= 2:
        stop = 3; step = 1
    else:
        step = ceil(max(studyingTimePerDaysList) / 3); stop = step * 4
    for i in range(start, stop, step):
        yTicks.append(i)
        yLabels.append('{}시간'.format(i))
    plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 8)
    plt.ylim(0, stop - step)
    plt.grid(axis = 'y', linestyle = ':')
    
    if shape == 'bar':
        plt.bar([i for i in range(dayCount)], studyingTimePerDaysList, color = '#00F7CF')
    else:
        plt.plot(studyingTimePerDaysList, color = '#00F7CF', linewidth = 0.5, markersize = 4)
        plt.fill_between([i for i in range(dayCount)], studyingTimePerDaysList, color = '#00F7CF', alpha = 0.55)

    plt.savefig('{}/Images/Graphs/studying_time_per_days_graph.png'.format(path))
    plt.close()

def makeGraphOfStudyingTimePerSubjects(user: User, graphFigSize: tuple[float],\
        graphDpi: int, dayCount: int = 7) -> None: # 지정 날짜동안 과목별 학습 시간 그래프를 그려주는 함수
    fontPath: str = '{}/Fonts/NanumGothic/NanumGothicBold.ttf'.format(path)
    fm.fontManager.addfont(fontPath)
    plt.rcParams['font.family'] = (fm.FontProperties(fname = fontPath)).get_name()
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = graphFigSize, dpi = graphDpi, facecolor = '#F0F7FF')
    plt.gca().set_facecolor('#FAFCFF')

    studyingTimePerSubjectsDict: dict = getStudyingTimePerSubjectsDict(user, dayCount) # 과목별 총 학습 시간 딕셔너리
    if len(studyingTimePerSubjectsDict) == 0:
        plt.text(0.5, 0.5, '{}일간 학습한 과목이 없습니다.'.format(dayCount), fontsize = 11, ha = 'center', va = 'center')
        plt.axis('off')
        plt.savefig('{}/Images/Graphs/studying_time_per_subjects_graph.png'.format(path))
        plt.close()
        return

    plt.title('{}일간 과목별 학습 시간'.format(dayCount), fontsize = 13)

    sortedDatas: dict = dict(sorted(studyingTimePerSubjectsDict.items(), key = lambda item: item[1], reverse = True))
    topDatas: dict = dict(); otherDatas: float = 0.0
    if len(sortedDatas) <= 5:
        topDatas = dict(list(sortedDatas.items()))
    else:
        topDatas = dict(list(sortedDatas.items())[:4])
        otherDatas: float = sum(list(sortedDatas.values())[4:])
    if len(sortedDatas) > 5:
        topDatas['기타'] = otherDatas

    plt.xticks(fontsize = 8)

    yTicks: list[int] = []; yLabels: list[str] = []
    start = 0; stop = 0; step = 0
    if max(topDatas.values()) <= 1:
        stop = 2; step = 1
    elif max(topDatas.values()) <= 2:
        stop = 3; step = 1
    else:
        step = ceil(max(topDatas.values()) / 3); stop = step * 4
    for i in range(start, stop, step):
        yTicks.append(i)
        yLabels.append('{}시간'.format(i))
    plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 8)
    plt.ylim(0, stop - step)
    plt.grid(axis = 'y', linestyle = ':')

    keyList: list[str] = []
    for key in topDatas.keys():
        if len(key) > 5: # 과목명이 길 경우, 두 줄로 처리함. (과목명 최대 10자)
            keyList.append(key[:5].strip() + '\n' + key[5:].strip())
        else:
            keyList.append(key.strip())
    plt.bar(keyList, topDatas.values(), color = '#00F7CF')
    
    plt.savefig('{}/Images/Graphs/studying_time_per_subjects_graph.png'.format(path))
    plt.close()

def makeGraphOfBreakTimePerDays(user: User, graphFigSize: tuple[float], graphDpi: int,\
        dayCount: int = 7, shape: str = 'normal') -> None: # 지정 날짜동안 휴식 시간 그래프를 그려주는 함수
    fontPath: str = '{}/Fonts/NanumGothic/NanumGothicBold.ttf'.format(path)
    fm.fontManager.addfont(fontPath)
    plt.rcParams['font.family'] = (fm.FontProperties(fname = fontPath)).get_name()
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = graphFigSize, dpi = graphDpi, facecolor = '#F0F7FF')
    plt.gca().set_facecolor('#FAFCFF')

    plt.title('{}일간 휴식 시간'.format(dayCount), fontsize = 13)

    breakTimePerDaysList: list[float] = getBreakTimePerDaysList(user, dayCount) # 하루 당 총 휴식 시간 리스트

    xTicks: list[int] = []; xLabels: list[str] = []
    if dayCount <= 7:
        xTicks: list[int] = [i for i in range(dayCount)]
    elif dayCount <= 20:
        xTicks: list[int] = linspace(0, dayCount - 1, 3, dtype = int)
    elif dayCount <= 30:
        xTicks: list[int] = linspace(0, dayCount - 1, 4, dtype = int)
    else:
        xTicks: list[int] = linspace(0, dayCount - 1, 5, dtype = int)
    xLabels: list[str] = ['{}일 전'.format(dayCount - xTick - 1) for xTick in xTicks]
    xLabels[len(xLabels) - 1] = '오늘'
    plt.xticks(ticks = xTicks, labels = xLabels, fontsize = 8)

    yTicks: list[int] = []; yLabels: list[str] = []
    start = 0; stop = 0; step = 0
    if max(breakTimePerDaysList) <= 1:
        stop = 2; step = 1
    elif max(breakTimePerDaysList) <= 2:
        stop = 3; step = 1
    else:
        step = ceil(max(breakTimePerDaysList) / 3); stop = step * 4
    for i in range(start, stop, step):
        yTicks.append(i)
        yLabels.append('{}시간'.format(i))
    plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 8)
    plt.ylim(0, stop - step)
    plt.grid(axis = 'y', linestyle = ':')
    
    if shape == 'bar':
        plt.bar([i for i in range(dayCount)], breakTimePerDaysList, color = '#FCD000')
    else:
        plt.plot(breakTimePerDaysList, color = '#FCD000', linewidth = 0.5, markersize = 4)
        plt.fill_between([i for i in range(dayCount)], breakTimePerDaysList, color = '#FCD000', alpha = 0.55)

    plt.savefig('{}/Images/Graphs/break_time_per_days_graph.png'.format(path))
    plt.close()

def makeGraphOfBreakTimePerSubjects(user: User, graphFigSize: tuple[float],\
        graphDpi: int, dayCount: int = 7) -> None: # 지정 날짜동안 과목별 학습 시간 그래프를 그려주는 함수
    fontPath: str = '{}/Fonts/NanumGothic/NanumGothicBold.ttf'.format(path)
    fm.fontManager.addfont(fontPath)
    plt.rcParams['font.family'] = (fm.FontProperties(fname = fontPath)).get_name()
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = graphFigSize, dpi = graphDpi, facecolor = '#F0F7FF')
    plt.gca().set_facecolor('#FAFCFF')

    breakTimePerSubjectsDict: dict = getBreakTimePerSubjectsDict(user, dayCount) # 과목별 총 휴식 시간 딕셔너리
    if len(breakTimePerSubjectsDict) == 0:
        plt.text(0.5, 0.5, '{}일간 학습한 과목이 없습니다.'.format(dayCount), fontsize = 11, ha = 'center', va = 'center')
        plt.axis('off')
        plt.savefig('{}/Images/Graphs/break_time_per_subjects_graph.png'.format(path))
        plt.close()
        return

    plt.title('{}일간 과목별 휴식 시간'.format(dayCount), fontsize = 13)

    sortedDatas: dict = dict(sorted(breakTimePerSubjectsDict.items(), key = lambda item: item[1], reverse = True))
    topDatas: dict = dict(); otherDatas: float = 0.0
    if len(sortedDatas) <= 5:
        topDatas = dict(list(sortedDatas.items()))
    else:
        topDatas = dict(list(sortedDatas.items())[:4])
        otherDatas: float = sum(list(sortedDatas.values())[4:])
    if len(sortedDatas) > 5:
        topDatas['기타'] = otherDatas

    plt.xticks(fontsize = 8)

    yTicks: list[int] = []; yLabels: list[str] = []
    start = 0; stop = 0; step = 0
    if max(topDatas.values()) <= 1:
        stop = 2; step = 1
    elif max(topDatas.values()) <= 2:
        stop = 3; step = 1
    else:
        step = ceil(max(topDatas.values()) / 3); stop = step * 4
    for i in range(start, stop, step):
        yTicks.append(i)
        yLabels.append('{}시간'.format(i))
    plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 8)
    plt.ylim(0, stop - step)
    plt.grid(axis = 'y', linestyle = ':')

    keyList: list[str] = []
    for key in topDatas.keys():
        if len(key) > 5: # 과목명이 길 경우, 두 줄로 처리함. (과목명 최대 10자)
            keyList.append(key[:5].strip() + '\n' + key[5:].strip())
        else:
            keyList.append(key.strip())
    plt.bar(keyList, topDatas.values(), color = '#FCD000')
    
    plt.savefig('{}/Images/Graphs/break_time_per_subjects_graph.png'.format(path))
    plt.close()

def makeGraphOfFocusRatePerDays(user: User, graphFigSize: tuple[float], graphDpi: int,\
        dayCount: int = 7, shape: str = 'normal') -> None: # 지정 날짜동안 집중도 그래프를 그려주는 함수
    fontPath: str = '{}/Fonts/NanumGothic/NanumGothicBold.ttf'.format(path)
    fm.fontManager.addfont(fontPath)
    plt.rcParams['font.family'] = (fm.FontProperties(fname = fontPath)).get_name()
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = graphFigSize, dpi = graphDpi, facecolor = '#F0F7FF')
    plt.gca().set_facecolor('#FAFCFF')

    plt.title('{}일간 집중도'.format(dayCount), fontsize = 13)

    focusRatePerDaysList: list[float] = getFocusRatePerDaysList(user, dayCount) # 하루 당 평균 집중도 리스트

    xTicks: list[int] = []; xLabels: list[str] = []
    if dayCount <= 7:
        xTicks: list[int] = [i for i in range(dayCount)]
    elif dayCount <= 20:
        xTicks: list[int] = linspace(0, dayCount - 1, 3, dtype = int)
    elif dayCount <= 30:
        xTicks: list[int] = linspace(0, dayCount - 1, 4, dtype = int)
    else:
        xTicks: list[int] = linspace(0, dayCount - 1, 5, dtype = int)
    xLabels: list[str] = ['{}일 전'.format(dayCount - xTick - 1) for xTick in xTicks]
    xLabels[len(xLabels) - 1] = '오늘'
    plt.xticks(ticks = xTicks, labels = xLabels, fontsize = 8)
    plt.yticks([0, 25, 50, 75, 100], ['0%', '25%', '50%', '75%', '100%'], fontsize = 8)
    plt.ylim(0, 100)
    plt.grid(axis = 'y', linestyle = ':')
    
    if shape == 'line plot':
        plt.plot(focusRatePerDaysList, marker = 'o', color = '#6883FF', linewidth = 1, markersize = 4)
        plt.fill_between([i for i in range(dayCount)], focusRatePerDaysList, color = '#6883FF', alpha = 0.55)
    else:
        plt.plot(focusRatePerDaysList, color = '#6883FF', linewidth = 1, markersize = 4)
        plt.fill_between([i for i in range(dayCount)], focusRatePerDaysList, color = '#6883FF', alpha = 0.55)

    plt.savefig('{}/Images/Graphs/focus_rate_per_days_graph.png'.format(path))
    plt.close()

def makeGraphOfFocusRatePerSubjects(user: User, graphFigSize: tuple[int],\
        graphDpi: int, dayCount: int) -> None: # 지정 날짜동안 과목별 집중도 그래프를 그려주는 함수
    fontPath: str = '{}/Fonts/NanumGothic/NanumGothicBold.ttf'.format(path)
    fm.fontManager.addfont(fontPath)
    plt.rcParams['font.family'] = (fm.FontProperties(fname = fontPath)).get_name()
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = graphFigSize, dpi = graphDpi, facecolor = '#F0F7FF')
    plt.gca().set_facecolor('#FAFCFF')

    focusRatePerSubjectsDict: dict = getFocusRatePerSubjectsDict(user, dayCount) # 과목별 평균 집중도 딕셔너리
    if len(focusRatePerSubjectsDict) == 0:
        plt.text(0.5, 0.5, '{}일간 학습한 과목이 없습니다.'.format(dayCount), fontsize = 11, ha = 'center', va = 'center')
        plt.axis('off')
        plt.savefig('{}/Images/Graphs/focus_rate_per_subjects_graph.png'.format(path))
        plt.close()
        return

    plt.title('{}일간 과목별 집중도'.format(dayCount), fontsize = 13)

    sortedDatas: dict = dict(sorted(focusRatePerSubjectsDict.items(), key = lambda item: item[1], reverse = True))
    topDatas: dict = dict(); otherDatas: float = 0.0
    if len(sortedDatas) <= 5:
        topDatas = dict(list(sortedDatas.items()))
    else:
        topDatas = dict(list(sortedDatas.items())[:4])
        otherDatas: float = sum(list(sortedDatas.values())[4:]) / len(list(sortedDatas.values())[4:])
    if len(sortedDatas) > 5:
        topDatas['기타'] = otherDatas

    plt.xticks(fontsize = 8)

    keyList: list[str] = []
    for key in topDatas.keys():
        if len(key) > 5: # 과목명이 길 경우, 두 줄로 처리함. (과목명 최대 10자)
            keyList.append(key[:5].strip() + '\n' + key[5:].strip())
        else:
            keyList.append(key.strip())
    plt.bar(keyList, topDatas.values(), color = '#6883FF')
    
    plt.savefig('{}/Images/Graphs/focus_rate_per_subjects_graph.png'.format(path))
    plt.close()

if DEBUG:
    testUser: User = User()
    testUser.setSubjectList(['국어', '수학', '영어'])
    testUser.setStudyDataList([\
            StudyData(dt.datetime(2026, 1, 12), '파이썬', [[dt.datetime(2026, 1, 12, 8, 30, 0), dt.datetime(2026, 1, 12, 12, 0, 0)]]),\
            StudyData(dt.datetime(2026, 1, 13), '영어', [[dt.datetime(2026, 1, 13, 17, 0, 0), dt.datetime(2026, 1, 13, 20, 0, 0)]]),\
            StudyData(dt.datetime(2026, 1, 14), '프로그래밍 기초', [[dt.datetime(2026, 1, 14, 23, 40, 0), dt.datetime(2026, 1, 15, 0, 20, 0)]]),\
            StudyData(dt.datetime(2026, 1, 16), '영어', [[dt.datetime(2026, 1, 16, 11, 30, 0), dt.datetime(2026, 1, 17, 0, 30, 0)],\
                                                        [dt.datetime(2026, 1, 17, 2, 30, 0), dt.datetime(2026, 1, 17, 2, 40, 0)]]),\
            StudyData(dt.datetime(2026, 1, 18), '사회', [[dt.datetime(2026, 1, 18, 8, 0, 0), dt.datetime(2026, 1, 18, 8, 0, 30)],\
                                                        [dt.datetime(2026, 1, 18, 8, 0, 40), dt.datetime(2026, 1, 18, 8, 1, 0)]]),\
            StudyData(dt.datetime(2026, 1, 18), '과학', [[dt.datetime(2026, 1, 18, 14, 0, 0), dt.datetime(2026, 1, 18, 14, 0, 30)]])\
    ])

    makeGraphOfFocusRatePerSubjects(testUser, (4, 3.5), 100, 7)
