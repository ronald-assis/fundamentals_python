import random


class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_halteres = {}
        self.restart_day()

    def restart_day(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def list_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]

    def list_space(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def get_halteres(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0

        return peso

    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)



class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo # 1 - normal | 2 - bagunceiro
        self.academia = academia
        self.peso = 0

    def start_treino(self):
        lista_pesos = self.academia.list_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.get_halteres(self.peso)

    def fiish_treino(self):
        espacos = self.academia.list_space()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)

        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)

        self.peso = 0


academia = Academia()

usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]
random.shuffle(usuarios)

academia.restart_day()

for i in range(10):
    random.shuffle(usuarios)
    for user in usuarios:
        user.start_treino()
    for user in usuarios:
        user.fiish_treino()

port = academia.porta_halteres
academia.calcular_caos()
print(port)


