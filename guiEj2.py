import tkinter
from tkinter import ttk
window=tkinter.Tk()
lista=['operaciones','resultados','notas','ajustes']
listbox=tkinter.Listbox(window)
for i in lista:
    listbox.insert(tkinter.END,i)
listbox.pack()
label_anuncio=tkinter.Label(window,text="Opcion de Configuracion")
label_anuncio.pack()


window.mainloop()