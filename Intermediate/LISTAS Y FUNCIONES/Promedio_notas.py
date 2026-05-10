"""Ejemplo 2: Promedio de Notas"""
### calcula el promedio de una lista de notas

def calcular_promedio(notas): 
    promedio=sum(notas)/len(notas)
    
    return promedio
    #funcion paara mostrar el resultado

def mostrar_resultado(nombre, materia, promedio): 
    print("\n"+"=" *30)
    print("RESULTADO DEL ESTUDIANTE")
    print("=" *30)
    print(f"NOMBRE: {nombre}" )
    print(f"MATERIA: {materia}")
    print(f"PROMEDIO: {promedio:.2f}")
    print("=" *30)

## entradad de datos
nombre = input("Ingrese el nombre del estudiante: ")
materia = input("Ingrese la materia: ")
#ingrese las notas del estudiante
notas = []
for i in range(1, 6):
    nota = float(input(f"INGRESE LA NOTA {i}: "))
    notas.append(nota)

#calcular el promedio
promedio = calcular_promedio(notas)
#mostrar el resultado
mostrar_resultado(nombre, materia, promedio)


