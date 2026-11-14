from tkinter import *
from PIL import Image, ImageTk
import stt
import action

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#38384E")


# ask function
def ask():
    user_val = stt.speech()
    if not user_val:
        text.insert(END, "BOT <---I didn't catch that\n")
        return

    text.insert(END, "user--->" + user_val + "\n")
    bot_val = action.Action(user_val)

    if bot_val is not None:
        text.insert(END, "BOT <---" + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()


# send function
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END , 'User--->'+ send+"\n")
    if bot != None:
        text.insert(END , "BOT <---"+str(bot)+"\n")
    if bot == "ok sir" :
        root.destroy()



# delete function
def delete():
    text.delete('1.8' , "end")


# Center the frame
frame = LabelFrame(
    root,
    padx=10,
    pady=10,
    borderwidth=3,
    relief="raised"
)
frame.place(relx=0.5, y=50, anchor="n", width=480, height=350)

# Heading
heading = Label(
    frame,
    text="AI Assistant",
    font=("Arial", 18, "bold"),
    bg="#3674A5",
    fg="black"
)
heading.pack(pady=15)

# Image
img = Image.open("image/chatbotai.jpg")
img.thumbnail((400, 250), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(img)

image_label = Label(frame, image=image, borderwidth=0)
image_label.pack(pady=10)
image_label.image = image

# Text area (chat log)
text = Text(root, font=("courier", 10, "bold"), bg="#356696")
text.place(x=100, y=375, width=375, height=100)

# Entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

# Buttons
Button1 = Button(root, text="ASK", bg="#356696", pady=16, padx=40,
                 borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

Button2 = Button(root, text="SEND", bg="#356696", pady=16, padx=40,
                 borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

Button3 = Button(root, text="DELETE", bg="#356696", pady=16, padx=40,
                 borderwidth=3, relief=SOLID, command=delete)
Button3.place(x=240, y=575)

root.mainloop()