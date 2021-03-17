#creating input or entry with tkinter
#using Function in tkinter

from tkinter import Tk,Label,Entry
from tkmacosx import Button
#tkmacosx is for mac user
root = Tk()
root.title("Button") #Title to be displayed above
root.geometry("400x750") #size of opening window

e = Entry(root,width=50)
e.insert(0,"Enter your Name")



def myClick():
    myLabel = Label(root,text=e.get())
    myLabel.pack()



#creating a label

myButton1 = Button(root,text="Enter your Name",padx=50,pady=50,command=myClick)

#packing the label in screen
e.pack()
myButton1.pack()


root.mainloop()
