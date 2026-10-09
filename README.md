# 🧠 Propogame (Adivina la Proposición)

Juego interactivo desarrollado en Python para practicar lógica proposicional y deducción de tablas de verdad. El proyecto cuenta con **dos modalidades de juego**: una versión directa por terminal y una versión visual interactiva construida con Tkinter.

---

## ✨ Características

* **Banco de Proposiciones:** Incluye 10 operaciones lógicas fundamentales (Conjunción, Disyunción, Condicional, Bicondicional, XOR, NOR, NAND, Condicional Inverso y Negaciones de $P$ y $Q$).
* **Preguntas Dinámicas sin Repetición:** Las tablas se gestionan mediante un mazo activo (`mazo.pop()`) para evitar que una misma proposición aparezca más de una vez por partida.
* **Generación Aleatoria de Opciones:** En cada turno se seleccionan 3 distractores al azar del banco general (excluyendo la respuesta correcta) y se barajan junto a la solución.
* **Doble Interfaz:**
  * **Modo Consola (`main.py`):** Juego ágil en terminal con validación de entradas numéricas (1 a 4).
  * **Modo Gráfico (`game.py`):** Interfaz GUI estilizada con Tkinter, eventos en Canvas mediante rectángulos interactivos y contador final de puntaje.
* **Diseño Modular y POO:** Lógica de juego desacoplada en la clase `Prepogame` (`prepogame.py`), facilitando su reutilización tanto en scripts de consola como en aplicaciones gráficas.

---

## 📂 Estructura del Proyecto

```text
prepogame/
├── datos.py         # Tablas de verdad, respuestas y arte ASCII
├── prepogame.py     # Clase Prepogame (lógica del juego, mazo, validación)
├── game.py          # Interfaz gráfica de usuario con Tkinter
├── main.py          # Versión jugable desde la terminal
└── README.md        # Documentación del proyecto
```

---

## 🚀 Requisitos e Instalación

### Requisitos previos
* **Python 3.8+**
* `tkinter` (incluido por defecto en instalaciones estándar de Python en Windows y macOS; en Linux/Ubuntu se puede instalar vía `sudo apt-get install python3-tk`).

### Instalación
1. Clona el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/propogame.git](https://github.com/tu-usuario/propogame.git)
   cd propogame

   ```

---

## 🎮 Ejecución

Elige la modalidad que prefieras ejecutar:

### 1. Modo Interfaz Gráfica (Recomendado)
```bash
python3 game.py
```
* Haz clic directamente sobre cualquiera de los cuatro bloques de opciones para enviar tu respuesta.
* Al completar las 10 preguntas, se mostrará en pantalla tu puntaje final (`Score: X/10`).

### 2. Modo Terminal
```bash
python3 main.py
```
* Observa la tabla de verdad desplegada en consola.
* Ingresa el número correspondiente a tu respuesta (1 al 4) y presiona `Enter`.

---

## 📝 Licencia

Distribuido bajo la licencia MIT. Siéntete libre de utilizarlo, modificarlo y agregar nuevas tablas de verdad o niveles de dificultad.
