# 성적 분석 기능과 관련된 각종 함수가 포함된 모듈

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import datetime as dt
from user import *
from math import ceil, floor
import numpy as np
from sklearn.linear_model import LinearRegression

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

def getGradeDataList(user: User, dataCount: int, type: int, subject: str = '과목명') -> list[any]: # 특정 개수의 성적 데이터 리스트를 반환하는 함수
    if type == GradeData.TOEIC:
        tempList: SortedList[GradeData] = user.getToeicGradeDataList()
    elif type == GradeData.TOEFL:
        tempList: SortedList[GradeData] = user.getToeflGradeDataList()
    elif type == GradeData.CSAT:
        tempList: SortedList[GradeData] = user.getCsatGradeDataList()
    else: # GradeData.OTHER
        tempList: SortedList[GradeData] = user.getOtherGradeDataList()

    gradeDataList: list[GradeData] = []
    count: int = 0
    for i in range(len(tempList) - 1, -1, -1):
        if type == GradeData.TOEIC or type == GradeData.TOEFL\
                or (type == GradeData.CSAT or type == GradeData.OTHER) and tempList[i].getSubject() == subject:
            gradeDataList.append(tempList[i])
            count += 1
            if count == dataCount:
                break
    gradeDataList.reverse()
    return gradeDataList

def predictGradeData(user: User, type: int, subject: str = '과목명', predictedMaxScore: float = 100, predictedMinScore: float = 0) -> GradeData: # 성적 예측 함수
    # 선형 회귀 분석을 이용하여 성적을 예측함.
    # 기타 성적의 경우, 최고점·최저점을 고려한 정규화·비정규화 과정이 진행됨.

    if type == GradeData.TOEIC:
        toeicGradeDataList: SortedList[TOEICGradeData] = user.getToeicGradeDataList()
        rcList: list[int] = []; lcList: list[int] = []
        for toeicGradeData in toeicGradeDataList:
            rc: int = toeicGradeData.getRc()
            lc: int = toeicGradeData.getLc()

            rcList.append(rc)
            lcList.append(lc)

        x1: np.NDArray[int] = np.array(range(len(rcList))).reshape(-1, 1)
        x2: np.NDArray[int] = np.array(range(len(lcList))).reshape(-1, 1)

        y1: np.NDArray[int] = np.array(rcList)
        y2: np.NDArray[int] = np.array(lcList)

        model1: LinearRegression = LinearRegression()
        model2: LinearRegression = LinearRegression()

        model1.fit(x1, y1)
        model2.fit(x2, y2)

        nextX1: np.NDArray[int] = np.array([[len(rcList)]])
        nextX2: np.NDArray[int] = np.array([[len(lcList)]])

        predictedRc: int = round(model1.predict(nextX1)[0])
        predictedLc: int = round(model2.predict(nextX2)[0])

        if predictedRc < 0:
            predictedRc = 0
        elif predictedRc > 495:
            predictedRc = 495

        if predictedLc < 0:
            predictedLc = 0
        elif predictedLc > 495:
            predictedLc = 495

        date: dt.datetime = dt.datetime.now()
        nextDate: dt.datetime = date + dt.timedelta(days = 1)
        return TOEICGradeData(nextDate, predictedRc, predictedLc)
    elif type == GradeData.TOEFL:
        toeflGradeDataList: SortedList[TOEFLGradeData] = user.getToeflGradeDataList()
        readingList: list[int] = []; listeningList: list[int] = []; speakingList: list[int] = []; writingList: list[int] = []
        for toeflGradeData in toeflGradeDataList:
            reading: int = toeflGradeData.getReading()
            listening: int = toeflGradeData.getListening()
            speaking: int = toeflGradeData.getSpeaking()
            writing: int = toeflGradeData.getWriting()

            readingList.append(reading)
            listeningList.append(listening)
            speakingList.append(speaking)
            writingList.append(writing)

        x1: np.NDArray[int] = np.array(range(len(readingList))).reshape(-1, 1)
        x2: np.NDArray[int] = np.array(range(len(listeningList))).reshape(-1, 1)
        x3: np.NDArray[int] = np.array(range(len(speakingList))).reshape(-1, 1)
        x4: np.NDArray[int] = np.array(range(len(writingList))).reshape(-1, 1)

        y1: np.NDArray[int] = np.array(readingList)
        y2: np.NDArray[int] = np.array(listeningList)
        y3: np.NDArray[int] = np.array(speakingList)
        y4: np.NDArray[int] = np.array(writingList)

        model1: LinearRegression = LinearRegression()
        model2: LinearRegression = LinearRegression()
        model3: LinearRegression = LinearRegression()
        model4: LinearRegression = LinearRegression()

        model1.fit(x1, y1)
        model2.fit(x2, y2)
        model3.fit(x3, y3)
        model4.fit(x4, y4)

        nextX1: np.NDArray[int] = np.array([[len(readingList)]])
        nextX2: np.NDArray[int] = np.array([[len(listeningList)]])
        nextX3: np.NDArray[int] = np.array([[len(speakingList)]])
        nextX4: np.NDArray[int] = np.array([[len(writingList)]])

        predictedReading: int = round(model1.predict(nextX1)[0])
        predictedListening: int = round(model2.predict(nextX2)[0])
        predictedSpeaking: int = round(model3.predict(nextX3)[0])
        predictedWriting: int = round(model4.predict(nextX4)[0])

        if predictedReading < 0:
            predictedReading = 0
        elif predictedReading > 30:
            predictedReading = 30

        if predictedListening < 0:
            predictedListening = 0
        elif predictedListening > 30:
            predictedListening = 30

        if predictedSpeaking < 0:
            predictedSpeaking = 0
        elif predictedSpeaking > 30:
            predictedSpeaking = 30

        if predictedWriting < 0:
            predictedWriting = 0
        elif predictedWriting > 30:
            predictedWriting = 30

        date: dt.datetime = dt.datetime.now()
        nextDate: dt.datetime = date + dt.timedelta(days = 1)
        return TOEFLGradeData(nextDate, predictedReading, predictedListening, predictedSpeaking, predictedWriting)
    elif type == GradeData.CSAT:
        def percentileToGrade(percentile: int) -> int: # 백분위를 등급으로 변환하는 함수
            if percentile >= 96:
                return 1
            elif percentile >= 89:
                return 2
            elif percentile >= 77:
                return 3
            elif percentile >= 60:
                return 4
            elif percentile >= 40:
                return 5
            elif percentile >= 23:
                return 6
            elif percentile >= 11:
                return 7
            elif percentile >= 4:
                return 8
            else:
                return 9

        csatGradeDataList: SortedList[CSATGradeData] = user.getCsatGradeDataList()
        percentileList: list[int] = []
        for csatGradeData in csatGradeDataList:
            if csatGradeData.getSubject() == subject:
                percentile: int = csatGradeData.getPercentile()
                percentileList.append(percentile)

        x: np.NDArray[int] = np.array(range(len(percentileList))).reshape(-1, 1)
        y: np.NDArray[int] = np.array(percentileList)
        model: LinearRegression = LinearRegression()
        model.fit(x, y)
        nextX: np.NDArray[int] = np.array([[len(percentileList)]])
        predictedPercentile: int = round(model.predict(nextX)[0])
        predictedGrade: int = percentileToGrade(predictedPercentile)

        date: dt.datetime = dt.datetime.now()
        nextDate: dt.datetime = date + dt.timedelta(days = 1)
        return CSATGradeData(nextDate, subject, 100, predictedGrade, predictedPercentile)
    else: # GradeData.OTHER
        def normalize(score: float, maxScore: float, minScore: float) -> float: # 점수 정규화(0~100점 범위)
            score -= minScore
            maxScore -= minScore
            return score / maxScore * 100

        def denormalize(score: float, maxScore: float, minScore: float) -> float: # 점수 비정규화(최저점~최고점 범위)
            originalScore: float = score / 100 * (maxScore - minScore)
            return originalScore + minScore

        otherGradeDataList: SortedList[OtherGradeData] = user.getOtherGradeDataList()
        normalizedScoreList: list[float] = []
        for otherGradeData in otherGradeDataList:
            if otherGradeData.getSubject() == subject:
                score: float = otherGradeData.getScore()
                maxScore: float = otherGradeData.getMaxScore()
                minScore: float = otherGradeData.getMinScore()

                normalizedScore: float = normalize(score, maxScore, minScore)
                normalizedScoreList.append(normalizedScore)

        x: np.NDArray[float] = np.array(range(len(normalizedScoreList))).reshape(-1, 1)
        y: np.NDArray[float] = np.array(normalizedScoreList)
        model: LinearRegression = LinearRegression()
        model.fit(x, y)
        nextX: np.NDArray[float] = np.array([[len(normalizedScoreList)]])
        predictedNormalizedScore: float = model.predict(nextX)[0]
        predictedDenormalizedScore: float = denormalize(predictedNormalizedScore, predictedMaxScore, predictedMinScore)

        date: dt.datetime = dt.datetime.now()
        nextDate: dt.datetime = date + dt.timedelta(days = 1)
        return OtherGradeData(nextDate, subject, predictedDenormalizedScore, predictedMaxScore, predictedMinScore)

def makeGraphOfGradeData(user: User, type: int, graphFigSize: tuple[float], graphDpi: int,\
        dataCount: int = 5, subject: str = '과목명', csatType: str = 'standard_score',\
        predictedMaxScore: float = 100, predictedMinScore: float = 0) -> None: # 특정 개수의 데이터를 그래프로 만들어주는 함수
    fontPath: str = '{}/Fonts/NanumGothic/NanumGothicBold.ttf'.format(path)
    fm.fontManager.addfont(fontPath)
    plt.rcParams['font.family'] = (fm.FontProperties(fname = fontPath)).get_name()
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = graphFigSize, dpi = graphDpi, facecolor = '#F0F7FF')
    plt.gca().set_facecolor('#FAFCFF')

    if type == GradeData.TOEIC:
        gradeDataList: list[GradeData] = getGradeDataList(user, dataCount, type)
        count: int = len(gradeDataList)
        if len(gradeDataList) >= 2:
            count += 1
        plt.title('{}개 토익 성적'.format(count), fontsize = 13)
    elif type == GradeData.TOEFL:
        gradeDataList: list[GradeData] = getGradeDataList(user, dataCount, type)
        count: int = len(gradeDataList)
        if len(gradeDataList) >= 2:
            count += 1
        plt.title('{}개 토플 성적'.format(count), fontsize = 13)
    elif type == GradeData.CSAT:
        gradeDataList: list[GradeData] = getGradeDataList(user, dataCount, type, subject)
        count: int = len(gradeDataList)
        if len(gradeDataList) >= 2 and csatType != 'standard_score':
            count += 1
        plt.title('{}개 수능 성적'.format(count), fontsize = 13)
    else: # GradeData.OTHER
        gradeDataList: list[GradeData] = getGradeDataList(user, dataCount, type, subject)
        count: int = len(gradeDataList)
        if len(gradeDataList) >= 2:
            count += 1
        plt.title('{}개 기타 성적'.format(count), fontsize = 13)

    xTicks: list[int] = [i for i in range(len(gradeDataList))]
    xLabels: list[str] = []
    for i in range(len(gradeDataList)):
        date: dt.datetime = gradeDataList[i].getDate()
        xLabels.append('{}/\n{}/{}'.format(date.year, date.month, date.day))
    if len(gradeDataList) >= 10:
        xFontSize: int = 7
    elif len(gradeDataList) >= 5:
        xFontSize = 7
    else:
        xFontSize = 8
    
    if len(gradeDataList) >= 2 and not (type == GradeData.CSAT and csatType == 'standard_score'):
        xTicks.append(len(gradeDataList))
        xLabels.append('성적\n예측')
    plt.xticks(ticks = xTicks, labels = xLabels, fontsize = xFontSize)

    if type == GradeData.TOEIC:
        yTicks: list[int] = [0, 165, 330, 495, 660, 825, 990]
        yLabels: list[str] = ['{}'.format(i) for i in yTicks]

        plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 9)
        plt.grid(axis = 'y', linestyle = ':')

        plt.ylim(0, 990)

        rcList: list[int] = []; lcList: list[int] = []
        totalList: list[int] = [] # rc + lc
        for i in range(len(gradeDataList)):
            rc: int = gradeDataList[i].getRc()
            lc: int = gradeDataList[i].getLc()
            rcList.append(rc)
            lcList.append(lc)
            totalList.append(rc + lc)

        if len(gradeDataList) >= 2:
            predictedToeicGradeData: TOEICGradeData = predictGradeData(user, type)
            predictedRc: int = predictedToeicGradeData.getRc()
            predictedLc: int = predictedToeicGradeData.getLc()

            rcList.append(predictedRc)
            lcList.append(predictedLc)
            totalList.append(predictedRc + predictedLc)

        plt.plot(rcList, color = '#6F88FF', marker = 'o', markersize = 4, label = 'RC')
        plt.plot(lcList, color = '#FF6D9C', marker = 'o', markersize = 4, label = 'LC')
        plt.bar([i for i in range(len(totalList))], totalList, color = '#FFE328', label = '총점')
        plt.legend(fontsize = 8, framealpha = 0.5)
    elif type == GradeData.TOEFL:
        yTicks: list[int] = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
        yLabels: list[str] = ['{}'.format(i) for i in yTicks]

        plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 8)
        plt.grid(axis = 'y', linestyle = ':')

        plt.ylim(0, 120)

        readingList: list[int] = []; listeningList: list[int] = []; speakingList: list[int] = []; writingList: list[int] = []
        totalList: list[int] = [] # reading + listening + speaking + writing
        for i in range(len(gradeDataList)):
            reading: int = gradeDataList[i].getReading()
            listening: int = gradeDataList[i].getListening()
            speaking: int = gradeDataList[i].getSpeaking()
            writing: int = gradeDataList[i].getWriting()

            readingList.append(reading)
            listeningList.append(listening)
            speakingList.append(speaking)
            writingList.append(writing)
            totalList.append(reading + listening + speaking + writing)

        if len(gradeDataList) >= 2:
            predictedToeflGradeData: TOEFLGradeData = predictGradeData(user, type)
            predictedReading: int = predictedToeflGradeData.getReading()
            predictedListening: int = predictedToeflGradeData.getListening()
            predictedSpeaking: int = predictedToeflGradeData.getSpeaking()
            predictedWriting: int = predictedToeflGradeData.getWriting()

            readingList.append(predictedReading)
            listeningList.append(predictedListening)
            speakingList.append(predictedSpeaking)
            writingList.append(predictedWriting)
            totalList.append(predictedReading + predictedListening + predictedSpeaking + predictedWriting)

        plt.plot(readingList, color = '#FFBC5D', marker = 'o', markersize = 4, label = 'Reading')
        plt.plot(listeningList, color = '#5DFFC3', marker = 'o', markersize = 4, label = 'Listening')
        plt.plot(speakingList, color = '#61B8FF', marker = 'o', markersize = 4, label = 'Speaking')
        plt.plot(writingList, color = '#FF6AF8', marker = 'o', markersize = 4, label = 'Writing')
        plt.bar([i for i in range(len(totalList))], totalList, color = '#E2FF5A', label = '총점')
        plt.legend(fontsize = 8, framealpha = 0.5)
    elif type == GradeData.CSAT:
        def percentileToGrade(percentile: int) -> int: # 백분위를 등급으로 변환하는 함수
            if percentile >= 96:
                return 1
            elif percentile >= 89:
                return 2
            elif percentile >= 77:
                return 3
            elif percentile >= 60:
                return 4
            elif percentile >= 40:
                return 5
            elif percentile >= 23:
                return 6
            elif percentile >= 11:
                return 7
            elif percentile >= 4:
                return 8
            else:
                return 9

        if len(gradeDataList) >= 2:
            predictedCsatGradeData: CSATGradeData = predictGradeData(user, type, subject)

        if csatType == 'standard_score': # 표준점수
            yTicks: list[int] = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
            yLabels: list[str] = ['{}'.format(i) for i in yTicks]

            plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 8)
            plt.grid(axis = 'y', linestyle = ':')

            plt.ylim(0, 200)

            standardScoreList: list[int] = []
            for i in range(len(gradeDataList)):
                standardScore: int = gradeDataList[i].getStandardScore()
                standardScoreList.append(standardScore)

            plt.bar([i for i in range(len(standardScoreList))], standardScoreList, color = '#FFC12F', label = '표준점수')
            plt.legend(fontsize = 8, framealpha = 0.5)
        elif csatType == 'grade': # 등급
            yTicks: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            yLabels: list[str] = ['9등급', '8등급', '7등급', '6등급', '5등급', '4등급', '3등급', '2등급', '1등급']

            plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 8)
            plt.grid(axis = 'y', linestyle = ':')

            plt.ylim(0, 8)

            gradeList: list[int] = []
            for i in range(len(gradeDataList)):
                grade: int = gradeDataList[i].getGrade()
                gradeList.append(9 - grade)

            if len(gradeDataList) >= 2:
                predictedGrade: int = percentileToGrade(predictedCsatGradeData.getPercentile())
                gradeList.append(9 - predictedGrade)

            plt.bar([i for i in range(len(gradeList))], gradeList, color = '#2AFFC9', label = '등급')
            plt.legend(fontsize = 8)
        else: # 'percentile' - 백분위
            yTicks: list[int] = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
            yLabels: list[str] = ['{}'.format(i) for i in yTicks]

            plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 8)
            plt.grid(axis = 'y', linestyle = ':')

            plt.ylim(0, 100)

            percentileList: list[int] = []
            for i in range(len(gradeDataList)):
                percentile: int = gradeDataList[i].getPercentile()
                percentileList.append(percentile)

            if len(gradeDataList) >= 2:
                predictedPercentile: int = predictedCsatGradeData.getPercentile()
                percentileList.append(predictedPercentile)

            plt.bar([i for i in range(len(percentileList))], percentileList, color = '#E12FFF', label = '백분위')
            plt.legend(fontsize = 8)
    else: # GradeData.OTHER
        scoreList: list[float] = []; maxScoreList: list[float] = []; minScoreList: list[float] = []
        for i in range(len(gradeDataList)):
            score: float = gradeDataList[i].getScore()
            maxScore: float = gradeDataList[i].getMaxScore()
            minScore: float = gradeDataList[i].getMinScore()

            scoreList.append(score)
            maxScoreList.append(maxScore)
            minScoreList.append(minScore)

        if len(gradeDataList) >= 2:
            predictedOtherGradeData: OtherGradeData = predictGradeData(user, type, subject, predictedMaxScore, predictedMinScore)
            predictedScore: float = predictedOtherGradeData.getScore()
            scoreList.append(predictedScore)
            maxScoreList.append(predictedMaxScore)
            minScoreList.append(predictedMinScore)

        highestMaxScore: int = ceil(max(maxScoreList)) # 가장 높은 최고점
        lowestMinScore: int = floor(min(minScoreList)) # 가장 낮은 최고점
        
        yTicks: list[int] = []
        if highestMaxScore - lowestMinScore >= 11:
            yTicks: list[int] = np.linspace(lowestMinScore, highestMaxScore, 11, dtype = int)
        else:
            yTicks: list[int] = [i for i in range(highestMaxScore - lowestMinScore + 1)]
        yLabels: list[str] = ['{}'.format(i) for i in yTicks]

        plt.yticks(ticks = yTicks, labels = yLabels, fontsize = 8)
        plt.grid(axis = 'y', linestyle = ':')

        plt.ylim(lowestMinScore, highestMaxScore)

        plt.plot(scoreList, color = '#7C70FF', marker = 'o', markersize = 4, label = '점수')
        plt.plot(maxScoreList, color = '#6B0000', label = '최고점')
        plt.plot(minScoreList, color = '#00096B', label = '최저점')
        plt.fill_between([i for i in range(len(maxScoreList))], highestMaxScore, maxScoreList, color = '#6B0000')
        plt.fill_between([i for i in range(len(minScoreList))], lowestMinScore, minScoreList, color = '#00096B')
        plt.legend(fontsize = 8, framealpha = 0.5)

    plt.savefig('{}/Images/Graphs/grade_data_graph.png'.format(path))
    plt.close()

if DEBUG:
    testUser: User = User()

    toeicGradeDataList: SortedList[TOEICGradeData] = SortedList()
    toeflGradeDataList: SortedList[TOEFLGradeData] = SortedList()
    csatGradeDataList: SortedList[CSATGradeData] = SortedList()
    otherGradeDataList: SortedList[OtherGradeData] = SortedList()

    toeicList: list[TOEICGradeData] = [TOEICGradeData(dt.datetime(2026, 4, 28), 100, 150),\
                                    TOEICGradeData(dt.datetime(2026, 4, 30), 150, 200),\
                                    TOEICGradeData(dt.datetime(2026, 5, 1), 200, 250),\
                                    TOEICGradeData(dt.datetime(2026, 5, 2), 250, 300)]
    toeflList: list[TOEFLGradeData] = [TOEFLGradeData(dt.datetime(2026, 4, 20), 10, 15, 20, 11),\
                                    TOEFLGradeData(dt.datetime(2026, 4, 21), 15, 14, 25, 12),\
                                    TOEFLGradeData(dt.datetime(2026, 4, 22), 8, 15, 30, 8),\
                                    TOEFLGradeData(dt.datetime(2026, 4, 24), 7, 7, 30, 18),\
                                    TOEFLGradeData(dt.datetime(2026, 4, 28), 14, 28, 12, 12),\
                                    TOEFLGradeData(dt.datetime(2026, 4, 29), 10, 27, 28, 19),\
                                    TOEFLGradeData(dt.datetime(2026, 4, 30), 20, 30, 27, 24),\
                                    TOEFLGradeData(dt.datetime(2026, 5, 1), 28, 29, 26, 27),\
                                    TOEFLGradeData(dt.datetime(2026, 5, 2), 30, 27, 28, 26),\
                                    TOEFLGradeData(dt.datetime(2026, 5, 3), 18, 28, 27, 27)]
    csatList: list[CSATGradeData] = [CSATGradeData(dt.datetime(2026, 4, 28), '국어', 150, 1, 99),\
                                    CSATGradeData(dt.datetime(2026, 4, 30), '국어', 118, 2, 92),\
                                    CSATGradeData(dt.datetime(2026, 5, 1), '화학Ⅰ', 80, 3, 84)]
    otherList: list[OtherGradeData] = [OtherGradeData(dt.datetime(2026, 4, 28), '국어', 30.5, 45.6, -12.4),\
                                    OtherGradeData(dt.datetime(2026, 4, 30), '국어', 80.58, 100, 0),\
                                    OtherGradeData(dt.datetime(2026, 5, 1), '국어', 57.82, 78.2, -25.4),\
                                    OtherGradeData(dt.datetime(2025, 5, 2), '국어', 70.5, 100, -10)]

    for toeicGradeData in toeicList:
        toeicGradeDataList.add(toeicGradeData)
    for toeflGradeData in toeflList:
        toeflGradeDataList.add(toeflGradeData)
    for csatGradeData in csatList:
        csatGradeDataList.add(csatGradeData)
    for otherGradeData in otherList:
        otherGradeDataList.add(otherGradeData)

    testUser.setToeicGradeDataList(toeicGradeDataList)
    testUser.setToeflGradeDataList(toeflGradeDataList)
    testUser.setCsatGradeDataList(csatGradeDataList)
    testUser.setOtherGradeDataList(otherGradeDataList)

    makeGraphOfGradeData(testUser, GradeData.OTHER, (4, 3.5), 100, 4, '국어', predictedMaxScore = 300, predictedMinScore = 9)

    '''
    predictedToeicGradeData: TOEICGradeData = predictGradeData(testUser, GradeData.TOEIC)
    predictedToeflGradeData: TOEFLGradeData = predictGradeData(testUser, GradeData.TOEFL)
    predictedCsatGradeData: CSATGradeData = predictGradeData(testUser, GradeData.CSAT, '국어')
    predictedOtherGradeData: OtherGradeData = predictGradeData(testUser, GradeData.OTHER, '국어', -10, 50)

    print('[토익] RC: {}, LC: {}'.format(predictedToeicGradeData.getRc(), predictedToeicGradeData.getLc()))
    print('[토플] Reading: {}, Listening: {}, Speaking: {}, Writing: {}'\
            .format(predictedToeflGradeData.getReading(), predictedToeflGradeData.getListening(),\
            predictedToeflGradeData.getSpeaking(), predictedToeflGradeData.getWriting()))
    print('[수능] 과목: {}, 등급: {}, 백분위: {}'.format(predictedCsatGradeData.getSubject(),\
            predictedCsatGradeData.getGrade(), predictedCsatGradeData.getPercentile()))
    print('[기타] 과목: {}, 점수: {:.2f}, 최고점: {:.2f}, 최저점: {:.2f}'\
            .format(predictedOtherGradeData.getSubject(), predictedOtherGradeData.getScore(),\
            predictedOtherGradeData.getMaxScore(), predictedOtherGradeData.getMinScore()))
    '''
