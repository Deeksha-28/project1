#!/usr/bin/env python
# coding: utf-8

# In[7]:




apikey ="BejZRpAbQi8MemO-E3Y8nT506g3OlSvvRr7Ck8Re7BdX"

url = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/ac7e1892-3919-4892-a8d3-d7ec8b28aacf"


# In[8]:



import json
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox, scrolledtext
try:
    from ibm_watson import LanguageTranslatorV3
    from ibm_watson import ApiException
    from PIL import Image, ImageTk
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
except ImportError as e:
    from pip._internal import  main as install
    install(["install", "pillow"])
    install(["install", "ibm-watson>=4.7.1"])
finally:
    pass
class NoTextException(Exception):
    pass
root = Tk()
root.title("Language Identifier")
root.iconbitmap("trans.png")
window_width, window_height = 600,300
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
position_top,position_right = int(screen_height/2 - window_height/2), int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.resizable(False, False)

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{version}',
    authenticator=authenticator
)
language_translator.set_service_url(f'{url}')

def close():
    val = messagebox.askyesnocancel("Language Identifier", "Are you sure you want to close the Language Identifier "
                                                           "App?")
    return root.quit() or root.destroy() if val else root.focus()
def clear(yes):
    if yes:
        val = messagebox.askokcancel("Language Identifier",
                                 "By clearing, you will "
                                 "loose all the infomation you have typed")
        if val:
            text.delete('0.0', END)
            text.delete('0.0', END)
        else:
            root.focus()
    else:
        text.delete('0.0', END)
        return
    return
def detect():
    try:
        try:
            text_to_detect = text.get('0.0', END)
            if len(text_to_detect) == 0:
                raise NoTextException("The Language Identifier can not detect language if the text is NULL")
            else:

                languages = language_translator.identify(text_to_detect).get_result()
                # Take the first language from the list of languages
                estimated_language = languages["languages"][0]["language"]
                # print(estimated_language)
                # search for the language_name from the language lists
                identifiable_languages = language_translator.list_identifiable_languages().get_result()
                # find the index of the correct language
                index_of_correct_language, i =0, 0
                for lang in identifiable_languages["languages"]:
                    if estimated_language == lang["language"]:
                        index_of_correct_language = i
                    else:
                        index_of_correct_language = index_of_correct_language
                    i += 1
                #  Display the language to the user
                messagebox.showinfo("Language Identifier", "The language was detected to be: {} ({}).".format(
                    str(identifiable_languages["languages"][index_of_correct_language]["name"]).upper(),
                    identifiable_languages[
                        "languages"][index_of_correct_language]["language"]))
                # print(identifiable_languages["languages"][index_of_correct_language])
        except NoTextException as error :
            messagebox.showerror("Language Identifier",
                                 error)
        finally:
            pass
    except ApiException:
        messagebox.showerror("Language Identifier", "Make sure you are connected to internet and your API credentials are working.")
    finally:
        pass
    return

label_image = ImageTk.PhotoImage(Image.open("arrow.png"))
label1 = Label(root, text="", font=("arial", 15, "bold"), fg="lightseagreen",
       compound=RIGHT)
label1.grid(row=0, column=0, columnspan=6)
label1 = Label(root, text="Type Text Bellow", font=("arial", 10, "bold"), fg="lightseagreen")
label1.grid(row=1, column=0, columnspan=3)
text = scrolledtext.ScrolledText(root, width=62, height=5, font=("arial", 12))
text.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
Button(root, bg="green", relief="solid", activebackground="blue",
       text="detect" ,fg="white", width=15, bd=1, command=detect).grid(
    row=3, column=1)
Button(root, bg="orange", relief="solid", activebackground="red",
       text="clear" ,fg="white", width=15, bd=1, command=lambda : clear(True)).grid(
    row=3, column=2)
Button(root, bg="red", relief="solid", activebackground="orange",
       text="close",fg="white", width=15, bd=1, command =close).grid(
    row=3, column=0, sticky=W, padx=5, pady=5)
root.mainloop(0)


# In[ ]:




