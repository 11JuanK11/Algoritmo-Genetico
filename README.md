# Algoritmo Genético para la Optimización de un Tablero de Ajedrez

## Descripción General

Este proyecto implementa un **algoritmo genético** para optimizar la configuración de un tablero de ajedrez. El objetivo es encontrar una disposición de piezas que coincida exactamente con una configuración objetivo, en este caso, la posición inicial de un tablero de ajedrez estándar.

Dado que la generación inicial del tablero es aleatoria, el algoritmo evoluciona mediante **selección, cruce y mutación** hasta alcanzar la configuración deseada. La visualización de la evolución del proceso se realiza mediante una interfaz gráfica con **Tkinter**.

## Funcionalidades

- Generación aleatoria de tableros de ajedrez como población inicial.
- Evaluación de la similitud de cada tablero con la configuración objetivo.
- Aplicación de operadores genéticos de **cruce** y **mutación** para mejorar las soluciones.
- Visualización del proceso evolutivo mediante **Tkinter**.

## Instalación y Ejecución

### Prerrequisitos

Asegúrate de tener instalado **Python 3.x** en tu sistema.

### Instalación de Dependencias

Ejecuta el siguiente comando para instalar las librerías necesarias:

```bash
pip install tk
```

### Ejecución del Proyecto

Para ejecutar la aplicación, simplemente corre el siguiente comando en la terminal:

```bash
python main.py
```

## Funcionamiento del Algoritmo

### Función Objetivo

La función objetivo mide cuántas casillas de un tablero generado coinciden con la configuración del tablero objetivo. Se calcula de la siguiente manera:

$$
f(x) = \sum_{i=0}^{7} \sum_{j=0}^{7} \delta (individuo[i][j], destino[i][j])
$$

donde \(\delta(x, y)\) es 1 si \(x = y\) y 0 en caso contrario.

### Población y Representación del Cromosoma

Cada individuo en la población es un **tablero de ajedrez de 8x8**, representado como una matriz donde cada casilla puede contener una pieza de ajedrez o estar vacía.

### Operadores Genéticos

- **Cruce:** Se selecciona un área aleatoria de 3x3 en el tablero y se reemplaza con la configuración objetivo.
- **Mutación:** Se selecciona aleatoriamente una región de 2x2 y se reemplaza con nuevas piezas aleatorias para introducir diversidad.

## Tecnologías Utilizadas

- **Python** para la implementación del algoritmo.
- **Tkinter** para la visualización de la evolución del tablero.
- **Random y Copy** para la manipulación de datos y generación aleatoria.

## Contribución

Si deseas mejorar el proyecto, sigue estos pasos:

1. Realiza un **fork** del repositorio.
2. Crea una nueva rama con tu mejora: `git checkout -b mi-mejora`.
3. Realiza tus cambios y haz un commit: `git commit -m "Agrega nueva funcionalidad"`.
4. Sube tus cambios: `git push origin mi-mejora`.
5. Abre un **pull request** para su revisión.

## Licencia

Este proyecto está bajo la licencia **MIT**. Puedes usarlo y modificarlo libremente.

---

**Autor:** Juan Camilo Alzate Bedoya]  

