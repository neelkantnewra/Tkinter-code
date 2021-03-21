from tkinter import Tk,Label,Toplevel
from tkmacosx import Button,CircleButton
from PIL import Image,ImageTk

root = Tk()

def open():
    global myImage
    top =Toplevel()
    myImage = ImageTk.PhotoImage(Image.open("learning/src/Landscape2.jpeg").resize((400,200)))
    myLabel = Label(top,image = myImage).pack()
    CircleButton(top,text = "Close",command = top.destroy).pack(padx=10,pady=10)

button = Button(root,text="Open",command=open).pack(padx=20,pady=20)

root.mainloop()