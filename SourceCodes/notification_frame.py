# 알림 화면 관련 모듈

from path_settings import path

from tkinter import *
from user import *
from notification_system import NotificationSystem

DEBUG: bool = False

class NotificationFrame(Frame):
    def __init__(self, misc: Misc, user: User) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)
        self.__user: User = user

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/notification_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 홈', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goBack(misc))
        goBackButton.place(x = 10, y = 10)

        # 리마인더 관련 알림 업데이트
        NotificationSystem.updateReminderNotification(self.__user)

        self.__notificationFrameList: list[Frame] = []
        self.__messageLabel: Label = None # 알림 목록이 없을 경우 표시해주는 메시지 레이블
        self.__notificationList: list[Notification] = self.__user.getNotificationList()
        self.__lastIndex: int = len(self.__notificationList) - 1 # 마지막 알림을 가리키는 인덱스

        self.__previousButton: Button = Button(self, text = '▲', font = ('Arial', 10, 'bold'), bg = 'white', fg = 'black',\
                width = 2, borderwidth = 1, command = lambda: self.showPreviousNotifications())
        self.__nextButton: Button = Button(self, text = '▼', font = ('Arial', 10, 'bold'), bg = 'white', fg = 'black',\
                width = 2, borderwidth = 1, command = lambda: self.showNextNotifications())

        self.showNotifications()

    def showNotifications(self) -> None: # 알림 리스트를 보여주는 메소드
        for i in range(len(self.__notificationFrameList)):
            self.__notificationFrameList[i].destroy()
        self.__notificationFrameList.clear()
        if self.__messageLabel != None:
            self.__messageLabel.destroy()

        if len(self.__notificationList) == 0: # 알림 목록이 없을 경우 메시지를 표시함.
            self.__previousButton.place_forget()
            self.__nextButton.place_forget()

            self.__messageLabel = Label(self, text = '알림이 없습니다.', font = ('Arial', 13, 'bold'), bg = '#EBFBFF', borderwidth = 0)
            self.__messageLabel.place(x = 235, y = 320)
        else: # 알림 목록이 있을 경우 최대 8개의 알림을 표시함.
            if len(self.__notificationList) <= 8:
                self.__previousButton.config(state = 'disabled')
                self.__nextButton.config(state = 'disabled')
            else:
                if self.__lastIndex >= len(self.__notificationList) - 1:
                    self.__nextButton.config(state = 'disabled')
                else:
                    self.__nextButton.config(state = 'normal')

                if self.__lastIndex - 7 <= 0:
                    self.__previousButton.config(state = 'disabled')
                else:
                    self.__previousButton.config(state = 'normal')

            self.__previousButton.place(x = 508, y = 160)
            self.__nextButton.place(x = 508, y = 503)

            notificationList: list[Notification] = []
            if self.__lastIndex + 1 >= 8:
                for i in range(self.__lastIndex - 7, self.__lastIndex + 1, 1):
                    notificationList.append(self.__notificationList[i])
            else:
                for i in range(len(self.__notificationList)):
                    notificationList.append(self.__notificationList[i])

            for i in range(len(notificationList)):
                notificationDataFrame: Frame = Frame(self, width = 400, height = 40, bg = 'white', borderwidth = 0)
                date: dt.datetime = notificationList[i].getDate()
                memo: str = notificationList[i].getMemo()
                notificationLabel: Label = Label(notificationDataFrame, text = '[{}/{}/{} {:2d}:{:2d}:{:2d}] {}'\
                        .format(date.year, date.month, date.day, date.hour, date.minute, date.second, memo),\
                        font = ('Arial', 10, 'bold'), bg = 'white', borderwidth = 0)
                notificationLabel.place(x = 15, y = 10)
                removeButton: Button = Button(notificationDataFrame, text = 'X', font = ('Arial', 10, 'bold'),\
                        bg = 'white', fg = 'blue', activebackground = 'white', activeforeground = 'yellow', borderwidth = 0,\
                        command = lambda index = i: self.removeNotification(index))
                removeButton.place(x = 370, y = 9)
                self.__notificationFrameList.append(notificationDataFrame)

            for i in range(len(self.__notificationFrameList)):
                self.__notificationFrameList[i].place(x = 100, y = 160 + 47 * i)

    def removeNotification(self, index: int) -> None: # 특정 알림을 삭제하는 메소드
        popIndex: int = -1
        if len(self.__notificationList) > 8:
            popIndex = self.__lastIndex - 7 + index
        else:
            popIndex = index
        self.__notificationList.pop(popIndex)
        if self.__lastIndex + 1 >= len(self.__notificationList):
            self.__lastIndex -= 1
        self.__user.setNotificationList(self.__notificationList)

        removeUser(self.__user.getId())
        addUser(self.__user)

        self.showNotifications()

    def showPreviousNotifications(self) -> None: # 이전 알림을 보여주는 메소드
        self.__lastIndex -= 1
        self.showNotifications()

    def showNextNotifications(self) -> None: # 다음 알림을 보여주는 메소드
        self.__lastIndex += 1
        self.showNotifications()

    def goBack(self, misc: Misc) -> None: # 뒤로가기 메소드
        misc.showTimeTable()
        self.destroy()

if DEBUG:
    window: Tk = Tk()
    window.title('Notification Frame')
    window.geometry('600x600')

    testUser: User = User()
    notificationList: list[Notification] = []
    for i in range(15):
        notification: Notification = Notification(dt.datetime.now(), 'notification {}'.format(i + 1))
        notificationList.append(notification)
    testUser.setNotificationList(notificationList)

    notificationFrame: NotificationFrame = NotificationFrame(window, testUser)
    notificationFrame.place(x = 0, y = 0)

    window.mainloop()
