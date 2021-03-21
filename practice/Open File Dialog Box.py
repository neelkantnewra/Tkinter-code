from tkinter import Tk,Label,Toplevel
from tkinter import filedialog 
from tkmacosx import Button,CircleButton
from PIL import Image,ImageTk

root = Tk()
root.title("Image Open Dialog")
root.filename = filedialog.askopenfile(initialdir="src",title = "Select a file",filetypes=(("png","*.png"),("jpeg","*.jpeg")))
my_image = ImageTk.PhotoImage(Image.open(root.filename.name))
my_image_label = Label(root,image=my_image).pack(padx=10,pady=10)
my_label = Label(root,text="Source: " + root.filename.name).pack(padx=10,pady=10)

root.mainloop()