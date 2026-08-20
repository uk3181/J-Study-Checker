# 사용자 관련 모듈

import pickle as pk
from sortedcontainers import SortedList
import datetime as dt

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

class Notification: # 알림 클래스
    def __init__(self, date: dt.datetime, memo: str) -> None:
        self.__date: dt.datetime = date
        self.__memo: str = memo

    ################################ Getter/Setter ####################################
    def getDate(self) -> dt.datetime:
        return self.__date

    def getMemo(self) -> str:
        return self.__memo
    ####################################################################################

class StudyData: # 학습 데이터 클래스
    def __init__(self, studyDate: dt.datetime, subject: str, studyingTimeList: list[list[dt.datetime]], targetStudyingTime: int = 1800):
        self.__studyDate: dt.datetime = studyDate # 학습 날짜
        self.__subject: str = subject # 과목
        self.__studyingTimeList: list[list[dt.datetime]] = studyingTimeList # 학습을 진행한 시간을 담는 리스트
                                                                            # [[시작 시간 1, 종료 시간 1], [시작 시간 2, 종료 시간 2], ...]
        self.__targetStudyingTime: int = targetStudyingTime # 목표 학습 시간

    ################################ Getter/Setter ####################################
    def getStudyDate(self) -> dt.datetime:
        return self.__studyDate

    def getSubject(self) -> str:
        return self.__subject

    def getStudyingTimeList(self) -> list[list[dt.datetime]]:
        return self.__studyingTimeList

    def getTargetStudyingTime(self) -> int:
        return self.__targetStudyingTime
    ####################################################################################

class GradeData: # 성적 데이터 클래스
    TOEIC: int = 0; TOEFL: int = 1; CSAT: int = 2; OTHER: int = 3

    def __init__(self, date: dt.datetime) -> None:
        self.__date: dt.datetime = date

    def __lt__(self, other) -> bool:
        return self.__date.date() < other.__date.date()

    def __le__(self, other) -> bool:
        return self.__date.date() <= other.__date.date()

    def __eq__(self, other) -> bool:
        return self.__date.date() == other.__date.date()

    def __ne__(self, other) -> bool:
        return self.__date.date() != other.__date.date()

    def __gt__(self, other) -> bool:
        return self.__date.date() > other.__date.date()

    def __ge__(self, other) -> bool:
        return self.__date.date() >= other.__date.date()

    ################################ Getter/Setter ####################################
    def getDate(self) -> dt.datetime:
        return self.__date
    ####################################################################################

class TOEICGradeData(GradeData): # 토익 성적 데이터 클래스
    def __init__(self, date: dt.datetime, rc: int, lc: int) -> None:
        super().__init__(date)
        self.__rc: int = rc # rc
        self.__lc: int = lc # lc

    ################################ Getter/Setter ####################################
    def getRc(self) -> int:
        return self.__rc
    
    def getLc(self) -> int:
        return self.__lc
    ####################################################################################

class TOEFLGradeData(GradeData): # 토플 성적 데이터 클래스
    def __init__(self, date: dt.datetime, reading: int, listening: int, speaking: int, writing: int) -> None:
        super().__init__(date)
        self.__reading: int = reading # reading
        self.__listening: int = listening # listening
        self.__speaking: int = speaking # speaking
        self.__writing: int = writing # writing

    ################################ Getter/Setter ####################################
    def getReading(self) -> int:
        return self.__reading

    def getListening(self) -> int:
        return self.__listening

    def getSpeaking(self) -> int:
        return self.__speaking

    def getWriting(self) -> int:
        return self.__writing
    ####################################################################################

class CSATGradeData(GradeData): # 수능 성적 데이터 클래스
    def __init__(self, date: dt.datetime, subject: str, standardScore: int, grade: int, percentile: int) -> None:
        super().__init__(date)
        self.__subject: str = subject # 과목
        self.__standardScore: int = standardScore # 표준점수
        self.__grade: int = grade # 등급
        self.__percentile: int = percentile # 백분위

    ################################ Getter/Setter ####################################
    def getSubject(self) -> str:
        return self.__subject

    def getStandardScore(self) -> int:
        return self.__standardScore

    def getGrade(self) -> int:
        return self.__grade

    def getPercentile(self) -> int:
        return self.__percentile
    ####################################################################################

class OtherGradeData(GradeData): # 기타 성적 데이터 클래스
    def __init__(self, date: dt.datetime, subject: str, score: float, maxScore: float, minScore: float) -> None:
        super().__init__(date)
        self.__subject: str = subject # 과목
        self.__score: float = score # 점수
        self.__maxScore: float = maxScore # 최고점
        self.__minScore: float = minScore # 최저점

    ################################ Getter/Setter ####################################
    def getSubject(self) -> str:
        return self.__subject

    def getScore(self) -> float:
        return self.__score

    def getMaxScore(self) -> float:
        return self.__maxScore

    def getMinScore(self) -> float:
        return self.__minScore
    ####################################################################################

class ReminderData: # 리마인더 클래스
    def __init__(self, date: dt.datetime, memo: str) -> None:
        self.__date: dt.datetime = date
        self.__memo: str = memo

    def __lt__(self, other) -> bool:
        return self.__date.date() < other.__date.date()

    def __le__(self, other) -> bool:
        return self.__date.date() <= other.__date.date()

    def __eq__(self, other) -> bool:
        return self.__date.date() == other.__date.date()

    def __ne__(self, other) -> bool:
        return self.__date.date() != other.__date.date()

    def __gt__(self, other) -> bool:
        return self.__date.date() > other.__date.date()

    def __ge__(self, other) -> bool:
        return self.__date.date() >= other.__date.date()

    ################################ Getter/Setter ####################################
    def getDate(self) -> dt.datetime:
        return self.__date

    def setMemo(self, memo: str) -> None:
        self.__memo = memo

    def getMemo(self) -> str:
        return self.__memo
    ####################################################################################

class User: # 사용자 클래스
    MAN: int = 0; WOMAN: int = 1; # 남/여

    def __init__(self, id: str = 'uk3181', password: str = 'uk3181@', name: str = '정재욱',\
                age: int = 20, gender: int = MAN) -> None:
        self.__id: str = id # ID
        self.__password: str = password # 비밀번호

        self.__name: str = name # 이름
        self.__age: int = age # 나이
        self.__gender: int = gender # 성별

        self.__notificationList: list[Notification] = [] # 알림 리스트
        self.__studyDataList: list[StudyData] = [] # 학습 데이터 리스트

        self.__toeicGradeDataList: SortedList[TOEICGradeData] = SortedList() # 토익 성적 데이터 리스트
        self.__toeflGradeDataList: SortedList[TOEFLGradeData] = SortedList() # 토플 성적 데이터 리스트
        self.__csatGradeDataList: SortedList[CSATGradeData] = SortedList() # 수능 성적 데이터 리스트
        self.__otherGradeDataList: SortedList[OtherGradeData] = SortedList() # 기타 성적 데이터 리스트

        self.__subjectLst: list[str] = [] # 저장된 과목 리스트
        self.__reminderList: SortedList[ReminderData] = SortedList() # 리마인더 리스트

    def __lt__(self, other) -> bool:
        return self.__id < other.__id

    def __le__(self, other) -> bool:
        return self.__id <= other.__id

    def __eq__(self, other) -> bool:
        return self.__id == other.__id

    def __ne__(self, other) -> bool:
        return self.__id != other.__id
    
    def __gt__(self, other) -> bool:
        return self.__id > other.__id

    def __ge__(self, other) -> bool:
        return self.__id >= other.__id

    ################################ Getter/Setter ####################################
    def getId(self) -> str:
        return self.__id

    def setPassword(self, password: str) -> None:
        self.__password = password

    def getPassword(self) -> str:
        return self.__password

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setAge(self, age: int) -> None:
        self.__age = age

    def getAge(self) -> int:
        return self.__age

    def setGender(self, gender: int) -> None:
        self.__gender = gender

    def getGender(self) -> int:
        return self.__gender

    def setNotificationList(self, notificationList: list[Notification]) -> None:
        self.__notificationList = notificationList

    def getNotificationList(self) -> list[Notification]:
        return self.__notificationList

    def setStudyDataList(self, studyDataList: list[StudyData]) -> None:
        self.__studyDataList = studyDataList

    def getStudyDataList(self) -> list[StudyData]:
        return self.__studyDataList

    def setToeicGradeDataList(self, toeicGradeDataList: SortedList[TOEICGradeData]) -> None:
        self.__toeicGradeDataList = toeicGradeDataList

    def getToeicGradeDataList(self) -> SortedList[TOEICGradeData]:
        return self.__toeicGradeDataList

    def setToeflGradeDataList(self, toeflGradeDataList: SortedList[TOEFLGradeData]) -> None:
        self.__toeflGradeDataList = toeflGradeDataList

    def getToeflGradeDataList(self) -> SortedList[TOEFLGradeData]:
        return self.__toeflGradeDataList

    def setCsatGradeDataList(self, csatGradeDataList: SortedList[CSATGradeData]) -> None:
        self.__csatGradeDataList = csatGradeDataList

    def getCsatGradeDataList(self) -> SortedList[CSATGradeData]:
        return self.__csatGradeDataList

    def setOtherGradeDataList(self, otherGradeDataList: SortedList[OtherGradeData]) -> None:
        self.__otherGradeDataList = otherGradeDataList

    def getOtherGradeDataList(self) -> SortedList[OtherGradeData]:
        return self.__otherGradeDataList

    def setSubjectList(self, subjectList: list[str]) -> None:
        self.__subjectLst = subjectList

    def getSubjectList(self) -> list[str]:
        return self.__subjectLst

    def getReminderList(self) -> SortedList[ReminderData]:
        return self.__reminderList
    ####################################################################################

    def searchReminder(self, date: dt.datetime) -> bool: # 반환값: 인덱스 (실패 시 -1)
        tempReminder: ReminderData = ReminderData(date, '')
        try:
            return self.__reminderList.index(tempReminder)
        except ValueError:
            return -1

    def addReminder(self, reminder: ReminderData) -> None:
        self.__reminderList.add(reminder)

    def removeReminder(self, date: dt.datetime) -> None:
        tempReminder: ReminderData = ReminderData(date, '')
        self.__reminderList.remove(tempReminder)

def setUserList(userList: SortedList[User]) -> None: # 파일 'user_list.bin'에 사용자 목록을 갱신하는 함수
    userListFile = open('{}/Datas/user_list.bin'.format(path), mode = 'wb')
    pk.dump(file = userListFile, obj = userList)
    userListFile.close()

def getUserList() -> SortedList[User]: # 파일 'user_list.bin'으로부터 사용자 목록을 가져오는 함수
    userListFile = open('{}/Datas/user_list.bin'.format(path), mode = 'rb')
    userList: SortedList[User] = pk.load(file = userListFile)
    userListFile.close()
    return userList

def searchUser(id: str) -> int: # 파일 'user_list.bin'의 사용자 목록에서 특정 사용자를 ID 기준으로 검색하는 함수
                                # 반환값: 인덱스 (실패 시 -1)
    userList: SortedList[User] = getUserList()
    tempUser: User = User(id)
    try:
        return userList.index(tempUser)
    except ValueError:
        return -1

def addUser(user: User) -> None: # 파일 'user_list.bin'의 사용자 목록에 새로운 사용자를 추가하는 함수
    userList: SortedList[User] = getUserList()
    userList.add(user)
    setUserList(userList)

def removeUser(id: str) -> None: # 파일 'user_list.bin'의 사용자 목록에서 특정 사용자를 ID 기준으로 삭제하는 함수
    userList: SortedList[User] = getUserList()
    tempUser: User = User(id)
    userList.remove(tempUser)
    setUserList(userList)

def searchStudyData(studyDataList: list[StudyData], year: int, month: int, day: int) -> tuple[int]: # 학습 데이터 리스트에서 특정 날짜의 학습 데이터를 검색하는 함수
    startIndex: int = 0; endIndex: int = len(studyDataList) - 1
    while startIndex <= endIndex:
        middleIndex: int = (startIndex + endIndex) // 2
        studyDate: dt.datetime = studyDataList[middleIndex].getStudyDate()
        if year > studyDate.year:
            startIndex = middleIndex + 1
        elif year == studyDate.year:
            if month > studyDate.month:
                startIndex = middleIndex + 1
            elif month == studyDate.month:
                if day > studyDate.day:
                    startIndex = middleIndex + 1
                elif day == studyDate.day:
                    leftFromMiddleIndex: int = middleIndex; rightFromMiddleIndex: int = middleIndex
                    while leftFromMiddleIndex >= 0 and (studyDataList[leftFromMiddleIndex].getStudyDate().year == year and studyDataList[leftFromMiddleIndex].getStudyDate().month == month\
                            and studyDataList[leftFromMiddleIndex].getStudyDate().day == day):
                        leftFromMiddleIndex -= 1
                    leftFromMiddleIndex += 1
                    while rightFromMiddleIndex <= len(studyDataList) - 1 and (studyDataList[rightFromMiddleIndex].getStudyDate().year == year and studyDataList[rightFromMiddleIndex].getStudyDate().month == month\
                            and studyDataList[rightFromMiddleIndex].getStudyDate().day == day):
                        rightFromMiddleIndex += 1
                    rightFromMiddleIndex -= 1
                    return (leftFromMiddleIndex, rightFromMiddleIndex)
                else:
                    endIndex = middleIndex - 1
            else:
                endIndex = middleIndex - 1
        else:
            endIndex = middleIndex - 1
    return (-1, -1)

if DEBUG:
    userList: SortedList[User] = SortedList()
    userList.add(User('uk3181', 'wook2874@sb', '정재욱', 23, User.MAN))

    setUserList(userList)

    userList = getUserList()
    for i in range(len(userList)):
        user: User = userList[i]
        print('ID: {}'.format(user.getId()))
        print('비밀번호: {}'.format(user.getPassword()))
        print('이름: {}'.format(user.getName()))
        print('나이: {}세'.format(user.getAge()))
        if user.getGender() == User.MAN:
            print('성별: {}'.format('남'))
        else:
            print('성별: {}'.format('여'))
