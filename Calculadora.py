class Calculadora:
    """Clase matemática. No usa validaciones 'if' para la división."""
    
    def sumar(self, a, b):
        return a + b
        
    def restar(self, a, b):
        return a - b
        
    def multiplicar(self, a, b):
        return a * b
        
    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: División por cero indefinida."
        
    def porcentaje(self, a, b):
        try: 
            return (a * b) / 100
        except ZeroDivisionError:
            return "Error: División por cero indefinida."


class Menu:
    def __init__(self):
        self.calc = Calculadora()
        
        # Mapeamos las opciones directamente a los métodos correspondientes
        self.operaciones = {
            "1": self.ejecutar_suma,
            "2": self.ejecutar_resta,
            "3": self.ejecutar_multiplicacion,
            "4": self.ejecutar_division,
            "5": self.ejecutar_porcentaje,
            "6": self.salir
        }

    def mostrar_opciones(self):
        print("\n=== MENÚ CALCULADORA (SIN IFs) ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Porcentaje")
        print("6. Salir")
        
    def pedir_numeros(self):
        try:
            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))
            return n1, n2
        except ValueError:
            print("Entrada inválida. Se usarán valores por defecto (0, 0).")
            return 

    # Métodos intermedios para envolver la acción y la lectura de datos
    def ejecutar_suma(self):
        n1, n2 = self.pedir_numeros()
        print(f"Resultado: {n1} + {n2} = {self.calc.sumar(n1, n2)}")

    def ejecutar_resta(self):
        n1, n2 = self.pedir_numeros()
        print(f"Resultado: {n1} - {n2} = {self.calc.restar(n1, n2)}")

    def ejecutar_multiplicacion(self):
        n1, n2 = self.pedir_numeros()
        print(f"Resultado: {n1} * {n2} = {self.calc.multiplicar(n1, n2)}")

    def ejecutar_division(self):
        n1, n2 = self.pedir_numeros()
        print(f"Resultado: {self.calc.dividir(n1, n2)}")
    
    def ejecutar_porcentaje(self): 
        n1, n2 = self.pedir_numeros()
        print(f"Resultado: {n1} % {n2} = {self.calc.porcentaje(n1, n2)}")

    def salir(self):
        print("Saliendo del programa. ¡Hasta luego!")
        raise SystemExit # Termina la ejecución del programa limpiamente sin romper el ciclo manualmente

    def manejar_opcion_invalida(self):
        print("Opción no válida. Intente de nuevo.")

    def ejecutar(self):
        while True:
            self.mostrar_opciones()
            opcion = input("Seleccione una opción (1-6): ")
            
            # Buscamos la función en el diccionario. 
            # Si no existe la opción, devuelve el método de opción inválida por defecto.
            accion = self.operaciones.get(opcion, self.manejar_opcion_invalida)
            accion()

# --- Bloque Principal ---
if __name__ == "__main__":
    interfaz = Menu()
    interfaz.ejecutar()