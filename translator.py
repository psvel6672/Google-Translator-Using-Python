# Tkinter Components

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import pyautogui as pag

from googletrans import Translator
import datetime, threading, pyperclip

class TranslatorAPP:

    def __init__(self):
        
        self.MainController = Translator(service_urls=["translate.google.com"])

        self.TransWind = Tk()
        self.TransWind.geometry("500x480+500+100")
        self.TransWind.title("Google Translator")
        self.TransWind.resizable(0,0)
        self.TransWind.iconbitmap("logo.ico")

        self.langVal = tk.StringVar()

        self.EditorLabel = Label(self.TransWind, text="Enter Your Text")
        self.EditorLabel.place(x= 5, y = 5)

        self.EditorText = Text(self.TransWind, width=40, height=7)
        self.EditorText.place(x= 5, y = 35)

        self.ConvertedLabel = Label(self.TransWind, text="Converted Text")
        self.ConvertedLabel.place(x= 5, y = 200)

        self.langList = ttk.Combobox(self.TransWind, textvariable=self.langVal)
        self.langList.place(x= 256, y = 200)

        self.langList['values'] = ('Select Language', 'Tamil','English','Hindi', 'Kanada', 'Telugu')

        self.langDefault = "Select Language"
        self.langList.set(self.langDefault)

        self.OutputText = Text(self.TransWind, width=40, height=7, state=tk.DISABLED)
        self.OutputText.place(x= 5, y = 235)

        self.ConvertBtn = Button(self.TransWind, text="Convert", width=10, command=self._translatorThread)
        self.ConvertBtn.place(x= 5, y = 400)

        self.CopyBtn = Button(self.TransWind, text="Copy", width=10, command=self._copyText)
        self.CopyBtn.place(x= 120, y = 400)

        self.ClearBtn = Button(self.TransWind, text="Clear", width=10, command=self._clearEditor)
        self.ClearBtn.place(x= 235, y = 400)

        chkCurrentYear = datetime.datetime.now().strftime("%Y")

        if int(chkCurrentYear) > 2023:
            cpyrightYear = "2023 - "+str(chkCurrentYear)
        else:
            cpyrightYear = "2023"

        self.authorLabel = Label(self.TransWind, text='PS Thamizhan - © '+str(cpyrightYear)+'. V1.0', font=("Segoe UI", 7))
        self.authorLabel.pack(side=BOTTOM, ipady=10)


    def _translatorThread(self):

        Content = self.EditorText.get('1.0', END)
        language = self.langVal.get()

        if str(Content.strip()) != "" and len(Content) > 0:

            if str(language.strip()) != "" and str(language) != str(self.langDefault):
                actualLang = language[:2].lower()
                convertThread = threading.Thread(target = self._translator, args=(str(Content), str(actualLang), ), name="Start Translator")
                convertThread.start()
            else:
                messagebox.showerror("Google Translator Alert", "Please select a language.         ")
        else:
            messagebox.showerror("Google Translator Alert", "Please enter text to convert")

        return True

    def _clearEditor(self):

        try:
            self.EditorText.delete('1.0', END)
            self.langList.set(self.langDefault)
            self.OutputText.config(state=tk.NORMAL)
            self.OutputText.delete('1.0', END)
            self.OutputText.config(state=tk.DISABLED)
        except:
            messagebox.showerror("Google Translator Alert", "Something wrong, Try again after sometime")
        return True

    def _translator(self, word, lang):

        try:
            translated = self.MainController.translate(word, dest=lang).text
            self.OutputText.config(state=tk.NORMAL)
            self.OutputText.delete('1.0', END)
            self.OutputText.insert("insert", str(translated))
            self.OutputText.config(state=tk.DISABLED)
        except:
            messagebox.showerror("Google Translator Alert", "Something wrong, Try again after sometime")
        return True

    def _copyText(self):
        try:
            CopyContent = self.OutputText.get('1.0', END)

            if(str(CopyContent.strip()) != ""):
                pyperclip.copy(str(CopyContent))
                messagebox.showinfo("Google Translator Alert", "Content copied to clipboard.")
            else:
                messagebox.showerror("Google Translator Alert", "No content.               ")

        except:
            messagebox.showerror("Google Translator Alert", "Something wrong, Try again after sometime")

    def runModule(self):
        self.TransWind.mainloop()

mod = TranslatorAPP()
mod.runModule()
