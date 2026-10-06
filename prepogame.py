import random
from datos import tablas_proposiciones


class Prepogame:
    def __init__(self) -> None:
        self.OPTIONS_QUANTITY = 3
        self.wins = 0
        self.games = 0
        self.mazo = tablas_proposiciones.copy()
        self.current_quest = {}

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
            self.games += 1
            return True
        else:
            print("Respuesta incorrecta :(")
            self.games += 1
            return False
        