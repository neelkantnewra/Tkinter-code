#creating butoon with tkinter
#using Function in tkinter

from tkinter import Tk,Label
from tkmacosx import Button
#tkmacosx is for mac user
root = Tk()
root.title("Button") #Title to be displayed above
root.geometry("400x750") #size of opening window

def myClick():
    myLabel = Label(root,text="clicked")
    myLabel.pack()

#creating a label

myButton1 = Button(root,text="1",padx=50,pady=50,command=myClick,bg="skyblue",fg = "violet")
myButton2 = Button(root,text="2")
myButton3 = Button(root,text="3")
myButton4 = Button(root,text="4")

#packing the label in screen
myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()

root.mainloop()
