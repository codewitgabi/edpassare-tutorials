import kivy

kivy.require("2.3.0")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (300, 500)  # Set window size to 300x500 pixels


class EventWidget(Widget):
    def on_click_button(self):
        print("I am clicking on the button")

    def print_user_input(self):
        user_input = self.ids.get("user_input")

        print(user_input.text)


class WidgetApp(App):
    def build(self):
        # Window.clear_color = (1, 1, 1, 1)

        return EventWidget()


if __name__ == "__main__":
    WidgetApp().run()
