#Ejercicio 7

print('Ejercicio 7: Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas).\n')

def es_palindromo(a):
    inv = ""
    for i in a:
        inv = i + inv
    if inv == a:
        return True

a = "radxar"

if es_palindromo(a):
    print("La palabra",a,"es palindromo :)")
else:
    print("La palabra",a,"no es palindromo :(")

assert es_palindromo(a) == True
assert es_palindromo(a) == False
