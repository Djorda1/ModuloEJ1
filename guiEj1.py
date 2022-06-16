
import tkinter
from tkinter import ttk


def reset(event):
    selecionado.set(None)
    Label_anuncio.config(text="")
def showLabel():
    Label_anuncio.config(text="{}".format(selecionado.get()))

window=tkinter.Tk()
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

selecionado=tkinter.StringVar()
button1=ttk.Radiobutton(window,text='acepto',value='acepto',variable=selecionado,command=showLabel)
button2=ttk.Radiobutton(window,text='no acepto',value='no acepto',variable=selecionado,command=showLabel)
button1.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)
button2.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)
Label_anuncio=tkinter.Label(window)
Label_reset=tkinter.Button(window,text="reset")
Label_anuncio.grid(column=0,row=2,sticky=tkinter.W,padx=5,pady=5)
Label_reset.grid(column=0,row=3,sticky=tkinter.W,padx=5,pady=5)
Label_reset.bind('<Button-1>', reset)

window.mainloop()

