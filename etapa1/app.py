# Definimos una lista de diccionarios
productos = []

# Agregar un producto (create)

def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):
    
    # Verificamos la existencia del producto (esto no va a ser necesario ya que el codigo sera auto-incremental en la BD)
    if consultar_producto(codigo): # Si encontraste el producto ...
        return False #... salí de la función
    
    nuevo_producto = { # Generamos un diccionario con los datos del producto, cada dato será luego una columna de la tabla de la BD
        'codigo': codigo,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio,
        'imagen': imagen,
        'proveedor': proveedor
    }
    productos.append(nuevo_producto)   #agrego el producto a la lista de diccionarios
    return True # Confirmación de que el producto se agregó ok

def consultar_producto(codigo):
    for producto in productos:   # recorro productos, la lista que almacena todos los productos disponibles en la aplicación. 
        if producto['codigo'] == codigo: #verifica si el valor de la clave 'codigo' en el diccionario del producto coincide con el valor proporcionado en el parámetro codigo
            return producto    #retorno el diccionario con los datos del producto 
    return False # indica que el producto no se encontró
            
# Modificar un producto (update)

def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
    for producto in productos:
        if producto['codigo'] == codigo:  #Si se encuentra un producto con el código coincidente, la función procede a actualizar los valores de sus claves en el diccionario
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            producto['imagen'] = nueva_imagen
            producto['proveedor'] = nuevo_proveedor
            return True   # cuando la modificación fue exitosa
    return False # Cuando el producto no fue encontrado
            
# Listar productos (read)
def listar_productos():
    print("*" * 50)    #separador de ***** para facilitar la lectura por pantalla
    for producto in productos:  #recorro la lista de productos y los imprimo por pantalla
        print(f"Código.......: {producto['codigo']}")
        print(f"Descripción..: {producto['descripcion']}")
        print(f"Cantidad.....: {producto['cantidad']}")
        print(f"Precio.......: {producto['precio']}")
        print(f"Imagen.......: {producto['imagen']}")
        print(f"Proveedor....: {producto['proveedor']}")
        print("*" * 50)
        
        
def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)    #elimino el producto de la lista
            return True
    return False   #si no encontró el código del producto a eliminar
        
        
        
        

# -------------------------------------------------------------------------
# Programa principal

# AGREGAMOS PRODUCTOS
agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500, 'monitor22.jpg', 103)
agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500, 'monitor27.jpg', 104)
agregar_producto(5, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)
agregar_producto(3, 'Parlantes USB', 4, 2500, 'parlantes.jpg', 105) # No se debe agregar porque ese código ya existe.

# for producto in productos:
#     print(producto)
#     print()

# CONSULTAMOS PRODUCTOS
print("Consulto dos productos, el 3 y el 6:")
print(consultar_producto(3)) # Existe
print(consultar_producto(6)) # No Existe

# MODIFICAMOS PRODUCTOS
print("Imprimo el producto 3 antes de modificarlo:")
print(consultar_producto(3)) # Existe
modificar_producto(3, 'Monitor LCD 22 pulgadas', 20, 60000, 'monitor22.jpg', 104)
print("Imprimo el producto 3 después de modificarlo:")
print(consultar_producto(3)) # Existe

listar_productos()

# Eliminamos un producto
print("Eliminamos el producto....")
eliminar_producto(5)

print("Listo los productos luego de haber eliminado el producto 5")
listar_productos()

