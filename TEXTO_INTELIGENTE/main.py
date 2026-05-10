"""
procesador de texto inteligente
-contar el numero de palabras
-contar el numero de vocales
-elimina las vocales del texto
-cuenta la frecuencia de cada palabra
###-elimina signos de puntuacion
###-identifica y cuenta los tipos de caracteres
###-estadisticas de texto NPL(procesamiento de lenguaje)
"""

import string

def contar_palabras(texto): 
    palabras = texto.split()
    return len(palabras)

def contar_vocales(texto): 
    
    contador = 0

    for letra in texto.upper(): 
        if letra in "AEIOU": 
            contador += 1
        
    return contador

def eliminar_vocales(texto): 
    resultado = ""

    for letra in texto: 
        if letra.upper() in "AEIOU": 
            continue

        resultado += letra


    return resultado

def frecuencia_palabras(texto): 
    palabras = texto.lower().split() #todo en minusculas
    conteo = {}

    for palabra in palabras: 
        if palabra in conteo: 
            conteo[palabra] += 1
        else: 
            conteo[palabra] = 1


    return conteo 

def limpiar_texto(texto): 
    texto = texto.lower() # todo en minuscula
    texto = texto.translate(str.maketrans('', '', string.punctuation))


def filtrar_palabras(palabras): 
    stop_words = set(["el", "la", "los", "las", "un", "una", "unos", "unas", "y", "o", "de", "a", "en"])
    return [p for p in palabras if p not in stop_words]

def procesar_texto(texto): 
    texto = limpiar_texto(texto) ### limpiar signos de puntuacion y minusculas
    palabras = texto.split()     ### divide en palabras
    palabras = filtrar_palabras(palabras)    ### flitrar stopwords
    texto_final = " ".join(palabras)   ### unir palabras filtradas

    return texto_final



# entrada de datos
texto = input("Ingrese un texto: ")


# proceso
num_palabras = contar_palabras(texto)
num_vocales = contar_vocales(texto)
texto_sin_vocales = eliminar_vocales(texto)
frecuencia = frecuencia_palabras(texto)
texto_procesado = procesar_texto(texto)

# resultado

print("\n---RESULTADO---")
print(f"Numero de palabras: {num_palabras}")
print(f"Numero de vocales: {num_vocales}")
print(f"Texto sin vocales: {texto_sin_vocales}")
print("\nfrecuencia de palabras:")
for palabra, cantidad in sorted(frecuencia.items(), key=lambda x: x[1], reverse=True):
    print(f"{palabra}: {cantidad}")
print(f"Texto procesado: {texto_procesado}")



