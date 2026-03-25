# Parcial 2 - Estructura de Datos II

## Proyecto: Rendimiento con Algoritmos de Ordenamiento y Búsqueda en Datos Reales

Este proyecto desarrolla un módulo para la gestión de productos en una tienda en línea, enfocado en analizar el rendimiento de algoritmos de ordenamiento y búsqueda aplicados sobre objetos complejos.

---

## Objetivos

- Modelar productos con atributos reales.
- Implementar algoritmos de ordenamiento sobre objetos.
- Comparar el rendimiento entre distintos algoritmos.
- Aplicar técnicas de búsqueda eficientes.
- Analizar resultados según la teoría de complejidad.

---

## Estructura del Proyecto

```
src/
│── producto.py
│── generador_datos.py
│── ordenamientos.py
│── busquedas.py
│── main.py
```

---

## Funcionalidades

- Generación de 50 productos con datos aleatorios coherentes
- Ordenamiento por precio (ascendente)
- Ordenamiento por calificación (descendente)

Algoritmos de ordenamiento:
- Quick Sort
- Merge Sort
- Insertion Sort

Algoritmos de búsqueda:
- Búsqueda binaria por ID
- Búsqueda lineal por nombre

- Medición de tiempos de ejecución

---

## Ejecución

1. Abrir terminal en la carpeta `src`
2. Ejecutar:

```
python main.py
```

---

## Resultados

- Quick Sort suele ser el más rápido en la práctica.
- Merge Sort mantiene estabilidad.
- Insertion Sort es menos eficiente.

En búsquedas:

- Búsqueda binaria: O(log n)
- Búsqueda lineal: O(n)

---

## Conclusiones

- El rendimiento depende del algoritmo y del tipo de datos.
- O(n log n) es ideal para ordenamiento eficiente.
- La búsqueda binaria es óptima para claves únicas ordenadas.
- La búsqueda por texto requiere estructuras más avanzadas en producción.

---

## Autor

Rances Hernandez