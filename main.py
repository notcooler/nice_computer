#Imports
import requests
import sys
import webview
import tkinter as tk
from tkinter import messagebox

url = "https://notcooler.github.io/"

def check_conn():
    try:
        request = requests.get("http://www.google.com", timeout=5)
    except(requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        messagebox.showerror("No internet connection!", "Please make sure you have a connection to the internet!")
        sys.exit(0)

def play_video():
    window = webview.create_window("nice computer you got there", url, fullscreen=True)
    webview.start()

if __name__ == "__main__":
    check_conn()
    #download_video()
    play_video()