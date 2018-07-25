from practico_05.ejercicio_01 import Socio
from practico_06.ejercicio_01 import NegocioSocio

from tkinter import *
import tkinter as tk
from tkinter import ttk

class Aplicacion(ttk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        raiz.title("ABM Socios")

        self.treeview = ttk.Treeview(self, columns=("nombre","apellido","dni"), selectmode=tk.BROWSE)
        self.treeview.bind("<<TreeviewSelect>>")

        self.treeview.heading("#0", text="ID")
        self.treeview.heading("nombre", text="Nombre")
        self.treeview.heading("apellido", text="Apellido")
        self.treeview.heading("dni", text="DNI")

        self.datos = NegocioSocio()

        lp = self.datos.todos()
        for x in lp:
            self.treeview.insert("",END, text=x.idSoci, values=(x.nombre,x.apellido,x.dni))
        self.treeview.pack()

        self.pack()
        self.agregar = Button(raiz, text="Alta", command=lambda:self.add()).pack(side=LEFT)
        self.modificar = Button(raiz, text="Modificacion", command=lambda:self.edit()).pack(side=LEFT)
        self.eliminar = Button(raiz, text="Baja", command=lambda:self.delete()).pack(side=LEFT)

    def add(self):
        formadd = Tk()
        formadd.geometry("200x200")

        id = Label(formadd, text="ID")
        textId = Entry(formadd)
        nombre = Label(formadd, text="Nombre")
        textNombre = Entry(formadd)
        apellido = Label(formadd, text="Apellido")
        textApellido = Entry(formadd)
        dni = Label(formadd, text="DNI")
        textDni = Entry(formadd)
        botonAceptar = Button(formadd, text="Confirmar", command=lambda:self.agreg(textId.get(),textNombre.get(),textApellido.get(),textDni.get(),formadd))

        id.pack()
        textId.pack()
        nombre.pack()
        textNombre.pack()
        apellido.pack()
        textApellido.pack()
        dni.pack()
        textDni.pack()
        botonAceptar.pack()

    def agreg(self,textId,textNombre,textApellido,textDni,formadd):
        ns = Socio()
        ns.idSoci = int(textId)
        ns.nombre = textNombre
        ns.apellido = textApellido
        ns.dni = int(textDni)

        b = self.datos.alta(ns)
        if b[0]:
            self.treeview.insert("", END, text=textId, values=(textNombre,textApellido,textDni))
        else:
            print("\nNo se puede dar de alta")
            print("ERROR:", b[1])

        formadd.destroy()

    def edit(self):
        formedit = Tk()
        formedit.geometry("200x200")

        id = Label(formedit, text="ID")
        textId = Entry(formedit)
        valor = self.treeview.item(self.treeview.selection(), option="text")
        textId.insert(END,valor)

        nombre = Label(formedit, text="Nombre")
        textNombre = Entry(formedit)
        valor = self.treeview.item(self.treeview.selection(), option="values")[0]
        textNombre.insert(END,valor)

        apellido = Label(formedit, text="Apellido")
        textApellido = Entry(formedit)
        valor = self.treeview.item(self.treeview.selection(), option="values")[1]
        textApellido.insert(END,valor)

        dni = Label(formedit, text="DNI")
        textDni = Entry(formedit)
        valor = self.treeview.item(self.treeview.selection(), option="values")[2]
        textDni.insert(END,valor)

        botonAceptar = Button(formedit, text="Confirmar", command=lambda:self.modif(textId.get(),textNombre.get(),textApellido.get(),textDni.get(),formedit))

        id.pack()
        textId.pack()
        nombre.pack()
        textNombre.pack()
        apellido.pack()
        textApellido.pack()
        dni.pack()
        textDni.pack()
        botonAceptar.pack()

    def modif(self,textId,textNombre,textApellido,textDni,formedit):
        vs = Socio()
        vs.idSoci = int(textId)
        vs.nombre = textNombre
        vs.apellido = textApellido
        vs.dni = int(textDni)

        b = self.datos.modificar(vs)
        if b[0]:
            self.treeview.item(self.treeview.selection(), text=textId)
            self.treeview.item(self.treeview.selection(), values=(textNombre,textApellido,textDni))
        else:
            print("\nNo se ha podido modificar el socio")
            print("ERROR:", b[1].args[0])


        formedit.destroy()

    def delete(self):
        id = self.treeview.item(self.treeview.selection(), option="text")
        vs = self.datos.buscar(id)
        b = self.datos.borrar(vs)
        if b[0]:
            self.treeview.delete(self.treeview.selection())
        else:
            print("\nNo se ha podido eliminar el socio")
            print("ERROR:", b[1].args[0])

raiz = Tk()
app = Aplicacion(raiz)
app.mainloop()
