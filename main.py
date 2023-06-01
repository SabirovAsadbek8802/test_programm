from tkinter import *
from tkinter.messagebox import *
import json
import random

oyna = Tk()
oyna.geometry("600x450+200+50")

d={
    "savollar":{
    }
}

file=open('data_base.txt','r',encoding="utf8")
data=file.readlines()
t = 0
for i in range(0,len(data),5):
    t+=1
    a={
        f"savol{t}":{
            "savol":data[i],
             "javoblar":{
                 data[i+1]:"A",
                 data[i+2]:"B",
                 data[i+3]:"C",
                 data[i+4]:"D",
             },
            "tj":data[i+1]
        }
    }
    d['savollar'].update(a)
dd=json.dumps(d)

a = ''

def click():
    pass
    a = d['savollar']['savol1']

Label(oyna, text=d['savollar']['savol1']['savol']).grid(row=0, column=1)
Radiobutton(oyna, text=d['savollar']['savol1']['javoblar']).grid(row=1,column=1)

oyna.mainloop()
