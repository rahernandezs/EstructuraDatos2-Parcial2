class Producto:
    def __init__(self, id, nombre, precio, categoria, stock, calificacion_promedio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.calificacion_promedio = calificacion_promedio

    def __repr__(self):
        return f"{self.id} - {self.nombre} | ${self.precio} | {self.categoria} | Stock: {self.stock} | Rating: {self.calificacion_promedio}"