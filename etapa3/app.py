import mysql.connector   

# abrir XAMPP
# en  phpMyAdmin crear la BD miapp

class Catalogo:
#el constructor init Inicializa una instancia de Catalogo y crea una conexión a la base de datos
#usa el metodo connect al que le paso los datos del host, user, password y base de datos y se conecta con la BD
    def __init__(self, host, user, password, database):
                        
        self.conn = mysql.connector.connect(  # pág 19 - "conector" es conjunto de herramientas o una biblioteca que facilita la interacción entre Python y la BD
            host=host,
            user=user,
            password=password,
            database=database
        )

        # El cursor actúa como un intermediario entre tu programa Python y la base de datos MySQL. 
        # # Permite ejecutar comandos SQL (como SELECT, INSERT, UPDATE, DELETE) desde Python
        #el cursor por defecto trabaja con tuplas, pero nosotros vamos a trabajar con diccionarios
        self.cursor = self.conn.cursor(dictionary=True)  #el cursor se configura para que devuelva valores como diccionarios, el cursor va a ejecutar las sentencias sql
        
        # creamos la tabla automáticamente desde python, si no existiere
        # el codigo es auto incremental entonces evitamos el ingreso de duplicados
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (  
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(4))''')
        
        #con el commit confirmamos la operación 
        #el conn es una instancia del objeto my sql connector propia de esa libreria , este objeto maneja la conexión con la base de datos my sql
        self.conn.commit()  
    
    #ya no pasamos el codigo porque será auto-incremental:
    #el diccionario que teníamos en el ejemplo anterior es reemplazado por el insert    
    def agregar_producto(self, descripcion, cantidad, precio, imagen, proveedor):
       #en la variable sql se construye una consulta SQL que inserta una nueva fila en la tabla productos
        sql = "INSERT INTO productos (descripcion, cantidad, precio, imagen_url, proveedor) VALUES (%s, %s, %s, %s, %s)" #Los %s se reemplazan por los valores que pasamos al llamar el metodo
        valores = (descripcion, cantidad, precio, imagen, proveedor)
        self.cursor.execute(sql,valores)  #La base de datos guarda el nuevo producto en la tabla productos
        self.conn.commit()  #Se confirma la transacción
        return self.cursor.lastrowid   #retornamos el id del ultimo registro insertado en la tabla productos, o sea, el codigo del producto

    def consultar_producto(self, codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()    #el cursor obtiene una sola fila del resultado de la consulta,retorna un diccionario con la información del producto consultado

    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        sql = "UPDATE productos SET descripcion = %s, cantidad = %s, precio = %s, imagen_url = %s, proveedor = %s WHERE codigo = %s"   #pongo where sino pisa todos los productos
        valores = (nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor, codigo)  #valores es una tupla

        self.cursor.execute(sql, valores)  # ejecuto la consulta a la base de datos (execute es metodo del cursor)
        self.conn.commit()                 # confirmo la operación
        return self.cursor.rowcount > 0    # devuelve cuántas filas fueron afectadas por la modificación
    
    def mostrar_producto(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_producto(codigo)  #trae el producto en forma de diccionario
        if producto:
            print("-" * 40)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")

    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()   #fetch all es un metodo que trae todas las filas de la tabla, lista de diccionarios
        return productos

    def eliminar_producto(self, codigo):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()               # confirmo
        return self.cursor.rowcount > 0  # devuelve cuántas filas fueron afectadas por la modificación

# Programa principal (inicializo el catálogo)
catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')

# Agregamos productos a la tabla
catalogo.agregar_producto('Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
catalogo.agregar_producto('Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
catalogo.agregar_producto('Monitor LED', 5, 25000, 'monitor.jpg', 102)

# Consultamos un producto y lo mostramos
cod_prod = int(input("Ingrese el código del producto: "))
producto = catalogo.consultar_producto(cod_prod)
if producto:
    print(f"Producto encontrado: {producto['codigo']} - {producto['descripcion']}")
else:
    print(f'Producto {cod_prod} no encontrado.')

# Modificar un producto
catalogo.mostrar_producto(10)
catalogo.modificar_producto(10, 'Teclado mecánico', 20, 35000, 'teclado2.jpg', 102)
catalogo.mostrar_producto(10)

# Listar productos
productos = catalogo.listar_productos()
for producto in productos:  # recorro la lista de productos
    print(producto)         # imprimo el diccionario

catalogo.eliminar_producto(8)
productos = catalogo.listar_productos()
for producto in productos:
    print(producto)
