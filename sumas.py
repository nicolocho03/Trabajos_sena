import numpy as np
import random
#Ejercicio 1
lista = [3,5,7,9,11]

suma = sum(lista)

print("La suma de lista es:", suma)

#Ejercicio 2
lista1 = [1,2,3]
lista2 = [4,5,6]

suma_listas = [x+y for x,y in zip(lista1,lista2)]

print("La suma de las listas es: ", suma_listas)

#Ejercicio 3
a=1
b=5 

sumar_rango = sum(range(a,b + 1))


print(f"La suma de los numeros entre {a} y {b} es:", sumar_rango)

#Ejercicio 4 

numero=1234 

suma_digitos = sum(int(digito) for digito in str(numero))

print("La suma de los digitos es:", suma_digitos)

#Ejercicio 5 
lista = [1,2,2,3,4,4,5]

elemento_unicos = set(lista)

suma_unicos = sum(elemento_unicos)

print("La suma de los elementos unicos es:", suma_unicos)

#Ejercicio 6 

matriz1 = np.array([[1,2], [3,4]])
matriz2 = np.array([[5,6], [7,8]])
suma_matrices = np.add(matriz1, matriz2)
print("La suma de las matrices es", suma_matrices)

#Ejercicio 7
n=10

numeros_aleatorios = [random.randint(1,100) for _ in range(n)]
suma_aleatorios = sum(numeros_aleatorios)
print("La suma de los numeros aleatorios es:", suma_aleatorios)

#Ejercicio 8 

def suma_numeros_naturales(n):
    if n == 1:
        return 1
    else: 
        return n + suma_numeros_naturales(n - 1)

n = 10

suma_n = suma_numeros_naturales(n)

print(f"La suma de los primeros {n} numeros naturales es:", suma_n)

#Ejercicio 9

lista_anidada = [1, [2, 3], [4, [5, 6]], 7]

def suma_lista_anidada(lista):
    suma = 0
    for elemento in lista:
        if isinstance(elemento, list):
            suma += suma_lista_anidada(elemento)
        else:
            suma += elemento
    return suma

suma_anidada = suma_lista_anidada(lista_anidada)

print("La suma de los números en la lista anidada es:", suma_anidada)

#Ejercicio 10 

diccionario = {'a': 10, 'b': 20, 'c': 30}

suma_valores = sum(diccionario.values())

print("La suma de los valores en el diccionario es:", suma_valores)

#Ejercicio 11

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def suma_primos_menores_que(n):
    suma = 0
    for i in range(2, n):
        if es_primo(i):
            suma += i
    return suma

n = 10

suma_primos = suma_primos_menores_que(n)

print(f"La suma de todos los números primos menores que {n} es:", suma_primos)

#Ejercicio 12 
# Matriz cuadrada de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Inicializamos las sumas de las diagonales
suma_diagonal_principal = 0
suma_diagonal_secundaria = 0
n = len(matriz)

# Iteramos sobre la matriz
for i in range(n):
    suma_diagonal_principal += matriz[i][i]
    suma_diagonal_secundaria += matriz[i][n - 1 - i]

# Imprimir el resultado
print(f"La suma de los elementos en la diagonal principal es:", suma_diagonal_principal)
print(f"La suma de los elementos en la diagonal secundaria es:", suma_diagonal_secundaria)
#Ejercicio 13 
def suma_serie_cuadrados(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i**2
    return suma

# Número dado
n = 5

# Calcular la suma de la serie
suma_serie = suma_serie_cuadrados(n)

# Imprimir el resultado
print(f"La suma de la serie 1^2 + 2^2 + ... + {n}^2 es:", suma_serie)
#Ejercicio 14 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función recursiva para sumar los valores de los nodos
def suma_nodos(arbol):
    if arbol is None:
        return 0
    return arbol.valor + suma_nodos(arbol.izquierda) + suma_nodos(arbol.derecha)

# Ejemplo de árbol binario
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)

# Calcular la suma de todos los nodos
suma_arbol = suma_nodos(raiz)

# Imprimir el resultado
print("La suma de todos los nodos del árbol es:", suma_arbol)

#Ejercicio 15 

# Matriz dispersa de ejemplo
matriz_dispersa = [
    [0, 0, 3],
    [0, 0, 0],
    [2, 0, 0]
]

# Inicializamos la suma
suma_no_nulos = 0

# Iteramos sobre la matriz
for fila in matriz_dispersa:
    for elemento in fila:
        if elemento != 0:
            suma_no_nulos += elemento

# Imprimir el resultado
print("La suma de todos los elementos no nulos en la matriz dispersa es:", suma_no_nulos)
