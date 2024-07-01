import mysql.connector
print("MySQL Connector Python is installed and imported successfully.")

class Inventario:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (  
                isbn INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                quantity INT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                image VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                year INT
            );
        ''')
        self.conn.commit()

    def agregar_libro(self, isbn, title, quantity, price, image, author, year):
        sql = "INSERT INTO libros (isbn, title, quantity, price, image, author, year) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (isbn, title, quantity, price, image, author, year)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def consultar_libro(self, isbn):
        self.cursor.execute(f"SELECT * FROM libros WHERE isbn = {isbn}")
        return self.cursor.fetchone()

    def modificar_libro(self, isbn, new_title, new_quantity, new_price, new_image, new_author, new_year):
        sql = "UPDATE libros SET title = %s, quantity = %s, price = %s, image = %s, author = %s, year = %s WHERE isbn = %s"
        valores = (new_title, new_quantity, new_price, new_image, new_author, new_year, isbn)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def mostrar_libro(self, isbn):
        libro = self.consultar_libro(isbn)
        if libro:
            print("-" * 40)
            print(f"ISBN: {libro['isbn']}")
            print(f"Título: {libro['title']}")
            print(f"Cantidad: {libro['quantity']}")
            print(f"Precio: {libro['price']}")
            print(f"Imagen: {libro['image']}")
            print(f"Autor: {libro['author']}")
            print(f"Año: {libro['year']}")
            print("-" * 40)
        else:
            print("Producto no encontrado")

    def listar_libro(self):
        self.cursor.execute("SELECT * FROM libros")
        libros = self.cursor.fetchall()
        return libros

    def eliminar_libro(self, isbn):
        self.cursor.execute(f"DELETE FROM libros WHERE isbn = {isbn}")
        self.conn.commit()
        return self.cursor.rowcount > 0

inventario = Inventario(host='localhost', user='root', password='', database='veterinarnia')

# Agregamos productos a la tabla
inventario.agregar_libro(1, 'la biblia', 10, 4500, 'biblia.jpg', 'unknow', 33)
inventario.agregar_libro(2, 'la casa del rio', 10, 4500, 'casa.jpg', 'pastor', 2000)
inventario.agregar_libro(3, 'platero y yo', 10, 2345, 'platero.jpg', 'burro', 1970)
inventario.agregar_libro(4, 'el codigo limpio', 10, 8500, 'codigo.jpg', 'christian', 2000)
inventario.agregar_libro(5, '1984', 5, 2500, '1984.jpg', 'geoge orwel', 1984)
inventario.agregar_libro(6, 'simulacion y simulacro', 15, 52500, 'simulacion.jpg', 'wachovski', 103)

# Consultamos un producto y lo mostramos
codigo_libro = int(input("Ingrese el ISBN del libro: "))
libro = inventario.consultar_libro(codigo_libro)
if libro:
    print(f"Libro encontrado: {libro['isbn']} - {libro['title']}")
else:
    print(f'Libro {codigo_libro} no encontrado.')

# Modificar un libro
inventario.mostrar_libro(1)
inventario.modificar_libro(1, 'la biblia', 10, 4500, 'biblia.jpg', 'unknow', 0)
inventario.mostrar_libro(1)

# Listar libros
libros = inventario.listar_libro()
for libro in libros:
    print(libro)

inventario.eliminar_libro(2)
libros = inventario.listar_libro()
for libro in libros:
    print(libro)
