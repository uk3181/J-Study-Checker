# 성적 분석 기능
# 분석 방법: 선형 회귀 + 시계열 분석

from path_settings import path

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from sortedcontainers import SortedList, SortedSet
from menu_button import MenuButton
from user import *
from datetime import datetime
from anaylsis_grades import *

DEBUG: bool = False

class InputGradeFrame(Frame): # 성적 입력 프레임
    def __init__(self, misc: Misc, user: User, type: int = GradeData.TOEIC) -> None:
        super().__init__(misc, width = 400, height = 350, bg = '#F0F7FF', borderwidth = 0)
        self.__user: User = user
        self.__type: int = type # 성적 체계

        yearLabel: Label = Label(self, text = '년', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
        monthLabel: Label = Label(self, text = '월', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
        dayLabel: Label = Label(self, text = '일', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)

        self.__yearEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 7, borderwidth = 1)
        self.__monthEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 7, borderwidth = 1)
        self.__dayEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 7, borderwidth = 1)

        self.__yearEntry.place(x = 60, y = 35); yearLabel.place(x = 125, y = 35)
        self.__monthEntry.place(x = 160, y = 35); monthLabel.place(x = 225, y = 35)
        self.__dayEntry.place(x = 260, y = 35); dayLabel.place(x = 325, y = 35)

        if type == GradeData.TOEIC:
            rcLabel: Label = Label(self, text = 'RC', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            lcLabel: Label = Label(self, text = 'LC', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)

            self.__rcEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)
            self.__lcEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)

            rcLabel.place(x = 60, y = 120); self.__rcEntry.place(x = 114, y = 120)
            lcLabel.place(x = 60, y = 205); self.__lcEntry.place(x = 114, y = 205)
        elif type == GradeData.TOEFL:
            readingLabel: Label = Label(self, text = 'Reading', font = ('Arial', 8, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            listeningLabel: Label = Label(self, text = 'Listening', font = ('Arial', 8, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            speakingLabel: Label = Label(self, text = 'Speaking', font = ('Arial', 8, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            writingLabel: Label = Label(self, text = 'Writing', font = ('Arial', 8, 'bold'), bg = '#F0F7FF', borderwidth = 0)

            self.__readingEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)
            self.__listeningEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)
            self.__speakingEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)
            self.__writingEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)

            readingLabel.place(x = 60, y = 89); self.__readingEntry.place(x = 114, y = 86)
            listeningLabel.place(x = 60, y = 140); self.__listeningEntry.place(x = 114, y = 137)
            speakingLabel.place(x = 60, y = 194); self.__speakingEntry.place(x = 114, y = 191)
            writingLabel.place(x = 60, y = 245); self.__writingEntry.place(x = 114, y = 242)
        elif type == GradeData.CSAT:
            subjectLabel: Label = Label(self, text = '과목', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            standardScoreLabel: Label = Label(self, text = '표준점수', font = ('Arial', 10, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            gradeLabel: Label = Label(self, text = '등급', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            percentileLabel: Label = Label(self, text = '백분위', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)

            self.__subjectEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)
            self.__standardScoreEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)
            self.__gradeCombobox: Combobox = Combobox(self, font = ('Arial', 11, 'normal'), width = 26, height = 3, state = 'readonly')
            gradeComboboxList: list[str] = ['--- 등급 선택 ---', '1등급', '2등급', '3등급', '4등급', '5등급', '6등급', '7등급', '8등급', '9등급']
            self.__gradeCombobox['value'] = gradeComboboxList
            self.__gradeCombobox.current(0)
            self.__percentileEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)

            subjectLabel.place(x = 60, y = 86); self.__subjectEntry.place(x = 114, y = 86)
            standardScoreLabel.place(x = 60, y = 137); self.__standardScoreEntry.place(x = 114, y = 137)
            gradeLabel.place(x = 60, y = 191); self.__gradeCombobox.place(x = 114, y = 191)
            percentileLabel.place(x = 60, y = 242); self.__percentileEntry.place(x = 114, y = 242)
        else: # GradeData.OTHER
            subjectLabel: Label = Label(self, text = '과목', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            scoreLabel: Label = Label(self, text = '점수', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            maxScoreLabel: Label = Label(self, text = '최고점', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)
            minScoreLabel: Label = Label(self, text = '최저점', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', borderwidth = 0)

            self.__subjectEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)
            self.__scoreEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)
            self.__maxScoreEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)
            self.__minScoreEntry: Entry = Entry(self, font = ('Arial', 11, 'normal'), width = 28, borderwidth = 1)

            subjectLabel.place(x = 60, y = 86); self.__subjectEntry.place(x = 114, y = 86)
            scoreLabel.place(x = 60, y = 137); self.__scoreEntry.place(x = 114, y = 137)
            maxScoreLabel.place(x = 60, y = 191); self.__maxScoreEntry.place(x = 114, y = 191)
            minScoreLabel.place(x = 60, y = 242); self.__minScoreEntry.place(x = 114, y = 242)

        saveButton: Button = Button(self, text = '저장', font = ('Arial', 10, 'bold'), bg = '#F7E4FF',\
                width = 5, borderwidth = 1, command = lambda: self.saveGrade())
        saveButton.place(x = 180, y = 290)

    def saveGrade(self) -> None: # 성적 저장 메소드
        # 1. 년도 체크
        if not self.__yearEntry.get().strip():
            messagebox.showwarning('경고', '년도를 입력하세요.')
            return
        try:
            year: int = int(self.__yearEntry.get())
            if year < 2000 or year > 9999:
                messagebox.showwarning('경고', '년도는 2000 이상 9999 이하로 입력하세요.')
                return
        except ValueError:
            messagebox.showwarning('경고', '년도는 정수로 입력하세요.')
            return

        # 2. 월 체크
        if not self.__monthEntry.get().strip():
            messagebox.showwarning('경고', '월을 입력하세요.')
            return
        try:
            month: int = int(self.__monthEntry.get())
            if month < 1 or month > 12:
                messagebox.showwarning('경고', '월은 1 이상 12 이하로 입력하세요.')
                return
        except ValueError:
            messagebox.showwarning('경고', '월은 정수로 입력하세요.')
            return

        # 3. 일 체크
        if not self.__dayEntry.get().strip():
            messagebox.showwarning('경고', '일을 입력하세요.')
            return
        try:
            day: int = int(self.__dayEntry.get())
            if day < 1 or day > 31:
                messagebox.showwarning('경고', '일은 1 이상 31 이하로 입력하세요.')
                return

            try:
                datetime(year, month, day)
            except ValueError:
                messagebox.showwarning('경고', '입력된 날짜가 올바르지 않습니다.')
                return
        except ValueError:
            messagebox.showwarning('경고', '일은 정수로 입력하세요.')
            return

        date: datetime = datetime(year, month, day) # 날짜 데이터

        # 4. 성적 관련 각 데이터 유효성 확인
        if self.__type == GradeData.TOEIC:
            # RC 체크
            if not self.__rcEntry.get().strip():
                messagebox.showwarning('경고', 'RC를 입력하세요.')
                return
            try:
                rc: int = int(self.__rcEntry.get())
                if rc < 0 or rc > 495:
                    messagebox.showwarning('경고', 'RC는 0 이상 495 이하로 입력하세요.')
                    return
            except ValueError:
                messagebox.showwarning('경고', 'RC는 정수로 입력하세요.')
                return
            
            # LC 체크
            if not self.__lcEntry.get().strip():
                messagebox.showwarning('경고', 'LC를 입력하세요.')
                return
            try:
                lc: int = int(self.__lcEntry.get())
                if lc < 0 or lc > 495:
                    messagebox.showwarning('경고', 'LC는 0 이상 495 이하로 입력하세요.')
                    return
            except ValueError:
                messagebox.showwarning('경고', 'LC는 정수로 입력하세요.')
                return

            # 저장
            toeicGradeDataList: SortedList[TOEICGradeData] = self.__user.getToeicGradeDataList()
            if TOEICGradeData(date, 0, 0) in toeicGradeDataList:
                toeicGradeDataList.remove(TOEICGradeData(date, 0, 0))
            toeicGradeDataList.add(TOEICGradeData(date, rc, lc))
            self.__user.setToeicGradeDataList(toeicGradeDataList)

            removeUser(self.__user.getId())
            addUser(self.__user)
        elif self.__type == GradeData.TOEFL:
            # Reading 체크
            if not self.__readingEntry.get().strip():
                messagebox.showwarning('경고', 'Reading을 입력하세요.')
                return
            try:
                reading: int = int(self.__readingEntry.get())
                if reading < 0 or reading > 30:
                    messagebox.showwarning('경고', 'Reading은 0 이상 30 이하로 입력하세요.')
                    return
            except ValueError:
                messagebox.showwarning('경고', 'Reading은 정수로 입력하세요.')
                return

            # Listening 체크
            if not self.__listeningEntry.get().strip():
                messagebox.showwarning('경고', 'Listening을 입력하세요.')
                return
            try:
                listening: int = int(self.__listeningEntry.get())
                if listening < 0 or listening > 30:
                    messagebox.showwarning('경고', 'Listening은 0 이상 30 이하로 입력하세요.')
                    return
            except ValueError:
                messagebox.showwarning('경고', 'Listening은 정수로 입력하세요.')
                return
            # Speaking 체크
            if not self.__speakingEntry.get().strip():
                messagebox.showwarning('경고', 'Speaking을 입력하세요.')
                return
            try:
                speaking: int = int(self.__speakingEntry.get())
                if speaking < 0 or speaking > 30:
                    messagebox.showwarning('경고', 'Speaking은 0 이상 30 이하로 입력하세요.')
                    return
            except ValueError:
                messagebox.showwarning('경고', 'Speaking은 정수로 입력하세요.')
                return
            # Writing 체크
            if not self.__writingEntry.get().strip():
                messagebox.showwarning('경고', 'Writing을 입력하세요.')
                return
            try:
                writing: int = int(self.__writingEntry.get())
                if writing < 0 or writing > 30:
                    messagebox.showwarning('경고', 'Writing은 0 이상 30 이하로 입력하세요.')
                    return
            except ValueError:
                messagebox.showwarning('경고', 'Writing은 정수로 입력하세요.')
                return

            # 저장
            toeflGradeDataList: SortedList[GradeData] = self.__user.getToeflGradeDataList()
            if TOEFLGradeData(date, 0, 0, 0, 0) in toeflGradeDataList:
                toeflGradeDataList.remove(TOEFLGradeData(date, 0, 0, 0, 0))
            toeflGradeDataList.add(TOEFLGradeData(date, reading, listening, speaking, writing))
            self.__user.setToeflGradeDataList(toeflGradeDataList)

            removeUser(self.__user.getId())
            addUser(self.__user)
        elif self.__type == GradeData.CSAT:
            # 과목 체크
            if not self.__subjectEntry.get().strip():
                messagebox.showwarning('경고', '과목을 입력하세요.')
                return
            subject: str = self.__subjectEntry.get()
            if len(subject) > 10:
                messagebox.showwarning('경고', '과목은 10자 이하로 입력하세요.')
                return

            # 표준점수 체크
            if not self.__standardScoreEntry.get().strip():
                messagebox.showwarning('경고', '표준점수를 입력하세요.')
                return
            try:
                standardScore: int = int(self.__standardScoreEntry.get())
                if standardScore < 0 or standardScore > 200:
                    messagebox.showwarning('경고', '표준점수는 0 이상 200 이하로 입력하세요.')
                    return
            except ValueError:
                messagebox.showwarning('경고', '표준점수는 정수로 입력하세요.')
                return
            # 등급 체크
            strGrade: str = self.__gradeCombobox.get()
            if strGrade == '--- 등급 선택 ---':
                messagebox.showwarning('경고', '등급을 선택하세요.')
                return
            grade: int = int(strGrade[0])
            # 백분위 체크
            if not self.__percentileEntry.get().strip():
                messagebox.showwarning('경고', '백분위를 입력하세요.')
                return
            try:
                percentile: int = int(self.__percentileEntry.get())
                if percentile < 0 or percentile > 100:
                    messagebox.showwarning('경고', '백분위는 0 이상 100 이하로 입력하세요.')
                    return
            except ValueError:
                messagebox.showwarning('경고', '백분위는 정수로 입력하세요.')
                return

            # 저장
            csatGradeDataList: SortedList[CSATGradeData] = self.__user.getCsatGradeDataList()
            if CSATGradeData(date, '과목명', 0, 9, 0) in csatGradeDataList:
                csatGradeDataList.remove(CSATGradeData(date, '과목명', 0, 9, 0))
            csatGradeDataList.add(CSATGradeData(date, subject, standardScore, grade, percentile))
            self.__user.setCsatGradeDataList(csatGradeDataList)

            removeUser(self.__user.getId())
            addUser(self.__user)
        else: # GradeData.OTHER
            # 과목 체크
            if not self.__subjectEntry.get().strip():
                messagebox.showwarning('경고', '과목을 입력하세요.')
                return
            subject: str = self.__subjectEntry.get()
            if len(subject) > 10:
                messagebox.showwarning('경고', '과목은 10자 이하로 입력하세요.')
                return

            # 점수 체크
            if not self.__scoreEntry.get().strip():
                messagebox.showwarning('경고', '점수를 입력하세요.')
                return
            try:
                score: float = float(self.__scoreEntry.get())
            except ValueError:
                messagebox.showwarning('경고', '점수는 실수로 입력하세요.')
                return

            # 최고점 체크
            if not self.__maxScoreEntry.get().strip():
                messagebox.showwarning('경고', '최고점을 입력하세요.')
                return
            try:
                maxScore: float = float(self.__maxScoreEntry.get())
            except ValueError:
                messagebox.showwarning('경고', '최고점은 실수로 입력하세요.')
                return

            # 최저점 체크
            if not self.__minScoreEntry.get().strip():
                messagebox.showwarning('경고', '최저점을 입력하세요.')
                return
            try:
                minScore: float = float(self.__minScoreEntry.get())
            except ValueError:
                messagebox.showwarning('경고', '최저점은 실수로 입력하세요.')
                return

            # 점수의 범위 체크
            if not (minScore <= maxScore):
                messagebox.showwarning('경고', '점수의 범위가 올바르지 않습니다.')
                return
            if not (score >= minScore and score <= maxScore):
                messagebox.showwarning('경고', '점수의 범위가 올바르지 않습니다.')
                return

            # 저장
            otherGradeDataList: SortedList[OtherGradeData] = self.__user.getOtherGradeDataList()
            if OtherGradeData(date, '과목명', 0, 50, 100) in otherGradeDataList:
                otherGradeDataList.remove(OtherGradeData(date, '과목명', 0, 50, 100))
            otherGradeDataList.add(OtherGradeData(date, subject, score, maxScore, minScore))
            self.__user.setOtherGradeDataList(otherGradeDataList)

            removeUser(self.__user.getId())
            addUser(self.__user)

        messagebox.showinfo('알림', '성적 입력이 완료되었습니다.')

class AnalysisGradesFrame(Frame):
    # 성적 입력 / 성적 분석
    INPUT_GRADE: int = 0; ANALYSIS_GRADE: int = 1

    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)
        self.__user: User = user

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/analysis_grades_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 홈', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goBack(misc))
        goBackButton.place(x = 10, y = 10)

        # 각종 성적 데이터 지표
        self.__option: int = self.INPUT_GRADE # 성적 입력 / 성적 분석
        self.__gradeType: int = GradeData.TOEIC

        # 1. 성적 입력 / 성적 분석
        self.__inputGradeButton: MenuButton = MenuButton(self, buttonText = '성적 입력', buttonBackground = '#C1DDFF',\
                buttonForeground = 'yellow', activeForeground = 'yellow', buttonCommand = lambda: None)
        self.__analysisGradeButton: MenuButton = MenuButton(self, buttonText = '성적 분석', buttonBackground = '#C1DDFF',\
                buttonForeground = 'black', activeForeground = 'yellow',\
                buttonCommand = lambda: self.analysisGrade(self.ANALYSIS_GRADE, self.__gradeType))

        self.__inputGradeButton.place(x = 60, y = 147)
        self.__analysisGradeButton.place(x = 150, y = 147)

        # 2. 성적 체계
        self.__toeicButton: MenuButton = MenuButton(self, buttonText = '토익', buttonBackground = 'white',\
                buttonForeground = '#C1DDFF', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: None)
        self.__toeflButton: MenuButton = MenuButton(self, buttonText = '토플', buttonBackground = 'white',\
                buttonForeground = 'black', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: self.inputGrade(self.INPUT_GRADE, GradeData.TOEFL))
        self.__csatButton: MenuButton = MenuButton(self, buttonText = '수능', buttonBackground = 'white',\
                buttonForeground = 'black', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: self.inputGrade(self.INPUT_GRADE, GradeData.CSAT))
        self.__otherButton: MenuButton = MenuButton(self, buttonText = '기타', buttonBackground = 'white',\
                buttonForeground = 'black', activeForeground = '#C1DDFF',\
                buttonCommand = lambda: self.inputGrade(self.INPUT_GRADE, GradeData.OTHER))

        self.__toeicButton.config(width = 6)
        self.__toeflButton.config(width = 6)
        self.__csatButton.config(width = 6)
        self.__otherButton.config(width = 6)

        self.__toeicButton.place(x = 61, y = 191)
        self.__toeflButton.place(x = 61, y = 221)
        self.__csatButton.place(x = 61, y = 251)
        self.__otherButton.place(x = 61, y = 281)

        self.__inputGradeFrame: InputGradeFrame = InputGradeFrame(self, self.__user)
        self.__gradeDataGraphPhotoImage: PhotoImage = None
        self.__gradeDataGraphLabel: Label = None
        self.__inputGradeFrame.place(x = 140, y = 190)

        # 수능, 기타 성적과 같이 과목을 선택해야 할 경우 필요한 요소
        self.__subjectCombobox: Combobox = None
        self.__csatTypeCombobox: Combobox = None
        self.__maxScoreLabel: Label = None; self.__minScoreLabel: Label = None
        self.__maxScoreEntry: Entry = None; self.__minScoreEntry: Entry = None
        self.__applyButton: Button = None
        self.__currentCsatSubjectIndex: int = 0
        self.__currentCsatTypeIndex: int = 0
        self.__currentOtherSubjectIndex: int = 0
        self.__currentMaxScore: float = 100; self.__currentMinScore: float = 0

    def setStateOfButtons(self) -> None: # 각 메뉴 버튼의 상태를 설정하는 메소드
        self.__inputGradeButton.setButtonForeground('black')
        self.__inputGradeButton.config(command = lambda: self.inputGrade(self.INPUT_GRADE, self.__gradeType))
        self.__analysisGradeButton.setButtonForeground('black')
        self.__analysisGradeButton.config(command = lambda: self.analysisGrade(self.ANALYSIS_GRADE, self.__gradeType))

        self.__toeicButton.setButtonForeground('black')
        self.__toeflButton.setButtonForeground('black')
        self.__csatButton.setButtonForeground('black')
        self.__otherButton.setButtonForeground('black')
        if self.__option == self.INPUT_GRADE:
            self.__toeicButton.config(command = lambda: self.inputGrade(self.INPUT_GRADE, GradeData.TOEIC))
            self.__toeflButton.config(command = lambda: self.inputGrade(self.INPUT_GRADE, GradeData.TOEFL))
            self.__csatButton.config(command = lambda: self.inputGrade(self.INPUT_GRADE, GradeData.CSAT))
            self.__otherButton.config(command = lambda: self.inputGrade(self.INPUT_GRADE, GradeData.OTHER))
        else: # self.ANALYSIS_GRADE
            self.__toeicButton.config(command = lambda: self.analysisGrade(self.__option, GradeData.TOEIC))
            self.__toeflButton.config(command = lambda: self.analysisGrade(self.__option, GradeData.TOEFL))
            self.__csatButton.config(command = lambda: self.analysisGrade(self.__option, GradeData.CSAT))
            self.__otherButton.config(command = lambda: self.analysisGrade(self.__option, GradeData.OTHER))

        if self.__option == self.INPUT_GRADE:
            self.__inputGradeButton.setButtonForeground('yellow')
            self.__inputGradeButton.config(command = lambda: None)
        else: # self.ANALYSIS_GRADE
            self.__analysisGradeButton.setButtonForeground('yellow')
            self.__analysisGradeButton.config(command = lambda: None)

        if self.__gradeType == GradeData.TOEIC:
            self.__toeicButton.setButtonForeground('#C1DDFF')
            self.__toeicButton.config(command = lambda: None)
        elif self.__gradeType == GradeData.TOEFL:
            self.__toeflButton.setButtonForeground('#C1DDFF')
            self.__toeflButton.config(command = lambda: None)
        elif self.__gradeType == GradeData.CSAT:
            self.__csatButton.setButtonForeground('#C1DDFF')
            self.__csatButton.config(command = lambda: None)
        else: # GradeData.OTHER
            self.__otherButton.setButtonForeground('#C1DDFF')
            self.__otherButton.config(command = lambda: None)

    def inputGrade(self, option: int, gradeType: int) -> None: # 성적 입력 메소드
        self.__option = option
        self.__gradeType = gradeType
        self.setStateOfButtons()

        if self.__gradeDataGraphPhotoImage != None:
            self.__gradeDataGraphPhotoImage = None
        if self.__gradeDataGraphLabel != None:
            self.__gradeDataGraphLabel.destroy()
            self.__gradeDataGraphLabel = None

        if self.__inputGradeFrame != None:
            self.__inputGradeFrame.destroy()
            self.__inputGradeFrame = None

        self.__inputGradeFrame = InputGradeFrame(self, self.__user, self.__gradeType)
        self.__inputGradeFrame.place(x = 140, y = 190)

    def analysisGrade(self, option: int, gradeType: int) -> None: # 성적 분석 메소드
        def convertCsatType(csatType: str) -> str: # 수능 성적의 종류를 한글에서 영어로 변환하는 메소드
            if csatType == '표준점수':
                return 'standard_score'
            elif csatType == '등급':
                return 'grade'
            else: # '백분위'
                return 'percentile'

        if self.__inputGradeFrame != None:
            self.__inputGradeFrame.destroy()
            self.__inputGradeFrame = None

        if self.__gradeDataGraphPhotoImage != None:
            self.__gradeDataGraphPhotoImage = None
        if self.__gradeDataGraphLabel != None:
            self.__gradeDataGraphLabel.destroy()
            self.__gradeDataGraphLabel = None

        if (gradeType == GradeData.TOEIC or gradeType == GradeData.TOEFL):
            if gradeType == GradeData.TOEIC:
                dataCount: int = len(self.__user.getToeicGradeDataList())
            else: # GradeData.TOEFL
                dataCount: int = len(self.__user.getToeflGradeDataList())

            if dataCount == 0:
                if self.__option == self.INPUT_GRADE:
                    self.inputGrade(self.__option, self.__gradeType)
                else: # self.ANALYSIS_GRADE
                    self.analysisGrade(self.__option, self.__gradeType)

                if (gradeType == GradeData.TOEIC):
                    messagebox.showinfo('알림', '저장된 토익 성적이 없습니다.')
                else: # GradeData.TOEFL
                    messagebox.showinfo('알림', '저장된 토플 성적이 없습니다.')
                return
            if dataCount > 10: # dataCount는 최대 10개까지만 가능
                dataCount = 10
            
            self.unsetAllElements()
            
            makeGraphOfGradeData(self.__user, gradeType, (4, 3.5), 100, dataCount)
        elif gradeType == GradeData.CSAT:
            dataCount: int = len(self.__user.getCsatGradeDataList())
            if dataCount == 0:
                if self.__option == self.INPUT_GRADE:
                    self.inputGrade(self.__option, self.__gradeType)
                else: # self.ANALYSIS_GRADE
                    self.analysisGrade(self.__option, self.__gradeType)

                messagebox.showinfo('알림', '저장된 수능 성적이 없습니다.')
                return
            if dataCount > 10:
                dataCount = 10

            self.unsetAllElements()
            self.setSubjectCombobox(gradeType)
            self.setCsatTypeCombobox()
            self.setApplyButton(option, gradeType)

            makeGraphOfGradeData(self.__user, gradeType, (4, 3.25), 100, dataCount, self.__subjectCombobox.get(),\
                    convertCsatType(self.__csatTypeCombobox.get()))
        else: # GradeData.OTHER
            dataCount: int = len(self.__user.getOtherGradeDataList())
            if dataCount == 0:
                if self.__option == self.INPUT_GRADE:
                    self.inputGrade(self.__option, self.__gradeType)
                else: # self.ANALYSIS_GRADE
                    self.analysisGrade(self.__option, self.__gradeType)

                messagebox.showinfo('알림', '저장된 기타 성적이 없습니다.')
                return
            if dataCount > 10:
                dataCount = 10

            self.unsetAllElements()
            self.setSubjectCombobox(gradeType)
            self.setElementsOfRangeOfScore()
            self.setApplyButton(option, gradeType)

            makeGraphOfGradeData(self.__user, gradeType, (4, 3.25), 100, dataCount, self.__subjectCombobox.get(),\
                    predictedMaxScore = float(self.__maxScoreEntry.get()), predictedMinScore = float(self.__minScoreEntry.get()))

        self.__option = option
        self.__gradeType = gradeType
        self.setStateOfButtons()

        self.__gradeDataGraphPhotoImage = PhotoImage(file = '{}/Images/Graphs/grade_data_graph.png'.format(path))
        self.__gradeDataGraphLabel = Label(self, borderwidth = 0, image = self.__gradeDataGraphPhotoImage)
        self.__gradeDataGraphLabel.place(x = 140, y = 190)

    def setSubjectCombobox(self, gradeType: int) -> None: # 과목 콤보박스를 설정하는 메소드
        subjectSet: SortedSet[str] = SortedSet()
        if gradeType == GradeData.CSAT:
            csatGradeDataList: SortedList[CSATGradeData] = self.__user.getCsatGradeDataList()
            for csatGradeData in csatGradeDataList:
                subject: str = csatGradeData.getSubject()
                subjectSet.add(subject)
        else: # GradeData.OTHER
            otherGradeDataList: SortedList[OtherGradeData] = self.__user.getOtherGradeDataList()
            for otherGradeData in otherGradeDataList:
                subject: str = otherGradeData.getSubject()
                subjectSet.add(subject)

        subjectList: list[str] = []
        for subject in subjectSet:
            subjectList.append(subject)

        self.__subjectCombobox = Combobox(self, font = ('Arial', 10, 'normal'), width = 11, height = 5, state = 'readonly')
        self.__subjectCombobox['value'] = subjectList
        if gradeType == GradeData.CSAT:
            self.__subjectCombobox.current(self.__currentCsatSubjectIndex)
            self.__subjectCombobox.place(x = 220, y = 518)
        else: # GradeData.OTHER
            self.__subjectCombobox.current(self.__currentOtherSubjectIndex)
            self.__subjectCombobox.place(x = 190, y = 518)

    def unsetSubjectCombobox(self) -> None: # 과목 콤보박스를 설정 해제하는 메소드
        if self.__subjectCombobox != None:
            self.__subjectCombobox.destroy()
            self.__subjectCombobox = None

    def setCsatTypeCombobox(self) -> None: # 수능 성적 종류 콤보박스를 설정하는 메소드
        self.__csatTypeCombobox = Combobox(self, font = ('Arial', 10, 'normal'), width = 8, height = 5, state = 'readonly')
        self.__csatTypeCombobox['value'] = ['표준점수', '등급', '백분위']
        self.__csatTypeCombobox.current(self.__currentCsatTypeIndex)
        self.__csatTypeCombobox.place(x = 330, y = 518)

    def unsetCsatTypeCombobox(self) -> None: # 수능 성적 종류 콤보박스를 설정 해제하는 메소드
        if self.__csatTypeCombobox != None:
            self.__csatTypeCombobox.destroy()
            self.__csatTypeCombobox = None

    def setElementsOfRangeOfScore(self) -> None: # 점수의 범위와 관련된 요소를 설정하는 메소드
        self.__maxScoreLabel = Label(self, text = '최고점', font = ('Arial', 10, 'bold'), bg = '#F0F7FF', borderwidth = 0)
        self.__minScoreLabel = Label(self, text = '최저점', font = ('Arial', 10, 'bold'), bg = '#F0F7FF', borderwidth = 0)

        self.__maxScoreEntry = Entry(self, font = ('Arial', 10), width = 4, borderwidth = 1)
        self.__minScoreEntry = Entry(self, font = ('Arial', 10), width = 4, borderwidth = 1)
        self.__maxScoreEntry.insert(0, str(self.__currentMaxScore)); self.__minScoreEntry.insert(0, str(self.__currentMinScore))

        self.__maxScoreLabel.place(x = 297, y = 518); self.__maxScoreEntry.place(x = 337, y = 518)
        self.__minScoreLabel.place(x = 377, y = 518); self.__minScoreEntry.place(x = 417, y = 518)

    def unsetElementsOfRangeOfScore(self) -> None: # 점수의 범위와 관련된 요소를 설정 해제하는 메소드
        if self.__maxScoreLabel != None:
            self.__maxScoreLabel.destroy()
            self.__maxScoreLabel = None
        if self.__maxScoreEntry != None:
            self.__maxScoreEntry.destroy()
            self.__maxScoreEntry = None
        if self.__minScoreLabel != None:
            self.__minScoreLabel.destroy()
            self.__minScoreLabel = None
        if self.__minScoreEntry != None:
            self.__minScoreEntry.destroy()
            self.__minScoreEntry = None

    def setApplyButton(self, option: int, gradeType: int) -> None: # 적용 버튼을 설정하는 메소드
        self.__applyButton = Button(self, text = '적용', font = ('Arial', 8, 'bold'), width = 5,\
                bg = 'white', borderwidth = 1, command = lambda: self.apply(option, gradeType))
        if gradeType == GradeData.CSAT:
            self.__applyButton.place(x = 420, y = 517)
        else: # GradeData.OTHER
            self.__applyButton.place(x = 455, y = 517)

    def unsetApplyButton(self) -> None: # 적용 버튼을 설정 해제하는 메소드
        if self.__applyButton != None:
            self.__applyButton.destroy()
            self.__applyButton = None

    def unsetAllElements(self) -> None: # 세부 성적 데이터 관련 모든 요소를 설정 해제하는 메소드
        self.unsetSubjectCombobox()
        self.unsetCsatTypeCombobox()
        self.unsetElementsOfRangeOfScore()
        self.unsetApplyButton()

    def apply(self, option: int, gradeType: int) -> None: # 세부 성적 적용 메소드
        if gradeType == GradeData.OTHER:
            # 최고점 체크
            if not self.__maxScoreEntry.get().strip():
                messagebox.showwarning('경고', '최고점을 입력하세요.')
                return
            try:
                maxScore: float = float(self.__maxScoreEntry.get())
            except ValueError:
                messagebox.showwarning('경고', '최고점은 실수로 입력하세요.')
                return

            # 최저점 체크
            if not self.__minScoreEntry.get().strip():
                messagebox.showwarning('경고', '최저점을 입력하세요.')
                return
            try:
                minScore: float = float(self.__minScoreEntry.get())
            except ValueError:
                messagebox.showwarning('경고', '최저점은 실수로 입력하세요.')
                return

            # 범위 체크
            if minScore > maxScore:
                messagebox.showwarning('경고', '점수의 범위가 올바르지 않습니다.')
                return

        if gradeType == GradeData.CSAT:
            self.__currentCsatSubjectIndex = self.__subjectCombobox.current()
            self.__currentCsatTypeIndex = self.__csatTypeCombobox.current()
        else: # GradeData.OTHER
            self.__currentOtherSubjectIndex = self.__subjectCombobox.current()
            self.__currentMaxScore = float(self.__maxScoreEntry.get())
            self.__currentMinScore = float(self.__minScoreEntry.get())

        self.analysisGrade(option, gradeType)

    def goBack(self, misc: Misc) -> None: # 뒤로가기 메소드
        misc.showTimeTable()
        self.destroy()

if DEBUG:
    window: Tk = Tk()
    window.title('Analysis Grades Frame')
    window.geometry('600x600')

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

    addUser(testUser)

    analysisGradesFrame: AnalysisGradesFrame = AnalysisGradesFrame(window, testUser)
    analysisGradesFrame.place(x = 0, y = 0)

    window.mainloop()
