from services.inventario import agregar_producto, listar_productos

def mostrar_menu():
    print("\n--- SISTEMA DE VENTAS ---")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Salir")


def ejecutar_sistema():
    """Controla el flujo principal del sistema."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            agregar_producto(id, nombre, precio, stock)

        elif opcion == "2":
            listar_productos()

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    ejecutar_sistema()