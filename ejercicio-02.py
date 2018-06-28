from tkinter import *

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Calculadora v2.0")

        self.valores= ""
        self.cuenta = Entry(self.raiz)

        self.num1 = Button(self.raiz, text="1", command=lambda:self.set_cuenta(1))
        self.num2 = Button(self.raiz, text="2", command=lambda:self.set_cuenta(2))
        self.num3 = Button(self.raiz, text="3", command=lambda:self.set_cuenta(3))
        self.num4 = Button(self.raiz, text="4", command=lambda:self.set_cuenta(4))
        self.num5 = Button(self.raiz, text="5", command=lambda:self.set_cuenta(5))
        self.num6 = Button(self.raiz, text="6", command=lambda:self.set_cuenta(6))
        self.num7 = Button(self.raiz, text="7", command=lambda:self.set_cuenta(7))
        self.num8 = Button(self.raiz, text="8", command=lambda:self.set_cuenta(8))
        self.num9 = Button(self.raiz, text="9", command=lambda:self.set_cuenta(9))
        self.num0 = Button(self.raiz, text="0", command=lambda:self.set_cuenta(0))
        self.boton1 = Button(self.raiz, text="+", command=lambda:self.set_cuenta("+"))
        self.boton2 = Button(self.raiz, text="-", command=lambda:self.set_cuenta("-"))
        self.boton3 = Button(self.raiz, text="/", command=lambda:self.set_cuenta("/"))
        self.boton4 = Button(self.raiz, text="*", command=lambda:self.set_cuenta("*"))
        self.boton5 = Button(self.raiz, text="=", command=lambda:self.set_cuenta("="))

        self.cuenta.grid(row=0, column=0, columnspan=4)
        self.num0.grid(row=4, column=0)
        self.num1.grid(row=3, column=0)
        self.num2.grid(row=3, column=1)
        self.num3.grid(row=3, column=2)
        self.num4.grid(row=2, column=0)
        self.num5.grid(row=2, column=1)
        self.num6.grid(row=2, column=2)
        self.num7.grid(row=1, column=0)
        self.num8.grid(row=1, column=1)
        self.num9.grid(row=1, column=2)

        self.boton1.grid(row=1, column=3)
        self.boton2.grid(row=2, column=3)
        self.boton3.grid(row=4, column=3)
        self.boton4.grid(row=3, column=3)
        self.boton5.grid(row=4, column=1, columnspan=2)

        self.raiz.mainloop()

    def set_cuenta(self, valor):
        self.valores = self.valores + str(valor)
        global numero, bandera, operador, resultado, array
        if (len(self.valores) == 1):
            numero = 0
            operador = ""
            array = []
        self.cuenta.insert(END,valor)
        if (type(valor) == int):
            numero = (numero * 10) + valor
        elif (type(valor) != int):
            array.append(numero)
            numero = 0
            if (valor != "="):
                array.append(valor)
                operador = valor
            else:
                for x in range(len(array)):
                    if (array[x] == "*"):
                        res = array[x-1] * array[x+1]
                        del(array[x+1])
                        del(array[x])
                        del(array[x-1])
                        array.insert(x-1, res)
                        array.insert(x-1, "+")
                        array.insert(x-1, 0)
                    elif (array[x]== "/"):
                        res = array[x-1] / array[x+1]
                        del(array[x+1])
                        del(array[x])
                        del(array[x-1])
                        array.insert(x-1, res)
                        array.insert(x-1, "+")
                        array.insert(x-1, 0)
                for x in range(len(array)):
                    if (array[x] == "-"):
                        res = array[x-1] - array[x+1]
                        del(array[x+1])
                        del(array[x])
                        del(array[x-1])
                        array.insert(x-1, res)
                        array.insert(x-1, "+")
                        array.insert(x-1, 0)
                total = 0
                for x in range(len(array)):
                    if (array[x]== "+"):
                        total = total + array[x-1] + array[x+1]
                        del(array[x+1])
                        del(array[x])
                        del(array[x-1])
                        array.insert(x-1, 0)
                        array.insert(x-1, "+")
                        array.insert(x-1, 0)
                print(self.valores, total)
                self.cuenta.delete(0,END)
                self.valores = ""


def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()


