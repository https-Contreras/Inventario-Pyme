from Backend.inventario import Inventario



def prueba_productos():
    productos = Inventario.obtener_lista_productos()
    for f in productos:
        print(f)
    
    
    
if __name__=="__main__":
    prueba_productos()