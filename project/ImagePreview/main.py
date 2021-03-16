from tkinter import Tk,Label,DISABLED,N,S,E,W
from tkmacosx import Button,CircleButton
from PIL import Image,ImageTk

def main():
    root = Tk()
    root.title("Image Preview")
    root.resizable(0,0)
    #image initialisation and opening
    myImg1 = ImageTk.PhotoImage(Image.open("src/Landscape1.jpeg").resize((800,400)))
    myImg2 = ImageTk.PhotoImage(Image.open("src/Landscape2.jpeg").resize((800,400)))
    myImg3 = ImageTk.PhotoImage(Image.open("src/Landscape3.jpeg").resize((800,400)))
    myImg4 = ImageTk.PhotoImage(Image.open("src/Landscape4.jpeg").resize((800,400)))
    myImg5 = ImageTk.PhotoImage(Image.open("src/Landscape5.jpeg").resize((800,400)))
    myImg6 = ImageTk.PhotoImage(Image.open("src/Landscape6.jpeg").resize((800,400)))
    myImg7 = ImageTk.PhotoImage(Image.open("src/Landscape7.jpeg").resize((800,400)))

    #Button Image
    back = ImageTk.PhotoImage(Image.open("src/left.png").resize((50,50)))
    forward = ImageTk.PhotoImage(Image.open("src/right.png").resize((55,55)))
    close = ImageTk.PhotoImage(Image.open("src/close.png").resize((55,50)))
    disableBack = ImageTk.PhotoImage(Image.open("src/disableBack.png").resize((55,55)))
    disableForward = ImageTk.PhotoImage(Image.open("src/disableForward.png").resize((59,59)))

    #list of Image
    myImgList = [myImg1,myImg2,myImg3,myImg4,myImg5,myImg6,myImg7]
    global myLabel

    myLabel = Label(image=myImg1)
    myLabel.grid(row=0,column=0,columnspan=7)

    global button_back
    global button_forward

    def click(img):
        global myLabel
        global button_back
        global button_forward    
        myLabel.grid_forget()
        myLabel = Label(image=myImgList[img-1])
        myLabel.grid(row=0,column=0,columnspan=7)
        if img == len(myImgList):
            button_forward = CircleButton(root,image=disableForward,takefocus=0,state=DISABLED )
            button_forward.grid(row = 1,column=4,sticky=W)   
            button_back = CircleButton(root,image=back,takefocus=0,command =lambda: click(img-1))
            button_back.grid(row = 1,column=2,sticky=E)
        elif img== 1:
            button_forward = CircleButton(root,image=forward,takefocus=0,command =lambda: click(img+1) )
            button_forward.grid(row = 1,column=4,sticky=W)   
            button_back = CircleButton(root,image=disableBack,takefocus=0,state=DISABLED)
            button_back.grid(row = 1,column=2,sticky=E)
        else:
            button_forward = CircleButton(root,image=forward,takefocus=0,command =lambda: click(img+1) )
            button_forward.grid(row = 1,column=4,sticky=W)
            button_back = CircleButton(root,image=back,takefocus=0,command =lambda: click(img-1))
            button_back.grid(row = 1,column=2,sticky=E)  

    # #image display


    button_back = CircleButton(root,image=disableBack,takefocus=0)
    button_back.grid(row = 1,column=2,sticky=E)

    button_close = CircleButton(root,image=close,command=root.quit)
    button_close.grid(row = 1,column=3)

    button_forward = CircleButton(root,image=forward,takefocus=0,command =lambda: click(2) )
    button_forward.grid(row = 1,column=4,sticky=W)

    root.mainloop()

if __name__ == "__main__":
    main()