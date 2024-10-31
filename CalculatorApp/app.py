import kivy

kivy.require("2.3.0")

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (300, 500)  # Set window size to 300x500 pixels


class CalculatorWidget(Widget):
    pass


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
