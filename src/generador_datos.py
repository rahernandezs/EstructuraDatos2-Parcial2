import random
from producto import Producto

def generar_productos(n=50):
    nombres = ["Laptop", "Mouse", "Teclado", "Monitor", "Silla", "Camisa", "Libro", "Balon"]
    categorias = ["Electronica", "Ropa", "Libros", "Hogar", "Deportes"]

    productos = []

    for i in range(1, n + 1):
        nombre = random.choice(nombres) + f" {i}"
        precio = round(random.uniform(10, 2000), 2)
        categoria = random.choice(categorias)
        stock = random.randint(0, 100)
        calificacion = round(random.uniform(1.0, 5.0), 1)

        productos.append(Producto(i, nombre, precio, categoria, stock, calificacion))

    return productos