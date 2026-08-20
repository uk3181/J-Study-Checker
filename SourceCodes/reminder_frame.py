# 리마인더 관련 모듈

from tkinter import *
from tkinter import messagebox
from user import *

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

class ReminderDataFrame(Frame): # 지정 날짜의 리마인더 정보를 보여주는 프레임
    def __init__(self, misc: Misc, user: User, date: dt.datetime) -> None:
        super().__init__(misc, width = 350, height = 300, bg = '#EEF6FF', borderwidth = 0)
        self.__user = user
        self.__date = date

        # 프레임 닫는 기능
        exitButton: Button = Button(self, text = 'X', font = ('Arial', 9, 'bold'), bg = '#EEF6FF', fg = 'blue',\
                activebackground = '#EEF6FF', activeforeground = 'yellow', borderwidth = 0,\
                command = lambda: self.closeFrame(misc, date.year, date.month))
        exitButton.place(x = 325, y = 10)

        dateLabel: Label = Label(self, text = '{}/{}/{}'.format(date.year, date.month, date.day),\
                font = ('Arial', 14, 'bold'), bg = '#EEF6FF', width = 15, borderwidth = 0)
        dateLabel.place(x = 80, y = 30)

        index: int = self.__user.searchReminder(date)

        self.__memoText: Text = Text(self, font = ('Arial', 11, 'normal'), bg = 'white', width = 33, height = 9, borderwidth = 0)
        if index != -1:
            self.__memoText.insert('1.0', self.__user.getReminderList()[index].getMemo())
        if date.date() < dt.datetime.now().date():
            self.__memoText.config(state = 'disabled')
        self.__memoText.place(x = 40, y = 82)

        editButton: Button = Button(self, text = '수정', font = ('Arial', 10, 'bold'), bg = 'white',\
                width = 5, borderwidth = 1, command = lambda: self.editMemo())
        removeButton: Button = Button(self, text = '삭제', font = ('Arial', 10, 'bold'), bg = '#FFB9B9',\
                width = 5, borderwidth = 1, command = lambda: self.removeMemo())
        if date.date() < dt.datetime.now().date():
            editButton.config(state = 'disabled')
            removeButton.config(state = 'disabled')
        editButton.place(x = 125, y = 242); removeButton.place(x = 180, y = 242)

    def editMemo(self) -> None: # 메모를 수정하는 메소드
        memo: str = self.__memoText.get('1.0', 'end-1c')
        if not memo.strip():
            messagebox.showwarning('경고', '메모를 입력하세요.')
            return

        if self.__user.searchReminder(self.__date) != -1:
            self.__user.removeReminder(self.__date)
        self.__user.addReminder(ReminderData(self.__date, memo))
        removeUser(self.__user.getId())
        addUser(self.__user)

        self.__memoText.delete('1.0', END)
        self.__memoText.insert('1.0', memo)
        messagebox.showinfo('알림', '메모 수정이 완료되었습니다.')

    def removeMemo(self) -> None: # 메모를 삭제하는 메소드
        if self.__user.searchReminder(self.__date) != -1:
            self.__user.removeReminder(self.__date)
        removeUser(self.__user.getId())
        addUser(self.__user)

        self.__memoText.delete('1.0', END)
        messagebox.showinfo('알림', '메모 삭제가 완료되었습니다.')

    def closeFrame(self, misc: Misc, year: int, month: int) -> None: # 현재 창을 닫는 메소드
        misc.showCalendar(year, month)
        self.destroy()

class ReminderFrame(Frame):
    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)
        self.__user: User = user

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/reminder_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 홈', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goBack(misc))
        goBackButton.place(x = 10, y = 10)

        # 캘린더 구성
        self.__date: dt.datetime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, 1)

        self.__monthLabel: Label = Label(self, text = '{}년 {}월'.format(self.__date.year, self.__date.month), font = ('Arial', 14, 'bold'), width = 15, bg = '#F0F7FF')
        self.__monthLabel.place(x = 208, y = 142)

        self.__goPreviousMonthButton: Button = Button(self, text = '<', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', fg = 'blue',\
                activebackground = '#F0F7FF', activeforeground = 'yellow', disabledforeground = 'steel blue',\
                borderwidth = 0, command = lambda: self.goPreviousMonth())
        if self.__date.year == 2000 and self.__date.month == 1:
            self.__goPreviousMonthButton.config(state = 'disabled')
        self.__goNextMonthButton: Button = Button(self, text = '>', font = ('Arial', 11, 'bold'), bg = '#F0F7FF', fg = 'blue',\
                activebackground = '#F0F7FF', activeforeground = 'yellow', disabledforeground = 'steel blue',\
                borderwidth = 0, command = lambda: self.goNextMonth())
        self.__goPreviousMonthButton.place(x = 220, y = 143); self.__goNextMonthButton.place(x = 362, y = 143)
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

        self.__bellButtonList: list[Button] = []
        xPositionList: list[int] = [60, 129, 199, 268, 337, 406, 475]
        yPositionList: list[int] = [227, 280, 333, 387, 440, 494]
        for i in range(daysOfMonth):
            index: int = self.__user.searchReminder(dt.datetime(date.year, date.month, i + 1))
            dayFrame: Frame = Frame(self, width = 63, height = 46, bg = 'white', borderwidth = 0)
            dayLabel: Label = Label(dayFrame, text = '{}'.format(i + 1), font = ('Arial', 11, 'bold'), bg = 'white', borderwidth = 0)
            bellButton: Button = Button(dayFrame, text = '⨁', font = ('Arial', 16, 'normal'), bg = 'white', fg = 'gray',\
                    activebackground = 'white', activeforeground = '#00F7CF', width = 2, borderwidth = 0,\
                    command = lambda day = i + 1: self.openReminderDataFrame(date.year, date.month, day))
            if index != -1:
                dayFrame.config(bg = '#00F7CF')
                dayLabel.config(bg = '#00F7CF')
                bellButton.config(text = '🔔', font = ('Arial', 16, 'bold'), bg = '#00F7CF', fg = 'black', activebackground = '#00F7CF', activeforeground = 'white')
                bellButton.place(x = 24, y = 2)
                self.__bellButtonList.append(bellButton)
            else:
                date: dt.datetime = dt.datetime(year, month, i + 1)
                if date.date() >= dt.datetime.now().date():
                    bellButton.place(x = 24, y = 4)
                    self.__bellButtonList.append(bellButton)
            dayLabel.place(x = 4, y = 1)
            self.__dayFrameList.append(dayFrame)
        for i in range((dt.datetime(date.year, date.month, 1).weekday() + 1) % 7):
            dayFrame: Frame = Frame(self, width = 63, height = 46, bg = 'light gray', borderwidth = 0)
            dayLabel: Label = Label(dayFrame, text = '{}'.format((dt.datetime(date.year, date.month, 1).date() - dt.timedelta(days = i + 1)).day),\
                    font = ('Arial', 11, 'bold'), bg = 'light gray', fg = 'gray', borderwidth = 0)
            dayLabel.place(x = 4, y = 1)
            self.__dayFrameList.insert(0, dayFrame)
        leftDaysOnCalendar: int = 42 - len(self.__dayFrameList)
        for i in range(leftDaysOnCalendar):
            dayFrame: Frame = Frame(self, width = 63, height = 46, bg = 'light gray', borderwidth = 0)
            dayLabel: Label = Label(dayFrame, text = '{}'.format(i + 1),\
                    font = ('Arial', 11, 'bold'), bg = 'light gray', fg = 'gray', borderwidth = 0)
            dayLabel.place(x = 4, y = 1)
            self.__dayFrameList.append(dayFrame)

        xPositionIndex: int = 0
        yPositionIndex: int = 0
        for i in range(len(self.__dayFrameList)):
            self.__dayFrameList[i].place(x = xPositionList[xPositionIndex], y = yPositionList[yPositionIndex])
            xPositionIndex = (xPositionIndex + 1) % 7
            if xPositionIndex == 0:
                yPositionIndex += 1

    def openReminderDataFrame(self, year: int, month: int, day: int) -> None: # 지정 날짜의 리마인더 정보를 보여주는 메소드
        # 캘린더의 각 날짜에 배되된 버튼은 모두 눌러도 아무 작업이 수행되지 않도록 설정되어야 함.
        for i in range(len(self.__bellButtonList)):
            self.__bellButtonList[i].config(command = lambda: None)

        reminderDataFrame: ReminderDataFrame = ReminderDataFrame(self, self.__user, dt.datetime(year, month, day))
        reminderDataFrame.place(x = 125, y = 150)

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

    def goBack(self, misc: Misc) -> None: # 뒤로가기 메소드
        misc.showTimeTable()
        self.destroy()

if DEBUG:
    window: Tk = Tk()
    window.title('Reminder Frame')
    window.geometry('600x600')

    userList: SortedList[User] = SortedList()
    testUser: User = User()
    testUser.addReminder(ReminderData(dt.datetime(2026, 1, 20), '국어 모의고사 자가채점'))
    testUser.addReminder(ReminderData(dt.datetime(2025, 12, 25), '크리스마스 특강 참석'))
    userList.add(testUser)
    setUserList(userList)

    analysisStudyFrame: ReminderFrame = ReminderFrame(window, testUser)
    analysisStudyFrame.place(x = 0, y = 0)

    window.mainloop()
