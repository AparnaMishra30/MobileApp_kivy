from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.metrics import dp

from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

from utils.api import login_api


class LoginScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        main_layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(20)
        )

        # Center Card
        card = MDCard(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(20),
            size_hint=(0.9, None),
            height=dp(500),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[20, 20, 20, 20],
            elevation=4
        )

        # Title
        self.title = MDLabel(
            text="BC service App",
            halign="center",
            font_style="H4",
            bold=True,
            size_hint_y=None,
            height=dp(50)
        )

        # Logo
        self.logo = Image(
            source="assets/logo.png",
            size_hint=(1, None),
            height=dp(120),
            allow_stretch=True
        )

        # Username
        self.user = MDTextField(
            hint_text="Login ID",
            icon_right="account",
            size_hint_x=1
        )

        # Password
        self.password = MDTextField(
            hint_text="Password",
            password=True,
            icon_right="lock"
        )

        # Login Button
        self.btn = MDRaisedButton(
            text="LOGIN",
            pos_hint={"center_x": 0.5},
            size_hint=(0.6, None),
            height=dp(45)
        )

        self.btn.bind(on_press=self.do_login)

        # Status Label
        self.status = MDLabel(
            text="",
            halign="center",
            theme_text_color="Error"
        )

        # Add widgets to card
        card.add_widget(self.title)
        card.add_widget(self.logo)
        card.add_widget(self.user)
        card.add_widget(self.password)
        card.add_widget(self.btn)
        card.add_widget(self.status)

        # Add card to screen
        main_layout.add_widget(card)

        self.add_widget(main_layout)

    def do_login(self, instance):
        username = self.user.text
        dashboard = self.manager.get_screen("dashboard")
        dashboard.set_user(username)
        
        self.user.text = ""
        self.password.text = ""

        self.manager.current = "dashboard"


        # response = login_api(
        #     self.user.text,
        #     self.password.text
        # )

        # self.user.text = ""
        # self.password.text = ""

        # if response["status"] == "success":

        #     self.manager.current = "dashboard"

        # else:

        #     self.status.text = "Invalid Login"

