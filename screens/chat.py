from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

from utils.api import chat_api
import webbrowser


class ChatScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(
            orientation="vertical"
        )

        # ================= TOP BAR =================
        top_bar = MDTopAppBar(
            title="PDF Chat Assistant",
            left_action_items=[
                ["arrow-left", lambda x: self.go_back()]
            ],
            elevation=3
        )

        # ================= CHAT AREA =================
        self.scroll = ScrollView()

        self.chat_layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint_y=None,
            padding=10
        )

        self.chat_layout.bind(
            minimum_height=self.chat_layout.setter("height")
        )

        self.scroll.add_widget(self.chat_layout)

        # ================= INPUT AREA =================
        bottom_layout = BoxLayout(
            size_hint_y=None,
            height=dp(70),
            spacing=10,
            padding=10
        )

        self.input = MDTextField(
            hint_text="Type your message...",
            multiline=False
        )

        send_btn = MDRaisedButton(
            text="Send",
            size_hint_x=None,
            width=dp(100)
        )

        send_btn.bind(on_press=self.send_message)

        bottom_layout.add_widget(self.input)
        bottom_layout.add_widget(send_btn)

        # ================= DEFAULT MESSAGE =================
        self.add_message(
            "Bot",
            "Hello! Ask something from PDF..."
        )

        # ================= ADD WIDGETS =================
        main_layout.add_widget(top_bar)
        main_layout.add_widget(self.scroll)
        main_layout.add_widget(bottom_layout)

        self.add_widget(main_layout)

    # =====================================================
    # GO BACK
    # =====================================================

    def go_back(self):
        self.manager.current = "dashboard"

    # =====================================================
    # ADD CHAT MESSAGE
    # =====================================================

    def add_message(self, sender, message):

        # Message Card
        card = MDCard(
            orientation="vertical",
            padding=15,
            spacing=10,
            size_hint=(0.85, None),
            radius=[15],
            elevation=2
        )

        card.height = dp(80)

        # Different colors for user/bot

        if sender == "You":
            card.md_bg_color = (0.78, 0.89, 1, 1)
            pos_x = 0.15
            text_color = (0, 0, 0, 1)
        else:
            # Light Grey
            card.md_bg_color = (0.92, 0.92, 0.92, 1)
            pos_x = 0
            text_color = (0, 0, 0, 1)

        card.pos_hint = {"x": pos_x}

        label = MDLabel(
        text=f"[b]{sender}:[/b] {message}",
        markup=True,
        theme_text_color="Custom",
        text_color=text_color,
        adaptive_height=True
    )

        card.add_widget(label)

        self.chat_layout.add_widget(card)

    # =====================================================
    # SEND MESSAGE
    # =====================================================

    def send_message(self, instance):

        user_text = self.input.text.strip()

        if not user_text:
            return

        # Show user message
        self.add_message("You", user_text)

        # Clear textbox
        self.input.text = ""

        # ================= CUSTOM COMMANDS =================

        if user_text.lower() == "training pdf" or user_text.lower() == "pdf":

            webbrowser.open(
                "http://192.168.100.29:5000/download-training"
            )

            response = "Training PDF downloaded successfully."

        elif user_text.lower() in "redirect" or user_text.lower() in "play store":

            webbrowser.open(
                "https://play.google.com/store"
            )

            response = "Redirected to Play Store."

        else:

            api_response = chat_api(user_text)

            response = api_response["reply"]

        # Show bot response
        self.add_message("Bot", response)

        # Auto scroll bottom
        self.scroll.scroll_y = 0
        
# from kivy.uix.screenmanager import Screen
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.uix.toolbar import MDTopAppBar
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.label import MDLabel

# from utils.api import chat_api
# import webbrowser

# class ChatScreen(Screen):

#     def __init__(self, **kwargs):

#         super().__init__(**kwargs)

#         layout = BoxLayout(
#             orientation="vertical",
#             padding=20,
#             spacing=20
#         )
#         top_bar = MDTopAppBar(
#             left_action_items=[["arrow-left", lambda x: self.go_back()]]
#         )

#         self.chat_output = MDLabel(
#             text="Ask something from PDF...",
#             halign="left"
#         )

#         self.input = MDTextField(
#             hint_text="Type question"
#         )

#         send_btn = MDRaisedButton(
#             text="SEND"
#         )

#         send_btn.bind(on_press=self.send_message)

#         layout.add_widget(self.chat_output)
#         layout.add_widget(self.input)
#         layout.add_widget(send_btn)
#         layout.add_widget(top_bar)

#         self.add_widget(layout)

#     def go_back(self):
#         self.manager.current = "dashboard"

#     def send_message(self, instance):
#         if str(self.input.text).lower() == "training pdf":
#             webbrowser.open("http://192.168.100.29:5000/download-training")
#             response = "Hope training pdf downloaded successfully"
#             self.chat_output.text = response
#         elif str(self.input.text).lower() == "paly store redirect":
#             webbrowser.open("")
#             response = "Hope u r redirect to Playstore"
#             self.chat_output.text = response
#         else:
#             response = chat_api(
#             self.input.text
#             )
#             self.chat_output.text = response["reply"]