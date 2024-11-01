import kivy

kivy.require("2.3.0")

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase, DEFAULT_FONT

# Register the Google Font as the default font for the app
LabelBase.register(DEFAULT_FONT, "./fonts/Poppins-Medium.ttf")

Window.size = (300, 500)  # Set window size to 300x500 pixels


class CalculatorWidget(Widget):
    pass


class CalculatorApp(App):
    def build(self):
        Window.clear_color = 36 / 255, 38 / 255, 42 / 255, 1

        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
