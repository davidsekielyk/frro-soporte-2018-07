from tkinter import *
from tkinter import font

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
        fuente = font.Font(weight='bold')

        self.etiq1 = Label(self.raiz, text="Primer numero:", font=fuente)
        self.etiq2 = Label(self.raiz, text="Segundo numero:", font=fuente)


        self.ctext1 = Entry(self.raiz)
        self.ctext2 = Entry(self.raiz)

        self.boton1 = Button(self.raiz, text="+", command=self.sumar)
        self.boton2 = Button(self.raiz, text="-", command=self.restar)
        self.boton3 = Button(self.raiz, text="/", command=self.dividir)
        self.boton4 = Button(self.raiz, text="*", command=self.multiplicar)

        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton2.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton3.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton4.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        self.raiz.mainloop()


    def sumar(self):
        resultado = int(self.ctext1.get()) + int(self.ctext2.get())
        print(resultado)
    def restar(self):
        resultado = int(self.ctext1.get()) - int(self.ctext2.get())
        print(resultado)
    def dividir(self):
        if int(self.ctext2.get()) == 0:
            print ("Pero mira si vas a dividir por cero, tonto")
        else:
            resultado = int(self.ctext1.get()) / int(self.ctext2.get())
            print(resultado)
    def multiplicar(self):
        resultado = int(self.ctext1.get()) * int(self.ctext2.get())
        print(resultado)

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
