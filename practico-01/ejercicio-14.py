#Ejercicio 14:
print("Ejercicio 14: Programa un algoritmo recursivo que encuentre la salida de un laberinto , \nteniendo en cuenta que el laberinto se tomo como entrada y que es una matriz de valores True , False , (x,y) , \ndonde True indica un obstáculo , False una celda donde se puede caminar , (x,y) es el punto donde comienza a buscarse la salida y (a,b) , la salida del laberinto . \n")

vida = [[True,True,True,True,True,False,True],
          [True,False,True,False,False,False,True],
          [True,False,True,True,True,False,True],
          [True,False,False,False,False,False,True],
          [True,True,True,False,True,True,True],
          [True,False,False,False,False,False,"felicidad"],
          [True,True,True,True,True,True,True]
          ]

vida_de_david = [ [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0]
                  ]

def david_en_busca_de_la_felicidad(a,b):
    print("posicion de david: x =",b+1,"\n                   y =",a+1)
    if vida[a][b] == "felicidad":
        vida_de_david[a][b] =':)'
        for i in range (7):
            print(vida_de_david[i])
        print("\nDAVID HA ALCANZADO LA FELICIDAD ABSOLUTA :)")
        return
    vida_de_david[a][b] = 1
    contador = 0

    c = a
    d = b
    if (not vida[a][b+1] or vida[a][b+1]=="felicidad") and (vida_de_david[a][b+1] == 0):
        contador = contador + 1
        d = b+1
    if (not vida[a][b-1] or vida[a][b-1]=="felicidad") and (vida_de_david[a][b-1] == 0):
        contador = contador + 1
        if d != b+1:
            d = b-1
    if (not vida[a+1][b] or vida[a+1][b]=="felicidad") and (vida_de_david[a+1][b] == 0):
        contador = contador + 1
        if d != b+1 and d != b-1:
            c = a+1
    if (not vida[a-1][b] or vida[a-1][b]=="felicidad") and (vida_de_david[a-1][b] == 0):
        contador = contador + 1
        if d != b+1 and d != b-1 and c != a+1:
            c = a-1
    if contador == 2:
        vida_de_david[a][b] = 2
    if contador == 3:
        vida_de_david[a][b] = 3
    a = c
    b = d

    for i in range (7):
            print(vida_de_david[i])

    if contador == 0:
        for i in range(7):
            for j in range(7):
                if vida_de_david[i][j] > 1:
                    a = i
                    b = j
    print()
    david_en_busca_de_la_felicidad(a,b)

david_en_busca_de_la_felicidad(0,5)


