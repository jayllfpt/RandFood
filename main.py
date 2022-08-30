from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from random import randint

def getfood():
    file = open("listoffood.data", "r")
    lst = []
    for x in file:
        lst.append(x)
    return lst

class BoxLayoutEx(BoxLayout):
    food = getfood()
    NoFood = len(food) - 1
    lblText = StringProperty("Mom's food is the best\n")
    def on_button_click(self):
        self.lblText = self.food[randint(0, self.NoFood)]

class KivyApp(App):
    pass

KivyApp().run()