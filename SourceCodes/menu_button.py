# 메뉴바에 들어갈 버튼 관련 모듈

from path_settings import path

from tkinter import *

class MenuButton(Button):
    def __init__(self, misc: Misc, buttonText: str, buttonBackground: str, buttonForeground: str, activeForeground: str, buttonCommand) -> None:
        super().__init__(misc, text = buttonText, font = ('Arial', 11, 'bold'), bg = buttonBackground, fg = buttonForeground,\
                command = buttonCommand, activebackground = buttonBackground, activeforeground = activeForeground, borderwidth = 0)
        self.__buttonForeground: str = buttonForeground
        self.__activeForeground: str = activeForeground

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    ################################ Getter/Setter ####################################
    def setButtonForeground(self, buttonForeground: str) -> None:
        self.__buttonForeground = buttonForeground
        self.config(fg = buttonForeground)
    ####################################################################################

    def onEnter(self, event: Event) -> None:
        self.config(fg = self.__activeForeground)

    def onLeave(self, event: Event) -> None:
        self.config(fg = self.__buttonForeground)

class UserButton(Frame):
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 28, height = 28, borderwidth = 0)
        self.__misc: Misc = misc

        self.__isMouseOnButton: bool = False
        self.__isMouseOnOptions: bool = False

        # 버튼 배경 이미지 설정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Icons/user_icon_1.png'.format(path))
        backgroundLabel: Label = Label(self, width = 28, height = 28, image = self.__backgroundPhotoImage, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 바인드 처리
        self.bind('<Enter>', lambda event: self.onEnter(event))
        self.bind('<Leave>', lambda event: self.onLeave(event))

        self.__optionsFrame: Frame = None # 옵션 프레임

    def onEnter(self, event: Event) -> None:
        self.__backgroundPhotoImage.config(file = '{}/Images/Icons/user_icon_2.png'.format(path))
        self.__isMouseOnButton = True
        self.showOptions()

    def onLeave(self, event: Event) -> None:
        self.__backgroundPhotoImage.config(file = '{}/Images/Icons/user_icon_1.png'.format(path))
        self.__isMouseOnButton = False
        self.hideOptions(Event(), 'button')

    def showOptions(self) -> None: # 사용자 관련 옵션을 보여주는 메소드
        def onOptionsFrame(event: Event) -> None:
            self.__isMouseOnOptions = True

        self.__optionsFrame: Frame = Frame(self.__misc, bg = '#F1F7FF', borderwidth = 0)
        self.__optionsFrame.bind('<Enter>', lambda event: onOptionsFrame(event))
        self.__optionsFrame.bind('<Leave>', lambda event: self.hideOptions(event, 'options'))

        userInfoButton: Button = Button(self.__optionsFrame, text = '사용자 정보', font = ('Arial', 10, 'bold'), bg = '#F1F7FF', activebackground = '#F1F7FF',\
                activeforeground = 'yellow', borderwidth = 0, command = lambda: self.__misc.openUserFrame())
        userInfoButton.bind('<Enter>', lambda event: userInfoButton.config(fg = 'yellow'))
        userInfoButton.bind('<Leave>', lambda event: userInfoButton.config(fg = 'black'))
        logoutButton: Button = Button(self.__optionsFrame, text = '로그아웃', font = ('Arial', 10, 'bold'), bg = '#F1F7FF', activebackground = '#F1F7FF',\
                activeforeground = 'yellow', borderwidth = 0, command = lambda: self.__misc.logout())
        logoutButton.bind('<Enter>', lambda event: logoutButton.config(fg = 'yellow'))
        logoutButton.bind('<Leave>', lambda event: logoutButton.config(fg = 'black'))
        removeUserButton: Button = Button(self.__optionsFrame, text = '사용자 삭제', font = ('Arial', 10, 'bold'), bg = '#F1F7FF', activebackground = '#F1F7FF',\
                activeforeground = 'yellow', borderwidth = 0)
        removeUserButton.bind('<Enter>', lambda event: removeUserButton.config(fg = 'yellow'))
        removeUserButton.bind('<Leave>', lambda event: removeUserButton.config(fg = 'black'))

        userInfoButton.grid(row = 0, column = 0)
        logoutButton.grid(row = 1, column = 0)
        removeUserButton.grid(row = 2, column = 0)
        self.__optionsFrame.place(x = 463, y = 153)

    def hideOptions(self, event: Event, type: str) -> None: # 사옹자 관련 옵션을 숨기는 메소드
                                                            # type은 마우스가 어디에서 빠져나왔는지 알려줌.
        def checkHideOptions() -> None:
            if not self.__isMouseOnButton and not self.__isMouseOnOptions: # 마우스가 버튼, 옵션 목록 모두 빠져나와 있으면 옵션 목록을 숨김.
                if self.__optionsFrame != None:
                    self.__optionsFrame.place_forget()
                    self.__optionsFrame = None

        if type == 'button':
            self.__isMouseOnButton = False
        elif type == 'options':
            self.__isMouseOnOptions = False

        self.after(100, checkHideOptions)

class ToolsButton(Button):
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, text = '도구', font = ('Arial', 11, 'bold'), bg = '#C1DDFF', fg = 'black',\
                activebackground = '#C1DDFF', activeforeground = 'yellow', borderwidth = 0)
        self.__misc: Misc = misc

        self.__isMouseOnButton: bool = False
        self.__isMouseOnOptions: bool = False

        # 바인드 처리
        self.bind('<Enter>', lambda event: self.onEnter(event))
        self.bind('<Leave>', lambda event: self.onLeave(event))

        self.__optionsFrame: Frame = None # 옵션 프레임

    def onEnter(self, event: Event) -> None:
        self.config(fg = 'yellow')

        self.__isMouseOnButton = True
        self.showOptions()

    def onLeave(self, event: Event) -> None:
        self.config(fg = 'black')

        self.__isMouseOnButton = False
        self.hideOptions(Event(), 'button')

    def showOptions(self) -> None: # 사용자 관련 옵션을 보여주는 메소드
        def onOptionsFrame(event: Event) -> None:
            self.__isMouseOnOptions = True

        self.__optionsFrame: Frame = Frame(self.__misc, bg = '#F1F7FF', borderwidth = 0)
        self.__optionsFrame.bind('<Enter>', lambda event: onOptionsFrame(event))
        self.__optionsFrame.bind('<Leave>', lambda event: self.hideOptions(event, 'options'))

        calculatorButton: Button = Button(self.__optionsFrame, text = '계산기', font = ('Arial', 10, 'bold'), bg = '#F1F7FF', activebackground = '#F1F7FF',\
                activeforeground = 'yellow', borderwidth = 0, command = lambda: self.__misc.openCalculatorFrame())
        calculatorButton.bind('<Enter>', lambda event: calculatorButton.config(fg = 'yellow'))
        calculatorButton.bind('<Leave>', lambda event: calculatorButton.config(fg = 'black'))
        timerButton: Button = Button(self.__optionsFrame, text = '타이머', font = ('Arial', 10, 'bold'), bg = '#F1F7FF', activebackground = '#F1F7FF',\
                activeforeground = 'yellow', borderwidth = 0, command = lambda: self.__misc.openTimerFrame())
        timerButton.bind('<Enter>', lambda event: timerButton.config(fg = 'yellow'))
        timerButton.bind('<Leave>', lambda event: timerButton.config(fg = 'black'))
        stopwatchButton: Button = Button(self.__optionsFrame, text = '스톱워치', font = ('Arial', 10, 'bold'), bg = '#F1F7FF', activebackground = '#F1F7FF',\
                activeforeground = 'yellow', borderwidth = 0, command = lambda: self.__misc.openStopwatchFrame())
        stopwatchButton.bind('<Enter>', lambda event: stopwatchButton.config(fg = 'yellow'))
        stopwatchButton.bind('<Leave>', lambda event: stopwatchButton.config(fg = 'black'))

        calculatorButton.grid(row = 0, column = 0)
        timerButton.grid(row = 1, column = 0)
        stopwatchButton.grid(row = 2, column = 0)
        self.__optionsFrame.place(x = 400, y = 153)

    def hideOptions(self, event: Event, type: str) -> None: # 사옹자 관련 옵션을 숨기는 메소드
                                                            # type은 마우스가 어디에서 빠져나왔는지 알려줌.
        def checkHideOptions() -> None:
            if not self.__isMouseOnButton and not self.__isMouseOnOptions: # 마우스가 버튼, 옵션 목록 모두 빠져나와 있으면 옵션 목록을 숨김.
                if self.__optionsFrame != None:
                    self.__optionsFrame.place_forget()
                    self.__optionsFrame = None

        if type == 'button':
            self.__isMouseOnButton = False
        elif type == 'options':
            self.__isMouseOnOptions = False

        self.after(100, checkHideOptions)

class NotificationButton(Frame):
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 25, height = 25, borderwidth = 0)
        self.__misc: Misc = misc

        # 버튼 배경 이미지 설정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Icons/notification_icon_1.png'.format(path))
        backgroundLabel: Label = Label(self, width = 25, height = 25, image = self.__backgroundPhotoImage, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 바인드 처리
        backgroundLabel.bind('<Enter>', self.onEnter)
        backgroundLabel.bind('<Leave>', self.onLeave)
        backgroundLabel.bind('<Button-1>', self.onClick)

    def onEnter(self, event: Event) -> None:
        self.__backgroundPhotoImage.config(file = '{}/Images/Icons/notification_icon_2.png'.format(path))

    def onLeave(self, event: Event) -> None:
        self.__backgroundPhotoImage.config(file = '{}/Images/Icons/notification_icon_1.png'.format(path))

    def onClick(self, event: Event) -> None:
        self.__misc.openNotificationFrame()
