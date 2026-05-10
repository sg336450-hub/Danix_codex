### Diccionarios ###
# Un diccionario es una colección de pares clave-valor. Es una estructura de datos que permite almacenar y organizar información de manera eficiente.
# Crear un diccionario
my_dict = dict()  # Crear un diccionario vacío
print(type(my_dict))  # Output: <class 'dict'>

my_other_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(my_other_dict)  # Output: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

my_dict = {
    "nombre": "Ana",
      "edad": 25,
        "ciudad": "Barcelona",
          "lenguaje": {"Python", "JavaScript", "C++"},  
            1:1.77
}

print(my_dict)  # Output: {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Barcelona', 'lenguaje': {'Python', 'JavaScript', 'C++'}}
print(my_other_dict)

print(len(my_dict))  # Output: 4
print(len(my_other_dict))  # Output: 3

print(my_dict["nombre"])  # Output: Ana

my_dict["nombre"] = "Carlos"  # Modificar el valor asociado a la clave "nombre"
print(my_dict["nombre"])  # Output: Carlos

print(my_dict[1])  # Output: 1.77

del my_dict[1]  # Eliminar la clave 1 y su valor asociado
print(my_dict)  # Output: {'nombre': 'Carlos', 'edad': 25, 'ciudad': 'Barcelona', 'lenguaje': {'Python', 'JavaScript', 'C++'}}

print("nombre" in my_dict)  # Output: True
print("Carlos" in my_dict)  # Output: False (Carlos es un valor, no una clave)  

print(my_dict.items())  # Output: dict_items([('nombre', 'Carlos'), ('edad', 25), ('ciudad', 'Barcelona'), ('lenguaje', {'Python', 'JavaScript', 'C++'})])
print(my_dict.keys())  # Output: dict_keys(['nombre', 'edad', 'ciudad', 'lenguaje'])
print(my_dict.values())  # Output: dict_values(['Carlos', 25, 'Barcelona', {'Python', 'JavaScript', 'C++'}])        

my_list = ["nombre", "edad", "ciudad"]

my_new_dict = dict.fromkeys(my_list, "desconocido")  # Crear un nuevo diccionario a partir de una lista de claves
my_new_dict = dict.fromkeys(my_list)  # Crear un nuevo diccionario a partir de una lista de claves sin valores
print(my_new_dict)  # Output: {'nombre': None, 'edad': None, 'ciudad': None}

my_new_dict = dict.fromkeys(my_dict, "space")  # Crear un nuevo diccionario a partir de las claves de otro diccionario
print(my_new_dict)  # Output: {'nombre': 'space', 'edad': 'space', 'ciudad': 'space', 'lenguaje': 'space'}

print(list(my_dict))  # Output: ['nombre', 'edad', 'ciudad', 'lenguaje']  # Convertir las claves del diccionario a una lista
