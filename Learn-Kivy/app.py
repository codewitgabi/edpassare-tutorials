import kivy

kivy.require("2.3.0")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (300, 500)  # Set window size to 300x500 pixels


class PageWidget(Widget):
    pass


class KivyLearnApp(App):
    def build(self):
        return PageWidget()


if __name__ == "__main__":
    KivyLearnApp().run()
