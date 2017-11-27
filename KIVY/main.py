from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from random import randint


class Hangman(App):

    def build(self):
        self.guessList = []
        self.labelTextList = []
        self.dict = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5':'E',
                     '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J',
                     '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O',
                     '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20':'T',
                     '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y',
                     '26':'Z', '0': ' '
                     }

        self.hangList = ['COMPUTING', 'WARWICK', 'GOOGLE', 'ALGORITHM']
        randWord = randint(0, len(self.hangList) - 1)

        self.hangWord = self.hangList[randWord]

        print(self.hangWord)

        for letter in self.hangWord:
            self.labelTextList.append('_ ')

        labelText = ''.join(self.labelTextList)

        b = BoxLayout(orientation='vertical')
        g = GridLayout(cols=9)
        self.l = Label(text = labelText, font_size=75)

        for more in range(0, 27):
            if more > 0:
                self.btn = Button(text=self.dict[str(more)], size=(35, 35), font_size=25)
                self.btn.bind(on_press=lambda instance, text=more: self.update(text))
                g.add_widget(self.btn)
            else:
                self.btn = Button(text='space', size=(35, 35), font_size=25)
                self.btn.bind(on_press=lambda instance, text=more: self.update(text))
                g.add_widget(self.btn)

        b.add_widget(self.l)
        b.add_widget(g)

        return b


    def update(self, text):

        newGuess = self.dict[str(text)]
        self.guessList.append(newGuess)
        print(self.guessList)
        print(self.btn)
        wordGuess = ''.join(self.guessList)
        print(wordGuess)
        self.l.text = wordGuess

        if newGuess in self.hangWord:
            if self.hangWord.count(newGuess) == 1:
                nope = "*"
               # self.btn[newGuess].text = nope
                print('change red all occurances')

            else:
                print('change orange more than one')

        if wordGuess == self.hangWord:
            self.l.text = "YOU WIN!"


if __name__ == "__main__":
    Hangman().run()
