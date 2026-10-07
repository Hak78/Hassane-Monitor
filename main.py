from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import os, json, urllib.parse

def parse_vless(link):
    try:
        parsed = urllib.parse.urlparse(link)
        user_info, netloc = parsed.netloc.split('@')
        ip, port = netloc.rsplit(':', 1)
        return f"{ip}:{port}"
    except:
        return "No Link"

class HassaneApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=
