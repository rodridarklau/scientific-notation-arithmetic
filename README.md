<div align="center">

# Aritmética en notación científica

### Representación numérica y operaciones elementales en Python

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Área](https://img.shields.io/badge/Área-Computación%20numérica-blue?style=flat-square)

</div>

## Descripción

Ejercicio académico que representa números mediante coeficiente, base y exponente, y realiza operaciones aritméticas utilizando esa representación.

$$x=c\times b^e$$

## Funcionalidades

| Función | Propósito |
| --- | --- |
| descomponer_notacion | Obtener coeficiente, base y exponente |
| sumar_notacion | Sumar dos números |
| restar_notacion | Restar dos números |
| multiplicar_notacion | Multiplicar dos números |
| dividir_notacion | Dividir dos números |

## Flujo

```mermaid
flowchart LR
    A[Dos números] --> B[Descomposición]
    B --> C[Operaciones aritméticas]
    C --> D[Resultados en consola]
```

## Ejecución

Requiere Python 3, sin bibliotecas externas.

```bash
git clone https://github.com/rodridarklau/tarea1_computacion_numerica.git
cd tarea1_computacion_numerica
python 1.py
```

Ingresar dos números positivos, por ejemplo 200 y 50. El programa muestra los números descompuestos y las cuatro operaciones.

## Limitaciones actuales

La implementación calcula el exponente a partir de la longitud de la representación textual. Por ello, no garantiza normalización para valores negativos, números menores que uno o notación exponencial. Tampoco controla explícitamente la división por cero. Es una aproximación didáctica y no una biblioteca de cálculo de precisión arbitraria.

## Estructura

`1.py` contiene la lógica y la interacción por consola.

## Créditos

Ejercicio académico de computación numérica.
