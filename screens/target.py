from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.core.window import Window

from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.progressbar import MDProgressBar

from utils.api import target_api


# White background
Window.clearcolor = (1, 1, 1, 1)


class TargetScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ================= MAIN LAYOUT =================

        main_layout = BoxLayout(
            orientation="vertical"
        )

        # ================= TOP BAR =================
        top_bar = MDTopAppBar(
            title="Target",
            left_action_items=[
                ["arrow-left", lambda x: self.go_back()]
            ],
            elevation=3,
        )
        top_bar.md_bg_color = (0.2, 0.7, 0.3, 1)

        # ================= FETCH DATA =================

        data = target_api(1)

        achieved = data["achieved"]

        # ================= CENTER CONTAINER =================

        center_layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(20)
        )

        # ================= CARD =================

        card = MDCard(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(20),
            radius=[25],
            elevation=4,
            size_hint=(0.95, None),
            height=dp(250),
            pos_hint={"center_x": 0.5},
            md_bg_color=(0.96, 0.97, 0.99, 1)
        )

        # ================= TITLE =================

        title = MDLabel(
            text="Monthly Target",
            halign="center",
            bold=True,
            font_style="H5",
            theme_text_color="Custom",
            text_color=(0.2, 0.2, 0.2, 1)
        )

        # ================= PERCENTAGE =================

        percent_label = MDLabel(
            text=f"{achieved}%",
            halign="center",
            bold=True,
            font_style="H3",
            theme_text_color="Custom",
            text_color=(0.2, 0.5, 0.9, 1)
        )

        # ================= STATUS =================

        status = MDLabel(
            text="Target Achieved",
            halign="center",
            font_style="Subtitle1",
            theme_text_color="Secondary"
        )

        # ================= PROGRESS BAR =================

        progress = MDProgressBar(
            value=achieved,
            max=100
        )

        progress.color = (0.4, 0.7, 1, 1)

        # ================= ADD TO CARD =================

        card.add_widget(title)
        card.add_widget(percent_label)
        card.add_widget(status)
        card.add_widget(progress)

        # ================= ADD TO MAIN =================

        center_layout.add_widget(card)

        main_layout.add_widget(top_bar)
        main_layout.add_widget(center_layout)

        self.add_widget(main_layout)

    # ================= BACK =================

    def go_back(self):
        self.manager.current = "dashboard"

# from kivy.uix.screenmanager import Screen
# from kivy.uix.boxlayout import BoxLayout

# from kivy.uix.progressbar import ProgressBar

# from kivymd.uix.label import MDLabel
# from kivymd.uix.toolbar import MDTopAppBar
# from utils.api import target_api


# class TargetScreen(Screen):

#     def __init__(self, **kwargs):

#         super().__init__(**kwargs)

#         layout = BoxLayout(
#             orientation="vertical",
#             padding=20,
#             spacing=20
#         )

#         top_bar = MDTopAppBar(
#             title="Targets",
#             left_action_items=[["arrow-left", lambda x: self.go_back()]]
#         )

#         data = target_api(1)

#         achieved = data["achieved"]

#         label = MDLabel(
#             text=f"Target Achieved: {achieved}%"
#         )

#         progress = ProgressBar(
#             max=100,
#             value=achieved
#         )

#         layout.add_widget(label)
#         layout.add_widget(progress)
#         layout.add_widget(top_bar)

#         self.add_widget(layout)

#     def go_back(self):
#         self.manager.current = "dashboard"

# # from kivy.uix.screenmanager import Screen
# # from kivy.uix.boxlayout import BoxLayout

# # from kivymd.uix.button import MDIconButton
# # from kivymd.uix.toolbar import MDTopAppBar
# # from kivymd.uix.label import MDLabel


# # class TargetScreen(Screen):

# #     def __init__(self, **kwargs):
# #         super().__init__(**kwargs)

# #         layout = BoxLayout(orientation="vertical")

# #         # TOP BAR WITH BACK BUTTON
# #         top_bar = MDTopAppBar(
# #             title="Targets",
# #             left_action_items=[["arrow-left", lambda x: self.go_back()]]
# #         )

# #         content = MDLabel(
# #             text="Your Targets Here",
# #             halign="center"
# #         )

# #         layout.add_widget(top_bar)
# #         layout.add_widget(content)

# #         self.add_widget(layout)

# #     def go_back(self):
# #         self.manager.current = "dashboard"