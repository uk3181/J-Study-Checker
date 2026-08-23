# 계산기 관련 모듈

from path_settings import path

from tkinter import *

DEBUG: bool = False

class CalculatorButton(Frame): # 계산기에 들어갈 각종 버튼
    def __init__(self, misc: Misc, buttonWidth: int, buttonHeight: int, buttonBg: str,\
                buttonText: str) -> None:
        super().__init__(misc, width = buttonWidth, height = buttonHeight, bg = buttonBg, borderwidth = 0)
        self.__misc: Misc = misc
        self.__buttonBg: str = buttonBg

        self.__buttonLabel: Label = Label(self, text = buttonText, font = ('Arial', 23, 'bold'), width = 4, height = 2,\
                bg = buttonBg, borderwidth = 0)
        self.__buttonLabel.place(x = 1, y = 1)

        # 바인드 처리
        self.__buttonLabel.bind('<Enter>', lambda event: self.onEnter(event))
        self.__buttonLabel.bind('<Leave>', lambda event: self.onLeave(event))
        self.__buttonLabel.bind('<Button-1>', lambda event: self.onClick(event))

    def onEnter(self, event: Event) -> None:
        self.config(bg = 'yellow')
        self.__buttonLabel.config(bg = 'yellow', fg = 'white')

    def onLeave(self, event: Event) -> None:
        self.config(bg = self.__buttonBg)
        self.__buttonLabel.config(bg = self.__buttonBg, fg = 'black')

    def onClick(self, event: Event) -> None:
        buttonText: str = self.__buttonLabel.cget('text')
        if buttonText == '=':
            self.__misc.calculate()
        elif buttonText == 'C':
            self.__misc.resetElements()
        else:
            self.__misc.inputElements(buttonText)

class CalculatorFrame(Frame):
    def __init__(self, misc: Misc) -> None:
        super().__init__(misc, width = 600, height = 600, borderwidth = 0)

        # 배경 이미지 지정
        self.__backgroundPhotoImage: PhotoImage = PhotoImage(file = '{}/Images/Backgrounds/calculator_background.png'.format(path))
        backgroundLabel: Label = Label(self, image = self.__backgroundPhotoImage, width = 600, height = 600, borderwidth = 0)
        backgroundLabel.place(x = 0, y = 0)

        # 뒤로가기 버튼
        goBackButton: Button = Button(self, text = '< 홈', font = ('Arial', 11, 'bold'), bg = '#EBFBFF',\
                fg = 'blue', activebackground = '#EBFBFF', activeforeground = 'yellow', borderwidth = 0, command = lambda: self.goBack(misc))
        goBackButton.place(x = 10, y = 10)

        # 연산 결과를 보여주는 레이블
        self.__resultLabel: Label = Label(self, text = '', width = 24, font = ('Arial', 20, 'bold'),\
                bg = 'white', anchor = 'w')
        self.__resultLabel.place(x = 92, y = 153)

        # 연산 결과
        self.__result: str = ''
        self.__isCalculated: bool = False # 연산을 수행했는지 여부를 나타냄.

        # 각종 버튼 배치
        # 1. 숫자 버튼
        button0: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '0')
        button00: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '00')
        button1: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '1')
        button2: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '2')
        button3: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '3')
        button4: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '4')
        button5: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '5')
        button6: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '6')
        button7: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '7')
        button8: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '8')
        button9: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '9')
        dotButton: CalculatorButton = CalculatorButton(self, 76, 76, '#A6FFDD', '.')
        equalButton: CalculatorButton = CalculatorButton(self, 76, 76, '#B0D5FF', '=')

        button1.place(x = 82, y = 210); button2.place(x = 172, y = 210); button3.place(x = 262, y = 210)
        button4.place(x = 82, y = 300); button5.place(x = 172, y = 300); button6.place(x = 262, y = 300)
        button7.place(x = 82, y = 390); button8.place(x = 172, y = 390); button9.place(x = 262, y = 390)
        button0.place(x = 82, y = 480); button00.place(x = 172, y = 480); dotButton.place(x = 262, y = 480)
        equalButton.place(x = 442, y = 480)

        # 2. 연산자 버튼
        addButton: CalculatorButton = CalculatorButton(self, 76, 76, '#FFF1BE', '+')
        subtractButton: CalculatorButton = CalculatorButton(self, 76, 76, '#FFF1BE', '-')
        multiplyButton: CalculatorButton = CalculatorButton(self, 76, 76, '#FFF1BE', 'x')
        divideButton: CalculatorButton = CalculatorButton(self, 76, 76, '#FFF1BE', '÷')
        leftParenthesisButton: CalculatorButton = CalculatorButton(self, 76, 76, '#FFF1BD', '(')
        rightParenthesisButton: CalculatorButton = CalculatorButton(self, 76, 76, '#FFF1BE', ')')

        addButton.place(x = 352, y = 210); subtractButton.place(x = 442, y = 210)
        multiplyButton.place(x = 352, y = 300); divideButton.place(x = 442, y = 300)
        leftParenthesisButton.place(x = 352, y = 390); rightParenthesisButton.place(x = 442, y = 390)

        # 3. 삭제 버튼
        clearButton: CalculatorButton = CalculatorButton(self, 76, 76, '#FFDADA', 'C')
        clearButton.place(x = 352, y = 480)

    def inputElements(self, element: str) -> None: # 숫자, 연산자 등 각종 요소를 입력하는 메소드
        if self.__isCalculated:
            self.resetElements()

        self.__result += element
        resultText: str = self.__result
        if len(self.__result) > 25:
            tempText: str = resultText
            resultText = '...'
            resultText += tempText[-25:]
        self.__resultLabel.config(text = resultText)

    def calculate(self) -> None: # 계산을 수행하는 메소드
        tempText: str = self.__resultLabel.cget('text')
        resultText = ''
        for ch in tempText:
            if ch == 'x':
                resultText += '*'
            elif ch == '÷':
                resultText += '/'
            else:
                resultText += ch

        try:
            self.__resultLabel.config(text = str(eval(resultText)))
        except SyntaxError:
            self.__resultLabel.config(text = '잘못된 수식입니다.')
        except ZeroDivisionError:
            self.__resultLabel.config(text = '0으로 나눌 수 없습니다.')

        self.__isCalculated = True

    def resetElements(self) -> None: # 각종 요소들을 초기화하는 메소드
        self.__result = ''
        self.__resultLabel.config(text = self.__result)
        self.__isCalculated = False

    def goBack(self, misc: Misc) -> None: # 뒤로가기 메소드
        misc.showTimeTable()
        self.destroy()

if DEBUG:
    window: Tk = Tk()
    window.geometry('600x600')
    window.title('Calculator Frame')

    calculatorFrame: CalculatorFrame = CalculatorFrame(window)
    calculatorFrame.place(x = 0, y = 0)

    window.mainloop()
