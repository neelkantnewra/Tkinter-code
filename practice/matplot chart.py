from tkinter import Tk,Label
from tkmacosx import Button
from PIL import Image,ImageTk
import numpy as np 
import matplotlib.pyplot as plt

root = Tk()
root.title("Graph")

def graph():
    house_price = np.random.normal(200000,25000,5000)
    plt.polar(house_price)
    plt.show()

Button(root,text="show graph",command=graph).pack()

root.mainloop()