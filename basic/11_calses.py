### Clases ###
class MyNonePersona: # las primeras letras de una clase se escriben en mayuscula
    
    pass 
persona = MyNonePersona()  # Crear una instancia de la clase MyNonePersona


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass
    def walk(self):
        print(f"{self.name} is walking")

    def talk(self): 
        print(f"{self.name} is talking...")

    def get_name(self):
        return self.name


Person1 = Person(input("Enter name: "), int(input("Enter age: ")))
  # Crear una instancia de la clase Person con nombre y edad
print(Person1.get_name())  # Output: Alice
print(Person1.age)   # Output: 30
Person1.walk()  # Output: Alice is walking
Person1.talk()  # Output: Alice is talking...

my_other_person = Person("Bob", 25)  # Crear otra instancia de la clase Person con nombre y edad
print(my_other_person.name)  # Output: Bob
print(my_other_person.age)   # Output: 25
my_other_person.name = "Charlie, el loco del chocolate"  # Modificar el nombre de la instancia my_other_person
print(my_other_person.name)  # Output: Charlie
