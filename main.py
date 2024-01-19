import psycopg2
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        lable = Label(text='Программа не работает\nВыключи её')

        return lable


if __name__ == "__main__":
    MyApp.run