### stes ###
# Conjuntos (Sets)
# Un conjunto es una colección no ordenada de elementos únicos. Se definen utilizando llaves {} o la función set().
# Crear un conjunto
mi_conjunto = {1, 2, 3, 4, 5}
print(mi_conjunto)  # Output: {1, 2, 3, 4, 5}
# Crear un conjunto a partir de una lista (elimina duplicados)
conjunto_desde_lista = set([1, 2, 2, 3, 4])
print(conjunto_desde_lista)  # Output: {1, 2, 3


my_set = set()
my_other_set = {}
print (type(my_set))  # Output: <class 'set'>  
print (type(my_other_set))  # Output: <class 'dict'>




my_other_set = {"brain", "is", "awesome", 35}
print(type(my_other_set))  # Output: <class 'set'>

len(my_other_set)  # Output: 4
print(len(my_other_set))  # Output: 4

### print(my_other_set[2]) error: 'set' object is not subscriptable

my_other_set.add("python") ## un set no es una estructura ordenada, por lo que no se pueden agregar elementos

print(my_other_set)  # un set no admite elementos duplicados, por lo que no se agregará "awesome" nuevamente

my_other_set.add("python")

print(my_other_set)  

print("python" in my_other_set)  # Output: True
print("java" in my_other_set)    # Output: False


my_other_set.remove("awesome")  # Elimina el elemento "awesome" del conjunto
print(my_other_set)  # Output: {'python', 'is', 35, 'brain'}

my_other_set  # Elimina el elemento "python" del conjunto si existe
print(len(my_other_set))
print(my_other_set.isdisjoint(my_other_set))  # Output: {'is', 35, 'brain'}

del my_other_set  # Elimina el conjunto completo
# print(my_other_set)  # Esto generará un error porque el conjunto ha sido eliminado

my_set = {"brain", "is", "awesome", 35}
my_list = list(my_set)  # Convertir el conjunto a una lista
print(my_list)  # Output: ['brain', 'is', 'awesome', 35]

my_other_set = {"kolin", "lincon", "python", 35}

my_new_set = my_set.union(my_other_set).union({"javaScript"})  # Unión de conjuntos
print(my_new_set)  # Output: {'kolin', 'lincon', 'python
print(my_set.difference(my_other_set))  # Output: {35} Intersección de conjuntos