import time
import random
from generador_datos import generar_productos
from ordenamientos import quick_sort, merge_sort, insertion_sort
from busquedas import busqueda_binaria, busqueda_lineal_nombre

productos = generar_productos()

# ---------------- ORDENAMIENTO ----------------

print("\n--- ORDENAMIENTO POR PRECIO (ASCENDENTE) ---")

for nombre, algoritmo in [
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort),
    ("Insertion Sort", insertion_sort)
]:
    inicio = time.time()
    algoritmo(productos.copy(), key=lambda x: x.precio)
    fin = time.time()
    print(f"{nombre}: {fin - inicio}")


print("\n--- ORDENAMIENTO POR CALIFICACION (DESCENDENTE) ---")

for nombre, algoritmo in [
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort),
    ("Insertion Sort", insertion_sort)
]:
    inicio = time.time()
    algoritmo(productos.copy(), key=lambda x: x.calificacion_promedio, reverse=True)
    fin = time.time()
    print(f"{nombre}: {fin - inicio}")


# ---------------- BUSQUEDAS ----------------

print("\n--- BUSQUEDA BINARIA ---")

productos_id = sorted(productos, key=lambda x: x.id)

ids_existentes = random.sample(range(1, 51), 10)
ids_no_existentes = [random.randint(51, 100) for _ in range(10)]

inicio = time.time()

for i in ids_existentes:
    busqueda_binaria(productos_id, i)

for i in ids_no_existentes:
    busqueda_binaria(productos_id, i)

fin = time.time()

print("Tiempo total:", fin - inicio)


print("\n--- BUSQUEDA POR NOMBRE ---")

subcadenas = ["lap", "cam", "tec", "xyz", "abc"]

inicio = time.time()

for s in subcadenas:
    busqueda_lineal_nombre(productos, s)

fin = time.time()

print("Tiempo total:", fin - inicio)