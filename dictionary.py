from difflib import get_close_matches
import tkinter
from tkinter import *
import json
data=json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        #  print("Do you mean '%s' instead" %get_close_matches(word,data.keys())[0])
         prompt="PROMPT:\nDo you mean '%s' instead\n" %get_close_matches(word,data.keys())[0]
         result.insert(0.0,"press 'y' for YES and 'n' for NO :")

         result.insert(0.0,prompt)
         pLabel=Label(win,text="Enter value for prompt ")
         
         pLabel.place(relx=0.3,rely=0.95, anchor=CENTER)
         p.place(relx=0.7,rely=0.95, anchor=CENTER)
         decide=promtValue.get()
         
         if decide == "y":
            return data[get_close_matches(word,data.keys()) [0]] 
         elif decide=="n":
            return ["Invalid word"]
         else  :
            print("Wrong choice press 'y' or 'n' ")
    else:
        return ["Invalid word"]

win = Tk()
win.title("Dictionary")
win.geometry("350x450")
def SearchedB():
    result.delete("1.0", "end")
    
    word=namevalue.get()
    output=translate(word)
    result.insert(0.0,"\n-------------------\n")
    if type(output)==list:
        for item in output:
            print(item+"\n")
            result.insert(0.0,item+"\n\n")
    p.delete(0,END)
    
label=Label(win,text="Enter the word you want to search")
namevalue=StringVar()
promtValue=StringVar()
e=Entry(win,textvariable=namevalue)

b=Button(win,text="Search",command=SearchedB)


label.grid(row=1,column=1,padx=10)
e.grid(row=1,column=2)

b.place(relx=0.5,rely=0.2, anchor=CENTER)
label.place(relx=0.3,rely=0.1, anchor=CENTER)
e.place(relx=0.8,rely=0.1, anchor=CENTER)

result = Text(win,height= 10,width=35,padx=10,pady=10)
result.grid(row=5,column=1 )
result.place(relx=0.5,rely=0.7, anchor=CENTER)
p=Entry(win,textvariable=promtValue)

win.mainloop()
