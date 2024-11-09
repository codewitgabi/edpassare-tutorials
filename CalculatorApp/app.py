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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.input_field = self.ids.get("input_field")
        self.operators = {"+": "+", "-": "-", "x": "*", "÷": "/", "%": "%"}

    def on_click(self, key):
        self.input_field.text += key.text

    def on_operator(self, key):
        self.input_field.text += f"{self.operators.get(key.text, '')}"

    def on_delete(self):
        """
        * Event handler for when the user clicks on the `DEL` button.
        * Should delete numbers one after the other.
        """

        self.input_field.text = self.input_field.text[:-1]
        # self.equation = self.

    def on_clear(self):
        """
        * Event handler for when the user clicks on the `AC` button.
        * Should clear the input field.
        """

        self.input_field.text = ""

    def on_equal_to(self):
        """
        * Event handler for when the user clicks on the equal to button
        """

        self.input_field.text = str(eval(self.input_field.text))


class CalculatorApp(App):
    def build(self):
        Window.clear_color = 36 / 255, 38 / 255, 42 / 255, 1

        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
