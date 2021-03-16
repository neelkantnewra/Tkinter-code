#lets make another calculator 
from tkinter import Tk,Label,END,Entry,DISABLED
from tkmacosx import Button

root = Tk()
root.resizable(0,0)
root.title("Simple Calculator")

#BackSpace Button

def cancel():
    lst = myEntry.get()
    lst = list(lst)
    lst = lst[0:len(lst)-1]
    lst = "".join(lst)
    myEntry.delete(0,END)
    myEntry.insert(0,lst)

#click Button
def click(number):
    if number == 0 and myEntry.get() == "":
        myEntry.insert(END,"")
    elif number == "⟵":
        cancel()
    else:
        myEntry.insert(END,number)

 #Arithmetic operation       
def equal():
    val = myEntry.get()
    val = list(val)
    val = list(map(lambda st: str.replace(st,"×","*"),val))
    val = list(map(lambda st: str.replace(st,"÷","/"),val))
    val = "".join(val)
    val = eval(str(val))
    myEntry.delete(0,END)
    myEntry.insert(0,val)

#clear the text area

def clear():
    myEntry.delete(0,END)

myEntry = Entry(root,width=35,font=("Calibri",18),justify="right")
myEntry.grid(row=0,column=0,columnspan=4,pady=10)
myEntry.bind("<Key>", lambda e: "break")

button_1 = Button(root,text="1",padx=8,pady=20,command = lambda:click(1))
button_2 = Button(root,text="2",padx=8,pady=20,command = lambda:click(2))
button_3 = Button(root,text="3",padx=8,pady=20,command = lambda:click(3))
button_4 = Button(root,text="4",padx=8,pady=20,command = lambda:click(4))
button_5 = Button(root,text="5",padx=8,pady=20,command = lambda:click(5))
button_6 = Button(root,text="6",padx=8,pady=20,command = lambda:click(6))
button_7 = Button(root,text="7",padx=8,pady=20,command = lambda:click(7))
button_8 = Button(root,text="8",padx=8,pady=20,command = lambda:click(8))
button_9 = Button(root,text="9",padx=8,pady=20,command = lambda:click(9))
button_0 = Button(root,text="0",padx=8,pady=20,command = lambda:click(0))
button_add = Button(root,text="+",pady=50,command = lambda:click("+"),font=("Calibri",18))
button_mul = Button(root,text="×",padx=8,pady=20,command = lambda:click("×"))
button_div = Button(root,text="÷",padx=8,pady=20,command = lambda:click("÷"))
button_back = Button(root,text="⟵",padx=8,pady=20,command = lambda:click("⟵"),bg="pink")
button_dot = Button(root,text=".",padx=8,pady=20,command = lambda:click("."))
button_equal= Button(root,text="=",padx=8,pady=20,command = equal)
button_clear= Button(root,text="Clear",padx=65,pady=20,command = clear)
button_min = Button(root,text="-",padx=8,pady=20,command = lambda:click("-"))

#button placing

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_div.grid(row=2,column=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_back.grid(row=1,column=3)

button_dot.grid(row=4,column=0)
button_0.grid(row=4,column=1)
button_add.grid(row=4,column=2,rowspan=2)
button_min.grid(row=4,column=3)

button_equal.grid(row=5,column=3)
button_clear.grid(row=5,column=0,columnspan=2)

root.mainloop()
