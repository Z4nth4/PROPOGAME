import random
from datos import tablas_proposiciones


class Prepogame:
    def __init__(self, cant_games = 10) -> None:
        self.OPTIONS_QUANTITY = 3
        self.wins = 0
        self.cant_games = cant_games
        self.mazo = tablas_proposiciones.copy()
        self.current_quest = {}
        self.high_score = 0
        self.dificultad = ""

    def init_question(self):
        if len(self.mazo) > 0:
            index = random.randrange(len(self.mazo))
            self.current_quest = self.mazo.pop(index)

    def option_creation(self) -> list:
        self.init_question()
        options_list = []
        all_answers = tablas_proposiciones.copy()
        all_answers.remove(self.current_quest)
        for _ in range(self.OPTIONS_QUANTITY):
            index = random.randrange(len(all_answers))
            distractor = all_answers.pop(index)
            options_list.append(distractor["nombre"])
        options_list.append(self.current_quest["nombre"])
        random.shuffle(options_list)
        return options_list

    def answer_validation(self, answer) -> bool:
        if answer == self.current_quest["nombre"]:
            print("Respuesta correcta :)")
            self.wins += 1
            self.cant_games -= 1
            return True
        else:
            print("Respuesta incorrecta :(")
            self.cant_games -= 1
            return False

    def init_score(self, dificultad: str):
        self.dificultad = dificultad
        if dificultad == "easy":    
            try:
                with open("easy.txt", "r") as file:
                    self.high_score = int(file.read())
            except:
                with open("easy.txt", "w") as file:
                    file.write("0")
            
        elif dificultad == "medium":    
            try:
                with open("medium.txt", "r") as file:
                    self.high_score = int(file.read())
            except:
                with open("medium.txt", "w") as file:
                    file.write("0")
        
        else:
            try:
                with open("hard.txt", "r") as file:
                    self.high_score = int(file.read())
            except:
                with open("hard.txt", "w") as file:
                    file.write("0")

    def save_score(self):
        if self.wins > self.high_score:
            with open(f"{self.dificultad}.txt", "w") as file:
                file.write(str(self.wins))