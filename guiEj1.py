import tkinter
from tkinter import ttk
import pprint



def reset(event):
    # No encuentro como resetear el radiobutton1 y 2
    pass



window=tkinter.Tk()
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)




selecionado=tkinter.StringVar()
button1=ttk.Radiobutton(window,text='acepto',value='1',variable=selecionado)
button2=ttk.Radiobutton(window,text='no acepto',value='0',variable=selecionado)
button1.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)
button2.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)
Label_anuncio=tkinter.Button(window,text='reset')
Label_anuncio.grid(column=0,row=2,sticky=tkinter.W,padx=5,pady=5)
Label_anuncio.bind('<Button-1>', reset)

window.mainloop()

