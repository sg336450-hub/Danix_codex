#Crear un algporitmo donde se calcule el
# iva de un producto y el precio final del producto
# con el iva incluido y que  imprima el resultado 
# El iva es del 19%



def calcular_iva(precio): 
    iva = precio * 0.19
    return iva

def calcular_precio_final(precio, iva): 
    precio_final= precio + iva
    return precio_final

def mostrar_recibo(precio, iva, precio_final):
    print("\n"+"=" *30)
    print("RESULTADO DE LA FACTURACION")
    print("=" *30)
    print(f"CLIENTE: {cliente}")
    print(f"PRODUCTO: {producto}")  
    print(f"PRECIO DEL PRODUCTO: {precio:.2f}")
    print(f"IVA: {iva:.2f}")
    print(f"PRECIO FINAL: {precio_final:.2f}")
    print("=" *30)


"""DATOS DE ENTRADA: CONSEPTOS DE FACTURACION"""
cliente= input("Ingrese el nombre del cliente:")
producto = input("Ingrese el nombre del producto:")
precio= float(input("Ingrese el precio del producto:"))
iva= calcular_iva(precio)
precio_final= calcular_precio_final(precio, iva)

mostrar_recibo(precio, iva, precio_final)

