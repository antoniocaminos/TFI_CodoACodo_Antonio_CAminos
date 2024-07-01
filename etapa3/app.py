import mysql.connector
from decimal import Decimal

class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,4
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def limpiar_tabla_animales(self):
        self.cursor.execute("DELETE FROM animales")
        self.conn.commit()

    def agregar_animal(self, nombre, especie, edad, peso, imagen, dueño):
        sql = "INSERT INTO animales (nombre, especie, edad, peso, imagen, dueño) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombre, especie, edad, peso, imagen, dueño)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def consultar_animal(self, codigo):
        self.cursor.execute("SELECT * FROM animales WHERE codigo = %s", (codigo,))
        return self.cursor.fetchone()

    def modificar_animal(self, codigo, nuevo_nombre, nueva_especie, nueva_edad, nuevo_peso, nueva_imagen, nuevo_dueño):
        sql = "UPDATE animales SET nombre = %s, especie = %s, edad = %s, peso = %s, imagen = %s, dueño = %s WHERE codigo = %s"
        valores = (nuevo_nombre, nueva_especie, nueva_edad, nuevo_peso, nueva_imagen, nuevo_dueño, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def mostrar_animal(self, codigo):
        animal = self.consultar_animal(codigo)
        if animal:
            print("-" * 40)
            print(f"Código.....: {animal['codigo']}")
            print(f"Nombre.....: {animal['nombre']}")
            print(f"Especie....: {animal['especie']}")
            print(f"Edad.......: {animal['edad']}")
            print(f"Peso.......: {animal['peso']} kg")
            print(f"Imagen.....: {animal['imagen']}")
            print(f"Dueño......: {animal['dueño']}")
            print("-" * 40)
        else:
            print(f"Animal {codigo} no encontrado.")

    def listar_animales(self):
        self.cursor.execute("SELECT * FROM animales")
        animales = self.cursor.fetchall()
        return animales

    def eliminar_animal(self, codigo):
        self.cursor.execute("DELETE FROM animales WHERE codigo = %s", (codigo,))
        self.conn.commit()
        return self.cursor.rowcount > 0

if __name__ == "__main__":
    # Programa principal (inicializo el catálogo)
    catalogo = Catalogo(host='localhost', user='root', password='', database='veterinaria')

    # Limpiamos la tabla de animales para iniciar desde cero
    catalogo.limpiar_tabla_animales()

    # Agregamos animales a la tabla y guardamos los códigos de los animales
    cod_animal1 = catalogo.agregar_animal('Luna', 'Perro', 3, Decimal('15.5'), 'luna.jpg', 'Carlos')
    cod_animal2 = catalogo.agregar_animal('Mia', 'Gato', 2, Decimal('4.2'), 'mia.jpg', 'Ana')
    cod_animal3 = catalogo.agregar_animal('Max', 'Perro', 5, Decimal('20.0'), 'max.jpg', 'Luis')

    # Consultamos un animal y lo mostramos
    cod_animal = int(input("Ingrese el código del animal: "))
    animal = catalogo.consultar_animal(cod_animal)
    if animal:
        print(f"Animal encontrado: {animal['codigo']} - {animal['nombre']}")
        catalogo.mostrar_animal(cod_animal)
    else:
        print(f'Animal {cod_animal} no encontrado.')

    # Modificar un animal
    catalogo.modificar_animal(cod_animal1, 'Luna', 'Perro', 4, Decimal('16.0'), 'luna.jpg', 'Carlos')
    catalogo.mostrar_animal(cod_animal1)

    # Listar animales después de realizar las operaciones
    print("Listado de animales:")
    animales = catalogo.listar_animales()
    for animal in animales:
        print(animal)

    # Eliminar un animal
    catalogo.eliminar_animal(cod_animal2)
    print("Animales después de eliminar:")
    animales = catalogo.listar_animales()
    for animal in animales:
        print(animal)
