# 🧠 Adivina la Proposición (Truth Table Quiz)

Juego interactivo de terminal desarrollado en Python para practicar y evaluar conocimientos en **lógica proposicional** y **tablas de verdad**.

El programa presenta una tabla de verdad aleatoria y desafía al usuario a deducir a qué conectiva u operación lógica corresponde, seleccionando entre cuatro opciones dinámicas.

---

## ✨ Características

* **Banco de tablas:** Contiene un conjunto de 10 tablas de verdad con operaciones proposicionales fundamentales (conjunción, disyunción, condicional, bicondicional, negaciones y combinaciones).
* **Preguntas sin repetición:** Las tablas se extraen de un mazo activo durante la partida para evitar preguntas duplicadas en la misma sesión.
* **Opciones múltiples aleatorias:** En cada ronda se generan 4 opciones (la respuesta correcta y 3 distractores aleatorios tomados del resto del banco).
* **Posiciones barajadas:** La respuesta correcta cambia de posición (1 a 4) en cada turno de forma impredecible.
* **Control y validación de entrada:** Verificación de selección numérica para evitar caídas o ingresos inválidos.
* **Contador de puntaje:** Registro del rendimiento y aciertos a lo largo de la ronda.

---

## 📂 Estructura del Proyecto

```text
adivina-la-proposicion/
├── main.py          # Flujo principal del juego y lógica de las rondas
├── datos.py         # Banco de tablas de verdad y respuestas asociadas
└── README.md        # Documentación del proyecto
