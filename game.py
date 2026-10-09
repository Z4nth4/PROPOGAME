from prepogame import Prepogame
import tkinter as tk
from PIL import Image, ImageTk

TEAL = "#08D9D6"
BLACK = "#252A34"
RED = "#FF2E63"
GREY = "#EAEAEA"

ventana = tk.Tk()
ventana.title("Prepogame")
ventana.geometry("640x540")
ventana.config(bg=TEAL)

game = Prepogame()
tabla = tk.Canvas(ventana, width=320, height=260, bg=BLACK, highlightthickness=0)
tabla.place(x=160, y=20)

options_space = tk.Canvas(ventana, width=500, height=200, bg=RED)
options_space.place(x=70, y=300)

texto_tabla = tabla.create_text(160, 130, text="Iniciar", fill=GREY, anchor="center", font=("Arial", 20, "bold"))

rect_one = options_space.create_rectangle(40, 20, 220, 80, fill=GREY, outline="black")
rect_two = options_space.create_rectangle(280, 20, 460, 80, fill=GREY, outline="black")
rect_three = options_space.create_rectangle(40, 100, 220, 160, fill=GREY, outline="black")
rect_four = options_space.create_rectangle(280, 100, 460, 160, fill=GREY, outline="black")

text1 = options_space.create_text(130, 50, text="", font=("Arial", 12, "bold"), fill=BLACK)
text2 = options_space.create_text(370, 50, text="", font=("Arial", 12, "bold"), fill=BLACK)
text3 = options_space.create_text(130, 130, text="", font=("Arial", 12, "bold"), fill=BLACK)
text4 = options_space.create_text(370, 130, text="", font=("Arial", 12, "bold"), fill=BLACK)

###################### GIFTS #######################################
################ Creacion de listas con fotogramas #################
fotograms_correct = []
fotograms_mistake = []

ruta_good = "./animaciones/correct.gif"
imagen_correct = Image.open(ruta_good)

ruta_bad = "./animaciones/mistake.gif"
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
label_animation = tk.Label(ventana, highlightthickness=0, background=TEAL)
label_animation.place(x=20, y=100)
#***********************************************

def actualizar_ani(lista: list, current_index = 0, speed = 50):
    if current_index < len(lista):
        label_animation.config(image=lista[current_index])
        next_index = (current_index + 1) #% len(lista)
    else:
        label_animation.config(image="")
        return
    ventana.after(speed, actualizar_ani, lista, next_index, speed)

def accion(option):
    if game.answer_validation(option):
        actualizar_ani(lista=fotograms_correct, current_index=0, speed=25)
    else:
        actualizar_ani(lista=fotograms_mistake, current_index=0, speed=100)
    if game.games == 10:
        print("fin del juego")
        options_space.tag_unbind("boton1", "<Button-1>")
        options_space.tag_unbind("boton2", "<Button-1>")
        options_space.tag_unbind("boton3", "<Button-1>")
        options_space.tag_unbind("boton4", "<Button-1>")
        tabla.itemconfig(texto_tabla, text=f"Score: {game.wins}/{game.games}")
        return
    ventana.after(500, iniciar)


def iniciar():
    options_list = game.option_creation()
    tabla.itemconfig(texto_tabla, text=game.current_quest["tabla"])
    options_space.itemconfig(text1, text=options_list[0])
    options_space.itemconfig(text2, text=options_list[1])
    options_space.itemconfig(text3, text=options_list[2])
    options_space.itemconfig(text4, text=options_list[3])

    options_space.addtag_withtag("boton1", rect_one)
    options_space.addtag_withtag("boton1", text1)
    options_space.addtag_withtag("boton2", rect_two)
    options_space.addtag_withtag("boton2", text2)
    options_space.addtag_withtag("boton3", rect_three)
    options_space.addtag_withtag("boton3", text3)
    options_space.addtag_withtag("boton4", rect_four)
    options_space.addtag_withtag("boton4", text4)
    
   
    options_space.tag_bind("boton1", "<Button-1>", lambda e: accion(options_list[0]))
    options_space.tag_bind("boton2", "<Button-1>", lambda e: accion(options_list[1]))
    options_space.tag_bind("boton3", "<Button-1>", lambda e: accion(options_list[2]))
    options_space.tag_bind("boton4", "<Button-1>", lambda e: accion(options_list[3]))

iniciar()
ventana.mainloop()
