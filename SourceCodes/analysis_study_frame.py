# 학습 분석 관련 모듈

from tkinter import *
from tkinter import messagebox
from user import *
from analysis_study import *
from menu_button import MenuButton

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

class InputDayCountFrame(Frame): # 학습 데이터의 범위를 입력받는 프레임
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 250, height = 150, bg = '#E9F1FA', borderwidth = 0)

        # 프레임 닫는 기능
        exitButton: Button = Button(self, text = 'X', font = ('Arial', 9, 'bold'), bg = '#E9F1FA', fg = 'blue',\
                activebackground = '#E9F1FA', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.closeFrame(misc))
        exitButton.place(x = 225, y = 10)

        infoLabel: Label = Label(self, text = '표시할 날짜 수를 입력하세요.', font = ('Arial', 12, 'bold'), bg = '#E9F1FA', borderwidth = 0)
        infoLabel.place(x = 20, y = 25)

        self.__dayCountEntry: Entry = Entry(self, font = ('Arial', 12), bg = 'white', width = 15)
        self.__dayCountEntry.place(x = 55, y = 65)

        okButton: Button = Button(self, text = '확인', font = ('Arial', 10, 'bold'), bg = 'white', width = 5,\
                borderwidth = 1, command = lambda: self.applyDayCount(misc))
        okButton.place(x = 98, y = 95)

    def applyDayCount(self, misc: Misc) -> None: # 입력 날짜 수를 적용하는 메소드
        if not self.__dayCountEntry.get().strip():
            messagebox.showwarning('경고', '날짜 수를 입력하세요.')
        else:
            try:
                dayCount: int = int(self.__dayCountEntry.get())
                if dayCount < 2 or dayCount > 1000:
                    messagebox.showwarning('경고', '날짜 수는 2 이상 1000 이하로 입력하세요.')
                else:
                    self.destroy()
                    misc.setCustomDayCount(dayCount)
                    misc.showGraphOfStudyData(misc.getDataType(), misc.DAYS_OF_CUSTOM, misc.getClassification())
            except ValueError:
                messagebox.showwarning('경고', '날짜 수는 정수로 입력하세요.')

    def closeFrame(self, misc: Misc) -> None: # 현재 창을 닫는 메소드
        misc.setStateOfButtons()
        self.destroy()

class StudyDataFrame(Frame): # 지정 날짜의 학습 기록을 보여주는 프레임
    def __init__(self, misc: Misc, studyDataList: list[StudyData], year: int, month: int, day: int) -> None:
        super().__init__(misc, width = 400, height = 350, bg = '#F0F7FF', borderwidth = 0)

        # 프레임 닫는 기능
        exitButton: Button = Button(self, text = 'X', font = ('Arial', 9, 'bold'), bg = '#F0F7FF', fg = 'blue',\
                activebackground = '#F0F7FF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.destroy())
        exitButton.place(x = 375, y = 10)

        indexTuple: tuple[int] = searchStudyData(studyDataList, year, month, day)
        self.__studyDataList: list[StudyData] = [] # 지정 날짜의 학습 데이터를 저장하고 있는 리스트
        for i in range(indexTuple[0], indexTuple[1] + 1):
            self.__studyDataList.append(studyDataList[i])
        self.__studyDataIndex: int = 0 # 보여줄 학습 데이터와 관련된 인덱스

        self.__studyData: StudyData = self.__studyDataList[self.__studyDataIndex]
        dateLabel: Label = Label(self, text = '{}/{}/{}'.format(self.__studyData.getStudyDate().year, self.__studyData.getStudyDate().month,\
                self.__studyData.getStudyDate().day), font = ('Arial', 14, 'bold'), width = 15, bg = '#F0F7FF', borderwidth = 0)
        dateLabel.place(x = 107, y = 25)

        subject: str = self.__studyData.getSubject() # 과목
        startedStudyDate: dt.datetime = self.getStartedStudyDate() # 학습 시작 일시
        finishedStudyDate: dt.datetime = self.getFinishedStudyDate() # 학습 종료 일시
        studyingTime: int = self.getStudyingTime() # 학습 시간
        breakTime: int = self.getBreakTime() # 휴식 시간
        targetStudyingTime: int = self.getTargetStudyingTime() # 목표 학습 시간
        self.__subjectLabel: Label = Label(self, text = '과목: {}'.format(subject), font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
        self.__startedStudyDateLabel: Label = Label(self, text = '학습 시작: {}/{}/{} {:02d}:{:02d}:{:02d}'.format(startedStudyDate.year, startedStudyDate.month,\
                startedStudyDate.day, startedStudyDate.hour, startedStudyDate.minute, startedStudyDate.second),\
                font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
        self.__finishedStudyDateLabel: Label = Label(self, text = '학습 종료: {}/{}/{} {:02d}:{:02d}:{:02d}'.format(finishedStudyDate.year, finishedStudyDate.month,\
                finishedStudyDate.day, finishedStudyDate.hour, finishedStudyDate.minute, finishedStudyDate.second),\
                font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
        self.__studyingTimeLabel: Label = Label(self, text = '학습 시간: {:02d}:{:02d}:{:02d}'\
                .format(studyingTime // 3600, (studyingTime % 3600) // 60, studyingTime % 60), font = ('Arial', 11, 'bold'),\
                bg = '#F0F7FF', borderwidth = 0)
        self.__breakTimeLabel: Label = Label(self, text = '휴식 시간: {:02d}:{:02d}:{:02d}'\
                .format(breakTime // 3600, (breakTime % 3600) // 60, breakTime % 60), font = ('Arial', 11, 'bold'),\
                bg = '#F0F7FF', borderwidth = 0)
        self.__targetStudyingTimeLabel: Label = Label(self, text = '목표 학습 시간: {:02d}:{:02d}:{:02d}'\
                .format(targetStudyingTime // 3600, (targetStudyingTime % 3600) // 60, targetStudyingTime % 60), font = ('Arial', 11, 'bold'),\
                bg = '#F0F7FF', borderwidth = 0)
        self.__detailText: Text = Text(self, font = ('Arial', 11, 'normal'), bg = 'white', width = 34, height = 7, state = 'disabled', borderwidth = 0)
        self.updateDetailText()
        
        self.__subjectLabel.place(x = 60, y = 60)
        self.__startedStudyDateLabel.place(x = 60, y = 85)
        self.__finishedStudyDateLabel.place(x = 60, y = 110)
        self.__targetStudyingTimeLabel.place(x = 60, y = 135)
        self.__studyingTimeLabel.place(x = 60, y = 160); self.__breakTimeLabel.place(x = 205, y = 160)
        self.__detailText.place(x = 60, y = 185)

        self.__goPreviousSectionButton: Button = Button(self, text = '<', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', fg = 'blue',\
                activebackground = '#F0F7FF', activeforeground = 'yellow', disabledforeground = 'steel blue',\
                borderwidth = 0, command = lambda: self.goPreviousSection())
        self.__goPreviousSectionButton.config(state = 'disabled')
        self.__goNextSectionButton: Button = Button(self, text = '>', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', fg = 'blue',\
                activebackground = '#F0F7FF', activeforeground = 'yellow', disabledforeground = 'steel blue',\
                borderwidth = 0, command = lambda: self.goNextSection())
        if self.__studyDataIndex == len(self.__studyDataList) - 1:
            self.__goNextSectionButton.config(state = 'disabled')
        self.__goPreviousSectionButton.place(x = 22, y = 160); self.__goNextSectionButton.place(x = 357, y = 160)

    def updateDetailText(self) -> None: # 세부 학습 정보 텍스트 업데이트
        studyingTimeList: list[list[dt.datetime]] = self.__studyData.getStudyingTimeList()

        self.__detailText.config(state = 'normal')
        self.__detailText.delete('1.0', END)
        self.__detailText.insert(END, '-------------------- 세부 사항 --------------------\n')
        for i in range(len(studyingTimeList)):
            startStudyingTime: dt.datetime = studyingTimeList[i][0] # 학습 시작 시간
            endStudyingTime: dt.datetime = studyingTimeList[i][1] # 학습 종료 시간
            self.__detailText.insert(END, '학습: {}/{}/{} {:02d}:{:02d}:{:02d}\n'\
                    .format(startStudyingTime.year, startStudyingTime.month, startStudyingTime.day,\
                    startStudyingTime.hour, startStudyingTime.minute, startStudyingTime.second))
            if i == len(studyingTimeList) - 1:
                self.__detailText.insert(END, '종료: {}/{}/{} {:02d}:{:02d}:{:02d}'\
                        .format(endStudyingTime.year, endStudyingTime.month, endStudyingTime.day,\
                        endStudyingTime.hour, endStudyingTime.minute, endStudyingTime.second))
            else:
                self.__detailText.insert(END, '휴식: {}/{}/{} {:02d}:{:02d}:{:02d}\n'\
                        .format(endStudyingTime.year, endStudyingTime.month, endStudyingTime.day,\
                        endStudyingTime.hour, endStudyingTime.minute, endStudyingTime.second))
        self.__detailText.config(state = 'disabled')

    def getStartedStudyDate(self) -> dt.datetime: # 학습 시작 일시를 구하는 메소드
        studyingTimeList: list[list[dt.datetime]] = self.__studyData.getStudyingTimeList()
        return studyingTimeList[0][0]

    def getFinishedStudyDate(self) -> dt.datetime: # 학습 종료 일시를 구하는 메소드
        studyingTimeList: list[list[dt.datetime]] = self.__studyData.getStudyingTimeList()
        return studyingTimeList[len(studyingTimeList) - 1][1]

    def getTargetStudyingTime(self) -> int: # 목표 학습 시간을 구하는 메소드
        return self.__studyData.getTargetStudyingTime()

    def getStudyingTime(self) -> int: # 학습 시간을 구하는 메소드
        studyingTime: int = 0
        studyingTimeList: list[list[dt.datetime]] = self.__studyData.getStudyingTimeList()
        for i in range(len(studyingTimeList)):
            startStudyingTime: dt.datetime = studyingTimeList[i][0] # 학습 시작 시간
            endStudyingTime: dt.datetime = studyingTimeList[i][1] # 학습 종료 시간
            studyingTime += int((endStudyingTime - startStudyingTime).total_seconds())
        return studyingTime

    def getBreakTime(self) -> int: # 휴식 시간을 구하는 메소드
        breakTime: int = 0
        studyingTimeList: list[list[dt.datetime]] = self.__studyData.getStudyingTimeList()
        if len(studyingTimeList) >= 2:
            for i in range(1, len(studyingTimeList), 1):
                previousEndStudyingTime: dt.datetime = studyingTimeList[i - 1][1] # 휴식 전 학습 종료 시간
                nextStartStudyingTime: dt.datetime = studyingTimeList[i][0] # 휴식 후 학습 시작 시간
                breakTime += int((nextStartStudyingTime - previousEndStudyingTime).total_seconds())
        return breakTime

    def updateStudyDataInfo(self) -> None: # 학습 데이터 정보를 업데이트하는 메소드
        self.__studyData: StudyData = self.__studyDataList[self.__studyDataIndex]

        subject: str = self.__studyData.getSubject() # 과목
        startedStudyDate: dt.datetime = self.getStartedStudyDate() # 학습 시작 일시
        finishedStudyDate: dt.datetime = self.getFinishedStudyDate() # 학습 종료 일시
        studyingTime: int = self.getStudyingTime() # 학습 시간
        breakTime: int = self.getBreakTime() # 휴식 시간
        targetStudyingTime: int = self.getTargetStudyingTime() # 목표 학습 시간
        self.__subjectLabel.config(text = '과목: {}'.format(subject))
        self.__startedStudyDateLabel.config(text = '학습 시작: {}/{}/{} {:02d}:{:02d}:{:02d}'.format(startedStudyDate.year, startedStudyDate.month,\
                startedStudyDate.day, startedStudyDate.hour, startedStudyDate.minute, startedStudyDate.second))
        self.__finishedStudyDateLabel.config(text = '학습 종료: {}/{}/{} {:02d}:{:02d}:{:02d}'.format(finishedStudyDate.year, finishedStudyDate.month,\
                finishedStudyDate.day, finishedStudyDate.hour, finishedStudyDate.minute, finishedStudyDate.second))
        self.__studyingTimeLabel.config(text = '학습 시간: {:02d}:{:02d}:{:02d}'\
                .format(studyingTime // 3600, (studyingTime % 3600) // 60, studyingTime % 60), font = ('Arial', 11, 'bold'))
        self.__breakTimeLabel.config(text = '휴식 시간: {:02d}:{:02d}:{:02d}'\
                .format(breakTime // 3600, (breakTime % 3600) // 60, breakTime % 60), font = ('Arial', 11, 'bold'))
        self.__targetStudyingTimeLabel.config(text = '목표 학습 시간: {:02d}:{:02d}:{:02d}'\
                .format(targetStudyingTime // 3600, (targetStudyingTime % 3600) // 60, targetStudyingTime % 60), font = ('Arial', 11, 'bold'))
        self.updateDetailText()

    def goPreviousSection(self) -> None: # 지정 날짜에서, 이전 학습 데이터로 넘어가는 메소드
        self.__goNextSectionButton.config(state = 'normal')

        self.__studyDataIndex -= 1
        self.updateStudyDataInfo()

        if self.__studyDataIndex == 0:
            self.__goPreviousSectionButton.config(state = 'disabled')

    def goNextSection(self) -> None: # 지정 날짜에서, 다음 학습 데이터로 넘어가는 메소드
        self.__goPreviousSectionButton.config(state = 'normal')

        self.__studyDataIndex += 1
        self.updateStudyDataInfo()

        if self.__studyDataIndex == len(self.__studyDataList) - 1:
            self.__goNextSectionButton.config(state = 'disabled')

class StudyCalendarFrame(Frame): # 학습 캘린더 프레임
    MON: int = 0; TUE: int = 1; WED: int = 2; THU: int = 3; FRI: int = 4; SAT: int = 5; SUN: int = 6

    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 400, height = 350, borderwidth = 0)
        self.__user: User = user

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/study_calendar_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 400, height = 350, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 캘린더 구성
        self.__date: dt.datetime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, 1)

        self.__monthLabel: Label = Label(self, text = '{}년 {}월'.format(self.__date.year, self.__date.month), font = ('Arial', 14, 'bold'), width = 15, bg = '#F0F7FF')
        self.__monthLabel.place(x = 108, y = 17)

        self.__goPreviousMonthButton: Button = Button(self, text = '<', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', fg = 'blue',\
                activebackground = '#F0F7FF', activeforeground = 'yellow', disabledforeground = 'steel blue',\
                borderwidth = 0, command = lambda: self.goPreviousMonth())
        if self.__date.year == 2000 and self.__date.month == 1:
            self.__goPreviousMonthButton.config(state = 'disabled')
        self.__goNextMonthButton: Button = Button(self, text = '>', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', fg = 'blue',\
                activebackground = '#F0F7FF', activeforeground = 'yellow', disabledforeground = 'steel blue',\
                borderwidth = 0, command = lambda: self.goNextMonth())
        self.__goPreviousMonthButton.place(x = 120, y = 18); self.__goNextMonthButton.place(x = 262, y = 18)
        if self.__date.year == 9999 and self.__date.month == 12:
            self.__goNextMonthButton.config(state = 'disabled')

        self.__dayFrameList: list[Frame] = []
        self.showCalendar(self.__date.year, self.__date.month)

    def showCalendar(self, year: int, month: int) -> None: # 캘린더 패널을 보여주는 메소드
        self.__monthLabel.config(text = '{}년 {}월'.format(year, month))

        for i in range(len(self.__dayFrameList)):
            self.__dayFrameList[i].destroy()
        self.__dayFrameList.clear()

        daysOfMonth: int = 0 # 한 달의 날짜 수
        date: dt.datetime = dt.datetime(year, month, 1)
        if date.month == 12:
            daysOfMonth += (dt.datetime(date.year + 1, 1, 1).date() - dt.datetime(date.year, 12, 1).date()).days
        else:
            daysOfMonth += (dt.datetime(date.year, date.month + 1, 1).date() - dt.datetime(date.year, date.month, 1).date()).days

        xPositionList: list[int] = [25, 76, 127, 177, 228, 278, 329]
        yPositionList: list[int] = [88, 128, 169, 209, 250, 291]
        for i in range(daysOfMonth):
            indexTuple: tuple[int] = searchStudyData(self.__user.getStudyDataList(), date.year, date.month, i + 1)
            dayFrame: Frame = Frame(self, width = 46, height = 35, bg = 'white', borderwidth = 0)
            dayLabel: Label = Label(dayFrame, text = '{}'.format(i + 1), font = ('Arial', 9, 'bold'), bg = 'white', borderwidth = 0)
            if indexTuple != (-1, -1):
                dayFrame.config(bg = '#00F7CF')
                dayLabel.config(bg = '#00F7CF')

                arrowButton: Button = Button(dayFrame, text = '→', font = ('Arial', 13, 'bold'), bg = '#00F7CF',\
                        activebackground = '#00F7CF', activeforeground = 'white', width = 2, borderwidth = 0,\
                        command = lambda day = i + 1: self.openStudyDataFrame(date.year, date.month, day))
                arrowButton.place(x = 19, y = 3)
            dayLabel.place(x = 2, y = 0)
            self.__dayFrameList.append(dayFrame)
        for i in range((dt.datetime(date.year, date.month, 1).weekday() + 1) % 7):
            dayFrame: Frame = Frame(self, width = 46, height = 35, bg = 'light gray', borderwidth = 0)
            dayLabel: Label = Label(dayFrame, text = '{}'.format((dt.datetime(date.year, date.month, 1).date() - dt.timedelta(days = i + 1)).day),\
                    font = ('Arial', 9, 'bold'), bg = 'light gray', fg = 'gray', borderwidth = 0)
            dayLabel.place(x = 2, y = 0)
            self.__dayFrameList.insert(0, dayFrame)
        leftDaysOnCalendar: int = 42 - len(self.__dayFrameList)
        for i in range(leftDaysOnCalendar):
            dayFrame: Frame = Frame(self, width = 46, height = 35, bg = 'light gray', borderwidth = 0)
            dayLabel: Label = Label(dayFrame, text = '{}'.format(i + 1),\
                    font = ('Arial', 9, 'bold'), bg = 'light gray', fg = 'gray', borderwidth = 0)
            dayLabel.place(x = 2, y = 0)
            self.__dayFrameList.append(dayFrame)

        xPositionIndex: int = 0
        yPositionIndex: int = 0
        for i in range(len(self.__dayFrameList)):
            self.__dayFrameList[i].place(x = xPositionList[xPositionIndex], y = yPositionList[yPositionIndex])
            xPositionIndex = (xPositionIndex + 1) % 7
            if xPositionIndex == 0:
                yPositionIndex += 1

    def goPreviousMonth(self) -> None: # 이전 달의 갤린더로 넘어가는 메소드
        self.__goNextMonthButton.config(state = 'normal')
        
        year: int = self.__date.year; month: int = self.__date.month
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
        self.__date = dt.datetime(year, month, 1)
        self.showCalendar(self.__date.year, self.__date.month)

        if self.__date.year == 2000 and self.__date.month == 1:
            self.__goPreviousMonthButton.config(state = 'disabled')

    def goNextMonth(self) -> None: # 다음 달의 캘린더로 넘어가는 메소드
        self.__goPreviousMonthButton.config(state = 'normal')

        year: int = self.__date.year; month: int = self.__date.month
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        self.__date = dt.datetime(year, month, 1)
        self.showCalendar(self.__date.year, self.__date.month)

        if self.__date.year == 9999 and self.__date.month == 12:
            self.__goNextMonthButton.config(state = 'disabled')

    def openStudyDataFrame(self, year: int, month: int, day: int) -> None: # 지정 날짜의 학습 기록 프레임을 여는 메소드
        studyDataFrame: StudyDataFrame = StudyDataFrame(self, self.__user.getStudyDataList(), year, month, day)
        studyDataFrame.place(x = 0, y = 0)

class AnalysisStudyFrame(Frame):
    # 학습 데이터의 종류
    STUDYING_TIME: int = 0; BREAK_TIME: int = 1; FOCUS_RATE: int = 2; CALENDAR: int = 3

    # 학습 데이터의 범위
    DAYS_OF_WEEK: int = 0; DAYS_OF_MONTH: int = 1; DAYS_OF_THREE_MONTHS: int = 2; DAYS_OF_SIX_MONTHS: int = 3
    DAYS_OF_YEAR: int = 4; DAYS_OF_CUSTOM: int = 5

    # 분류 기준
    PER_DAYS: int = 0; PER_SUBJECTS: int = 1

    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)
        self.__user: User = user

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/analysis_study_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 홈', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goBack(misc))
        goBackButton.place(x = 10, y = 10)

        # 각종 학습 데이터 지표
        self.__dataType: int = self.STUDYING_TIME # 보여줄 학습 데이터의 종류
        self.__dataRange: int = self.DAYS_OF_WEEK # 보여줄 학습 데이터의 범위
        self.__classification: int = self.PER_DAYS # 보여줄 분류 기준
        self.__customDayCount: int = 0 # 보여줄 학습 데이터의 날짜 수
        # 1. 학습 데이터의 종류
        self.__studyingTimeButton: MenuButton = MenuButton(self, buttonText = '학습 시간', buttonBackground = '#C1DDFF',\
                buttonForeground = 'yellow', activeForeground = 'yellow', buttonCommand = lambda: None)
        self.__breakTimeButton: MenuButton = MenuButton(self, buttonText = '휴식 시간', buttonBackground = '#C1DDFF',\
                buttonForeground = 'black', activeForeground = 'yellow',\
                buttonCommand = lambda: self.showGraphOfStudyData(self.BREAK_TIME, self.__dataRange, self.__classification))
        self.__focusRateButton: MenuButton = MenuButton(self, buttonText = '집중도', buttonBackground = '#C1DDFF',\
                buttonForeground = 'black', activeForeground = 'yellow',\
                buttonCommand = lambda: self.showGraphOfStudyData(self.FOCUS_RATE, self.__dataRange, self.__classification))
        self.__calendarButton: MenuButton = MenuButton(self, buttonText = '캘린더', buttonBackground = '#C1DDFF',\
                buttonForeground = 'black', activeForeground = 'yellow',\
                buttonCommand = lambda: self.showCalendar())

        self.__studyingTimeButton.place(x = 60, y = 147)
        self.__breakTimeButton.place(x = 150, y = 147)
        self.__focusRateButton.place(x = 240, y = 147)
        self.__calendarButton.place(x = 310, y = 147)

        # 2. 학습 데이터의 범위
        self.__daysOfWeekButton: MenuButton = MenuButton(self, buttonText = '7일', buttonBackground = 'white',\
                buttonForeground = '#C1DDFF', activeForeground = '#C1DDFF', buttonCommand = lambda: None)
        self.__daysOfMonthButton: MenuButton = MenuButton(self, buttonText = '30일', buttonBackground = 'white',\
                buttonForeground = 'black', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: self.showGraphOfStudyData(self.__dataType, self.DAYS_OF_MONTH, self.__classification))
        self.__daysOfThreeMonthsButton: MenuButton = MenuButton(self, buttonText = '90일', buttonBackground = 'white',\
                buttonForeground = 'black', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: self.showGraphOfStudyData(self.__dataType, self.DAYS_OF_THREE_MONTHS, self.__classification))
        self.__daysOfSixMonthsButton: MenuButton = MenuButton(self, buttonText = '180일', buttonBackground = 'white',\
                buttonForeground = 'black', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: self.showGraphOfStudyData(self.__dataType, self.DAYS_OF_SIX_MONTHS, self.__classification))
        self.__daysOfYearButton: MenuButton = MenuButton(self, buttonText = '365일', buttonBackground = 'white',\
                buttonForeground = 'black', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: self.showGraphOfStudyData(self.__dataType, self.DAYS_OF_YEAR, self.__classification))
        self.__daysOfCustomButton: MenuButton = MenuButton(self, buttonText = '사용자화', buttonBackground = 'white',\
                buttonForeground = 'black', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: self.openInputDayCountFrame())

        self.__daysOfWeekButton.config(width = 6)
        self.__daysOfMonthButton.config(width = 6)
        self.__daysOfThreeMonthsButton.config(width = 6)
        self.__daysOfSixMonthsButton.config(width = 6)
        self.__daysOfYearButton.config(width = 6)
        self.__daysOfCustomButton.config(width = 6)

        self.__daysOfWeekButton.place(x = 61, y = 191)
        self.__daysOfMonthButton.place(x = 61, y = 221)
        self.__daysOfThreeMonthsButton.place(x = 61, y = 251)
        self.__daysOfSixMonthsButton.place(x = 61, y = 281)
        self.__daysOfYearButton.place(x = 61, y = 311)
        self.__daysOfCustomButton.place(x = 61, y = 341)

        # 3. 분류 기준
        self.__perDaysButton: MenuButton = MenuButton(self, buttonText = '날짜별', buttonBackground = 'white',\
                buttonForeground = '#C1DDFF', activeForeground = '#C1DDFF', buttonCommand = lambda: None)
        self.__perSubjectsButton: MenuButton = MenuButton(self, buttonText = '과목별', buttonBackground = 'white',\
                buttonForeground = 'black', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: self.showGraphOfStudyData(self.__dataType, self.__dataRange, self.PER_SUBJECTS))

        self.__perDaysButton.config(width = 6)
        self.__perSubjectsButton.config(width = 6)

        self.__perDaysButton.place(x = 61, y = 481)
        self.__perSubjectsButton.place(x = 61, y = 511)

        makeGraphOfStudyingTimePerDays(self.__user, (4, 3.5), 100, 7, 'normal')
        self.__graphOfStudyDataPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Graphs/studying_time_per_days_graph.png'.format(path))
        self.__graphOfStudyDataLabel: Label = Label(self, borderwidth = 0, image = self.__graphOfStudyDataPhotoImage)
        self.__graphOfStudyDataLabel.place(x = 140, y = 190)

        self.__studyCalendarFrame: StudyCalendarFrame = None # 캘린더 프레임

    ################################ Getter/Setter ####################################
    def getDataType(self) -> int:
        return self.__dataType

    def setCustomDayCount(self, customDayCount: int) -> None:
        self.__customDayCount = customDayCount

    def getClassification(self) -> int:
        return self.__classification
    ####################################################################################

    def setStateOfButtons(self) -> None: # 각 메뉴 버튼의 상태를 설정하는 메소드
        self.__studyingTimeButton.setButtonForeground('black')
        self.__studyingTimeButton.config(command = lambda: self.showGraphOfStudyData(self.STUDYING_TIME, self.__dataRange, self.__classification))
        self.__breakTimeButton.setButtonForeground('black')
        self.__breakTimeButton.config(command = lambda: self.showGraphOfStudyData(self.BREAK_TIME, self.__dataRange, self.__classification))
        self.__focusRateButton.setButtonForeground('black')
        self.__focusRateButton.config(command = lambda: self.showGraphOfStudyData(self.FOCUS_RATE, self.__dataRange, self.__classification))
        self.__calendarButton.setButtonForeground('black')
        self.__calendarButton.config(command = lambda: self.showCalendar())

        self.__daysOfWeekButton.setButtonForeground('black')
        self.__daysOfWeekButton.config(command = lambda: self.showGraphOfStudyData(self.__dataType, self.DAYS_OF_WEEK, self.__classification))
        self.__daysOfMonthButton.setButtonForeground('black')
        self.__daysOfMonthButton.config(command = lambda: self.showGraphOfStudyData(self.__dataType, self.DAYS_OF_MONTH, self.__classification))
        self.__daysOfThreeMonthsButton.setButtonForeground('black')
        self.__daysOfThreeMonthsButton.config(command = lambda: self.showGraphOfStudyData(self.__dataType, self.DAYS_OF_THREE_MONTHS, self.__classification))
        self.__daysOfSixMonthsButton.setButtonForeground('black')
        self.__daysOfSixMonthsButton.config(command = lambda: self.showGraphOfStudyData(self.__dataType, self.DAYS_OF_SIX_MONTHS, self.__classification))
        self.__daysOfYearButton.setButtonForeground('black')
        self.__daysOfYearButton.config(command = lambda: self.showGraphOfStudyData(self.__dataType, self.DAYS_OF_YEAR, self.__classification))
        self.__daysOfCustomButton.config(command = lambda: self.openInputDayCountFrame())

        self.__perDaysButton.setButtonForeground('black')
        self.__perDaysButton.config(command = lambda: self.showGraphOfStudyData(self.__dataType, self.__dataRange, self.PER_DAYS))
        self.__perSubjectsButton.setButtonForeground('black')
        self.__perSubjectsButton.config(command = lambda: self.showGraphOfStudyData(self.__dataType, self.__dataRange, self.PER_SUBJECTS))

        if self.__dataType == self.STUDYING_TIME:
            self.__studyingTimeButton.setButtonForeground('yellow')
            self.__studyingTimeButton.config(command = lambda: None)
        elif self.__dataType == self.BREAK_TIME:
            self.__breakTimeButton.setButtonForeground('yellow')
            self.__breakTimeButton.config(command = lambda: None)
        elif self.__dataType == self.FOCUS_RATE:
            self.__focusRateButton.setButtonForeground('yellow')
            self.__focusRateButton.config(command = lambda: None)
        else:
            self.__calendarButton.setButtonForeground('yellow')
            self.__calendarButton.config(command = lambda: None)

        if self.__dataType == self.CALENDAR:
            self.__daysOfWeekButton.config(command = lambda: None)
            self.__daysOfMonthButton.config(command = lambda: None)
            self.__daysOfThreeMonthsButton.config(command = lambda: None)
            self.__daysOfSixMonthsButton.config(command = lambda: None)
            self.__daysOfYearButton.config(command = lambda: None)
            self.__daysOfCustomButton.config(command = lambda: None)

            self.__perDaysButton.config(command = lambda: None)
            self.__perSubjectsButton.config(command = lambda: None)
        else:
            if self.__dataRange == self.DAYS_OF_WEEK:
                self.__daysOfWeekButton.setButtonForeground('#C1DDFF')
                self.__daysOfWeekButton.config(command = lambda: None)
            elif self.__dataRange == self.DAYS_OF_MONTH:
                self.__daysOfMonthButton.setButtonForeground('#C1DDFF')
                self.__daysOfMonthButton.config(command = lambda: None)
            elif self.__dataRange == self.DAYS_OF_THREE_MONTHS:
                self.__daysOfThreeMonthsButton.setButtonForeground('#C1DDFF')
                self.__daysOfThreeMonthsButton.config(command = lambda: None)
            elif self.__dataRange == self.DAYS_OF_SIX_MONTHS:
                self.__daysOfSixMonthsButton.setButtonForeground('#C1DDFF')
                self.__daysOfSixMonthsButton.config(command = lambda: None)
            elif self.__dataRange == self.DAYS_OF_YEAR:
                self.__daysOfYearButton.setButtonForeground('#C1DDFF')
                self.__daysOfYearButton.config(command = lambda: None)

            if self.__classification == self.PER_DAYS:
                self.__perDaysButton.setButtonForeground('#C1DDFF')
                self.__perDaysButton.config(command = lambda: None)
            else:
                self.__perSubjectsButton.setButtonForeground('#C1DDFF')
                self.__perSubjectsButton.config(command = lambda: None)

    def openInputDayCountFrame(self) -> None: # 학습 데이터 입력 프레임을 여는 메소드
        self.__studyingTimeButton.config(command = lambda: None)
        self.__breakTimeButton.config(command = lambda: None)
        self.__focusRateButton.config(command = lambda: None)
        self.__calendarButton.config(command = lambda: None)

        self.__daysOfWeekButton.config(command = lambda: None)
        self.__daysOfMonthButton.config(command = lambda: None)
        self.__daysOfThreeMonthsButton.config(command = lambda: None)
        self.__daysOfSixMonthsButton.config(command = lambda: None)
        self.__daysOfYearButton.config(command = lambda: None)
        self.__daysOfCustomButton.config(command = lambda: None)

        self.__perDaysButton.config(command = lambda: None)
        self.__perSubjectsButton.config(command = lambda: None)

        inputDayCountFrame: InputDayCountFrame = InputDayCountFrame(self)
        inputDayCountFrame.place(x = 175, y = 225)

    def showGraphOfStudyData(self, dataType: int, dataRange: int, classification: int) -> None: # 학습 데이터 그래프를 보여주는 메소드
        self.__dataType = dataType
        self.__dataRange = dataRange
        self.__classification = classification
        self.setStateOfButtons()

        dayCount: int = 0
        if self.__dataRange == self.DAYS_OF_WEEK: # 1주일
            dayCount = 7
        elif self.__dataRange == self.DAYS_OF_MONTH: # 1개월
            dayCount = 30
        elif self.__dataRange == self.DAYS_OF_THREE_MONTHS: # 3개월
            dayCount = 90
        elif self.__dataRange == self.DAYS_OF_SIX_MONTHS: # 6개월
            dayCount = 180
        elif self.__dataRange == self.DAYS_OF_YEAR: # 1년
            dayCount = 365
        else: # 사용자 지정
            dayCount = self.__customDayCount

        if self.__studyCalendarFrame != None:
            self.__studyCalendarFrame.destroy()
        if self.__dataType == self.STUDYING_TIME:
            self.__graphOfStudyDataLabel.place_forget()
            if self.__classification == self.PER_DAYS:
                makeGraphOfStudyingTimePerDays(self.__user, (4, 3.5), 100, dayCount, 'normal')
                self.__graphOfStudyDataPhotoImage.config(file = '{}/Images/Graphs/studying_time_per_days_graph.png'.format(path))
            else:
                makeGraphOfStudyingTimePerSubjects(self.__user, (4, 3.5), 100, dayCount)
                self.__graphOfStudyDataPhotoImage.config(file = '{}/Images/Graphs/studying_time_per_subjects_graph.png'.format(path))
            self.__graphOfStudyDataLabel.place(x = 140, y = 190)
        elif self.__dataType == self.BREAK_TIME:
            self.__graphOfStudyDataLabel.place_forget()
            if self.__classification == self.PER_DAYS:
                makeGraphOfBreakTimePerDays(self.__user, (4, 3.5), 100, dayCount, 'normal')
                self.__graphOfStudyDataPhotoImage.config(file = '{}/Images/Graphs/break_time_per_days_graph.png'.format(path))
            else:
                makeGraphOfBreakTimePerSubjects(self.__user, (4, 3.5), 100, dayCount)
                self.__graphOfStudyDataPhotoImage.config(file = '{}/Images/Graphs/break_time_per_subjects_graph.png'.format(path))
            self.__graphOfStudyDataLabel.place(x = 140, y = 190)
        elif self.__dataType == self.FOCUS_RATE:
            self.__graphOfStudyDataLabel.place_forget()
            if self.__classification == self.PER_DAYS:
                makeGraphOfFocusRatePerDays(self.__user, (4, 3.5), 100, dayCount, 'normal')
                self.__graphOfStudyDataPhotoImage.config(file = '{}/Images/Graphs/focus_rate_per_days_graph.png'.format(path))
            else:
                makeGraphOfFocusRatePerSubjects(self.__user, (4, 3.5), 100, dayCount)
                self.__graphOfStudyDataPhotoImage.config(file = '{}/Images/Graphs/focus_rate_per_subjects_graph.png'.format(path))
            self.__graphOfStudyDataLabel.place(x = 140, y = 190)

    def showCalendar(self) -> None: # 캘린더를 보여주는 메소드
        self.__dataType = self.CALENDAR
        self.setStateOfButtons()

        self.__graphOfStudyDataLabel.place_forget()
        self.__studyCalendarFrame = StudyCalendarFrame(self, self.__user)
        self.__studyCalendarFrame.place(x = 140, y = 190)

    def goBack(self, misc: Misc) -> None: # 뒤로가기 메소드
        misc.showTimeTable()
        self.destroy()

if DEBUG:
    window: Tk = Tk()
    window.title('Analysis Study Frame')
    window.geometry('600x600')

    userList: SortedList[User] = SortedList()
    testUser: User = User()
    testUser.setSubjectList(['국어', '수학', '영어'])
    testUser.setStudyDataList([\
            StudyData(dt.datetime(2025, 12, 29), '영어', [[dt.datetime(2025, 12, 29, 17, 0, 0), dt.datetime(2025, 12, 29, 20, 0, 0)]]),\
            StudyData(dt.datetime(2026, 1, 4), '프로그래밍 기초', [[dt.datetime(2026, 1, 3, 23, 40, 0), dt.datetime(2026, 1, 4, 0, 20, 0)]]),\
            StudyData(dt.datetime(2026, 1, 6), '국어', [[dt.datetime(2026, 1, 6, 11, 30, 0), dt.datetime(2026, 1, 7, 0, 30, 0)],\
                                                        [dt.datetime(2026, 1, 7, 2, 30, 0), dt.datetime(2026, 1, 7, 2, 40, 0)]]),\
            StudyData(dt.datetime(2026, 1, 11), '사회', [[dt.datetime(2026, 1, 11, 8, 0, 0), dt.datetime(2026, 1, 11, 8, 0, 30)],\
                                                        [dt.datetime(2026, 1, 11, 8, 0, 40), dt.datetime(2026, 1, 11, 8, 1, 0)]]),\
            StudyData(dt.datetime(2026, 1, 11), '사회', [[dt.datetime(2026, 1, 11, 14, 0, 0), dt.datetime(2026, 1, 11, 14, 0, 30)]])\
    ])
    userList.add(testUser)
    setUserList(userList)

    analysisStudyFrame: AnalysisStudyFrame = AnalysisStudyFrame(window, testUser)
    analysisStudyFrame.place(x = 0, y = 0)

    window.mainloop()
