from datos import tablas_proposiciones, logo
import random
# "nombre": "Conjunción (P ∧ Q)",
#         "tabla": """+---+---+---+
# | P | Q | ? |
# +---+---+---+
# | V | V | V |
# | V | F | F |
# | F | V | F |
# | F | F | F |
# +---+---+---+"""

print(logo)
input("Presione enter para comenzar...")
ganadas = 0                                 
mazo = tablas_proposiciones.copy()                 #lista de preguntas que se usaran durante el juego, cada que una se use, se eliminara de la lista
while len(mazo) > 0:
    distractores = []

    indice = random.randrange(len(mazo))    #se selecciona un numero random entre 0 y la cantidad de preguntas en el mazo
    pregunta = mazo.pop(indice)             #Almacena la pregunta a jugar en pregunta y la elimina del mazo para evitar repeticiones
    
    tabla = pregunta["tabla"]               #almacena la tabla de la pregunta
    respuesta = pregunta["nombre"]          #almacena la respuesta de la pregunta

    ################### Creacion de opciones ##################
    opciones = tablas_proposiciones.copy()  #se crea otra copia de la lista original pero para obtener diferentes opciones
    opciones.remove(pregunta)               #eliminacion de la respuesta correcta para evitar duplicados
    for i in range(3):
        indice_dos = random.randrange(len(opciones))    #eleccion de numeros indices random para la aleatoreidad de las opciones
        distractor = opciones.pop(indice_dos)           #se guarda en una variable y se elimina de la lista para evitar duplicados
        distractores.append(distractor["nombre"])       #se agrega la respuesta distractora aleatoria a las opciones a mostrar
    distractores.append(respuesta)                      #agregacion de la respuesta correcta a las opciones a mostrar
    random.shuffle(distractores)                        #se barajean las opciones de respuestas para que salgan en diferente orden siempre
    
    ############# impresion de tabla y opciones ################
    print("\n\n\n\n\n", tabla)                          #impresion de la tabla a jugar
    for i in range(len(distractores)):                  
        print(f"{i+1}. {distractores[i]}")              #impresion de respuestas con un indice
    answer_indice = input("Proposicion?: ")             #almacenamiento de la respuesta del usuario, se usara como indice

    ########### Validacion de respuesta ####################
    while answer_indice not in "1234":
        answer_indice = input("Introduce un valor entre 1 a 4: ")   #dentro del while se valida que la respuesta sea 1,2,3 o 4

    usuario_answer = distractores[int(answer_indice) - 1]           #usando el indice anterior se almacena el texto de la respuesta en una variable
    if usuario_answer == respuesta:                                 #se valida que los strings sean iguales (respuesta correcta)
        print("Respuesta correcta :)")
        ganadas += 1
    else:
        print("Te equivocaste :(")
    input("\nPresione enter para ir a la siguiente pregunta")
print(f"\n\n\n\n\nResultados: {ganadas}/{len(tablas_proposiciones)}")