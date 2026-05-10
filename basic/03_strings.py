### strings ###

my_string = "Hello, World!"
my_other_string = 'Python is great!'    
print(len(my_string))  # Output: 13

print(my_string + " " + my_other_string)  # Concatenación   

my_new_string = "Este es un string\ncon salto de línea"
print(my_new_string)  # Output: Este es un string
                       #         con salto de línea

my_tabbed_string = "Este es un string\tcon tabulación"
print(my_tabbed_string)  # Output: Este es un string    con tabulación

# Formateo de strings

name, age, city = "Alice", 30, "New York"
print(f"My name is {name}, I'm {age} years old and I live in {city}.")  # Output: My name is Alice, I'm 30 years old and I live in New York.
print("My name is %s, I'm %d years old and I live in %s." % (name, age, city))  # Output: My name is Alice, I'm 30 years old and I live in New York.

# desempaquetado de caracteres
lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)  # Output: P   
print(b)  # Output: y
print(c)  # Output: t
print(d)  # Output: h
print(e)  # Output: o
print(f)  # Output: n

# divicion de strings
sentence = "Python is great"
print(sentence)

sentence = sentence[-2]  # Extrae los caracteres desde el índice 1 hasta el índice 3 (excluyendo el índice 4)
print(sentence)  

# reverse de un string
reversed_sentence = sentence[::-1]  # Invierte el string utilizando slicing
print(reversed_sentence)  # Output: taerg si nohtyP

# funciones 
print(sentence.upper())   
print(sentence.lower().isupper())  
print(sentence.split())  
print(sentence.count('o'))  
print(sentence.find('is'))  
print(sentence.replace('great', 'awesome'))  

