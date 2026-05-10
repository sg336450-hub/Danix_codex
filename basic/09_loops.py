### loops(bucles) ###

# while
 
my_number = 0
 
while my_number < 10:
    print(my_number)
    my_number += 2  # Incrementar el valor de my_number en 1 en cada iteración

else:
    print("my_number no ha alcanzado el valor de 10")

print("Bucle while continuado")

while my_number < 20:
    print(my_number)
    my_number += 1  # Incrementar el valor de my_number en 1 en cada iteración  
    
    if my_number == 15:
        print("Se detiene el bucle en 15")
        break  # Detener el bucle cuando my_number alcance el valor de 15


    print(my_number)


print("Bucle while continuado")


# for

my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)

my_tuple = (10, 20, 30, 40, 50)

for element in my_tuple:
    print(element)  

my_set = {100, 200, 300, 400, 500}

for element in my_set:
    print(element)  



my_dict = {"a": 1, "b": 2, "c": 3}

for value in my_dict.values():
    print(value)  # Imprime los valores del diccionario

    if value == 2:
        print("Continual la ejecucion del bucle for")
        continue  # Saltar a la siguiente iteración del bucle cuando se alcance el valor 2  
    
else:
    print("el bucle for para mi diccionario ha terminado")

print("Bucle for continuado")

    



 