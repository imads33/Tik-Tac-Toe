import sys
from PyQt5 import  QtWidgets,uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("TicTacToe.ui",self)

        self.Clicked = 0
        self.Xscore= 0
        self.Oscore= 0

        self.button1 = self.findChild(QPushButton, "Button1")
        self.button2 = self.findChild(QPushButton, "Button2")
        self.button3 = self.findChild(QPushButton, "Button_3")
        self.button4 = self.findChild(QPushButton, "Button_4")
        self.button5 = self.findChild(QPushButton, "Button_5")
        self.button6 = self.findChild(QPushButton, 'Button_6')
        self.button7 = self.findChild(QPushButton, 'Button_7')
        self.button8 = self.findChild(QPushButton, 'Button_8')
        self.button9 = self.findChild(QPushButton, 'Button_9')
        self.reset = self.findChild(QPushButton, "Reset")
        self.newGame = self.findChild(QPushButton, "NewGame")

        self.scoreX = self.findChild(QLabel,"ScoreX")
        self.scoreO = self.findChild(QLabel, "ScoreO")
        self.label = self.findChild(QLabel, "label_2")

# Buttons list
        self.buttons = [
            self.button1, self.button2, self.button3,
            self.button4, self.button5, self.button6,
            self.button7, self.button8, self.button9
        ]

# Call Function Each Time Button is
        self.button1.clicked.connect(lambda: self.check(self.button1))
        self.button2.clicked.connect(lambda: self.check(self.button2))
        self.button3.clicked.connect(lambda: self.check(self.button3))
        self.button4.clicked.connect(lambda :self.check(self.button4))
        self.button5.clicked.connect(lambda :self.check(self.button5))
        self.button6.clicked.connect(lambda :self.check(self.button6))
        self.button7.clicked.connect(lambda :self.check(self.button7))
        self.button8.clicked.connect(lambda :self.check(self.button8))
        self.button9.clicked.connect(lambda :self.check(self.button9))

        self.reset.clicked.connect(lambda : self.ResetFunc(self.buttons))
        self.newGame.clicked.connect(lambda : self.Newgame(self.buttons))


# Check Winning conditions
    def Checkwin(self):
        # Direction ( -------------> ) OR ( <------------ )
        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.Winner(self.button1,self.button2,self.button3)

        elif self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.Winner(self.button4,self.button5,self.button6)

        elif self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.Winner(self.button7,self.button8,self.button9)

    #     Direction Down-up or Up-down

        elif self.button1.text() != "" and self.button4.text() == self.button1.text() and self.button7.text() == self.button1.text():
            self.Winner(self.button1, self.button4, self.button7)

        elif self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button8.text() == self.button2.text():
            self.Winner(self.button2, self.button5, self.button8)

        elif self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button9.text() == self.button3.text():
            self.Winner(self.button3, self.button6, self.button9)

    #  Direction cross
        elif self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.Winner(self.button1, self.button5, self.button9)

        elif self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button7.text() == self.button3.text():
            self.Winner(self.button3, self.button5, self.button7)

        if self.button1.text() !="" and \
                self.button2.text() !="" and self.button3.text() !="" and \
                self.button4.text() !="" and self.button5.text() !="" and self.button6.text() !="" and \
                self.button7.text() !="" and self.button8.text() !="" and self.button9.text() !="":
            self.label.setText('Match Tie!')


# Show the Winner
    def Winner(self,buttonA,buttonB,buttonC):
        # Setting color for blocks
        buttonA.setStyleSheet('QPushButton {background-color: rgb(60, 255, 57);}')
        buttonB.setStyleSheet('QPushButton {background-color: rgb(60, 255, 57);}')
        buttonC.setStyleSheet('QPushButton {background-color: rgb(60, 255, 57);}')

        # wish for winner
        self.label.setText(f"Player {buttonA.text()} Wins !")
        if buttonA.text() == 'X':
            self.Xscore += 1
            self.scoreX.setText(str(self.Xscore))
        elif buttonA.text() == 'O':
            self.Oscore += 1
            self.scoreO.setText(str(self.Oscore))

        self.disableBoard(self.buttons)


    def disableBoard(self,buttons):
        for b in buttons:
            b.setEnabled(False)


# Start New Game
    def Newgame(self,buttons):
        self.ResetFunc(buttons)
        self.scoreX.setText("")
        self.scoreO.setText("")
        self.Xscore=0
        self.Oscore=0

# Reset Game
    def ResetFunc(self,buttons):

        for b in buttons:
            b.setText("")
            b.setStyleSheet('QPushButton {color: rgb(0,0,0);background-color: rgb(122, 122, 122);}QPushButton:hover {background-color: rgb(217, 252, 255);}')
            b.setEnabled(True)
        self.label.setText("X Goes First")
        self.Clicked=0


# Check which button is clicked
    def check (self,button):
        if self.Clicked % 2==0:
            fill='X'
            self.label.setText("O's Turn")
        else:
            fill='O'
            self.label.setText("X's Turn")

        button.setText(fill)
        button.setEnabled(False)
        self.Clicked += 1
        self.Checkwin()


def App():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

App()
