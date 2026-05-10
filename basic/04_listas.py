# Listas en Python
# Las listas son colecciones ordenadas de elementos que pueden ser de diferentes tipos de datos.

# Crear una lista
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)

# Acceder a elementos de una lista
print(mi_lista[0])  # Output: 1
print(mi_lista[-1])  # Output: 5

# Modificar elementos de una lista
mi_lista[0] = 10
print(mi_lista)  # Output: [10, 2, 3, 4, 5]

# Agregar elementos a una lista
mi_lista.append(6)
print(mi_lista)  # Output: [10, 2, 3, 4, 5, 6]

# Eliminar elementos de una lista
mi_lista.remove(2)
print(mi_lista)  # Output: [10, 3, 4, 5, 6]

# Longitud de una lista
print(len(mi_lista))  # Output: 5

# Iterar sobre una lista 
for elemento in mi_lista:
    print(elemento)

# Sublistas (slicing)
sublista = mi_lista[1:4]
print(sublista)  # Output: [3, 4, 5]

# Listas anidadas
lista_anidada = [1, [2, 3], 4]
print(lista_anidada[1])  # Output: [2, 3]

# pop() para eliminar el último elemento de la lista
ultimo_elemento = mi_lista.pop()
print(ultimo_elemento)  # Output: 6
print(mi_lista)  # Output: [10, 3, 4, 5]



