import random

from tkinter import *

root=Tk()
root.title("Lucky letter")
root.geometry("400x350")
names=["a","b","c","d","e"]

def lucky():
    n=random.randint(0,4)
    print(n)
    friend=names[n]
    print(friend)


btn=Button(root,text="Who is my lucky letter",command=lucky)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()
