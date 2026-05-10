from models.producto import Producto

inventario = []

def agregar_producto(id, nombre, precio, stock): 
    """Agrega un nuevo producto al inventario"""
    producto = Producto(id, nombre, precio, stock)
    inventario.append(producto)

def lista_productos(): 
    """Muestra todos los productos reguistrados"""
    if not inventario:
        print("No hay productos reguistrados")
        return
    for producto in inventario: 
        print(producto)
        