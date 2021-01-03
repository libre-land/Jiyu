from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager
from kivy.core.window import Window


Window.size = (414, 736)


class StartScreen(Screen):
    def next_screen_buttton(self):
        self.manager.current = 'login_screen'


class LoginScreen(Screen):
    def next_slide_button_1(self):
        self.ids.slide.load_next()
        self.ids.progress_bar_1.value = 100

        self.theme_cls = ThemeManager()
        self.ids.icon_1.text_color = self.theme_cls.primary_color


    def next_slide_button_2(self):
        self.ids.slide.load_next()
        self.ids.progress_bar_2.value = 100

        self.theme_cls = ThemeManager()
        self.ids.icon_2.text_color = self.theme_cls.primary_color


    def join_button(self):
        self.theme_cls = ThemeManager()
        self.ids.icon_3.text_color = self.theme_cls.primary_color

        self.manager.current = 'menu_screen'


    def previous_slide_button_1(self):
        self.ids.slide.load_previous()
        self.ids.progress_bar_1.value = 0
        self.ids.icon_1.text_color = 0, 0, 0, 1


    def previous_slide_button_2(self):
        self.ids.slide.load_previous()
        self.ids.progress_bar_1.value = 0
        self.ids.icon_2.text_color = 0, 0, 0, 1


    def previous_slide_button_3(self):
        self.ids.slide.load_previous()
        self.ids.progress_bar_2.value = 0
        self.ids.icon_3.text_color = 0, 0, 0, 1


class MenuScreen(Screen):
    pass


class MyMessengerApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start_screen'))
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(MenuScreen(name='menu_screen'))

        return sm


if __name__ == '__main__':
    app = MyMessengerApp()
    app.run()
