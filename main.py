from Backend.modelos.claseProducto import Producto
from Backend.inventario import Inventario

p=Producto("P002", "Lapiz", 10,2,4.00)
inventario=Inventario()
inventario.agregar_producto(p)
inventario.ListarProductos()
producto=inventario.BuscarProductos("codigo","P001")
if producto:
    print(f"Producto encontrado: {producto.nombre} - Stock: {producto.stock}")
"""  
print("Dando de baja tijeras:")
inventario.BajaProducto("P001")
inventario.ListarProductos()
"""
