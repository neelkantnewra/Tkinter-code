from tkinter import Tk,Label,messagebox,Message
from tkmacosx import Button

root = Tk()
root.title("Message Box")

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askyesnocancel.

def popup():
    response = messagebox.askyesno(title="This is Pop Up",message="Hello World")
    if response == 1:
        val = "You clicked Yes"
    else:
        val = "You click No"
    Label(root, text = val).pack()

Button(root,text="Pop button",command = popup).pack()
root.mainloop()