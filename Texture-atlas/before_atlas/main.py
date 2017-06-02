#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import OptionProperty

from src.components import CustomButton, CustomCheckBox


class Theming(BoxLayout):
    pass


class MainApp(App):

    def build(self):
        self.title = 'Theming'
        return Theming()


if __name__ == "__main__":
    app = MainApp()
    app.run()
