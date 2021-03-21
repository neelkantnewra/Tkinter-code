from tkinter import Tk,OptionMenu,Label,W,IntVar,StringVar,ttk
from tkmacosx import Button
from datetime import date

root = Tk()
root.title("Drop Down Menu")
root.geometry("300x400")

today = date.today()
d1 = today.strftime("%d/%m/%Y")

d1 = d1.split("/")
d1 = d1[2]

def submit():
    global d1
    global feedback
    feedback.grid_forget()
    feedback = Label(root,text= "Your Date of Birth is\n "+ day.get()+" " + month.get()+" " + year.get()+"\n and you age is " + str(int(d1) - int(year.get())))
    feedback.grid(row=3,column=0,padx=5,pady=5,columnspan=3)

Day = [str(x) for x in range(1,32)]
Month = ["January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"]

day = StringVar()
month = StringVar()
year = StringVar()

day.set("Day")
month.set("Month")
year.set("Year")

Year = [str(year) for year in range(2021,1990,-1)]

question = Label(root,text="What is your Date of Birth?")
day_drop_down = OptionMenu(root,day,*Day)
month_drop_down = OptionMenu(root,month,*Month)
year_drop_down = OptionMenu(root,year,*Year)
btn = Button(root,text="Submit",command=submit)

feedback = Label(root,text="Waiting for your Response...")


feedback.grid(row=3,column=0,padx=5,pady=5,columnspan=3)

day_drop_down.grid(row=1,column=0,sticky=W,padx=5)
month_drop_down.grid(row=1,column=1,sticky=W,padx=5)
year_drop_down.grid(row=1,column=2,sticky=W,padx=5)
question.grid(row=0,column=0,padx=5,pady=5,sticky=W,columnspan=3)
btn.grid(row=2,column=0,padx=5,pady=5,columnspan=3)






root.mainloop()


