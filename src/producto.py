class Producto:
    def __init__(self, id, nombre, precio, categoria, stock, calificacionPromedio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.calificacionPromedio = calificacionPromedio

    def __repr__(self):
        return f"{self.id} - {self.nombre} | ${self.precio} | {self.categoria} | Stock: {self.stock} | Rating: {self.calificacionPromedio}"