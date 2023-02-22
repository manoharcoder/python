from tkinter import *
def click(event):
    text=event.widget.cget("text") #to get values we use cget
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    #     clears the screen
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()#it update the values

root=Tk()
root.geometry("500x1000")
root.title("CALCULATOR    BY     MANOHAR")


# giving enty inputs
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,bg="yellow",textvar=scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx=10,pady=10,padx=10)

f=Frame(root,bg="light blue")
b=Button(f,text="9",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)


b=Button(f,text="7",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)


f.pack()
f=Frame(root,bg="light blue")
b=Button(f,text="6",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)


b=Button(f,text="4",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="light blue")
b=Button(f,text="3",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)


b=Button(f,text="1",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="light blue")
b=Button(f,text="0",padx=10,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=14,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=9,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=13,pady=3)
b.bind("<Button-1>",click)


b=Button(f,text="=",padx=9,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=14,pady=3)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="light blue")
b=Button(f,text="+",padx=10,pady=2,font="lucida 30 bold")
b.pack(side=LEFT,padx=16,pady=16)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=16,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="*",padx=10,pady=2,font="lucida 30 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="light blue")
b=Button(f,text="%",padx=10,pady=2,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=10,pady=2,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)


b=Button(f,text="C",padx=10,pady=2,font="lucida 30 bold")
b.pack(side=LEFT,padx=15,pady=3)
b.bind("<Button-1>",click)

Label(root,text="SIMPLE CALCULATOR",relief=SUNKEN).pack(side=BOTTOM,anchor="s")

f.pack()





f=Frame(root,bg="BLUE")
b=Button(f,fg="grey",text="MANOHAR",padx=1,pady=2,font="lucida 15 bold")
b.pack(side=TOP,padx=10,pady=3)
# b.bind("<Button-1>",click)
f.pack()
root.mainloop()