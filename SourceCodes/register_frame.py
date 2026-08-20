# 사용자 등록 관련 모듈

from tkinter import *
from tkinter import messagebox
from user import *

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

class RegisterFrame(Frame):
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/register_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 로그인', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.destroy())
        goBackButton.place(x = 10, y = 10)

        # 각종 사용자 정보 관련 기능
        idLabel: Label = Label(self, text = 'ID', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        passwordLabel: Label = Label(self, text = '비밀번호', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        passwordConfirmationLabel: Label = Label(self, text = '비밀번호 확인', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        nameLabel: Label = Label(self, text = '이름', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        ageLabel: Label = Label(self, text = '나이(만)', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        genderLabel: Label = Label(self, text = '성별', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')

        self.__idEntry: Entry = Entry(self, font = ('Arial', 13, 'normal'), bg = 'white', width = 22, borderwidth = 1)
        self.__passwordEntry: Entry = Entry(self, show = '●', font = ('Arial', 13, 'normal'), bg = 'white', width = 22, borderwidth = 1)
        self.__passwordConfirmationEntry: Entry = Entry(self, show = '●', font = ('Arial', 13, 'normal'), bg = 'white', width = 22, borderwidth = 1)
        self.__nameEntry: Entry = Entry(self, font = ('Arial', 13, 'normal'), bg = 'white', width = 22, borderwidth = 1)
        self.__ageEntry: Entry = Entry(self, font = ('Arial', 13, 'normal'), bg = 'white', width = 22, borderwidth = 1)
        self.__genderVar = StringVar()
        self.__genderVar.set('남')
        self.__menRadioButton: Radiobutton = Radiobutton(self, text = '남', font = ('Arial', 13, 'bold'),\
                value = '남', variable = self.__genderVar, bg = '#EBFBFF', activebackground = '#EBFBFF',\
                activeforeground = 'blue', fg = 'blue', borderwidth = 1)
        self.__womanRadioButton: Radiobutton = Radiobutton(self, text = '여', font = ('Arial', 13, 'bold'),\
                value = '여', variable = self.__genderVar, bg = '#EBFBFF', activebackground = '#EBFBFF',\
                activeforeground = 'red', fg = 'red', borderwidth = 1)

        idLabel.place(x = 135, y = 170); self.__idEntry.place(x = 250, y = 170)
        passwordLabel.place(x = 135, y = 220); self.__passwordEntry.place(x = 250, y = 220)
        passwordConfirmationLabel.place(x = 135, y = 270); self.__passwordConfirmationEntry.place(x = 250, y = 270)
        nameLabel.place(x = 135, y = 320); self.__nameEntry.place(x = 250, y = 320)
        ageLabel.place(x = 135, y = 370); self.__ageEntry.place(x = 250, y = 370)
        genderLabel.place(x = 135, y = 420)
        self.__menRadioButton.place(x = 245, y = 420); self.__womanRadioButton.place(x = 345, y = 420)

        # 사용자 등록 버튼
        registerButton: Button = Button(self, text = '사용자 등록', font = ('Arial', 11, 'bold'),\
                background = 'white', borderwidth = 1, command = lambda: self.registerUser())
        registerButton.place(x = 255, y = 480)

    def registerUser(self) -> None: # 사용자 등록 메소드
        # ID 엔트리 체크
        id: str = self.__idEntry.get()
        if not id.strip():
            messagebox.showwarning('경고', 'ID를 입력하세요.')
            return
        if len(id) < 5 or len(id) > 15:
            messagebox.showwarning('경고', 'ID는 5~15자로 입력하세요.')
            return
        for i in range(len(id)):
            if not (id[i] >= 'A' and id[i] <= 'Z' or id[i] >= 'a' and id[i] <= 'z' or id[i] >= '0' and id[i] <= '9'):
                messagebox.showwarning('경고', 'ID에는 영문자, 숫자만 포함 가능합니다.')
                return
        if searchUser(id) != -1:
            messagebox.showwarning('경고', '이미 존재하는 ID입니다.')
            return
        # 비밀번호 엔트리 체크
        password: str = self.__passwordEntry.get()
        if not password.strip():
            messagebox.showwarning('경고', '비밀번호를 입력하세요.')
            return
        if len(password) < 5 or len(password) > 15:
            messagebox.showwarning('경고', '비밀번호는 5~15자로 입력하세요.')
            return
        # 비밀번호 확인 엔트리 체크
        confirmedPassword: str = self.__passwordConfirmationEntry.get()
        if not confirmedPassword.strip():
            messagebox.showwarning('경고', '비밀번호를 입력하세요.')
            return 
        if password != confirmedPassword:
            messagebox.showwarning('경고', '비밀번호가 일치하지 않습니다.')
            return
        # 이름 엔트리 체크
        name: str = self.__nameEntry.get()
        if not name.strip():
            messagebox.showwarning('경고', '이름을 입력하세요.')
            return
        if len(name) > 15:
            messagebox.showwarning('경고', '이름이 너무 깁니다.')
            return
        # 나이 엔트리 체크
        if not self.__ageEntry.get().strip():
            messagebox.showwarning('경고', '나이를 입력하세요.')
            return
        try:
            age: int = int(self.__ageEntry.get())
        except ValueError:
            messagebox.showwarning('경고', '나이는 정수로 입력하세요.')
            return
        if age < 0 or age > 150:
            messagebox.showwarning('경고', '입력하신 나이를 다시 확인하세요.')
            return
        # 성별 엔트리 체크
        if self.__genderVar.get() == '남':
            gender: int = User.MAN
        else:
            gender: int = User.WOMAN

        # 새로운 사용자 생성 및 등록
        registeredUser: User = User(id, password, name, age, gender)
        addUser(registeredUser)
        messagebox.showinfo('알림', '사용자 등록이 완료되었습니다.')
        self.destroy()

if DEBUG:
    window: Tk = Tk()
    window.title('Register Frame')
    window.geometry('600x600')

    assignFrame: RegisterFrame = RegisterFrame(window)
    assignFrame.place(x = 0, y = 0)

    window.mainloop()
