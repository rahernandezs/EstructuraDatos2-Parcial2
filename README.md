# 📊 Parcial 2 - Estructura de Datos II

## 🧠 Proyecto: Rendimiento con Algoritmos de Ordenamiento y Búsqueda en Datos Reales

Este proyecto desarrolla un módulo para la gestión de productos en una tienda en línea, enfocado en analizar el rendimiento de algoritmos de ordenamiento y búsqueda aplicados sobre objetos complejos.

---

## 🎯 Objetivos

- Modelar productos con atributos reales.
- Implementar algoritmos de ordenamiento sobre objetos.
- Comparar el rendimiento entre distintos algoritmos.
- Aplicar técnicas de búsqueda eficientes.
- Analizar resultados según la teoría de complejidad.

---

## 🧱 Estructura del Proyecto

```
src/
│── producto.py
│── generador_datos.py
│── ordenamientos.py
│── busquedas.py
│── main.py
```

---

## ⚙️ Funcionalidades

- Generación de 50 productos con datos aleatorios coherentes
- Ordenamiento por precio (ascendente)
- Ordenamiento por calificación (descendente)

### Algoritmos de ordenamiento implementados:
- Quick Sort
- Merge Sort
- Insertion Sort

### Algoritmos de búsqueda:
- Búsqueda binaria por ID
- Búsqueda lineal por nombre (subcadena)

- Medición de tiempos de ejecución

---

## 🚀 Ejecución

1. Abrir terminal en la carpeta `src`
2. Ejecutar:

```
python main.py
```

---

## 📈 Resultados

- Quick Sort suele ser el más rápido en la práctica.
- Merge Sort mantiene estabilidad en el rendimiento.
- Insertion Sort es menos eficiente en comparación.

En búsquedas:

- La búsqueda binaria es altamente eficiente (O(log n)).
- La búsqueda por nombre es más costosa debido a la comparación de cadenas.

---

## 🧠 Conclusiones

- El rendimiento depende del algoritmo y del tipo de datos.
- Los algoritmos O(n log n) son ideales para ordenamiento eficiente.
- La búsqueda binaria es óptima para claves únicas ordenadas.
- Para búsquedas de texto, en sistemas reales se usan estructuras más avanzadas como índices o árboles de prefijos.

---

## 👨‍💻 Autor

Rances Hernandez