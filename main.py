from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.chat import ChatScreen
from screens.target import TargetScreen

class MyApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Blue"

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(ChatScreen(name="chat"))
        sm.add_widget(TargetScreen(name="target"))

        return sm


MyApp().run()