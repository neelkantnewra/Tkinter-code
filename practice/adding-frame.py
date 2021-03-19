from tkinter import Tk,Label,LabelFrame
from tkmacosx import Button

root = Tk()

frame = LabelFrame(root,text="Frame-1",padx=5,pady=5)
frame.grid(padx=10,pady=10,row=0,column=0)

frame1 = LabelFrame(root,text="Frame-2",padx=5,pady=5)
frame1.grid(row=1,column=0)

button_frame = LabelFrame(root,text="Frame-2",padx=5,pady=5)
button_frame.grid(row=1,column=0)


button1 = Button(frame,text="B1",padx=10,pady=10).grid(row=0,column=0)
button2 = Button(frame,text="B2",padx=10,pady=10).grid(row=0,column=1)
button3 = Button(frame,text="B3",padx=10,pady=10).grid(row=0,column=2)

button4 = Button(frame1,text="B1",padx=10,pady=10).grid(row=0,column=0)
button5 = Button(frame1,text="B2",padx=10,pady=10).grid(row=0,column=1)
button6 = Button(frame1,text="B3",padx=10,pady=10).grid(row=0,column=2)


root.mainloop()
