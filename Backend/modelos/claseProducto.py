class Producto:
    def __init__(self, codigo, nombre, stock, stock_minimo, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock
        self.stock_minimo = stock_minimo
        self.precio = precio
        
    def __str__(self):
        return f"{self.codigo} - {self.nombre} | Stock: {self.stock} | Mínimo: {self.stock_minimo}"