# 사용자 설정 관련 모듈

from tkinter import *
from tkinter import messagebox
from user import *
from notification_system import NotificationSystem

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

class UserFrame(Frame):
    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)
        self.__user = user

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/user_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 홈', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goBack(misc))
        goBackButton.place(x = 10, y = 10)

        # 각종 사용자 정보 관련 기능
        idLabel: Label = Label(self, text = 'ID', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        passwordLabel: Label = Label(self, text = '비밀번호', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        passwordConfirmationLabel: Label = Label(self, text = '비밀번호 확인', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        nameLabel: Label = Label(self, text = '이름', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        ageLabel: Label = Label(self, text = '나이(만)', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')
        genderLabel: Label = Label(self, text = '성별', font = ('Arial', 13, 'bold'), bg = '#EBFBFF')

        self.__idEntry: Entry = Entry(self, font = ('Arial', 13, 'normal'), bg = 'white', disabledbackground = 'white',\
                disabledforeground = 'black', width = 22, borderwidth = 1)
        self.__passwordEntry: Entry = Entry(self, show = '●', font = ('Arial', 13, 'normal'), bg = 'white', width = 22, borderwidth = 1)
        self.__passwordConfirmationEntry: Entry = Entry(self, show = '●', font = ('Arial', 13, 'normal'), bg = 'white', width = 17, borderwidth = 1)
        self.__nameEntry: Entry = Entry(self, font = ('Arial', 13, 'normal'), bg = 'white', width = 17, borderwidth = 1)
        self.__ageEntry: Entry = Entry(self, font = ('Arial', 13, 'normal'), bg = 'white', width = 17, borderwidth = 1)
        self.__genderVar = StringVar()
        if self.__user.getGender() == User.MAN:
            self.__genderVar.set('남')
        else:
            self.__genderVar.set('여')
        self.__menRadioButton: Radiobutton = Radiobutton(self, text = '남', font = ('Arial', 13, 'bold'),\
                value = '남', variable = self.__genderVar, bg = '#EBFBFF', activebackground = '#EBFBFF',\
                activeforeground = 'blue', fg = 'blue', borderwidth = 1)
        self.__womanRadioButton: Radiobutton = Radiobutton(self, text = '여', font = ('Arial', 13, 'bold'),\
                value = '여', variable = self.__genderVar, bg = '#EBFBFF', activebackground = '#EBFBFF',\
                activeforeground = 'red', fg = 'red', borderwidth = 1)

        editPasswordButton: Button = Button(self, font = ('Arial', 8, 'bold'), text = '수정', bg = 'white',\
                width = 4, borderwidth = 1, command = lambda: self.editPassword())
        editNameButton: Button = Button(self, font = ('Arial', 8, 'bold'), text = '수정', bg = 'white',\
                width = 4, borderwidth = 1, command = lambda: self.editName())
        editAgeButton: Button = Button(self, font = ('Arial', 8, 'bold'), text = '수정', bg = 'white',\
                width = 4, borderwidth = 1, command = lambda: self.editAge())
        editGenderButton: Button = Button(self, font = ('Arial', 8, 'bold'), text = '수정', bg = 'white',\
                width = 4, borderwidth = 1, command = lambda: self.editGender())

        idLabel.place(x = 135, y = 170); self.__idEntry.place(x = 250, y = 170)
        passwordLabel.place(x = 135, y = 220); self.__passwordEntry.place(x = 250, y = 220);
        passwordConfirmationLabel.place(x = 135, y = 270); self.__passwordConfirmationEntry.place(x = 250, y = 270); editPasswordButton.place(x = 415, y = 270)
        nameLabel.place(x = 135, y = 320); self.__nameEntry.place(x = 250, y = 320); editNameButton.place(x = 415, y = 320)
        ageLabel.place(x = 135, y = 370); self.__ageEntry.place(x = 250, y = 370); editAgeButton.place(x = 415, y = 370)
        genderLabel.place(x = 135, y = 420)
        self.__menRadioButton.place(x = 245, y = 420); self.__womanRadioButton.place(x = 327, y = 420)
        editGenderButton.place(x = 415, y = 420)

        self.__idEntry.insert(0, self.__user.getId())
        self.__idEntry.config(state = 'disabled')
        self.setEntries()

        # 취소 버튼
        cancelButton: Button = Button(self, text = '취소', font = ('Arial', 11, 'bold'),\
                background = 'white', width = 6, borderwidth = 1, command = lambda: self.goBack(misc))
        cancelButton.place(x = 265, y = 480)

    def goBack(self, misc: Misc) -> None: # 뒤로가기 메소드
        misc.showTimeTable()
        self.destroy()

    def setEntries(self) -> None: # 엔트리에 각종 정보를 표시해주는 메소드
        self.__passwordEntry.delete(0, END); self.__passwordEntry.insert(0, self.__user.getPassword())
        self.__passwordConfirmationEntry.delete(0, END)
        self.__nameEntry.delete(0, END); self.__nameEntry.insert(0, self.__user.getName())
        self.__ageEntry.delete(0, END); self.__ageEntry.insert(0, self.__user.getAge())
        if self.__user.getGender() == User.MAN:
            self.__genderVar.set('남')
        else:
            self.__genderVar.set('여')

    def editPassword(self) -> None: # 비밀번호 수정 메소드
        # 비밀번호 엔트리 체크
        password: str = self.__passwordEntry.get()
        if not password.strip():
            messagebox.showwarning('경고', '비밀번호를 입력하세요.')
            self.setEntries()
            return
        if len(password) < 5 or len(password) > 15:
            messagebox.showwarning('경고', '비밀번호는 5~15자로 입력하세요.')
            self.setEntries()
            return
        # 비밀번호 확인 엔트리 체크
        confirmedPassword: str = self.__passwordConfirmationEntry.get()
        if not confirmedPassword.strip():
            messagebox.showwarning('경고', '비밀번호를 입력하세요.')
            self.setEntries()
            return 
        if password != confirmedPassword:
            messagebox.showwarning('경고', '비밀번호가 일치하지 않습니다.')
            self.setEntries()
            return
        
        self.__user.setPassword(password)
        removeUser(self.__user.getId())
        addUser(self.__user)
        messagebox.showinfo('알림', '비밀번호 변경이 완료되었습니다.')
        self.setEntries()

        NotificationSystem.updateUserInfoNotification(self.__user, '비밀번호')

    def editName(self) -> None: # 이름 수정 메소드
        # 이름 엔트리 체크
        name: str = self.__nameEntry.get()
        if not name.strip():
            messagebox.showwarning('경고', '이름을 입력하세요.')
            self.setEntries()
            return
        if len(name) > 15:
            messagebox.showwarning('경고', '이름이 너무 깁니다.')
            self.setEntries()
            return

        self.__user.setName(name)
        removeUser(self.__user.getId())
        addUser(self.__user)
        messagebox.showinfo('알림', '이름 변경이 완료되었습니다.')
        self.setEntries()

        NotificationSystem.updateUserInfoNotification(self.__user, '이름')

    def editAge(self) -> None: # 나이 수정 메소드
        # 나이 엔트리 체크
        if not self.__ageEntry.get().strip():
            messagebox.showwarning('경고', '나이를 입력하세요.')
            self.setEntries()
            return
        try:
            age: int = int(self.__ageEntry.get())
        except ValueError:
            messagebox.showwarning('경고', '나이는 정수로 입력하세요.')
            self.setEntries()
            return
        if age < 0 or age > 150:
            messagebox.showwarning('경고', '입력하신 나이를 다시 확인하세요.')
            self.setEntries()
            return

        self.__user.setAge(age)
        removeUser(self.__user.getId())
        addUser(self.__user)
        messagebox.showinfo('알림', '나이 변경이 완료되었습니다.')
        self.setEntries()

        NotificationSystem.updateUserInfoNotification(self.__user, '나이')

    def editGender(self) -> None: # 성별 수정 메소드
        if self.__genderVar.get() == '남':
            self.__user.setGender(User.MAN)
        else:
            self.__user.setGender(User.WOMAN)
        removeUser(self.__user.getId())
        addUser(self.__user)
        messagebox.showinfo('알림', '성별 변경이 완료되었습니다.')
        self.setEntries()

        NotificationSystem.updateUserInfoNotification(self.__user, '성별')

if DEBUG:
    window: Tk = Tk()
    window.title('Home Frame')
    window.geometry('600x600')

    testUser: User = User()

    userFrame: UserFrame = UserFrame(window, testUser)
    userFrame.place(x = 0, y = 0)

    window.mainloop()
