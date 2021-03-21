from tkinter import Tk,Label,Checkbutton,IntVar,StringVar
from tkmacosx import Button

root = Tk()
root.title("Check Box")

# var = IntVar()
var = StringVar()

def checked():
    my_Label = Label(root,text=var.get()).pack()


# c = Checkbutton(root,text = "Option 1",variable=var)   #onvalue ,offvalue used if string var is used
c = Checkbutton(root,text = "Option 1",variable=var,onvalue="On",offvalue="Off") 
c.deselect()
c.pack()

my_button = Button(root,text="Submit",command=checked).pack()
my_Label = Label(root,text=var.get()).pack()

root.mainloop()