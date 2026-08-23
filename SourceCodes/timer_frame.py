# 타이머 기능

from path_settings import path

from tkinter import *
from tkinter import messagebox

DEBUG: bool = False

class TimerButton(Frame): # 타머머 버튼
    def __init__(self, misc: Misc, type: str) -> None:
        super().__init__(misc, width = 127, height = 37, borderwidth = 0)

        if type == 'one':
            photoImageFile1: str = '{}/Images/Icons/one_minute_timer_button_1.png'.format(path)
            photoImageFile2: str = '{}/Images/Icons/one_minute_timer_button_2.png'.format(path)
        elif type == 'five':
            photoImageFile1: str = '{}/Images/Icons/five_minutes_timer_button_1.png'.format(path)
            photoImageFile2: str = '{}/Images/Icons/five_minutes_timer_button_2.png'.format(path)
        elif type == 'ten':
            photoImageFile1: str = '{}/Images/Icons/ten_minutes_timer_button_1.png'.format(path)
            photoImageFile2: str = '{}/Images/Icons/ten_minutes_timer_button_2.png'.format(path)
        else: # custom
            photoImageFile1: str = '{}/Images/Icons/custom_timer_button_1.png'.format(path)
            photoImageFile2: str = '{}/Images/Icons/custom_timer_button_2.png'.format(path)

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = photoImageFile1)
        self.__backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 127, height = 37, borderwidth = 0)
        self.__backgroundLabel.place(x = 0, y = 0)

        self.bind('<Enter>', lambda event: self.onEnter(event, photoImageFile2))
        self.bind('<Leave>', lambda event: self.onLeave(event, photoImageFile1))
        self.__backgroundLabel.bind('<Button-1>', lambda event: self.onClick(event, misc, type))

    ################################ Getter/Setter ####################################
    def getBackgroundLabel(self) -> Label:
        return self.__backgroundLabel
    ####################################################################################

    def onEnter(self, event: Event, photoImageFile: str) -> None:
        self.__backgroundPhotoImage.config(file = photoImageFile)

    def onClick(self, event: Event, misc: Misc, type: str) -> None:
        if type == 'one':
            misc.setTimer(0, 1, 0)
        elif type == 'five':
            misc.setTimer(0, 5, 0)
        elif type == 'ten':
            misc.setTimer(0, 10, 0)
        else: # custom
            misc.openInputLeftTimeFrame()

    def onLeave(self, event: Event, photoImageFile: str) -> None:
        self.__backgroundPhotoImage.config(file = photoImageFile)

class InputLeftTimeFrame(Frame): # 타이머의 남은 시간을 입력받는 프레임
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 250, height = 150, bg = '#E9F1FA', borderwidth = 0)

        # 프레임 닫는 기능
        exitButton: Button = Button(self, text = 'X', font = ('Arial', 9, 'bold'), bg = '#E9F1FA', fg = 'blue',\
                activebackground = '#E9F1FA', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.closeFrame(misc))
        exitButton.place(x = 225, y = 10)

        infoLabel: Label = Label(self, text = '시간을 입력하세요.', font = ('Arial', 12, 'bold'), bg = '#E9F1FA', borderwidth = 0)
        infoLabel.place(x = 55, y = 25)

        hoursLabel: Label = Label(self, text = '시간', font = ('Arial', 12, 'bold'), bg = '#E9F1FA', borderwidth = 0)
        minutesLabel: Label = Label(self, text = '분', font = ('Arial', 12, 'bold'), bg = '#E9F1FA', borderwidth = 0)
        secondsLabel: Label = Label(self, text = '초', font = ('Arial', 12, 'bold'), bg = '#E9F1FA', borderwidth = 0)

        self.__hoursEntry: Entry = Entry(self, font = ('Arial', 12, 'normal'), width = 3, justify = 'right')
        self.__minutesEntry: Entry = Entry(self, font = ('Arial', 12, 'normal'), width = 3, justify = 'right')
        self.__secondsEntry: Entry = Entry(self, font = ('Arial', 12, 'normal'), width = 3, justify = 'right')

        self.__hoursEntry.place(x = 21, y = 55); hoursLabel.place(x = 58, y = 55)
        self.__minutesEntry.place(x = 106, y = 55); minutesLabel.place(x = 143, y = 55)
        self.__secondsEntry.place(x = 176, y = 55); secondsLabel.place(x = 213, y = 55)

        okButton: Button = Button(self, text = '확인', font = ('Arial', 10, 'bold'), bg = 'white', width = 5,\
                borderwidth = 1, command = lambda: self.applyLeftTime(misc))
        okButton.place(x = 98, y = 95)

    def applyLeftTime(self, misc: Misc) -> None: # 입력한 남은 시간을 적용하는 메소드
        # 1. 시간 체크
        if not self.__hoursEntry.get().strip():
            messagebox.showwarning('경고', '시간을 입력하세요.')
            return

        try:
            hours: int = int(self.__hoursEntry.get())
            if hours < 0 or hours > 23:
                messagebox.showwarning('경고', '시간은 0 이상 23 이하로 입력하세요.')
                return
        except ValueError:
            messagebox.showwarning('경고', '시간은 정수로 입력하세요.')
            return

        # 2. 분 체크
        if not self.__minutesEntry.get().strip():
            messagebox.showwarning('경고', '분을 입력하세요.')
            return

        try:
            minutes: int = int(self.__minutesEntry.get())
            if minutes < 0 or minutes > 59:
                messagebox.showwarning('경고', '분은 0 이상 59 이하로 입력하세요.')
                return
        except ValueError:
            messagebox.showwarning('경고', '분은 정수로 입력하세요.')
            return

        # 3. 초 체크
        if not self.__secondsEntry.get().strip():
            messagebox.showwarning('경고', '초를 입력하세요.')
            return

        try:
            seconds: int = int(self.__secondsEntry.get())
            if seconds < 0 or seconds > 59:
                messagebox.showwarning('경고', '초는 0 이상 59 이하로 입력하세요.')
                return
        except ValueError:
            messagebox.showwarning('경고', '초는 정수로 입력하세요.')
            return

        misc.setTimer(hours, minutes, seconds)
        self.closeFrame(misc)

    def closeFrame(self, misc: Misc) -> None: # 현재 창을 닫는 메소드
        misc.setStateOfButtons()
        self.destroy()

class TimerFrame(Frame):
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/timer_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 홈', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goBack(misc))
        goBackButton.place(x = 10, y = 10)

        # 타이머 기능
        self.__defaultLeftHours: int = 0; self.__defaultLeftMinutes: int = 1; self.__defaultLeftSeconds: int = 0

        self.__timerLabel: Label = Label(self, text = '{:02}:{:02}:{:02}'.format(self.__defaultLeftHours, self.__defaultLeftMinutes, self.__defaultLeftSeconds),\
                font = ('Arial', 37, 'bold'), bg = 'white')
        self.__timerLabel.place(x = 196, y = 223)

        self.__startTimerButton: Button = Button(self, text = 'Start', font = ('Arial', 9, 'bold'), bg = '#EBFBFF',\
                fg = '#2F8EFF', borderwidth = 0, activebackground = '#EBFBFF', activeforeground = 'yellow', command = lambda: self.startTimer())
        self.__stopTimerButton: Button = Button(self, text = 'Stop', font = ('Arial', 9, 'bold'), bg = '#EBFBFF',\
                fg = '#2F8EFF', borderwidth = 0, activebackground = '#EBFBFF', activeforeground = 'yellow', command = lambda: None)
        self.__resetTimerButton: Button = Button(self, text = 'Reset', font = ('Arial', 9, 'bold'), bg = '#EBFBFF',\
                fg = '#2F8EFF', borderwidth = 0, activebackground = '#EBFBFF', activeforeground = 'yellow', command = lambda: None)
        
        self.__startTimerButton.place(x = 186, y = 399)
        self.__stopTimerButton.place(x = 284, y = 399)
        self.__resetTimerButton.place(x = 377, y = 399)

        self.__started: bool = False # 타이머 시작 여부

        # 각종 타이머 버튼: 사용자는 타이머 시간을 설정할 수 있음.
        self.__oneMinuteButton: TimerButton = TimerButton(self, 'one')
        self.__fiveMinutesButton: TimerButton = TimerButton(self, 'five')
        self.__tenMinutesButton: TimerButton = TimerButton(self, 'ten')
        self.__customButton: TimerButton = TimerButton(self, 'custom')

        self.__oneMinuteButton.place(x = 166, y = 459)
        self.__fiveMinutesButton.place(x = 303, y = 459)
        self.__tenMinutesButton.place(x = 166, y = 506)
        self.__customButton.place(x = 303, y = 506)

    def setStateOfButtons(self) -> None: # 각 버튼의 상태를 설정하는 메소드
        self.__startTimerButton.config(command = lambda: self.startTimer())

        self.__oneMinuteButton.getBackgroundLabel().bind('<Button-1>', lambda event: self.__oneMinuteButton.onClick(event, self, 'one'))
        self.__fiveMinutesButton.getBackgroundLabel().bind('<Button-1>', lambda event: self.__fiveMinutesButton.onClick(event, self, 'five'))
        self.__tenMinutesButton.getBackgroundLabel().bind('<Button-1>', lambda event: self.__tenMinutesButton.onClick(event, self, 'ten'))
        self.__customButton.getBackgroundLabel().bind('<Button-1>', lambda event: self.__customButton.onClick(event, self, 'custom'))

    def openInputLeftTimeFrame(self) -> None: # 타이머 시간 설정 프레임을 여는 메소드
        if self.__started:
            self.stopTimer()

        self.__startTimerButton.config(command = lambda: None)

        self.__oneMinuteButton.getBackgroundLabel().bind('<Button-1>', lambda event: None)
        self.__fiveMinutesButton.getBackgroundLabel().bind('<Button-1>', lambda event: None)
        self.__tenMinutesButton.getBackgroundLabel().bind('<Button-1>', lambda event: None)
        self.__customButton.getBackgroundLabel().bind('<Button-1>', lambda event: None)

        inputLeftTimeFrame: InputLeftTimeFrame = InputLeftTimeFrame(self)
        inputLeftTimeFrame.place(x = 175, y = 225)

    def setTimer(self, hours: int, minutes: int, seconds: int) -> None: # 남은 시간을 설정하는 메소드
        self.__defaultLeftHours = hours; self.__defaultLeftMinutes = minutes; self.__defaultLeftSeconds = seconds
        self.__timerLabel.config(text = '{:02}:{:02}:{:02}'.format(self.__defaultLeftHours, self.__defaultLeftMinutes, self.__defaultLeftSeconds))

        self.__startTimerButton.config(command = lambda: self.startTimer())
        self.__stopTimerButton.config(command = lambda: None)
        self.__resetTimerButton.config(command = lambda: None)

    def startTimer(self) -> None: # 타이머 시작 메소드
        if self.__timerLabel.cget('text') == '00:00:00':
            self.stopTimer()
            self.__startTimerButton.config(command = lambda: None)
            messagebox.showinfo('알림', '타이머가 종료되었습니다.')
            return

        if not self.__started:
            self.__started = True

        self.__startTimerButton.config(command = lambda: None)
        self.__stopTimerButton.config(command = lambda: self.stopTimer())
        self.__resetTimerButton.config(command = lambda: self.resetTimer())

        timeDatas: list[int] = list(map(int, self.__timerLabel.cget('text').split(':')))
        totalSeconds: int = timeDatas[0] * 3600 + timeDatas[1] * 60 + timeDatas[2] - 1
        hours: int = totalSeconds // 3600
        minutes: int = (totalSeconds - hours * 3600) // 60
        seconds: int = totalSeconds % 60
        self.__timerLabel.config(text = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

        self.__afterId = self.__timerLabel.after(1000, lambda: self.startTimer())

    def stopTimer(self) -> None: # 타이머 종료 메소드
        self.__started = False

        self.__startTimerButton.config(command = lambda: self.startTimer())
        self.__stopTimerButton.config(command = lambda: None)
        self.__resetTimerButton.config(command = lambda: self.resetTimer())

        self.__timerLabel.after_cancel(self.__afterId)

    def resetTimer(self) -> None: # 타이머 초기화 메소드
        self.stopTimer()

        self.__startTimerButton.config(command = lambda: self.startTimer())
        self.__stopTimerButton.config(command = lambda: None)
        self.__resetTimerButton.config(command = lambda: self.resetTimer())

        self.__timerLabel.config(text = '{:02}:{:02}:{:02}'.format(self.__defaultLeftHours, self.__defaultLeftMinutes, self.__defaultLeftSeconds))

    def goBack(self, misc: Misc) -> None: # 뒤로가기 메소드
        misc.showTimeTable()
        self.destroy()

if DEBUG:
    window: Tk = Tk()
    window.title('Timer Frame')
    window.geometry('600x600')

    timerFrame: TimerFrame = TimerFrame(window)
    timerFrame.place(x = 0, y = 0)

    window.mainloop()
