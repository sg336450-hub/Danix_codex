#crear una matriz 3x3 con numeros y mostar  los valores impares y pares de la matriz


 

n, m = map(int,input("Ingrese filas y columnas: ").split())


 

matriz=[]

for i in range(n):

    fila=[]

    while len(fila)<m :

        fila+=list(map(int, input(f"fila {i}: ").split()))

    matriz.append(fila[:m])


 

for fila in matriz:

    print(fila)

# clasificamos los varores

for fila in matriz:

    for valor in fila:

     if valor % 2 == 0:

        print(f"Es par: {valor}")

     else:

        print(f"Es impar: {valor}")


## Crear una matriz con letras y diga cuantas veces esta la a y la b

n, m = map (int,input("Ingrese filas y columnas ").split())

matriz = []
for i in range (n):
    fila = []
    while len (fila)<m:
        fila += input(f"Fila {i}: ").split()
    matriz.append(fila[:m])
#mostrar la matriz
for fila in matriz:
    print(fila)
    
contador_a = 0
contador_b = 0

for fila in matriz:
    for elem in fila:
        if elem == 'a':
            contador_a += 1
        elif elem == 'b':
            contador_b += 1
            
print(f"a esta: {contador_a}")
print(f"b esta: {contador_b}")
 

#crear una matriz 3x3  con edades mostar el proemdio de la matriz principal

n, m = map (int,input("Ingrese filas y columnas ").split())

matriz = []
for i in range (n):
    fila = []
    while len (fila)<m:
        fila += list(map(int, input(f"Fila {i}: ").split()))
    matriz.append(fila[:m])
#mostrar la matriz
for fila in matriz:
    print(fila)
    
suma_total = 0
for fila in matriz:
    suma_total += sum(fila)
    
promedio = suma_total / (n * m)
print(f"\nEl promedio de las edades es: {promedio:.2f}")