from tkinter import *
import tkinter as tk
from tkinter import ttk

class Aplicacion(ttk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        raiz.title("Vista de árbol en Tkinter")

        self.treeview = ttk.Treeview(self, columns=("codigo_postal"), selectmode=tk.BROWSE)
        self.treeview.bind("<<TreeviewSelect>>")

        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("codigo_postal", text="Codigo Postal")
        self.treeview.insert("", END, text="Carlos Pellegrini", values=("2453"))
        self.treeview.insert("", END, text="Rosario", values="2000")
        self.treeview.insert("", END, text="Santa Fe", values="3000")
        self.treeview.insert("", END, text="Formosa", values="3600")
        self.treeview.insert("", END, text="Carcaraña", values="2138")
        self.treeview.pack()

        self.pack()
        self.agregar = Button(raiz, text="AGREGAR", command=lambda:self.add()).pack(side=LEFT)
        self.modificar = Button(raiz, text="EDITAR", command=lambda:self.edit()).pack(side=LEFT)
        self.eliminar = Button(raiz, text="ELIMINAR", command=lambda:self.delete()).pack(side=RIGHT)

    def add(self):
        formadd = Tk()
        formadd.geometry("200x200")

        ciudad = Label(formadd, text="Ciudad:")
        textCiudad = Entry(formadd)
        codigo = Label(formadd, text="Codigo Postal:" )
        textCodigo = Entry(formadd)
        botonAceptar = Button(formadd, text="Confirmar", command=lambda:self.agreg(textCiudad.get(),textCodigo.get(),formadd))

        ciudad.pack()
        textCiudad.pack()
        codigo.pack()
        textCodigo.pack()
        botonAceptar.pack()

    def agreg(self,textCiudad,textCodigo,formadd):
        self.treeview.insert("", END, text=textCiudad, values=(textCodigo))
        formadd.destroy()

    def edit(self):
        formedit = Tk()
        formedit.geometry("200x200")

        ciudad = Label(formedit, text="Ciudad:")
        textCiudad = Entry(formedit)
        valor = self.treeview.item(self.treeview.selection(), option="text")
        textCiudad.insert(END,valor)

        codigo = Label(formedit, text="Codigo Postal:" )
        textCodigo = Entry(formedit)
        valor = self.treeview.item(self.treeview.selection(), option="values")
        textCodigo.insert(END,valor)

        botonAceptar = Button(formedit, text="Confirmar", command=lambda:self.modif(textCiudad.get(),textCodigo.get(),formedit))

        ciudad.pack()
        textCiudad.pack()
        codigo.pack()
        textCodigo.pack()
        botonAceptar.pack()

    def modif(self,textCiudad,textCodigo,formedit):
        self.treeview.item(self.treeview.selection(), text=textCiudad)
        self.treeview.item(self.treeview.selection(), values=textCodigo)
        formedit.destroy()

    def delete(self):
        self.treeview.delete(self.treeview.selection())


raiz = Tk()
app = Aplicacion(raiz)
app.mainloop()
