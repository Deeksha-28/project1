#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob


# In[6]:


root = Tk()
root.title("Translator")
root.geometry("1200x600")


def lchange():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text =c)
    label2.configure(text=c1)
    root.after(1000,lchange)
    
def chng():
    global language
    try:
        text_=text1.get(1.0,END)
        c2 = combo1.get()
        c3 = combo2.get()
        if(text_):
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_=i
            words = words.translate(from_lang =lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletrans","try again")
            

logo = PhotoImage(file = "trans.png")
root.iconphoto(False, logo)

tr = PhotoImage(file = "arrow.png")
img1 = Label(root, image = tr , width=150)
img1.place(x=460,y=50)
language = googletrans.LANGUAGES
languageV= list(language.values())
lang1 = language.keys()
combo1 = ttk.Combobox(root, values = languageV, font = "Roboto14", state ="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")
label1 = Label(root, text = "ENGLISH", font = "segoe 30 bold",fg = "white", bg ="black", width = 18, bd=5, relief = GROOVE)
label1.place(x=10,y=50)

f = Frame(root, bg="white", bd=5)
f.place(x=10, y=110, width = 440 , height = 210)
text1 = Text(f,font = "Roboto 20", bg="black", relief = GROOVE, wrap = WORD,fg="white")
text1.place(x=0, y=0, width = 430, height=200)
scrollbar1 = Scrollbar(f)
scrollbar1.pack(side = "right", fill ="y")
scrollbar1.configure(command = text1.yview)
text1.configure(yscrollcommand = scrollbar1.set)

combo2 = ttk.Combobox(root, values = languageV, font = "Roboto14", state ="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")
label2 = Label(root, text = "ENGLISH", fg="white",font = "segoe 30 bold", bg ="black", width = 18, bd=5, relief = GROOVE)
label2.place(x=620,y=50)

f2 = Frame(root, bg="white", bd=5)
f2.place(x=620, y=110, width = 440 , height = 210)
text2 = Text(f2,font = "Roboto 20", bg="black", relief = GROOVE, wrap = WORD,fg="white")
text2.place(x=0, y=0, width = 430, height=200)
scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side = "right", fill ="y")
scrollbar2.configure(command = text2.yview)
text2.configure(yscrollcommand = scrollbar2.set)


trbutton = Button(root,text = "Translate", font ="Roboto 15 bold italic",
                 activebackground = "purple", cursor ="hand2", bd = 5,
                 bg ="cyan", fg = "black",command = chng)
trbutton.place(x=480,y=250)

lchange()




root.configure(bg="black")
root.mainloop()


# In[ ]:





# In[ ]:




