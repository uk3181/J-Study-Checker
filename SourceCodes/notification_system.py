# 알림 시스템

from user import *

class NotificationSystem:
    @staticmethod
    def updateReminderNotification(user: User) -> None: # 리마인더 알림을 업데이트하는 메소드
        now: dt.datetime = dt.datetime.now()
        reminderList: SortedList[ReminderData] = user.getReminderList()

        startIndex: int = 0; endIndex: int = len(reminderList) - 1
        while startIndex <= endIndex:
            middleIndex: int = (startIndex + endIndex) // 2
            reminderData: ReminderData = reminderList[middleIndex]
            if reminderData.getDate().date() > now.date():
                endIndex = middleIndex - 1
            elif reminderData.getDate().date() == now.date():
                notificationList: list[Notification] = user.getNotificationList()
                for i in range(len(notificationList) - 1, -1, -1):
                    if notificationList[i].getDate().date() == now.date()\
                            and notificationList[i].getMemo() == '예약된 리마인더가 있습니다.':
                        return
                notificationList.append(Notification(now, '예약된 리마인더가 있습니다.'))
                user.setNotificationList(notificationList)

                removeUser(user.getId())
                addUser(user)
                break
            else:
                startIndex = middleIndex + 1

    @staticmethod
    def updateUserInfoNotification(user: User, infoType: str) -> None: # 사용자 정보 변경 알림을 업데이트하는 메소드
        notificationList: list[Notification] = user.getNotificationList()
        notificationList.append(Notification(dt.datetime.now(), '사용자 정보({})가 변경되었습니다.'.format(infoType)))

        removeUser(user.getId())
        addUser(user)
