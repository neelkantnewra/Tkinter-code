# we will use grid system here 

from tkinter import Label,Tk

root = Tk()

#creating a label
mylabel1 = Label(root,text= "hello world!")
mylabel2 = Label(root,text= "My name is Neel")

#packing the label in screen
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=1)

root.mainloop()
