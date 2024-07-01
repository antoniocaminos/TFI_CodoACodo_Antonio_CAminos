# Definimos una lista de diccionarios
class Inventario:

    libros = []

    # Agregar un producto (create)

    def agregar_libro(self, isbn, title, quantity, price, image, author, year):
        # Verificamos la existencia del producto (esto no va a ser necesario ya que el codigo sera auto-incremental en la BD)
        if self.consultar_libro(isbn): # Si encontraste el producto ...
            return False #... salí de la función
        
        nuevo_libro = { # Generamos un diccionario con los datos del producto, cada dato será luego una columna de la tabla de la BD
            'isbn': isbn,
            'title':title,
            'quantity': quantity,
            'price': price,
            'image': image,
            'author': author,
            'year': year
        }
        self.libros.append(nuevo_libro)   #agrego el producto a la lista de diccionarios
        return True # Confirmación de que el producto se agregó ok

    def consultar_libro(self, isbn):
        for libro in self.libros:   # recorro productos, la lista que almacena todos los productos disponibles en la aplicación. 
            if libro['isbn'] == isbn: #verifica si el valor de la clave 'codigo' en el diccionario del producto coincide con el valor proporcionado en el parámetro codigo
                return libro    #retorno el diccionario con los datos del producto 
        return False # indica que el producto no se encontró
                
    # Modificar un producto (update)

    def modificar_libro(self, isbn, new_title, new_quantity, new_price,new_image, new_author, new_year):
        for libro in self.libros:
            if  libro['isbn'] == isbn:  #Si se encuentra un producto con el código coincidente, la función procede a actualizar los valores de sus claves en el diccionario
                libro['title'] = new_title
                libro['quantity'] = new_quantity
                libro['price'] = new_price
                libro['image'] = new_image
                libro['author'] = new_author
                libro['year'] = new_year
                return True   # cuando la modificación fue exitosa
        return False # Cuando el producto no fue encontrado
                
    # Listar productos (read)
    def listar_libros(self):
        print("*" * 50)    #separador de ***** para facilitar la lectura por pantalla
        for libro in self.libros:  #recorro la lista de productos y los imprimo por pantalla
            print(f"Código.......: {libro['isbn']}")
            print(f"Titulo.......: {libro['title']}")
            print(f"Cantidad.....: {libro['quantity']}")
            print(f"Precio.......: {libro['price']}")
            print(f"Tapa.........: {libro['image']}")
            print(f"Autor........: {libro['author']}")
            print(f"Año..........: {libro['year']}")
            print("*" * 50)
            
            
    def eliminar_libro(self, isbn):
        for libro in self.libros:
            if libro['isbn'] == isbn:
                self.libros.remove(libro)    #elimino el producto de la lista
                return True
        return False   #si no encontró el código del producto a eliminar

    def mostrar_libro(self, isbn):
        libro = self.consultar_libro(isbn)
        if libro:
            print("*" * 50)
            print(f"Código.......: {libro['isbn']}")
            print(f"Titulo.......: {libro['title']}")
            print(f"Cantidad.....: {libro['quantity']}")
            print(f"Precio.......: {libro['price']}")
            print(f"Tapa.........: {libro['image']}")
            print(f"Autor........: {libro['author']}")
            print(f"Año..........: {libro['year']}")
            print("*" * 50)
        else:
            print(f'El libro {isbn} no existe')

# -------------------------------------------------------------------------
# Programa principal
inventario = Inventario()

# AGREGAMOS PRODUCTOS(isbn, title, quantity, price, image, author, year):
inventario.agregar_libro(1, 'la biblia', 10, 4500, 'biblia.jpg', 'unknow', 33)
inventario.agregar_libro(2, 'la casa del rio', 10, 4500, 'casa.jpg', 'pastor', 2000)
inventario.agregar_libro(3, 'platero y yo', 10, 2345, 'platero.jpg', 'burro', 1970)
inventario.agregar_libro(4, 'el codigo limpio', 10, 8500, 'codigo.jpg', 'christian', 2000)
inventario.agregar_libro(5, '1984', 5, 2500, '1984.jpg', 'geoge orwel', 1984)
inventario.agregar_libro(6, 'simulacion y simulacro', 15, 52500, 'simulacion.jpg', 'wachovski', 103)

# for producto in productos:
#     print(producto)
#     print()

# CONSULTAMOS PRODUCTOS
print("Consulto un producto que existe y uno que no existe:")
print(inventario.consultar_libro(1)) # Existe
print(inventario.consultar_libro(9)) # No Existe

# MODIFICAMOS PRODUCTOS
print("Modifico un producto que existe y lo vuelvo a consultar:")
inventario.modificar_libro(1, 'la biblia', 100, 4500, 'biblia.jpg', 'unknow', 33)
print(inventario.consultar_libro(1)) # Existe

#LISTAMOS LIBROS
print("Listo los libros")
inventario.listar_libros()

#ELIMINAR LIBRO
inventario.eliminar_libro(3)
print("Elimino un producto y listo los productos:")
inventario.listar_libros()

#MOSTRAR UN LIBRO
print("Muestro un Libro que no existe y uno que existe:")
inventario.mostrar_libro(10)
inventario.mostrar_libro(2)
""" 
inventario.modificar_libro(3, 'platero y yo', 12, 2345, 'platero.jpg', 'burro', 1971)
print("Imprimo el producto 3 después de modificarlo:")
print(consultar_libro(3)) # Existe

listar_libros()

# Eliminamos un producto
print("Eliminamos el producto....")
eliminar_libro(5)

print("Listo los productos luego de haber eliminado el producto 5")
listar_libros() """

