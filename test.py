from windoweffect import WindowBlur
WindowBlur(5)

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.window import Window
from win32api import GetSystemMetrics

Window.left = 0
Window.top = 0
Window.size = (GetSystemMetrics(0),GetSystemMetrics(1) )
Window.borderless = True



class Test(Widget):
    pass


class Build(App):
    def build(self):
        return Test()


Build().run()