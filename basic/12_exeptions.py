### exceptions handling (manejo de errores) ###
numberOne = 5
numberTwo = 10
numberTwo = "5"  # Esto generará un error de tipo de dato (TypeError)
#numberTwo = 5  # Esto corregirá el error de tipo de dato

try: 
    print(numberOne + numberTwo)  # Intentar realizar la suma
    print("La suma se realizó correctamente")  # Si la suma se realiza sin errores, imprimir este mensaje
except TypeError:  # Capturar el error de tipo de dato
    print("Error: No se pueden sumar un número y una cadena de texto")  # Imprimir un mensaje de error personalizado
else: # Si no se produce ningún error, ejecutar este bloque
    print("La ejecucion continúa sin problemas")
finally: 
    print("Este bloque se ejecutará siempre, haya o no errores")  # Este bloque se ejecutará siempre, haya o no errores 


# excepciones por tipo de dato
try: 
    print(numberOne + numberTwo)  # Intentar realizar la suma
except TypeError:  # Capturar el error de tipo de dato
    print("Se ha producido un TypeError")  # Imprimir un mensaje de error personalizado
except ValueError:  # Capturar el error de tipo de dato
    print("se ha producido un ValueError")  # Imprimir un mensaje de error personalizado
    

# capturar cualquier tipo de error

try: 
    print(numberOne + numberTwo)  # Intentar realizar la suma   
    print("No se ha producido ningún error")  # Si la suma se realiza sin errores, imprimir este mensaje
except Exception as error:  # Capturar cualquier tipo de error y almacenar el error en la variable 'e'
    print(f"Se ha producido un error: {error}")  # Imprimir un mensaje de error personalizado con el mensaje del error original
except ValueError as error:  # Capturar cualquier tipo de error sin almacenar el error en una variable
    print(f"Se ha producido un error de tipo ValueError: {error}")  # Imprimir un mensaje de error genérico con el mensaje del error original
