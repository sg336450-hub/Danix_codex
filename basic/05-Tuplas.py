### Tuplas ###

my_tupla = (1, 2, 3, 4, 5)  
print(my_tupla)  # Output: (1, 2, 3, 4, 5)
print(my_tupla[0])  # Output: 1
print(my_tupla[-1])  # Output: 5
# Las tuplas son inmutables, no se pueden modificar después de su creación
# my_tupla[0] = 10  # Esto generará un error
# Las tuplas pueden contener elementos de diferentes tipos de datos
my_tupla_mixta = (1, "Hola", 3.14, [1, 2, 3], (4, 5))
print(my_tupla_mixta)  # Output: (1, 'Hola', 3.14, [1, 2, 3], (4, 5))
# Las tuplas también pueden ser anidadas
tupla_anidada = (1, (2, 3), 4)
print(tupla_anidada[1])  # Output: (2, 3)
# Longitud de una tupla
print(len(my_tupla))  # Output: 5
# Iterar sobre una tupla
for elemento in my_tupla:
    print(elemento)
# Slicing en tuplas
subtupla = my_tupla[1:4]
print(subtupla)  # Output: (2, 3, 4)
