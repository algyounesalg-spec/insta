from instagrapi import Client
import os

USERNAME = os.environ.get("IG_USERNAME")
PASSWORD = os.environ.get("IG_PASSWORD")

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")
print("Logged in successfully")
