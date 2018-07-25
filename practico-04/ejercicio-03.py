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

raiz = Tk()
app = Aplicacion(raiz)
app.mainloop()

