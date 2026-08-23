# 로그인 관련 모듈

from path_settings import path

from tkinter import *
from tkinter import messagebox
from register_frame import RegisterFrame
from home_frame import HomeFrame
from user import *

DEBUG: bool = False

class LoginFrame(Frame):
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/login_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # ID/비밀번호 관련 기능
        # 1. ID
        idLabel: Label = Label(self, text = 'ID', font = ('Arial', 13, 'bold'), background = '#EBFBFF')
        self.__idEntry: Entry = Entry(self, font = ('Arial', 13, 'normal'), background = 'white', width = 15, borderwidth = 1)
        idLabel.place(x = 185, y = 375); self.__idEntry.place(x = 275, y = 375)
        # 2. 비밀번호
        passwordLabel: Label = Label(self, text = 'Password', font = ('Arial', 13, 'bold'), background = '#EBFBFF')
        self.__passwordEntry: Entry = Entry(self, show = '●', font = ('Arial', 13, 'normal'), background = 'white', width = 15, borderwidth = 1)
        passwordLabel.place(x = 185, y = 420); self.__passwordEntry.place(x = 275, y = 420)

        # 로그인/회원가입 관련 기능
        loginButton: Button = Button(self, text = '로그인', font = ('Arial', 11, 'bold'), background = '#F7E4FF',\
                width = 8, borderwidth = 1, command = lambda: self.login())
        registerButton: Button = Button(self, text = '사용자 등록', font = ('Arial', 11, 'bold'), background = 'white',\
                borderwidth = 1, command = lambda: self.openRegisterFrame())
        loginButton.place(x = 205, y = 485); registerButton.place(x = 295, y = 485)

    def resetEntries(self) -> None: # 각종 엔트리에 입력된 내용을 초기화하는 메소드
        self.__idEntry.delete(0, END)
        self.__passwordEntry.delete(0, END)

    def openRegisterFrame(self) -> None: # 사용자 등록 프레임을 여는 메소드
        registerFrame: RegisterFrame = RegisterFrame(self)
        registerFrame.place(x = 0, y = 0)
        self.resetEntries()

    def login(self) -> None: # 로그인 메소드
                             # 로그인 성공 시 홈 프레임으로 넘어감.
        if not self.__idEntry.get().strip():
            messagebox.showwarning('알림', 'ID를 입력하세요.')
            return
        if not self.__passwordEntry.get().strip():
            messagebox.showwarning('알림', '비밀번호를 입력하세요.')
            return

        userIndex: int = searchUser(self.__idEntry.get())
        if userIndex == -1:
            messagebox.showinfo('경고', 'ID/비밀번호가 올바르지 않습니다.')
            return
        loginedUser: User = getUserList()[userIndex] # 로그인한 사용자
        if loginedUser.getPassword() != self.__passwordEntry.get():
            messagebox.showinfo('경고', 'ID/비밀번호가 올바르지 않습니다.')
            return

        homeFrame: HomeFrame = HomeFrame(self, loginedUser)
        homeFrame.place(x = 0, y = 0)
        self.resetEntries()

if DEBUG:
    window: Tk = Tk()
    window.title('Login Frame')
    window.geometry('600x600')

    loginFrame: LoginFrame = LoginFrame(window)
    loginFrame.place(x = 0, y = 0)

    window.mainloop()
