### funciones ###

def my_funcion (): 
    print("hola, soy una función")

my_funcion()  # Llamar a la función para ejecutarla

def sum_tow_values (a, b):
    return a + b 
    

result = sum_tow_values(5, 10)  # Llamar a la función con argumentos y almacenar el resultado
print(result)  # Output: 15

def print_full_name (name, surname, alias):
    full_name = name + " " + surname + " " + alias
    return full_name    


full_name_result = print_full_name("Stiven", "Daniel", "Cheo")  # Llamar a la función con argumentos y almacenar el resultado

print(full_name_result)  # Output: Stiven Daniel Cheo

def print_texts (*texts):
    for text in texts:
        print(text)

print_texts("Hola", "¿Cómo estás?", "¡Bienvenido a Python!")  # Llamar a la función con múltiples argumentos
print_texts("Python", "es", "genial")
