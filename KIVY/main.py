from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from random import randint


class Hangman(App):

    def build(self):
        self.guessList = []
        self.blanks = []
        self.startblanks = []
        self.dict = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5':'E',
                     '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J',
                     '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O',
                     '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20':'T',
                     '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y',
                     '26':'Z', '0': ' ', '27':'RESET'
                     }

        self.hangList = ['COMPUTING', 'WARWICK', 'GOOGLE', 'ALGORITHM']
        randWord = randint(0, len(self.hangList) - 1)
        self.hangword = self.hangList[randWord]
        self.answerList = list(self.hangword)
        print("Printing hangwordlist", self.answerList)
        numofguesses = len(self.hangword) + len(self.hangword) // 2
        for letter in range(numofguesses):
            self.guessList.append("_")
        for letter in self.hangword:
            self.blanks.append('_')
        starttext = " ".join(self.guessList)
        blankstext = " ".join(self.blanks)
        b = BoxLayout(orientation='vertical')
        g = GridLayout(cols=9)
        self.lword = Label(text = blankstext, font_size = 75)
        self.lguess = Label(text = starttext, font_size = 50)
        for more in range(0, 28):
            if more > 0 and more < 27:
                self.btn = Button(text=self.dict[str(more)], size=(135, 35), font_size=25)
                self.btn.bind(on_press=lambda instance, text=more: self.update(text))
                g.add_widget(self.btn)
            elif more == 0:
                self.btn = Button(text='SPACE', size=(150, 150), font_size=25)
                self.btn.bind(on_press=lambda instance, text=more: self.update(text))
                g.add_widget(self.btn)
            else:
                self.btn = Button(text='RESET', size=(150, 150), font_size=25)
                self.btn.bind(on_press=lambda instance, text=more: self.update(text))
                g.add_widget(self.btn)
        b.add_widget(self.lword)
        b.add_widget(self.lguess)
        b.add_widget(g)
        return b

    def update(self, text):
        newguess = self.dict[str(text)]
        #if newguess == "reset":
        #    print("reset")
        #if newguess in self.guessList:
        #        print("already in guess")
        #else:
        #        print("not in guess")
        if newguess not in self.answerList and newguess not in self.guessList:
            guessstring = "".join(self.guessList)
            print("><><><>><><><><", guessstring)
            guessstring = guessstring.replace("_", newguess, 1)
            print("''/''/'/'/'/'/'/'", guessstring)
            self.guessList = list(guessstring)
            print(self.guessList)
        print("Current guess list is", self.guessList)
    #   print("Last button pressed ws", self.btn)
        wordguess = ' '.join(self.guessList)
        print("wordguess is now", wordguess)
        stringblanks = " ".join(self.blanks)
        self.lword.text = stringblanks
        self.lguess.text = wordguess
        for index, item in enumerate(self.answerList):
            if item == newguess:
                self.blanks[index] = item
                stringblanks = " ".join(self.blanks)
                self.lword.text = stringblanks
                print("self.blanks : ", self.blanks, "self.answerlist :", self.answerList)
                self.lguess.text = wordguess
        if newguess in self.answerList and newguess not in self.guessList:
                guessstring = "".join(self.guessList)
                print("><><><>><><><><", guessstring)
                guessstring = guessstring.replace("_", newguess, 1)
                print("''/''/'/'/'/'/'/'", guessstring)
                self.guessList = list(guessstring)
                print(self.guessList)
        if self.blanks == self.answerList:
            self.lword.text = "You Won!"
            self.lguess.text = "#  S U P E R  S T A R  #"
        if "_" not in self.guessList:
            self.lword.text = "NO WAY"
            self.lguess.text = "# YOU LOST #"


if __name__ == "__main__":
    Hangman().run()
