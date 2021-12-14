#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tki
import json
from tkinter import *
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def click():  

    authenticator = IAMAuthenticator("BejZRpAbQi8MemO-E3Y8nT506g3OlSvvRr7Ck8Re7BdX")
    language_translator = LanguageTranslatorV3(version='2018-03-19',authenticator=authenticator)
    language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/ac7e1892-3919-4892-a8d3-d7ec8b28aacf")
    language_translator.set_disable_ssl_verification(False)
    
    fromThis=from_lang.get()
    toThis=to_lang.get()

    fromThis=fromThis[-2:]
    toThis=toThis[-2:]
    
    translation = language_translator.translate(
        text=w.get(),
        model_id=fromThis+'-'+toThis).get_result()
    tr=translation.get('translations')[0].get('translation')

    mylab=Label(root, font=('cambria 17'), text=tr)
    mylab.pack()

root=Tk()
root.geometry('450x425')
topframe=Frame(root, relief=RAISED, borderwidth=16)
topframe.pack(pady=20)
head=tki.Label(topframe, text ='Translator' ,fg='white', bg='black')
head.configure(font="arial 28 underline")
head.pack(pady=0)


tagline=tki.Label(root,text='AI powered', fg='black',bg='white')
tagline.configure(font='cambria 12')
tagline.pack(pady=12)

transframe=Frame(root)
transframe.pack()
choices=['English-en','Spanish-es', 'French-fr','Hindi-hi','German-de','Italian-it','Russian-ru','Japanese-ja','Korean-ko','Urdu-ur']
from_lang=StringVar()
to_lang=StringVar()

from_lang.set('English-en')
to_lang.set('Spanish-es')
langframe=Frame(transframe)

dropdown_left=OptionMenu(transframe,from_lang,*choices)
dropdown_left.pack(padx=9,side=LEFT)
dropdown_right=OptionMenu(transframe,to_lang,*choices)
dropdown_right.pack(padx=9,side=RIGHT)

entryframe=Frame(root)
entryframe.pack(pady=15)
w=Entry(entryframe, font=('arial,19'), width=40)
w.pack()
submit=Button(entryframe,font=('verdana 9'),text='Click',width=12, background='light blue',command=click)
submit.pack(pady=5)
mainloop()


# In[ ]:




