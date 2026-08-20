# 홈 화면 관련 모듈

from tkinter import *
import datetime as dt
from user import *
from menu_button import *
from notification_frame import NotificationFrame
from study_frame import StudyFrame
from time_table_frame import TimeTableFrame
from analysis_study_frame import *
from analysis_grades_frame import AnalysisGradesFrame
from reminder_frame import ReminderFrame
from calculator_frame import CalculatorFrame
from timer_frame import TimerFrame
from stopwatch_frame import StopwatchFrame
from user_frame import UserFrame

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

class ClockFrame(Frame): # 작은 시계를 표시하는 프레임
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 60, height = 25, borderwidth = 0, bg = '#EBFBFF')

        now: dt.datetime = dt.datetime.now()
        self.__timeLabel: Label = Label(self, text = '{:02d}:{:02d}:{:02d}'.format(now.hour, now.minute, now.second),\
                font = ('Arial', 11, 'bold'), bg = '#EBFBFF', borderwidth = 0)
        self.__timeLabel.place(x = 1, y = 2)

        self.setNextTime()

    def setNextTime(self) -> None: # 현재 시각을 계속 업데이트함.
        now: dt.datetime = dt.datetime.now()
        self.__timeLabel.config(text = '{:02d}:{:02d}:{:02d}'.format(now.hour, now.minute, now.second))

        self.after(1, lambda: self.setNextTime())

class HomeFrame(Frame):
    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)
        self.__user: User = user

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/home_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 알림 아이콘 설정
        notificationButton: NotificationButton = NotificationButton(self)
        notificationButton.place(x = 15, y = 15)

        # 상단 시계 설정
        clockFrame: ClockFrame = ClockFrame(self)
        clockFrame.place(x = 50, y = 17)

        # 메뉴바 설정
        startStudyButton: MenuButton = MenuButton(self, buttonText = '학습 시작', buttonBackground = '#C1DDFF',\
                buttonForeground = 'black', activeForeground = 'yellow', buttonCommand = lambda: self.openStudyFrame())
        analysisStudyButton: MenuButton = MenuButton(self, buttonText = '학습 분석', buttonBackground = '#C1DDFF',\
                buttonForeground = 'black', activeForeground = 'yellow', buttonCommand = lambda: self.openAnalysisStudyFrame())
        analysisGradesButton: MenuButton = MenuButton(self, buttonText = '성적 분석', buttonBackground = '#C1DDFF',\
                buttonForeground = 'black', activeForeground = 'yellow', buttonCommand = lambda: self.openAnalysisGradesFrame())
        reminderButton: MenuButton = MenuButton(self, buttonText = '리마인더', buttonBackground = '#C1DDFF',\
                buttonForeground = 'black', activeForeground = 'yellow', buttonCommand = lambda: self.openReminderFrame())
        toolsButton: ToolsButton = ToolsButton(self)
        userButton: UserButton = UserButton(self)

        startStudyButton.place(x = 60, y = 125)
        analysisStudyButton.place(x = 150, y = 125)
        analysisGradesButton.place(x = 240, y = 125)
        reminderButton.place(x = 325, y = 125)
        toolsButton.place(x = 410, y = 125)
        userButton.place(x = 511, y = 125)

        # 학습 시간표, 7일간 학습 시간 등 각종 데이터를 표시해주는 기능
        self.__shownDataIndex: int = 0 # 표시해주는 데이터를 구분하기 위한 인덱스
        # 1. 학습 시간표
        self.__timetableFrame: TimeTableFrame = TimeTableFrame(self, self.__user)
        self.__timetableFrame.place(x = 100, y = 177)
        # 2. 7일간 학습 시간
        makeGraphOfStudyingTimePerDays(self.__user, (4, 3.5), 100)
        self.__graphOfStudyingTimePerDaysPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Graphs/studying_time_per_days_graph.png'.format(path))
        self.__graphOfStudyingTimePerDaysLabel: Label = Label(self, borderwidth = 0, image = self.__graphOfStudyingTimePerDaysPhotoImage)
        # 3. 7일간 집중도
        makeGraphOfFocusRatePerDays(self.__user, (4, 3.5), 100)
        self.__graphOfFocusRatePerDaysPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Graphs/focus_rate_per_days_graph.png'.format(path))
        self.__graphOfFocusRatePerDaysLabel: Label = Label(self, borderwidth = 0, image = self.__graphOfFocusRatePerDaysPhotoImage)

        goLeftButton: Button = Button(self, text = '<', font = ('Arial', 11, 'bold'), bg = 'white', fg = 'blue',\
                activebackground = 'white', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goLeft())
        goRightButton: Button = Button(self, text = '>', font = ('Arial', 11, 'bold'), bg = 'white', fg = 'blue',\
                activebackground = 'white', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goRight())
        goLeftButton.place(x = 71, y = 338); goRightButton.place(x = 511, y = 338)

    def openNotificationFrame(self) -> None: # 알림 프레임을 여는 메소드
        notificationFrame: NotificationFrame = NotificationFrame(self, self.__user)
        notificationFrame.place(x = 0, y = 0)

    def openStudyFrame(self) -> None: # 학습 프레임을 여는 메소드
        studyFrame: StudyFrame = StudyFrame(self, self.__user)
        studyFrame.place(x = 0, y = 0)

    def openAnalysisStudyFrame(self) -> None: # 학습 분석 프레임을 여는 메소드
        analysisStudyFrame: AnalysisStudyFrame = AnalysisStudyFrame(self, self.__user)
        analysisStudyFrame.place(x = 0, y = 0)

    def openAnalysisGradesFrame(self) -> None: # 성적 분석 프레임을 여는 메소드
        analysisGradesFrame: AnalysisGradesFrame = AnalysisGradesFrame(self, self.__user)
        analysisGradesFrame.place(x = 0, y = 0)

    def openReminderFrame(self) -> None: # 리마인더 프레임을 여는 메소드
        reminderFrame: ReminderFrame = ReminderFrame(self, self.__user)
        reminderFrame.place(x = 0, y = 0)

    def openCalculatorFrame(self) -> None: # 계산기 프레임을 여는 메소드
        calculatorFrame: CalculatorFrame = CalculatorFrame(self)
        calculatorFrame.place(x = 0, y = 0)

    def openTimerFrame(self) -> None: # 타이머 프레임을 여는 메소드
        timerFrame: TimerFrame = TimerFrame(self)
        timerFrame.place(x = 0, y = 0)

    def openStopwatchFrame(self) -> None: # 스톱워치 프레임을 여는 메소드
        stopwatchFrame: StopwatchFrame = StopwatchFrame(self)
        stopwatchFrame.place(x = 0, y = 0)

    def openUserFrame(self) -> None: # 사용자 프레임을 여는 메소드
        userFrame: UserFrame = UserFrame(self, self.__user)
        userFrame.place(x = 0, y = 0)

    def logout(self) -> None: # 로그아웃 메소드
        self.destroy()

    def removeUser(self) -> None: # 사용자 삭제 메소드
        answer: bool = messagebox.askyesno('알림', '정말로 사용자를 삭제하시겠습니까?')
        if answer:
            removeUser(self.__user.getId())
            messagebox.showinfo('알림', '사용자 삭제가 완료되었습니다.')
            self.destroy()

    def showTimeTable(self) -> None: # 시간표를 보여주는 메소드
        self.__timetableFrame.destroy()
        self.__graphOfStudyingTimePerDaysLabel.place_forget()
        self.__graphOfFocusRatePerDaysLabel.place_forget()

        self.__timetableFrame: TimeTableFrame = TimeTableFrame(self, self.__user)
        self.__timetableFrame.place(x = 100, y = 177)

    def showGraphOfStudyingTimePerDays(self) -> None: # 7일간 학습 시간 그래프를 보여주는 메소드
        self.__timetableFrame.destroy()
        self.__graphOfStudyingTimePerDaysLabel.place_forget()
        self.__graphOfFocusRatePerDaysLabel.place_forget()

        makeGraphOfStudyingTimePerDays(self.__user, (4, 3.5), 100, shape = 'bar')
        self.__graphOfStudyingTimePerDaysPhotoImage.config(file = '{}/Images/Graphs/studying_time_per_days_graph.png'.format(path))
        self.__graphOfStudyingTimePerDaysLabel.place(x = 100, y = 177)

    def showGraphOfFocusRatePerDays(self) -> None: # 7일간 집중도 그래프를 보여주는 메소드
        self.__timetableFrame.destroy()
        self.__graphOfStudyingTimePerDaysLabel.place_forget()
        self.__graphOfFocusRatePerDaysLabel.place_forget()

        makeGraphOfFocusRatePerDays(self.__user, (4, 3.5), 100, shape = 'line plot')
        self.__graphOfFocusRatePerDaysPhotoImage.config(file = '{}/Images/Graphs/focus_rate_per_days_graph.png'.format(path))
        self.__graphOfFocusRatePerDaysLabel.place(x = 100, y = 177)

    def goLeft(self) -> None: # 표시해주는 데이터를 왼쪽 데이터로 넘어감.
        self.__shownDataIndex = (self.__shownDataIndex - 1 + 3) % 3
        if self.__shownDataIndex == 0:
            self.showTimeTable()
        elif self.__shownDataIndex == 1:
            self.showGraphOfStudyingTimePerDays()
        else:
            self.showGraphOfFocusRatePerDays()

    def goRight(self) -> None: # 표시해주는 데이터를 오른쪽 데이터로 넘어감.
        self.__shownDataIndex = (self.__shownDataIndex + 1) % 3
        if self.__shownDataIndex == 0:
            self.showTimeTable()
        elif self.__shownDataIndex == 1:
            self.showGraphOfStudyingTimePerDays()
        else:
            self.showGraphOfFocusRatePerDays()

if DEBUG:
    window: Tk = Tk()
    window.title('Home Frame')
    window.geometry('600x600')

    testUser: User = User('uk3181')
    testUser.setSubjectList(['국어', '수학', '영어'])
    testUser.setStudyDataList([\
            StudyData(dt.datetime(2025, 12, 29), '영어', [[dt.datetime(2025, 12, 29, 17, 0, 0), dt.datetime(2025, 12, 29, 20, 0, 0)]]),\
            StudyData(dt.datetime(2026, 1, 4), '프로그래밍 기초', [[dt.datetime(2026, 1, 4, 22, 0, 0), dt.datetime(2026, 1, 4, 22, 30, 0)]]),\
            StudyData(dt.datetime(2026, 1, 6), '국어', [[dt.datetime(2026, 1, 7, 0, 0, 0), dt.datetime(2026, 1, 7, 0, 30, 0)],\
                                                        [dt.datetime(2026, 1, 7, 2, 30, 0), dt.datetime(2026, 1, 7, 2, 40, 0)]])\
    ])

    homeFrame: HomeFrame = HomeFrame(window, testUser)
    homeFrame.place(x = 0, y = 0)

    window.mainloop()

    studyDataList: list[StudyData] = testUser.getStudyDataList()
    for i in range(len(studyDataList)):
        studyingTimeList: list[list[dt.datetime]] = studyDataList[i].getStudyingTimeList()
        for j in range(len(studyingTimeList)):
            print('{}/{}/{}, {}:{}:{}'.format(studyingTimeList[j][0].year, studyingTimeList[j][0].month, studyingTimeList[j][0].day,\
                    studyingTimeList[j][0].hour, studyingTimeList[j][0].minute, studyingTimeList[j][0].second), end = ' ~ ')
            print('{}/{}/{}, {}:{}:{}'.format(studyingTimeList[j][1].year, studyingTimeList[j][1].month, studyingTimeList[j][1].day,\
                    studyingTimeList[j][1].hour, studyingTimeList[j][1].minute, studyingTimeList[j][1].second))
