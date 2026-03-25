def busqueda_binaria(arr, objetivo_id):
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio].id == objetivo_id:
            return arr[medio]
        elif arr[medio].id < objetivo_id:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


def busqueda_lineal_nombre(arr, subcadena):
    resultados = []
    subcadena = subcadena.lower()

    for producto in arr:
        if subcadena in producto.nombre.lower():
            resultados.append(producto)

    return resultados