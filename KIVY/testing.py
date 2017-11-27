from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from random import randint


class Wefidget(App):

    def build(self):

        box1 = BoxLayout(orientation='vertical')

        title = Label(text = "Welcome to Wefidget", font_size = 25)

        box2 = BoxLayout(orientation='horizontal')
        g1 = GridLayout(cols = 1)
        g2 = GridLayout(cols=1)
        l1 = Label(text = 'Stress1', font_size=75)
        l2 = Label(text = 'Stress2', font_size=75)
        l3 = Label(text = 'Stress3', font_size=75)
        b1 = Button(text = 'Send Alert', font_size = 25)
        b2 = Button(text = 'Update', font_size = 25)
        g2.add_widget(l1)
        g2.add_widget(l2)
        g2.add_widget(l3)

        g1.add_widget(b1)
        g1.add_widget(b2)

        box1.add_widget(title)
        box1.add_widget(box2)

        box2.add_widget(g1)
        box2.add_widget(g2)

        return box1


if __name__ == "__main__":
    Wefidget().run()
