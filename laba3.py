import os, random, string, subprocess, tkinter as tk
from PIL import Image, ImageTk

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def block():
    # одна цифра + три буквы, перемешиваем
    chars = [random.choice(string.digits)] + random.choices(string.ascii_uppercase, k=3)
    random.shuffle(chars)
    return "".join(chars)

def generate():
    key.set("-".join(block() for _ in range(4)))

def blink(i=0):
    colors = ["cyan", "lime", "yellow", "magenta", "orange"]
    title.config(fg=colors[i % 5])
    root.after(300, blink, i + 1)

def play_music():
    # afplay - встроенный проигрыватель macOS; когда трек кончился, запускаем заново
    global music
    if music.poll() is not None:
        music = subprocess.Popen(["afplay", "music.mp3"])
    root.after(1000, play_music)

def close():
    music.terminate()
    root.destroy()

root = tk.Tk()
root.title("KeyGen")
root.geometry("800x500")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", close)

bg = ImageTk.PhotoImage(Image.open("background.jpg").resize((800, 500)))
tk.Label(root, image=bg).place(x=0, y=0)

title = tk.Label(root, text="KEYGEN", font=("Courier New", 44, "bold"), bg="black")
title.place(relx=0.5, y=60, anchor="center")

key = tk.StringVar(value="XXXX-XXXX-XXXX-XXXX")
tk.Entry(root, textvariable=key, font=("Courier New", 26, "bold"),
         justify="center", width=21, state="readonly").place(relx=0.5, y=300, anchor="center")

tk.Button(root, text="GENERATE", command=generate,
          font=("Courier New", 18, "bold")).place(relx=0.5, y=380, anchor="center")

music = subprocess.Popen(["afplay", "music.mp3"])
play_music()
blink()
root.mainloop()