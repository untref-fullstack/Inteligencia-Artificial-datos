class Producto:
    def __init__(self, datos_producto):
        self.codigo = datos_producto["codigo"]
        self.nombre = datos_producto["nombre"]
        self.precio = datos_producto["precio"]
        self.stock = datos_producto["stock"]

    def precio_con_iva(self, iva=21):
        return self.precio * (1 + iva / 100)
    
    def descontar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False