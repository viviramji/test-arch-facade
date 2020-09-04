# Parcial 

Para esta actividad usted tendrá que diseñar e implementar el patrón de software asignado. Los entregables de esta actividad son documento e implementación de un caso de estudio en Python. A continuación, se describen los criterios y porcentajes de evaluación de cada uno de los entregables.

## Criterios de evaluación.

1. Usos de estándar PEP8.
2. Documentación de las clases.
3. Prueba unitaria del patrón de software.
4. Prueba funcional del caso de estudio.

* [x] Teoría del patrón de software (corresponde toda la teoría relacionada con dicho patrón).
* [x] Diagrama de clases que describa el patrón de software.
* [x] Descripción detallada del caso de estudio aplicado.
* [x] Diagrama de clase del caso de estudio.
* [x] Máximo de páginas 4 con las referencias en formato PDF.

# Solución

# Parcial Facade

Fecha de inicio: Aug 28, 2020
Fecha límite de entrega: Sep 4, 2020
Tipo de actividad: parcial

# 🏁Introducción

*Presentado por Víctor Víctor Ramos Jiménez - T000XXXXX*

Un patrón (o patrón de diseño) es un documento escrito que describe **una solución general** a un problema de diseño que se repite en muchos proyectos.

Por otro lado un patrón puede contener la descripción de ciertos objetos y clases de objetos a utilizar, junto con sus atributos y dependencias, y el enfoque general de cómo resolver el problema.

### Categorías

- Patrones creacionales: singleton, factory, builder, etc.
    - Los patrones de creación proporcionan varios mecanismos de creación de objetos, que aumentan la flexibilidad y la reutilización del código existente.
- Patrones de estructura: decorator, adapter, facade, composite, etc.
    - Los patrones estructurales explican cómo ensamblar objetos y clases en estructuras más grandes manteniendo estas estructuras flexibles y eficientes.
- Patrones de comportamiento: observer, strategy, iterator. etc.
    - Los patrones de diseño de comportamiento están relacionados con los algoritmos y la asignación de responsabilidades entre los objetos.

# 📖 Concepto

Fachada es un patrón de diseño estructural que proporciona una interfaz simplificada para una biblioteca, un framework o cualquier otro conjunto complejo de clases.

# 💥 Problema

Imagina que debes hacer que tu código funcione con un amplio conjunto de objetos que pertenecen a una biblioteca o marco de trabajo sofisticado. Normalmente, necesitarías inicializar todos esos objetos, llevar un registro de las dependencias, ejecutar los métodos en el orden correcto, y así sucesivamente.

Como resultado, la lógica de negocio de tus clases se acoplaría estrechamente a los detalles de implementación de las clases de terceros, haciendo difícil de comprender y mantener

# 🥂 Solución

Como el concepto lo indica a través del patrón fachada podemos simplificar el acceso a clases o sistemas complejos, como puede ser un framework.

# 🐛Ejemplo práctico y técnico

- En la tienda, muchos artículos están disponibles pero el cliente no sabe la ubicación exacta del artículo en la tienda, así que le pedimos al comerciante una lista de artículos y el comerciante proporciona todos los artículos que el cliente quiere comprar, ya que el comerciante sabe dónde se encuentran los artículos. El tendero es la fachada de la tienda.
- La librería de Facebook SDK. Proporciona métodos muy fáciles y sencillos para acceder a todas las APIs de REST de forma sencilla y practica.

# 🧬 Estrucura

![Parcial%20Facade%207fe85927f05243cea68792a00adb7831/Untitled.png](Parcial%20Facade%207fe85927f05243cea68792a00adb7831/Untitled.png)

Foto tomada de [https://refactoring.guru/design-patterns/facade](https://refactoring.guru/design-patterns/facade)

### Hay tres puntos que intervienen para entender este patrón.

**Clase de fachada:**

Esta clase es para implementar la interfaz que será utilizada por la clase cliente. Esta clase utilizará servicios implementados en el sistema.

**Clase de sistema**

Múltiples clases de sistema pueden estar ahí en el sistema y cada clase de sistema es para un propósito específico.

**Clase de cliente** 
La clase de cliente utiliza la clase de fachada para acceder a la funcionalidad del sistema. Podría ser difícil acceder a la clase de sistema directamente, así que el cliente está usando la clase de fachada en su lugar. Hace peticiones a la Fachada para que se haga el trabajo de los subsistemas

# ⛯Diagrama de clases (Genérico)

![Parcial%20Facade%207fe85927f05243cea68792a00adb7831/Untitled%201.png](Parcial%20Facade%207fe85927f05243cea68792a00adb7831/Untitled%201.png)

Foto tomada de [https://upload.wikimedia.org/wikipedia/en/5/57/Example_of_Facade_design_pattern_in_UML.png](https://upload.wikimedia.org/wikipedia/en/5/57/Example_of_Facade_design_pattern_in_UML.png)

## 👍 Pros

- Puedes aislar tu código de la complejidad de un subsistema.
- Facilita el uso y el mantenimiento de un proceso estructural mayor.

# 👎 Contras

- Patrón fachada puede convertirse en un objeto de dios (god object) acoplado a todas las clases de una aplicación.

*Un objeto de Dios es un objeto que sabe demasiado y/o hace demasiado.*

# 🖇️Similitudes con otros patrones

- **Fachada** define una nueva interfaz para los objetos existentes, mientras que **Adaptador** intenta hacer utilizable la interfaz existente. **Adaptador** normalmente envuelve un solo objeto, mientras que fachada trabaja con todo un subsistema de objetos.
- **Fachada** y **Mediador** tienen trabajos similares: tratan de organizar la colaboración entre muchas clases estrechamente acopladas.
    - Fachada define una interfaz simplificada para un subsistema de objetos, pero no introduce ninguna nueva funcionalidad. El subsistema en sí mismo no conoce la fachada. Los objetos dentro del subsistema pueden comunicarse directamente.
    - El mediador centraliza la comunicación entre los componentes del sistema. Los componentes sólo conocen el objeto mediador y no se comunican directamente.

# 📚 Caso Estudio

Un restaurante requiere un programa para preparar comidas rápidas, diseñe un sistema de información para indicar el numero de platos servidos en una jornada laboral.

![Parcial%20Facade%207fe85927f05243cea68792a00adb7831/diagrama_de_clases.jpg](Parcial%20Facade%207fe85927f05243cea68792a00adb7831/diagrama_de_clases.jpg)

## Requerimientos Funcionales

- Permitir al usuario cerrar la jornada laboral
- Imprimir en pantalla el proceso

## Requerimientos no Funcionales

- Debe tomar al menos 1 segundos terminar una salchipapa

# Referencias

[Facade](https://refactoring.guru/design-patterns/facade)

[God object](https://en.wikipedia.org/wiki/God_object)

[What is pattern (design pattern) ? - Definition from WhatIs.com](https://searchsoftwarequality.techtarget.com/definition/pattern)

[Façade Pattern - Being Adaptive with Façade | Packt Hub](https://hub.packtpub.com/introduction-design-patterns/)

[Design Patterns in Python - Facade](https://medium.com/@hnmpatel/design-patterns-in-python-facade-65b8a393ff68)

### Este documento fue realizado en Notion

...