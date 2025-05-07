from modelos.claseProducto import Producto
from Inventarios.inventario import Inventario

p=Producto("0001", "Tijeras", 100,10,6.00)
inventario=Inventario()
inventario.ListarProductos()
producto=inventario.BuscarProductos("codigo","0001")
if producto:
    print(f"Producto encontrado: {producto.nombre} - Stock: {producto.stock}")