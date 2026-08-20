# 스톱워치 기능

from tkinter import *

DEBUG: bool = False
path: str = '.' # 필요에 따라 변경 가능

class StopwatchFrame(Frame):
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/stopwatch_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 홈', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goBack(misc))
        goBackButton.place(x = 10, y = 10)

        # 스톱워치 기능
        self.__stopwatchLabel: Label = Label(self, text = '00:00:00', font = ('Arial', 42, 'bold'), bg = 'white')
        self.__stopwatchLabel.place(x = 187, y = 233)

        self.__startStopWatchButton: Button = Button(self, text = 'Start', font = ('Arial', 10, 'bold'), bg = '#EBFBFF',\
                fg = '#2F8EFF', borderwidth = 0, activebackground = '#EBFBFF', activeforeground = 'yellow', command = lambda: self.startStopWatch())
        self.__stopStopWatchButton: Button = Button(self, text = 'Stop', font = ('Arial', 10, 'bold'), bg = '#EBFBFF',\
                fg = '#2F8EFF', borderwidth = 0, activebackground = '#EBFBFF', activeforeground = 'yellow', command = lambda: None)
        self.__resetStopWatchButton: Button = Button(self, text = 'Reset', font = ('Arial', 10, 'bold'), bg = '#EBFBFF',\
                fg = '#2F8EFF', borderwidth = 0, activebackground = '#EBFBFF', activeforeground = 'yellow', command = lambda: None)
        
        self.__startStopWatchButton.place(x = 173, y = 444)
        self.__stopStopWatchButton.place(x = 282, y = 444)
        self.__resetStopWatchButton.place(x = 387, y = 444)

        self.__started: bool = False # 스톱워치 시작 여부

    def startStopWatch(self) -> None: # 스톱워치 시작 메소드
        if self.__stopwatchLabel.cget('text') == '23:59:59':
            self.stopStopWatch()
            self.__startStopWatchButton.config(command = lambda: None)
            return

        if not self.__started:
            self.__started = True

        self.__startStopWatchButton.config(command = lambda: None)
        self.__stopStopWatchButton.config(command = lambda: self.stopStopWatch())
        self.__resetStopWatchButton.config(command = lambda: self.resetStopWatch())

        timeDatas: list[int] = list(map(int, self.__stopwatchLabel.cget('text').split(':')))
        totalSeconds: int = timeDatas[0] * 3600 + timeDatas[1] * 60 + timeDatas[2] + 1
        hours: int = totalSeconds // 3600
        minutes: int = (totalSeconds - hours * 3600) // 60
        seconds: int = totalSeconds % 60
        self.__stopwatchLabel.config(text = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

        self.__afterId = self.__stopwatchLabel.after(1000, lambda: self.startStopWatch())

    def stopStopWatch(self) -> None: # 스톱워치 종료 메소드
        self.__started = False

        self.__startStopWatchButton.config(command = lambda: self.startStopWatch())
        self.__stopStopWatchButton.config(command = lambda: None)
        self.__resetStopWatchButton.config(command = lambda: self.resetStopWatch())

        self.__stopwatchLabel.after_cancel(self.__afterId)

    def resetStopWatch(self) -> None: # 스톱워치 초기화 메소드
        self.stopStopWatch()

        self.__startStopWatchButton.config(command = lambda: self.startStopWatch())
        self.__stopStopWatchButton.config(command = lambda: None)
        self.__resetStopWatchButton.config(command = lambda: self.resetStopWatch())

        self.__stopwatchLabel.config(text = '00:00:00')

    def goBack(self, misc: Misc) -> None: # 뒤로가기 메소드
        misc.showTimeTable()
        self.destroy()

if DEBUG:
    window: Tk = Tk()
    window.title('Stopwatch Frame')
    window.geometry('600x600')

    stopWatchFrame: StopwatchFrame = StopwatchFrame(window)
    stopWatchFrame.place(x = 0, y = 0)

    window.mainloop()
