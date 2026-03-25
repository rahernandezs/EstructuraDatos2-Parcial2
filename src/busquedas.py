def busqueda_binaria(arr, objetivo):
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio].id == objetivo:
            return arr[medio]
        elif arr[medio].id < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


def busqueda_lineal_nombre(arr, texto):
    resultados = []

    for producto in arr:
        if texto.lower() in producto.nombre.lower():
            resultados.append(producto)

    return resultados