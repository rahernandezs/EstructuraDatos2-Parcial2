import time
import random
from generador_datos import generar_productos
from ordenamientos import quick_sort, merge_sort, insertion_sort
from busquedas import busqueda_binaria, busqueda_lineal_nombre

productos = generar_productos()

print("Cantidad de productos:", len(productos))


# =========================
# ORDENAMIENTOS
# =========================

def medir_tiempo(func, *args, repeticiones=5):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.time()
        func(*args)
        fin = time.time()
        tiempos.append(fin - inicio)
    return sum(tiempos) / len(tiempos)


print("\n--- ORDENAMIENTO POR PRECIO (ASCENDENTE) ---")
print("Quick Sort:", medir_tiempo(quick_sort, productos.copy(), lambda x: x.precio))
print("Merge Sort:", medir_tiempo(merge_sort, productos.copy(), lambda x: x.precio))
print("Insertion Sort:", medir_tiempo(insertion_sort, productos.copy(), lambda x: x.precio))


print("\n--- ORDENAMIENTO POR CALIFICACION (DESCENDENTE) ---")
print("Quick Sort:", medir_tiempo(quick_sort, productos.copy(), lambda x: x.calificacionPromedio, True))
print("Merge Sort:", medir_tiempo(merge_sort, productos.copy(), lambda x: x.calificacionPromedio, True))
print("Insertion Sort:", medir_tiempo(insertion_sort, productos.copy(), lambda x: x.calificacionPromedio, True))


# =========================
# BUSQUEDAS
# =========================

productos_ordenados = sorted(productos, key=lambda x: x.id)

# IDs existentes
ids_existentes = random.sample(range(1, 51), 10)

# IDs inexistentes
ids_inexistentes = [random.randint(100, 200) for _ in range(10)]

inicio = time.time()

for i in ids_existentes:
    busqueda_binaria(productos_ordenados, i)

for i in ids_inexistentes:
    busqueda_binaria(productos_ordenados, i)

fin = time.time()

print("\nBusqueda binaria (20 pruebas):", fin - inicio)


# BÚSQUEDA POR NOMBRE
subcadenas_existentes = ["lap", "cam", "lib", "tec", "mon", "bal", "sil", "mou", "top", "cla"]
subcadenas_inexistentes = ["zzz", "xxx", "qqq", "yyy", "abc", "def", "ghi", "nop", "rst", "uvw"]

inicio = time.time()

for s in subcadenas_existentes:
    busqueda_lineal_nombre(productos, s)

for s in subcadenas_inexistentes:
    busqueda_lineal_nombre(productos, s)

fin = time.time()

print("Busqueda por nombre (20 pruebas):", fin - inicio)