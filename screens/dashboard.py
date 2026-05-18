from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import (
    MDIconButton,
    MDFloatingActionButton
)
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.progressbar import MDProgressBar

from utils.api import target_api

import webbrowser


class DashboardScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.username_label = None

        # ================= ROOT =================

        root = BoxLayout(
            orientation="vertical"
        )

        # ================= TOP BAR =================
        welcome = MDCard(
            orientation="horizontal",
            padding=dp(12),
            spacing=dp(12),
            radius=[18],
            elevation=3,
            size_hint=(1, None),
            height=dp(90),   # smaller height
            md_bg_color=(0.15, 0.55, 0.95, 1)
        )

        logo = Image(
            source="assets/logo.png",
            size_hint=(None, None),
            size=(dp(55), dp(55))   # smaller logo
        )

        top_bar = MDTopAppBar(
            title="WELCOME {Username} ",
            # left_action_items=[
            #     ["menu", lambda x: None]
            # ],
            right_action_items=[
                ["logout", lambda x: self.change_screen("login")]
            ],
            md_bg_color=(0.15, 0.55, 0.95, 1),
        )

        root.add_widget(logo)
        root.add_widget(top_bar)
       

        self.username_label = top_bar

        # ================= SCROLL =================

        scroll = ScrollView()

        container = BoxLayout(
            orientation="vertical",
            spacing=dp(20),
            padding=dp(15),
            size_hint_y=None
        )

        container.bind(
            minimum_height=container.setter("height")
        )

        # ================= GRID CARDS =================

        grid = GridLayout(
            cols=2,
            spacing=dp(15),
            size_hint_y=None
        )

        grid.bind(
            minimum_height=grid.setter("height")
        )

        # ================= CARD FUNCTION =================

        def make_card(title, icon, color, callback):

            card = MDCard(
                orientation="vertical",
                padding=dp(18),
                spacing=dp(12),
                radius=[22],
                ripple_behavior=True,
                md_bg_color=color,
                size_hint=(1, None),
                height=dp(100),
                elevation=7
            )

            icon_btn = MDIconButton(
                icon=icon,
                icon_size="42sp",
                pos_hint={"center_x": 0.5},
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1)
            )

            label = MDLabel(
                text=title,
                halign="center",
                bold=True,
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1)
            )

            card.add_widget(icon_btn)
            card.add_widget(label)

            card.bind(
                on_release=lambda x: callback()
            )

            return card

        # ================= TARGET SECTION =================

        data = target_api(1)

        achieved = data["achieved"]

        target_card = MDCard(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(20),
            radius=[25],
            elevation=5,
            size_hint=(1, None),
            height=dp(250),
            md_bg_color=(0.96, 0.97, 0.99, 1)
        )

        target_title = MDLabel(
            text="Monthly Target",
            halign="center",
            font_style="H5",
            bold=True
        )

        percent_label = MDLabel(
            text=f"{achieved}%",
            halign="center",
            font_style="H2",
            bold=True,
            theme_text_color="Custom",
            text_color=(0.1, 0.5, 1, 1)
        )

        status = MDLabel(
            text="Target Achieved",
            halign="center",
            theme_text_color="Secondary"
        )

        progress = MDProgressBar(
            value=achieved,
            max=100
        )

        progress.color = (0.1, 0.5, 1, 1)

        target_card.add_widget(target_title)
        target_card.add_widget(percent_label)
        target_card.add_widget(status)
        target_card.add_widget(progress)

        container.add_widget(target_card)

        # ================= SCROLL ADD =================

        scroll.add_widget(container)

        root.add_widget(scroll)

        # ================= FLOAT CHAT BUTTON =================

        fab = MDFloatingActionButton(
            icon="message-text",
            md_bg_color=(0.1, 0.45, 0.85, 1),
            pos_hint={
                "right": 0.95,
                "y": 0.08,
            }
        )
        
        fab.bind(
            on_release=lambda x: self.change_screen("chat")
        )

        root.add_widget(fab)

        self.add_widget(root)

    # ================= NAVIGATION =================

    def change_screen(self, screen):

        self.manager.current = screen

    # ================= ACTIONS =================
    def set_user(self, username):

        self.username_label.title = f"Welcome, {username}"

    def download_pdf(self, *args):

        webbrowser.open(
            "http://192.168.100.29:5000/download-training"
        )

    def open_playstore(self, *args):

        webbrowser.open(
            "https://play.google.com/store/apps/details?id=com.integra.fi.ubi"
        )

# from kivy.uix.screenmanager import Screen
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout

# from kivymd.uix.card import MDCard
# from kivymd.uix.label import MDLabel
# from kivymd.uix.button import MDIconButton, MDFloatingActionButton
# from kivymd.uix.toolbar import MDTopAppBar

# import webbrowser


# class DashboardScreen(Screen):

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         root = BoxLayout(orientation="vertical")

#         # ===== TOP APP BAR =====
#         appbar = MDTopAppBar(
#             title="Dashboard",
#             elevation=4,
#             left_action_items=[["menu", lambda x: None]],
#             right_action_items=[["logout", lambda x: self.change_screen("login")]],
#         )

#         root.add_widget(appbar)

#         # ===== MAIN CONTENT AREA =====
#         content = BoxLayout(padding=20)

#         grid = GridLayout(
#             cols=2,
#             spacing=15,
#             size_hint_y=None
#         )
#         grid.bind(minimum_height=grid.setter("height"))

#         # ===== CARD BUILDER =====
#         def make_card(title, icon, color, callback):

#             card = MDCard(
#                 orientation="vertical",
#                 padding=15,
#                 spacing=10,
#                 radius=[18, 18, 18, 18],
#                 ripple_behavior=True,
#                 md_bg_color=color,
#                 size_hint=(1, None),
#                 height=150,
#                 elevation=8
#             )

#             icon_btn = MDIconButton(
#                 icon=icon,
#                 pos_hint={"center_x": 0.5},
#                 theme_text_color="Custom",
#                 text_color=(1, 1, 1, 1)
#             )

#             label = MDLabel(
#                 text=title,
#                 halign="center",
#                 theme_text_color="Custom",
#                 text_color=(1, 1, 1, 1),
#                 bold=True
#             )

#             card.add_widget(icon_btn)
#             card.add_widget(label)

#             card.bind(on_release=lambda x: callback())

#             return card

#         # ===== ACTIONS =====
#         cards = [
#             make_card("Chat", "chat", (0.2, 0.6, 1, 1),
#                       lambda: self.change_screen("chat")),

#             make_card("Targets", "target", (0.2, 0.7, 0.3, 1),
#                       lambda: self.change_screen("target")),
#         ]

#         for c in cards:
#             grid.add_widget(c)

#         content.add_widget(grid)
#         root.add_widget(content)

#         self.add_widget(root)

#     # ===== NAVIGATION =====
#     def change_screen(self, screen):
#         self.manager.current = screen

#     # ===== ACTIONS =====
#     def download_pdf(self, *args):
#         webbrowser.open("http://192.168.100.29:5000/download-training")

#     def open_playstore(self, *args):
#         webbrowser.open(
#             "https://play.google.com/store/apps/details?id=com.integra.fi.ubi"
#         )
