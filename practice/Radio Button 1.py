from tkinter import Tk,Label,Radiobutton,IntVar,StringVar
from tkmacosx import Button


def click(value):
    myLabel = Label(root,text = value)
    myLabel.pack()


def main():
    global root
    global mylabel
    root = Tk()
    root.title("Radio Button")
    r = StringVar()
    r.set("2")

    myLabel = Label(root,text = r.get())

    Radiobutton(root,text="option1",variable = r,value="1").pack()
    Radiobutton(root,text="option2",variable = r,value="2").pack()
    b1 = Button(root,text="ans",command = lambda:click(r.get())).pack()
    myLabel.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
