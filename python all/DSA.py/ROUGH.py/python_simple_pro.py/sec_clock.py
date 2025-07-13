import datetime
from tkinter import *
sp=Tk()
sp.title("+++++++++ SECOND CLOCK ++++++++")
sp.geometry("600x500")
sp.config(bg="green")
#for making simple box 
box=Label(sp,text="second clock",font=("time new roman",30),bg="skyblue",fg="blue")
box.place(x=150,y=80,height=50,width=300)
#clock second box
clock=Label(text="00",font=("time new roman",50,"bold"),bg="yellow",fg="orange")
clock.place(x=190,y=180,height=200,width=200)
button=Button(sp,text="Time Now",font=('time new romean',30,"bold"),bg='pink',fg='red',relief=RAISED)
button.place(x=150,y=420,height=40,width=300)

#secclock  block floating 
def second():
    sec=datetime.datetime.now()
    seco=sec.strftime("%S")
    clock.after(200,second)
    clock.config(text=seco)
second()
sp.mainloop()