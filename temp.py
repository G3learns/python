from tkinter import *
from gtts import gTTS
import os
COUNT=1
def entr():
    global COUNT
    str=taskentry.get()
    lst.insert(COUNT,str)
    COUNT+=1
    taskentry.delete(0,len(str))
def playtodo():
    alltask=lst.get(0,END)
    txt= "Good Morning Mridhini! Today's task are: "
    for i in alltask:
        txt=txt+str(i)+"........"
    tts=gTTS(txt,lang="en")
    tts.save("daytask.mp3")
    os.system("start daytask.mp3")    
        
if __name__=="__main__":
    gui=Tk()x
    gui.minsize(500,600)
    gui.config(bd=5,relief=SUNKEN,padx=20,pady=20)
    gui.title("To Do App")
    head=Label(gui,text="To-Do",font=("Times",40))
    head.pack(side="top")
    frcen=Frame(gui,width=450,bd=5,relief=SUNKEN)
    frcen.pack(side=TOP)
    fren=Frame(gui,width=450,bd=5,relief=SUNKEN)
    fren.pack(side=TOP)
    task=Label(frcen,text="Task",font=("Times",20))
    task.pack(side="left",padx=10,pady=10)
    taskentry=Entry(frcen,font=("Times",20),width=20)
    taskentry.pack(side="left",padx=10,pady=10)
    entr=Button(frcen,text="Add",font=("Times",20),command=entr)
    entr.pack(side="left",padx=10,pady=10)
    #scrtask=Scrollbar(fren,orient="vertical")
    lst=Listbox(fren,width=80)#,yscrollcommand=scrtask)
    lst.pack(side="top",pady=30)
    btnplay=Button(fren,text="Play",font=("Times",20),command=playtodo)
    btnplay.pack(side="top")
    gui.mainloop()