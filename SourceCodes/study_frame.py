# 학습 관련 모듈

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import datetime as dt
from user import *

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

class EditSubjectFrame(Frame): # 과목 수정 프레임
    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 300, height = 300, bg = '#EEF6FF', borderwidth = 0)
        self.__user: User = user

        misc.getEditSubjectListButton().config(state = 'disabled')

        # 프레임 닫는 기능
        exitButton: Button = Button(self, text = 'X', font = ('Arial', 9, 'bold'), bg = '#EEF6FF', fg = 'blue',\
                activebackground = '#EEF6FF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.closeFrame(misc))
        exitButton.place(x = 275, y = 10)

        # 과목 검색 관련 기능
        titleLabel: Label = Label(self, text = '과목 수정', font = ('Arial', 14, 'bold'), bg = '#EEF6FF')
        titleLabel.place(x = 110, y = 15)

        searchSubjectLabel: Label = Label(self, text = '과목', font = ('Arial', 12, 'bold'), bg = '#EEF6FF')
        self.__searchSubjectEntry: Entry = Entry(self, font = ('Arial', 12), bg = 'white', width = 11)

        searchSubjectLabel.place(x = 30, y = 60); self.__searchSubjectEntry.place(x = 80, y = 60)

        # 과목 추가/삭제 관련 기능
        addSubjectButton: Button = Button(self, text = '추가', font = ('Arial', 8, 'bold'), bg = '#E1FFE4',\
                width = 4, borderwidth = 1, command = lambda: self.addSubject(misc))
        deleteSubjectButton: Button = Button(self, text = '삭제', font = ('Arial', 8, 'bold'), bg = '#FFB9B9',\
                width = 4, borderwidth = 1, command = lambda: self.deleteSubject(misc))
        addSubjectButton.place(x = 190, y = 60); deleteSubjectButton.place(x = 230, y = 60)

        # 저장된 과목 목록 관련 기능
        self.__subjectListText: Text = Text(self, font = ('Arial', 12, 'normal'), width = 26, height = 10, bg = 'white', borderwidth = 0)
        subjectList: list[str] = self.__user.getSubjectList()
        for i in range(len(subjectList)):
            self.__subjectListText.insert(END, subjectList[i])
            if i != len(subjectList) - 1:
                self.__subjectListText.insert(END, '\n')
        self.__subjectListText.config(state = 'disabled')

        self.__noSubjectsLabel: Label = Label(self, text = '등록된 과목이 없습니다.', font = ('Arial', 12, 'bold'),\
                bg = '#EEF6FF') # 등록된 과목이 없을 경우 표시해주는 레이블

        if len(self.__user.getSubjectList()) == 0:
            self.__noSubjectsLabel.place(x = 58, y = 160)
        else:
            self.__subjectListText.place(x = 30, y = 97)

    def updateSubjectListText(self, misc: Misc) -> None: # 과목 목록 텍스트 업데이트
        subjectList: list[str] = self.__user.getSubjectList()
        if len(subjectList) == 0:
            self.__subjectListText.destroy()
            self.__noSubjectsLabel.place(x = 58, y = 160)
        else:
            self.__subjectListText.place(x = 30, y = 97)
            self.__noSubjectsLabel.destroy()

            self.__subjectListText.config(state = 'normal')
            self.__subjectListText.delete('1.0', END)
            for i in range(len(subjectList)):
                self.__subjectListText.insert(END, subjectList[i])
                if i != len(subjectList) - 1:
                    self.__subjectListText.insert(END, '\n')
            self.__subjectListText.config(state = 'disabled')

        subjectCombobox: Combobox = misc.getSubjectCombobox()
        subjectComboboxList: list[str] = ['--- 과목 선택 ---']
        subjectComboboxList += subjectList
        subjectCombobox['value'] = subjectComboboxList
        subjectCombobox.index(0)

    def addSubject(self, misc: Misc) -> None: # 과목 추가 메소드
        if not self.__searchSubjectEntry.get().strip():
            messagebox.showwarning('경고', '과목을 입력하세요.')
            return

        if len(self.__searchSubjectEntry.get()) > 10:
            messagebox.showwarning('경고', '과목은 10자 이하로 입력하세요.')
            return

        subjectList: list[str] = self.__user.getSubjectList()
        if self.__searchSubjectEntry.get() in subjectList:
            messagebox.showinfo('알림', '이미 등록된 과목입니다.')
            return

        subjectList.append(self.__searchSubjectEntry.get()) # 과목 삭제
        subjectList.sort() # 사전순으로 정렬
        self.__user.setSubjectList(subjectList)
        
        removeUser(self.__user.getId())
        addUser(self.__user)

        self.updateSubjectListText(misc)
        messagebox.showinfo('알림', '과목 추가가 완료되었습니다.')

    def deleteSubject(self, misc: Misc) -> None: # 과목 삭제 메소드
        if not self.__searchSubjectEntry.get().strip():
            messagebox.showwarning('경고', '과목을 입력하세요.')
            return

        subjectList: list[str] = self.__user.getSubjectList()
        if not (self.__searchSubjectEntry.get() in subjectList):
            messagebox.showinfo('알림', '등록되지 않은 과목입니다.')
            return

        subjectList.remove(self.__searchSubjectEntry.get())
        self.__user.setSubjectList(subjectList)

        removeUser(self.__user.getId())
        addUser(self.__user)

        self.updateSubjectListText(misc)
        messagebox.showinfo('알림', '과목 삭제가 완료되었습니다.')

    def closeFrame(self, misc: Misc) -> None: # 현재 창을 닫는 메소드
        misc.getEditSubjectListButton().config(state = 'normal')
        self.destroy()

class StudyFrame(Frame):
    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)
        self.__user: User = user

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/study_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 홈', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goBack(misc))
        goBackButton.place(x = 10, y = 10)

        # 스톱워치 기능
        self.__stopwatchLabel: Label = Label(self, text = '00:00:00', font = ('Arial', 30, 'bold'), bg = 'white')
        self.__stopwatchLabel.place(x = 217, y = 193)

        self.__startStopWatchButton: Button = Button(self, text = 'Start', font = ('Arial', 7, 'bold'), bg = '#EBFBFF',\
                fg = '#2F8EFF', borderwidth = 0, activebackground = '#EBFBFF', activeforeground = 'yellow', command = lambda: self.startStopWatch())
        self.__stopStopWatchButton: Button = Button(self, text = 'Stop', font = ('Arial', 7, 'bold'), bg = '#EBFBFF',\
                fg = '#2F8EFF', borderwidth = 0, activebackground = '#EBFBFF', activeforeground = 'yellow', command = lambda: None)
        self.__resetStopWatchButton: Button = Button(self, text = 'Reset', font = ('Arial', 7, 'bold'), bg = '#EBFBFF',\
                fg = '#2F8EFF', borderwidth = 0, activebackground = '#EBFBFF', activeforeground = 'yellow', command = lambda: None)
        
        self.__startStopWatchButton.place(x = 210, y = 331)
        self.__stopStopWatchButton.place(x = 287, y = 331)
        self.__resetStopWatchButton.place(x = 361, y = 331)

        # 학습 데이터 관련 기능
        # 1. 날짜
        yearLabel: Label = Label(self, text = '년도', font = ('Arial', 12, 'bold'), bg = 'white')
        monthLabel: Label = Label(self, text = '월', font = ('Arial', 12, 'bold'), bg = 'white')
        dayLabel: Label = Label(self, text = '일', font = ('Arial', 12, 'bold'), bg = 'white')

        yearEntry: Entry = Entry(self, font = ('Arial', 12, 'normal'), bg = 'white', width = 4); yearEntry.insert(0, str(dt.datetime.today().year)); yearEntry.config(state = 'disabled')
        monthEntry: Entry = Entry(self, font = ('Arial', 12, 'normal'), bg = 'white', width = 4); monthEntry.insert(0, str(dt.datetime.today().month)); monthEntry.config(state = 'disabled')
        dayEntry: Entry = Entry(self, font = ('Arial', 12, 'normal'), bg = 'white', width = 4); dayEntry.insert(0, str(dt.datetime.today().day)); dayEntry.config(state = 'disabled')

        yearLabel.place(x = 101, y = 414); yearEntry.place(x = 141, y = 414)
        monthLabel.place(x = 256, y = 414); monthEntry.place(x = 296, y = 414)
        dayLabel.place(x = 411, y = 414); dayEntry.place(x = 451, y = 414)

        # 2. 과목
        subjectLabel: Label = Label(self, text = '과목', font = ('Arial', 12, 'bold'), bg = 'white')
        self.__subjectCombobox: Combobox = Combobox(self, font = ('Arial', 12, 'normal'), width = 20, height = 3, state = 'readonly')
        subjectComboboxList: list[str] = ['--- 과목 선택 ---']
        for i in range(len(self.__user.getSubjectList())):
            subjectComboboxList.append(user.getSubjectList()[i])
        self.__subjectCombobox['value'] = subjectComboboxList
        self.__subjectCombobox.current(0)
        subjectLabel.place(x = 101, y = 444); self.__subjectCombobox.place(x = 216, y = 444)

        self.__editSubjectListButton: Button = Button(self, text = '수정', font = ('Arial', 9, 'bold'), bg = '#F7E4FF',\
                width = 7, borderwidth = 1, command = lambda: self.openEditSubjectFrame())
        self.__editSubjectListButton.place(x = 433, y = 444)

        # 3. 목표 학습 시간
        targetStudyingTimeLabel: Label = Label(self, text = '목표 학습 시간', font = ('Arial', 12, 'bold'), bg = 'white')
        self.__targetStudyingTimeCombobox: Combobox = Combobox(self, font = ('Arial', 12, 'normal'), width = 20, height = 5, state = 'readonly')
        self.__targetStudyingTimeCombobox['value'] = [\
            '--- 목표 학습 시간 선택 ---',
            '30분', '1시간', '1시간 30분', '2시간', '2시간 30분', '3시간', '3시간 30분', '4시간', '4시간 30분', '5시간', '5시간 30분',\
            '6시간', '6시간 30분', '7시간', '7시간 30분', '8시간', '8시간 30분', '9시간', '9시간 30분', '10시간', '10시간 30분', '11시간', '11시간 30분',\
            '12시간', '12시간 30분', '13시간', '13시간 30분', '14시간', '14시간 30분', '15시간', '15시간 30분', '16시간', '16시간 30분', '17시간', '17시간 30분',\
            '18시간', '18시간 30분', '19시간', '19시간 30분', '20시간', '20시간 30분', '21시간', '21시간 30분', '22시간', '22시간 30분', '23시간', '23시간 30분', '24시간'\
        ]
        self.__targetStudyingTimeCombobox.current(0)
        targetStudyingTimeLabel.place(x = 101, y = 474); self.__targetStudyingTimeCombobox.place(x = 216, y = 474)

        # 4. 학습 기록 저장
        self.__saveStudyButton: Button = Button(self, text = '저장', font = ('Arial', 11, 'bold'), bg = '#F7E4FF',
                width = 5, borderwidth = 1, command = lambda: self.saveStudy(misc))
        self.__saveStudyButton.place(x = 270, y = 530)

        # 학습 기록 데이터
        self.__started: bool = False
        self.__studyDate: dt.datetime = None; self.__subject: str = None; self.__studyingTimeList: list[list[dt.datetime]] = []
        self.__startStudyingTime: dt.datetime = None; self.__endStudyingTime: dt.datetime = None

    ################################ Getter/Setter ####################################
    def getEditSubjectListButton(self) -> Button:
        return self.__editSubjectListButton

    def getSubjectCombobox(self) -> Combobox:
        return self.__subjectCombobox
    ####################################################################################

    def goBack(self, misc: Misc) -> None: # 뒤로가기 메소드
        answer: bool = messagebox.askyesno('알림', '학습을 종료하시면 변경 내용이 저장되지 않습니다.\n정말 학습을 종료하시겠습니까?')
        if answer == YES:
            misc.showTimeTable()
            self.destroy()

    def openEditSubjectFrame(self) -> None: # 과목 수정 프레임을 여는 메소드
        editSubjectFrame: EditSubjectFrame = EditSubjectFrame(self, self.__user)
        editSubjectFrame.place(x = 150, y = 150)

    def startStopWatch(self) -> None: # 스톱워치 시작 메소드
        if self.__subjectCombobox.get() == '--- 과목 선택 ---':
            self.__startStopWatchButton.config(command = lambda: self.startStopWatch())
            self.__stopStopWatchButton.config(command = lambda: None)
            self.__resetStopWatchButton.config(command = lambda: None)
            messagebox.showinfo('알림', '과목을 먼저 선택하세요.')
            return
        if self.__targetStudyingTimeCombobox.get() == '--- 목표 학습 시간 선택 ---':
            self.__startStopWatchButton.config(command = lambda: self.startStopWatch())
            self.__stopStopWatchButton.config(command = lambda: None)
            self.__resetStopWatchButton.config(command = lambda: None)
            messagebox.showinfo('알림', '목표 학습 시간을 먼저 선택하세요.')
            return

        if self.__stopwatchLabel.cget('text') == '23:59:59':
            self.stopStopWatch()
            self.__startStopWatchButton.config(command = lambda: None)
            return

        if not self.__started:
            self.__studyDate: dt.datetime = dt.datetime.now()
            self.__subject = self.__subjectCombobox.get()
            self.__started = True
            self.__startStudyingTime = dt.datetime.now()

        self.__saveStudyButton.config(state = 'disabled')

        self.__startStopWatchButton.config(command = lambda: None)
        self.__stopStopWatchButton.config(command = lambda: self.stopStopWatch())
        self.__resetStopWatchButton.config(command = lambda: self.resetStopWatch())

        timeDatas: list[int] = list(map(int, self.__stopwatchLabel.cget('text').split(':')))
        totalSeconds: int = timeDatas[0] * 3600 + timeDatas[1] * 60 + timeDatas[2] + 1
        hours: int = totalSeconds // 3600
        minutes: int = (totalSeconds - hours * 3600) // 60
        seconds: int = totalSeconds % 60
        self.__stopwatchLabel.config(text = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

        self.__afterId = self.__stopwatchLabel.after(1000, lambda: self.startStopWatch())

    def stopStopWatch(self) -> None: # 스톱워치 종료 메소드
        self.__endStudyingTime = dt.datetime.now()
        self.__studyingTimeList.append([self.__startStudyingTime, self.__endStudyingTime])
        self.__startStudyingTime = None; self.__endStudyingTime = None
        self.__started = False

        self.__saveStudyButton.config(state = 'normal')

        self.__startStopWatchButton.config(command = lambda: self.startStopWatch())
        self.__stopStopWatchButton.config(command = lambda: None)
        self.__resetStopWatchButton.config(command = lambda: self.resetStopWatch())

        self.__stopwatchLabel.after_cancel(self.__afterId)

    def resetStopWatch(self) -> None: # 스톱워치 초기화 메소드
        self.stopStopWatch()
        self.__studyingTimeList = []

        self.__startStopWatchButton.config(command = lambda: self.startStopWatch())
        self.__stopStopWatchButton.config(command = lambda: None)
        self.__resetStopWatchButton.config(command = lambda: self.resetStopWatch())

        self.__stopwatchLabel.config(text = '00:00:00')

    def saveStudy(self, misc: Misc) -> None: # 학습 기록 저장 메소드
        if self.__subjectCombobox.get() == '--- 과목 선택 ---':
            messagebox.showinfo('알림', '과목을 먼저 선택하세요.')
            return
        if self.__targetStudyingTimeCombobox.get() == '--- 목표 학습 시간 선택 ---':
            messagebox.showinfo('알림', '목표 학습 시간을 먼저 선택하세요.')
            return

        if len(self.__studyingTimeList) == 0:
            messagebox.showinfo('알림', '저장된 학습 기록이 없습니다.')
        else:
            targetStudyingTime: int = self.__targetStudyingTimeCombobox.current() * 1800

            studyDataList: list[StudyData] = self.__user.getStudyDataList()
            studyDataList.append(StudyData(self.__studyDate, self.__subject, self.__studyingTimeList, targetStudyingTime))
            self.__user.setStudyDataList(studyDataList)

            removeUser(self.__user.getId())
            addUser(self.__user)
            messagebox.showinfo('알림', '학습 기록 저장이 완료되었습니다.')
        misc.showTimeTable()
        self.destroy()

if DEBUG:
    window: Tk = Tk()
    window.title('Study Frame')
    window.geometry('600x600')

    userList: SortedList[User] = SortedList()
    testUser: User = User()
    testUser.setSubjectList(['국어', '수학', '영어'])
    userList.add(testUser)
    setUserList(userList)

    studyFrame: StudyFrame = StudyFrame(window, testUser)
    studyFrame.place(x = 0, y = 0)

    window.mainloop()
