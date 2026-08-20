# 파일 'user_list.bin' 초기화 관련 모듈

from user import *
from sortedcontainers import SortedList

userList: SortedList[User] = SortedList()
setUserList(userList)
