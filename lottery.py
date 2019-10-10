from tkinter import *
w=Tk()

def generate():
    from random import sample
    n=sample(range(10),6)
    l1.configure(text=n[0])
    l2.configure(text=n[1])
    l3.configure(text=n[2])
    l4.configure(text=n[3])
    l5.configure(text=n[4])
    l6.configure(text=n[5])

def reset():
    l1.configure(text="...")
    l2.configure(text="...")
    l3.configure(text="...")
    l4.configure(text="...")
    l5.configure(text="...")
    l6.configure(text="...")
    
##Designing coponents
img=PhotoImage(file="G:\lottery.gif")

lblimage=Label(w,image=img)
l1=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="solid")
l2=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="solid")
l3=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="solid")
l4=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="solid")
l5=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="solid")
l6=Label(w,text="...",width=2,font=("arial",20,"bold"),relief="solid")
b1=Button(w,text="Get ur lucky no",font=("arial",20,"bold"),command=generate)
b2=Button(w,text="Reset",font=("arial",20,"bold"),command=reset)

##placing components

lblimage.grid(row=1,column=1,rowspan=2)
l1.grid(row=1,column=2)
l2.grid(row=1,column=3)
l3.grid(row=1,column=4)
l4.grid(row=1,column=5)
l5.grid(row=1,column=6)
l6.grid(row=1,column=7)
b1.grid(row=2,column=2,columnspan=4)
b2.grid(row=2,column=6,columnspan=2)
w.mainloop()
