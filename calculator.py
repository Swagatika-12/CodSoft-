from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        
        else:
            try:
                value=eval(screen.get())

            except Exception as e:
                print(e)
                value="Error"
                
        scvalue.set(value)
        screen.update()
    elif text=="AC":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
root = Tk()
root.geometry("644x900")
root.title("CALCULATOR BY SWAGATIKA")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f1=Frame(root,bg="purple")
bu=Button(f1,text="3",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="4",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="5",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="purple")
bu=Button(f1,text="6",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="7",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="8",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="purple")
bu=Button(f1,text="9",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="1",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="2",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="purple")
bu=Button(f1,text="0",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="/",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="%",padx=18,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="purple")
bu=Button(f1,text="*",padx=20,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="-",padx=20,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="+",padx=20,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="purple")
bu=Button(f1,text="=",padx=15,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text="AC",padx=15,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)

bu=Button(f1,text=".",padx=15,pady=12,font="lucida 25 bold")
bu.pack(side=LEFT,padx=18,pady=12)
bu.bind("<Button-1>",click)
f1.pack()

root.mainloop()
