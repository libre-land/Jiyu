import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Screen):
    def next_slide_button_1(self):
        self.ids.slide.load_next()
        self.ids.progress_bar_1.value = 100


    def next_slide_button_2(self):
        self.ids.slide.load_next()
        self.ids.progress_bar_2.value = 100


    def previous_slide_button_1(self):
        self.ids.slide.load_previous()
        self.ids.progress_bar_1.value = 0


    def previous_slide_button_2(self):
        self.ids.slide.load_previous()
        self.ids.progress_bar_2.value = 0


class MyMessengerApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_screen'))
        return sm


if __name__ == '__main__':
    app = MyMessengerApp()
    app.run()
