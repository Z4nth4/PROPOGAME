from prepogame import Prepogame
import tkinter as tk
from PIL import Image, ImageTk
from time import sleep

TEAL = "#08D9D6"
BLACK = "#252A34"
RED = "#FF2E63"
GREY = "#EAEAEA"

backg = "#0F172A"
pizarron = "#1E293B"
borde = "#F43F5E"
bgopc = "#334155"
FONDO_OPCIONES = "#27273A"

ventana = tk.Tk()
ventana.title("Prepogame")
ventana.geometry("640x600")
ventana.config(bg=backg)

game = Prepogame()
############### Canvas con la tabla en assci ##################################
tabla = tk.Canvas(ventana, width=320, height=350, bg=pizarron, highlightbackground=borde, highlightthickness=2)
tabla.place(x=160, y=20)

texto_tabla = tabla.create_text(160, 130, text="Iniciar", fill="#EDF2F7", anchor="center", font=("Courier New", 18, "bold"))
#******************************************************************************

################ Canvas con las opciones de respuesta #######################
options_space = tk.Canvas(ventana, width=500, height=180, bg=bgopc, highlightthickness=2, highlightbackground=borde)
options_space.place(x=70, y=400)

rect_one = options_space.create_rectangle(30, 20, 230, 80, fill=FONDO_OPCIONES, outline="#C7528D")
rect_two = options_space.create_rectangle(270, 20, 470, 80, fill=FONDO_OPCIONES, outline="#C7528D")
rect_three = options_space.create_rectangle(30, 100, 230, 160, fill=FONDO_OPCIONES, outline="#C7528D")
rect_four = options_space.create_rectangle(270, 100, 470, 160, fill=FONDO_OPCIONES, outline="#C7528D")

text1 = options_space.create_text(130, 50, text="", font=("Arial", 11, "bold"), fill="#F8FAFC")
text2 = options_space.create_text(370, 50, text="", font=("Arial", 11, "bold"), fill="#F8FAFC")
text3 = options_space.create_text(130, 130, text="", font=("Arial", 11, "bold"), fill="#F8FAFC")
text4 = options_space.create_text(370, 130, text="", font=("Arial", 11, "bold"), fill="#F8FAFC")

options_space.addtag_withtag("boton1", rect_one)
options_space.addtag_withtag("boton1", text1)
options_space.addtag_withtag("boton2", rect_two)
options_space.addtag_withtag("boton2", text2)
options_space.addtag_withtag("boton3", rect_three)
options_space.addtag_withtag("boton3", text3)
options_space.addtag_withtag("boton4", rect_four)
options_space.addtag_withtag("boton4", text4)
#******************************************************************************

###################### GIFTS #######################################
################ Creacion de listas con fotogramas #################
fotograms_correct = []
fotograms_mistake = []

ruta_good = "./animaciones/correct2.gif"
imagen_correct = Image.open(ruta_good)

ruta_bad = "./animaciones/mistake2.gif"
imagen_mistake = Image.open(ruta_bad)

try:
    while True:
        frame_tk_correct = ImageTk.PhotoImage(imagen_correct.copy())
        fotograms_correct.append(frame_tk_correct)

        imagen_correct.seek(len(fotograms_correct))
except EOFError:
    pass

try:
    while True:
        frame_tk_mistake = ImageTk.PhotoImage(imagen_mistake.copy())
        fotograms_mistake.append(frame_tk_mistake)

        imagen_mistake.seek(len(fotograms_mistake))
except EOFError:
    pass
#**********************************************************************

######## Labels para gifts #####################
label_animation = tk.Label(ventana, highlightthickness=0, background=backg)
label_animation.place(x=20, y=250)
#***********************************************

############### Canvas para el menu de opciones ##############################
menu = tk.Canvas(ventana, width=640, height=600, bg=BLACK, highlightthickness=0)
menu.place(x=0, y=0)

title = menu.create_text(320, 120, text="PREPOGAME", font=("Consolas", 50, "bold"), fill="#FFFFFF")
subtitle = menu.create_text(320, 230, text="ELIGE LA CANTIDAD\nDE PREGUNTAS", font=("Consolas", 20, "bold"), fill="#94A3B8", justify="center")

rect_easy = menu.create_rectangle(50, 320, 270, 390, fill="#1E2433", outline="#22C55E")
rect_medium = menu.create_rectangle(370, 320, 590, 390, fill="#1E2433", outline="#F59E0B")
rect_hard = menu.create_rectangle(210, 420, 430, 490, fill="#1E2433", outline="#F43F5E")

text_easy = menu.create_text(160, 355, text="Facil", font=("Consolas", 30, "bold"), fill="#F8FAFC")
text_medium = menu.create_text(480, 355, text="Medio", font=("Consolas", 30, "bold"), fill="#F8FAFC")
text_hard = menu.create_text(325, 455, text="Dificil", font=("Consolas", 30, "bold"), fill="#F8FAFC")

menu.addtag_withtag("btn_easy", rect_easy)
menu.addtag_withtag("btn_easy", text_easy)
menu.addtag_withtag("btn_medium", rect_medium)
menu.addtag_withtag("btn_medium", text_medium)
menu.addtag_withtag("btn_hard", rect_hard)
menu.addtag_withtag("btn_hard", text_hard)

menu.tag_bind("btn_easy", "<Button-1>", lambda e: elegir_dificultad("easy"))
menu.tag_bind("btn_medium", "<Button-1>", lambda e: elegir_dificultad("medium"))
menu.tag_bind("btn_hard", "<Button-1>", lambda e: elegir_dificultad("hard"))
#*****************************************************************************

cantidad_de_preguntas = 0
def elegir_dificultad(dificultad: str):
    global menu
    global cantidad_de_preguntas
    if dificultad == "easy":
        cantidad_de_preguntas = 10
    elif dificultad == "medium":
        cantidad_de_preguntas = 15
    else:
        cantidad_de_preguntas = 20
    sleep(0.3)
    menu.destroy()
    game.cant_games = cantidad_de_preguntas

animacion = None
def actualizar_ani(lista: list, current_index = 0, speed = 50):
    global animacion
    if current_index < len(lista):
        label_animation.config(image=lista[current_index])
        next_index = (current_index + 1)
    else:
        label_animation.config(image="")
        animacion = None
        return
    animacion = ventana.after(speed, actualizar_ani, lista, next_index, speed)

def stop_animation():
    global animacion
    if animacion is not None:
        ventana.after_cancel(animacion)
        animacion = None

def validacion(option):
    global cantidad_de_preguntas
    stop_animation()
    if game.answer_validation(option):
        actualizar_ani(lista=fotograms_correct, current_index=0, speed=35)
    else:
        actualizar_ani(lista=fotograms_mistake, current_index=0, speed=85)
    if game.cant_games == 0:
        print("fin del juego")
        options_space.tag_unbind("boton1", "<Button-1>")
        options_space.tag_unbind("boton2", "<Button-1>")
        options_space.tag_unbind("boton3", "<Button-1>")
        options_space.tag_unbind("boton4", "<Button-1>")
        tabla.itemconfig(texto_tabla, text=f"\n\nScore: {game.wins}/{cantidad_de_preguntas}", font=("Arial", 30, "bold"))
        return
    ventana.after(500, iniciar)


def iniciar():
    options_list = game.option_creation()
    tabla.itemconfig(texto_tabla, text=game.current_quest["tabla"])
    options_space.itemconfig(text1, text=options_list[0])
    options_space.itemconfig(text2, text=options_list[1])
    options_space.itemconfig(text3, text=options_list[2])
    options_space.itemconfig(text4, text=options_list[3])

    options_space.tag_bind("boton1", "<Button-1>", lambda e: validacion(options_list[0]))
    options_space.tag_bind("boton2", "<Button-1>", lambda e: validacion(options_list[1]))
    options_space.tag_bind("boton3", "<Button-1>", lambda e: validacion(options_list[2]))
    options_space.tag_bind("boton4", "<Button-1>", lambda e: validacion(options_list[3]))

iniciar()
ventana.mainloop()
