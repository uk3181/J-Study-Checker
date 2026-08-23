# 최종적으로 실행될 코드

from path_settings import path

from tkinter import *
from os import system
from login_frame import LoginFrame

class App:
    def __init__(self) -> None:
        window: Tk = Tk()
        window.iconphoto(True, PhotoImage(file = '{}/Images/Icons/app_icon.png'.format(path))) # 윈도우 아이콘 설정
        window.title('J Study Checker') # 제목 설정
        window.geometry('600x600') # 창 크기 설정
        window.resizable(False, False) # 창 크기를 조정하지 못하도록 함.

        loginFrame: LoginFrame = LoginFrame(window)
        loginFrame.place(x = 0, y = 0)

        window.mainloop()

def main() -> None:
    App()
main()
