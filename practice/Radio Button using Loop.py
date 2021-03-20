from tkinter import Tk,Radiobutton,StringVar,W,Label
from tkmacosx import CircleButton

root = Tk()
root.title("Radio button using Loop")

def click():
    global mylabel
    mylabel.grid_forget()
    mylabel = Label(root,text=pizza.get())
    mylabel.grid(row=4,column=0)


MODES = [
    ("Pepper","Pepper"),
    ("Cheese","Cheese"),
    ("Panner","Panner"),
    ("Onion","Onion"),
]


pizza = StringVar()
pizza.set("Pepper")
i=0
for text_item,mode in MODES:
    Radiobutton(root,text=text_item,variable=pizza,value=mode).grid(row=i,column=0,sticky=W)
    i+=1

mylabel = Label(root,text=pizza.get())
mylabel.grid(row=4,column=0)

mybutton = CircleButton(root,text="Click Me",command=click)
mybutton.grid(row=5,column=0)
root.mainloop()
