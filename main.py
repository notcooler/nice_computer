#Imports
import requests
import sys
import vlc
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from tkinter import messagebox

url = "https://github.com/notcooler/nice_computer/raw/6086b6d8237790e95e9d3bbc904544fdddf57bb1/data/e.mp4"
url2 = ""
filePath = "e.mp4"
filePath2 = "e.mp3"

def check_conn():
    try:
        request = requests.get("http://www.google.com", timeout=5)
    except(requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        messagebox.showerror("No internet connection!", "Please make sure you have a connection to the internet!")
        sys.exit(0)
def main():
    r = requests.get(url, allow_redirects=True)
    with open(filePath, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    f.close()
    r = requests.get(url2, allow_redirects=True)
    with open(filePath2, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    f.close()
    print("play")
    play_video()
def play_video():
    root = tk.Tk()
    root.title("nice computer you got there")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(str(screen_width) + 'x' + str(screen_height))
    videoplayer = TkinterVideo(master=root, scaled=True)
    pathMP4 = filePath
    videoplayer.load(pathMP4)
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()
    root.mainloop()
    s = vlc.MediaPlayer("e.mp3")

if __name__ == "__main__":
    check_conn()
    main()