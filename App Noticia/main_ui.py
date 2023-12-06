from noticia import Noticia
from tkinter import *
from tkinter import ttk

def cadastrar():
    print('x')

window = Tk()

titulo = StringVar()
categoria = StringVar()
texto = StringVar()
palavras_chave = StringVar()

Button(window, text='Cadastrar',command=cadastrar).grid(row=0,column=0)
Button(window, text='Buscar',command=cadastrar).grid(row=0,column=1)
Button(window, text='Remover',command=cadastrar).grid(row=0,column=2)
Button(window, text='Limpar',command=cadastrar).grid(row=0,column=3)

Label(window,text='Título ').grid(row=1,column=0)
Entry(window,textvariable=titulo).grid(row=1,column=1)

categorias = ('Entretenimento', 'Esportes', 'Política')
Label(window,text='Categoria ').grid(row=2,column=0)
ttk.Combobox(window,textvariable=categoria,values=categorias).grid(row=2,column=1)

Label(window,text='Palavras-chave (1,2,3) ').grid(row=2,column=3)
Entry(window,textvariable=titulo).grid(row=2,column=4)

Label(window,text='Texto ').grid(row=3,column=0)
Entry(window,textvariable=texto).grid(row=3,column=1)


window.mainloop()