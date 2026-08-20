# 시간표 관련 모듈

from tkinter import *
import datetime as dt
from user import *

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

class TimeTableFrame(Frame):
    MON: int = 0; TUE: int = 1; WED: int = 2; THU: int = 3; FRI: int = 4; SAT: int = 5; SUN: int = 6
    COLOR_LIST: list[str] = [\
            '#FADADD', '#F8E1E7', '#F6E8F2', '#EADCF8', '#E0D9FA', '#DADDFB', '#DDE7FA', '#E3F2FD',\
            '#E0F7FA', '#E0F2F1', '#E6F4EA', '#EDF7ED' ,'#F1F8E9', '#F9FBE7', '#FFFDE7', '#FFF8E1',\
            '#FFECB3', '#FFE0B2', '#FFDAD6', '#F8D7DA', '#F5DDE0', '#F2E2E6', '#EFE7EB', '#ECECF1',\
            '#FADFE3', '#F8E6EA', '#F6EDF1', '#EEE3F8', '#E6E0FA', '#E0E3FB', '#E3EDFA', '#E9F4FD',\
            '#E6FAFB', '#E6F5F3', '#ECF7EF', '#F2FAF2', '#F5FBEF', '#FBFDF1', '#FFFFF2', '#FFFBEA',\
            '#FFF1CC', '#FFE7C2', '#FFE1DC', '#FADDE1', '#F7E3E6', '#F4E8EB', '#F1EDF0', '#EEF2F5',\
            '#FBE4E8', '#FAEBEF', '#F9F2F6', '#F1EAFB', '#EBE7FD', '#E6EAFD', '#E8F1FC', '#EDF6FE',\
            '#EBFCFD', '#EBF8F6', '#F0FAF4', '#F6FCF6', '#F8FDF4', '#FCFEF5', '#FFFFF7', '#FFFCF0',\
            '#FFF5D9', '#FFEDD1', '#FFE8E2', '#FCE4E8', '#FAE9EC', '#F7EEF1', '#F4F3F6', '#F1F8FB',\
            '#FCE9ED', '#FBF0F3', '#FAF7FA', '#F4EFFD', '#EFEFFD', '#EBF1FE', '#EDF5FD', '#F2F9FE',\
            '#F0FEFF', '#F0FAF9', '#F4FCF8', '#F9FDF9', '#FBFEF8', '#FEFFF9', '#FFFFFF', '#FFFDF6',\
            '#FFF8E6', '#FFF1DF', '#FFEDE8', '#FDE9ED', '#FCEEF1', '#FAF3F6', '#F8F8FB', '#F5FCFE',\
            '#FAD1D8', '#F7D8DE', '#F4DEE5', '#E9D8F4', '#DFD5F7', '#D8D9F8', '#DCE4F7', '#E1EEFB',\
            '#DFF5F7', '#DFF1EE', '#E4F3EA', '#EAF6EE', '#EEF8EB', '#F6F9EC', '#FCFCEB', '#FCF7DF',\
            '#FCEBC2', '#FADFC1', '#FAD8CE', '#F5D4DA', '#F2DAE0', '#EEE0E6', '#EBE6EC', '#E8ECF2',\
            '#F6C8D0', '#F3CFD7', '#F0D6DE', '#E4D0F1', '#DACDF4', '#D3D1F5', '#D7DCF4', '#DCE7F8',\
            '#DAF0F3', '#DAECE9', '#DEF0E5', '#E4F3E9', '#E8F5E6', '#F0F7E7', '#F7F8E6', '#F7F3DA',\
            '#F7E8BE', '#F5DDBE', '#F5D6CB', '#F0D2D8', '#EDD8DE', '#E9DEE4', '#E6E4EA', '#E3EAF0',\
            '#F2BFC8', '#EFC6CF', '#ECCDD6', '#DEC7EE', '#D4C4F1', '#CDC8F2', '#D1D3F1', '#D6DFF5',\
            '#D4EBEF', '#D4E7E4', '#D8EBE0', '#DEEEE4', '#E2F0E1', '#EAF2E2', '#F1F3E1', '#F1EFD6',\
            '#F1E4BB', '#EFDABB', '#EFD3C8', '#EACFD5', '#E7D5DB', '#E3DBE1', '#E0E1E7', '#DDE7ED'\
    ]

    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 400, height = 350, bg = 'white', borderwidth = 0)

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/time_table_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 400, height = 350, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 각 요일 별 학습 시간 기록
        studyDataList: list[StudyData] = user.getStudyDataList()
        subjectList: list[str] = []
        breakLoop: bool = False
        for i in range(len(studyDataList) - 1, -1, -1):
            studyData: StudyData = studyDataList[i]
            subject: str = studyData.getSubject()
            studyingTimeList: list[list[dt.datetime]] = studyData.getStudyingTimeList()

            for j in range(len(studyingTimeList)):
                startStudyingTime: dt.datetime = studyingTimeList[j][0] # 학습 시작 시간
                endStudyingTime: dt.datetime = studyingTimeList[j][1] # 학습 종료 시간

                if not (subject in subjectList):
                    subjectList.append(subject)
                colorIndex: int = subjectList.index(subject) % 168 # 과목별 색깔 지정

                subjectTextInLabel: str = subject # 시간표에 표시될 과목명 (최대 5글자)
                if len(subject) > 5:
                    subjectTextInLabel = subject[0:5] + '...'

                now: dt.datetime = dt.datetime.now() # 오늘
                if startStudyingTime.weekday() == self.SUN: # 일
                    if (now + dt.timedelta(days = -7)).isocalendar()[:2] != startStudyingTime.isocalendar()[:2]:
                        breakLoop = True
                        break
                    if startStudyingTime.weekday() == endStudyingTime.weekday():
                        studyingFrame: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight: int = int(14 / 3600 * (endStudyingTime - startStudyingTime).total_seconds())
                        studyingFrame.config(width = 50, height = studyingFrameHeight)
                        studyingFrame.place(x = 50, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame.pack_propagate(False)
                        if studyingFrameHeight >= 14:
                            subjectLabel: Label = Label(studyingFrame, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel.pack(expand = True)
                    else:
                        studyingFrame1: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrame2: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight1: int = int(350 - 14 - 14 / 3600 * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second))
                        studyingFrameHeight2: int = int(14 / 3600 * (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second))
                        studyingFrame1.config(width = 50, height = studyingFrameHeight1)
                        studyingFrame2.config(width = 50, height = studyingFrameHeight2)
                        studyingFrame1.pack_propagate(False)
                        studyingFrame2.pack_propagate(False)
                        studyingFrame1.place(x = 50, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame2.place(x = 100, y = 14)
                        if studyingFrameHeight1 >= 14:
                            subjectLabel1: Label = Label(studyingFrame1, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel1.pack(expand = True)
                        if studyingFrameHeight2 >= 14:
                            subjectLabel2: Label = Label(studyingFrame2, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel2.pack(expand = True)
                elif startStudyingTime.weekday() == self.MON: # 월
                    if now.weekday() == self.SUN or now.isocalendar()[:2] != startStudyingTime.isocalendar()[:2]:
                        breakLoop = True
                        break
                    if startStudyingTime.weekday() == endStudyingTime.weekday():
                        studyingFrame: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight: int = int(14 / 3600 * (endStudyingTime - startStudyingTime).total_seconds())
                        studyingFrame.config(width = 50, height = studyingFrameHeight)
                        studyingFrame.place(x = 100, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame.pack_propagate(False)
                        if studyingFrameHeight >= 14:
                            subjectLabel: Label = Label(studyingFrame, text = subjectTextInLabel, font = ('Arial', 6, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel.pack(expand = True)
                    else:
                        studyingFrame1: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrame2: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight1: int = int(350 - 14 - 14 / 3600 * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second))
                        studyingFrameHeight2: int = int(14 / 3600 * (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second))
                        studyingFrame1.config(width = 50, height = studyingFrameHeight1)
                        studyingFrame2.config(width = 50, height = studyingFrameHeight2)
                        studyingFrame1.place(x = 100, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame2.place(x = 150, y = 14)
                        studyingFrame1.pack_propagate(False)
                        studyingFrame2.pack_propagate(False)
                        if studyingFrameHeight1 >= 14:
                            subjectLabel1: Label = Label(studyingFrame1, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel1.pack(expand = True)
                        if studyingFrameHeight2 >= 14:
                            subjectLabel2: Label = Label(studyingFrame2, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel2.pack(expand = True)
                elif startStudyingTime.weekday() == self.TUE: # 화
                    if now.weekday() == self.SUN or now.weekday() == self.MON\
                            or now.isocalendar()[:2] != startStudyingTime.isocalendar()[:2]:
                        breakLoop = True
                        break
                    if startStudyingTime.weekday() == endStudyingTime.weekday():
                        studyingFrame: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight: int = int(14 / 3600 * (endStudyingTime - startStudyingTime).total_seconds())
                        studyingFrame.config(width = 50, height = studyingFrameHeight)
                        studyingFrame.place(x = 150, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame.pack_propagate(False)
                        if studyingFrameHeight >= 14:
                            subjectLabel: Label = Label(studyingFrame, text = subjectTextInLabel, font = ('Arial', 6, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel.pack(expand = True)
                    else:
                        studyingFrame1: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrame2: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight1: int = int(350 - 14 - 14 / 3600 * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second))
                        studyingFrameHeight2: int = int(14 / 3600 * (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second))
                        studyingFrame1.config(width = 50, height = studyingFrameHeight1)
                        studyingFrame2.config(width = 50, height = studyingFrameHeight2)
                        studyingFrame1.place(x = 150, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame2.place(x = 200, y = 14)
                        studyingFrame1.pack_propagate(False)
                        studyingFrame2.pack_propagate(False)
                        if studyingFrameHeight1 >= 14:
                            subjectLabel1: Label = Label(studyingFrame1, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel1.pack(expand = True)
                        if studyingFrameHeight2 >= 14:
                            subjectLabel2: Label = Label(studyingFrame2, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel2.pack(expand = True)
                elif startStudyingTime.weekday() == self.WED: # 수
                    if now.weekday() == self.SUN or now.weekday() == self.MON or now.weekday() == self.TUE\
                            or now.isocalendar()[:2] != startStudyingTime.isocalendar()[:2]:
                        breakLoop = True
                        break
                    if startStudyingTime.weekday() == endStudyingTime.weekday():
                        studyingFrame: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight: int = int(14 / 3600 * (endStudyingTime - startStudyingTime).total_seconds())
                        studyingFrame.config(width = 50, height = studyingFrameHeight)
                        studyingFrame.place(x = 200, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame.pack_propagate(False)
                        if studyingFrameHeight >= 14:
                            subjectLabel: Label = Label(studyingFrame, text = subjectTextInLabel, font = ('Arial', 6, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel.pack(expand = True)
                    else:
                        studyingFrame1: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrame2: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight1: int = int(350 - 14 - 14 / 3600 * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second))
                        studyingFrameHeight2: int = int(14 / 3600 * (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second))
                        studyingFrame1.config(width = 50, height = studyingFrameHeight1)
                        studyingFrame2.config(width = 50, height = studyingFrameHeight2)
                        studyingFrame1.place(x = 200, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame2.place(x = 250, y = 14)
                        studyingFrame1.pack_propagate(False)
                        studyingFrame2.pack_propagate(False)
                        if studyingFrameHeight1 >= 14:
                            subjectLabel1: Label = Label(studyingFrame1, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel1.pack(expand = True)
                        if studyingFrameHeight2 >= 14:
                            subjectLabel2: Label = Label(studyingFrame2, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel2.pack(expand = True)
                elif startStudyingTime.weekday() == self.THU: # 목
                    if now.weekday() == self.SUN or now.weekday() == self.MON or now.weekday() == self.TUE or now.weekday() == self.WED\
                            or now.isocalendar()[:2] != startStudyingTime.isocalendar()[:2]:
                        breakLoop = True
                        break
                    if startStudyingTime.weekday() == endStudyingTime.weekday():
                        studyingFrame: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight: int = int(14 / 3600 * (endStudyingTime - startStudyingTime).total_seconds())
                        studyingFrame.config(width = 50, height = studyingFrameHeight)
                        studyingFrame.place(x = 250, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame.pack_propagate(False)
                        if studyingFrameHeight >= 14:
                            subjectLabel: Label = Label(studyingFrame, text = subjectTextInLabel, font = ('Arial', 6, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel.pack(expand = True)
                    else:
                        studyingFrame1: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrame2: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight1: int = int(350 - 14 - 14 / 3600 * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second))
                        studyingFrameHeight2: int = int(14 / 3600 * (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second))
                        studyingFrame1.config(width = 50,\
                                height = studyingFrameHeight1)
                        studyingFrame2.config(width = 50, height = studyingFrameHeight2)
                        studyingFrame1.place(x = 250, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame2.place(x = 300, y = 14)
                        studyingFrame1.pack_propagate(False)
                        studyingFrame2.pack_propagate(False)
                        if studyingFrameHeight1 >= 14:
                            subjectLabel1: Label = Label(studyingFrame1, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel1.pack(expand = True)
                        if studyingFrameHeight2 >= 14:
                            subjectLabel2: Label = Label(studyingFrame2, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel2.pack(expand = True)
                elif startStudyingTime.weekday() == self.FRI: # 금
                    if now.weekday() == self.SUN or now.weekday() == self.MON or now.weekday() == self.TUE or now.weekday() == self.WED or now.weekday() == self.THU\
                            or now.isocalendar()[:2] != startStudyingTime.isocalendar()[:2]:
                        breakLoop = True
                        break
                    if startStudyingTime.weekday() == endStudyingTime.weekday():
                        studyingFrame: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight: int = int(14 / 3600 * (endStudyingTime - startStudyingTime).total_seconds())
                        studyingFrame.config(width = 50, height = studyingFrameHeight)
                        studyingFrame.place(x = 300, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame.pack_propagate(False)
                        if studyingFrameHeight >= 14:
                            subjectLabel: Label = Label(studyingFrame, text = subjectTextInLabel, font = ('Arial', 6, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel.pack(expand = True)
                    else:
                        studyingFrame1: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrame2: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight1: int = int(350 - 14 - 14 / 3600 * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second))
                        studyingFrameHeight2: int = int(14 / 3600 * (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second))
                        studyingFrame1.config(width = 50, height = studyingFrameHeight1)
                        studyingFrame2.config(width = 50, height = studyingFrameHeight2)
                        studyingFrame1.place(x = 300, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame2.place(x = 350, y = 14)
                        studyingFrame1.pack_propagate(False)
                        studyingFrame2.pack_propagate(False)
                        if studyingFrameHeight1 >= 14:
                            subjectLabel1: Label = Label(studyingFrame1, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel1.pack(expand = True)
                        if studyingFrameHeight2 >= 14:
                            subjectLabel2: Label = Label(studyingFrame2, text = subjectTextInLabel, font = ('Arial', 5, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel2.pack(expand = True)
                else: # 토
                    if now.weekday() == self.SUN or now.weekday() == self.MON or now.weekday() == self.TUE or now.weekday() == self.WED\
                            or now.weekday() == self.THU or now.weekday() == self.FRI\
                            or now.isocalendar()[:2] != startStudyingTime.isocalendar()[:2]:
                        breakLoop = True
                        break
                    if startStudyingTime.weekday() == endStudyingTime.weekday():
                        studyingFrame: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight: int = int(14 / 3600 * (endStudyingTime - startStudyingTime).total_seconds())
                        studyingFrame.config(width = 50, height = studyingFrameHeight)
                        studyingFrame.place(x = 350, y = int(14 + 14 / 3600\
                                * (startStudyingTime.hour * 3600 + startStudyingTime.minute * 60 + startStudyingTime.second)))
                        studyingFrame.pack_propagate(False)
                        if studyingFrameHeight >= 14:
                            subjectLabel: Label = Label(studyingFrame, text = subjectTextInLabel, font = ('Arial', 6, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel.pack(expand = True)
                    else:
                        studyingFrame: Frame = Frame(self, bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                        studyingFrameHeight: int = int(14 / 3600 * (endStudyingTime.hour * 3600 + endStudyingTime.minute * 60 + endStudyingTime.second))
                        studyingFrame.config(width = 50, height = studyingFrameHeight)
                        studyingFrame.place(x = 50, y = 14)
                        studyingFrame.pack_propagate(False)
                        if studyingFrameHeight >= 14:
                            subjectLabel: Label = Label(studyingFrame, text = subjectTextInLabel, font = ('Arial', 6, 'bold'), bg = self.COLOR_LIST[colorIndex], borderwidth = 0)
                            subjectLabel.pack(expand = True)
            if breakLoop:
                break

if DEBUG:
    window: Tk = Tk()
    window.title('Time Table Frame')
    window.geometry('400x350')

    testUser: User = User()
    testUser.setSubjectList(['국어', '수학', '영어'])
    testUser.setStudyDataList([\
            StudyData(dt.datetime(2025, 12, 29), '영어', [[dt.datetime(2025, 12, 29, 17, 0, 0), dt.datetime(2025, 12, 29, 20, 0, 0)]]),\
            StudyData(dt.datetime(2026, 1, 4), '프로그래밍 기초', [[dt.datetime(2026, 1, 4, 18, 0, 0), dt.datetime(2026, 1, 4, 21, 30, 0)]]),\
            StudyData(dt.datetime(2026, 1, 6), '국어', [[dt.datetime(2026, 1, 6, 16, 30, 0), dt.datetime(2026, 1, 7, 2, 0, 0)],\
                                                        [dt.datetime(2026, 1, 7, 2, 30, 0), dt.datetime(2026, 1, 7, 3, 0, 0)]])\
    ])

    timeTableFrame: TimeTableFrame = TimeTableFrame(window, testUser)
    timeTableFrame.place(x = 0, y = 0)

    window.mainloop()
