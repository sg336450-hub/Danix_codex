

class Producto: 
    """Represeneta un producto del inventario de la tienda"""
    def __init__(self, id, nombre, precio, stock): 
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stok = stock

    def actualizar_stock(self, cantidad): 
        """Actualizar el stock del producto despues de una venta"""
        self.stock -=cantidad
    
    def __str__(self): 
        return f"{self.id}: {self.nombre}: | ${self.precio} | stock: {self.stock}"
    