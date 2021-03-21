from tkinter import Tk,Label,Scale,HORIZONTAL
from tkmacosx import Button

root = Tk()
root.title("Slider")

root.geometry("400x400")

def slider():
    my_label = Label(root,text=str(horizontal.get())+" x "+str(verticle.get())).pack() 
    root.geometry(str(horizontal.get())+"x"+str(verticle.get()))

verticle = Scale(root,from_=0,to=800)
verticle.pack()
horizontal = Scale(root,from_=0,to=800,orient=HORIZONTAL)
horizontal.pack()


# Here We set the default position of the slider 

my_label = Label(root,text=str(horizontal.get())+" x "+str(verticle.get())).pack() 



btn = Button(root,text="Click",command = slider).pack()

root.mainloop()