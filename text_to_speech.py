from tkinter import *
from tkinter import messagebox
import pyttsx3
from PIL import ImageTk, Image
from gtts import gTTS
import datetime

language = "en"
engine = pyttsx3.init()
root = Tk()

# icon
photo = PhotoImage(file="logo.png")
root.iconphoto(False, photo)

# jenny is an assistant like Google Assistant or siri
root.title("Div1 - 101,129,130,142")
root.configure(bg="#262626")
root.geometry("600x350")

# jenny voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# file name in date and time format
basename = "txt_to_speech"
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
filename = "_".join([basename, suffix])


def speak():
    sy = entry1.get()
    engine.say(sy)
    engine.runAndWait()
    engine.stop()
    if sy == "":
        messagebox.showerror("ERROR", "Write something \nthen tap on speak.")


# saving file
def save():
    text1 = entry1.get()
    if text1 == "":
        messagebox.showerror("ERROR", 'First write something,then tap on save file.')
    else:
        saving = gTTS(text=text1, lang=language, slow=False)
        saving.save(filename + ".mp3")


# label frame
img = ImageTk.PhotoImage(Image.open("audio.png"))
img1 = ImageTk.PhotoImage(Image.open("save.png"))
frame = LabelFrame(root, text="𝕿𝖊𝖝𝖙 𝕿𝖔 𝕾𝖕𝖊𝖊𝖈𝖍", font="50", bg="#595959", fg="White", labelanchor="n")
frame.pack(fill="both", expand="yes", padx=10, pady=0)
label = Label(frame, image=img, bg="#595959")

# label for gtts
label1 = Label(frame, image=img1, bg="#595959")

# entry widget
txt = StringVar()
entry1 = Entry(frame, width=50, textvariable=txt, bg="#D9D9D9")
entry1.pack(padx=100, pady=30)

# Button
Button(frame, label, font=15, command=speak).pack(pady=5)
Button(frame, label1, font=15, command=save).pack(pady=5)


root.mainloop()
