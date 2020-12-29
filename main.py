import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Screen):
    def next_slide_button(self):
        self.ids.slide.load_next()


    def previous_slide_button(self):
        self.ids.slide.load_previous()


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class MyMessengerApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_screen'))
        return sm


if __name__ == '__main__':
    app = MyMessengerApp()
    app.run()
