import datetime
from tkinter import *
soot=Tk()
soot.title("page1")
soot.geometry("900x500")
soot.config(bg="skyblue")
#for text box
hr=Label(soot,text='hr',font=("Time New Roman",30),bg="green")
hr.place(x=30,y=160,height=30,width=100)

mi=Label(soot,text="min",font=("Time new Roman",30),bg="green")
mi.place(x=260,y=160,height=30,width=100)

sec=Label(soot,text="sec",font=("time new roman",30),bg="green")
sec.place(x=460,y=160,height=30,width=100)

am=Label(soot,text="am/pm",font=("time new roman",20),bg="green")
am.place(x=660,y=160,height=30,width=100)


#for time hours 
hr_lab=Label(soot,text='hr',font=('Time New Roman',40,"bold"),bg='blue',fg='white')
hr_lab.place(x=30,y=30,height=100,width= 100)
#for sec
mi_lab=Label(soot,text='min',font=('Time New Roman',40,"bold"),bg='blue',fg='white')
mi_lab.place(x=260,y=30,height=100,width= 100)
#for second
sec_lab=Label(soot,text='00',font=('Time New Roman',40,"bold"),bg='blue',fg='white')
sec_lab.place(x=460,y=30,height=100,width= 100)
#for am pm
sec_am=Label(soot,text='00',font=('Time New Roman',40,"bold"),bg='blue',fg='white')
sec_am.place(x=660,y=30,height=100,width= 100)

def date():
    timer=datetime.datetime.now()
    hr=timer.strftime("%I")
    mi=timer.strftime("%M")
    sec=timer.strftime("%S")
    ampm=timer.strftime("%p")
    hr_lab.config(text=hr)
    mi_lab.config(text=mi)
    sec_lab.config(text=sec)
    sec_am.config(text=ampm)

    day=Label(soot,text="day",font=("time New roman",40),bg="blue",fg="white")
    day.place(x=30,y=240,height=100,width=100)

    mon=Label(soot,text="month",font=("time New roman",40),bg="blue",fg="white")
    mon.place(x=260,y=240,height=100,width=100)

    year=Label(soot,text="year",font=("time new roman",40),bg="blue",fg="white")
    year.place(x=460,y=240,height=100,width=100)

    din=Label(text='00',font=('time new roman',40,"bold"),bg='blue',fg='white')
    din.place(x=660,y=240,height=100,width=100)
    


    day_txt=Label(soot,text="date",font=("time New roman",25),bg="white",fg="black")
    day_txt.place(x=30,y=370,height=30,width=100)

    mon_txt=Label(soot,text="month",font=("time New roman",25),bg="white",fg="black")
    mon_txt.place(x=260,y=370,height=30,width=100)

    year_txt=Label(soot,text="year",font=("time new roman",23),bg="white",fg="black")
    year_txt.place(x=460,y=370,height=30,width=100)

    din_txt=Label(text='day',font=('time new roman',25,"bold"),bg='white',fg='black')
    din_txt.place(x=660,y=370,height=30,width=100)
    
    dat=datetime.datetime.now()
    di=dat.strftime("%a")
    da=dat.strftime("%d")
    mo=dat.strftime("%m")
    yr=dat.strftime("%y")
    din.config(text=di)
    day.config(text=da)
    mon.config(text=mo)
    year.config(text=yr)
    hr_lab.after(200,date) 

#last text calanader clock
calandar=Label(text='******* CLOCK CALANDAR *******',font=('time new roman',20,"bold"),fg='green',bg='yellow')
calandar.place(x=30,y=430,height=40,width=840)

date()
soot.mainloop()