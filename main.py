#Imports
import requests
import sys
import tkinter as tk
from tkinter import  messagebox

def check_conn():
    try:
        request = requests.get("http://www.google.com", timeout=5)
    except(requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        messagebox.showerror("No internet connection!", "Please make sure you have a connection to the internet!")
        sys.exit(0)
def download_video():
    request = requests.get("")

if __name__ == "__main__":
    check_conn()