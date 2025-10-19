# classes/herois.py

class Mago:
    def __init__(self):
        self.nome = 'Mago'
        self.vida_max = 23
        self.vida_atual = 23
        self.mana_max = 200
        self.mana_atual = 200
        self.defesa = 15
        self.ataque = 40
        self.level = 1
        self.xp = 0
    
    def subir_level(self):
        self.level += 1
        self.vida_max += 5
        self.ataque += 5
        self.defesa += 3
        self.vida_atual = self.vida_max
        print(f"{self.nome} subiu para o nível {self.level}!")


class Cavaleiro:
    def __init__(self):
        self.nome = 'Cavaleiro'
        self.vida_max = 60
        self.vida_atual = 60
        self.energia_max = 50
        self.energia_atual = 50
        self.defesa = 50
        self.ataque = 12
        self.level = 1
        self.xp = 0
    
    def subir_level(self):
        self.level += 1
        self.vida_max += 10
        self.ataque += 2
        self.defesa += 4
        self.vida_atual = self.vida_max
        print(f"{self.nome} subiu para o nível {self.level}!")


class Arqueiro:
    def __init__(self):
        self.nome = 'Arqueiro'
        self.vida_max = 30
        self.vida_atual = 30
        self.energia_max = 300
        self.energia_atual = 300
        self.defesa = 30
        self.ataque = 20
        self.level = 1
        self.xp = 0
    
    def subir_level(self):
        self.level += 1
        self.vida_max += 6
        self.ataque += 4
        self.defesa += 2
        self.vida_atual = self.vida_max
        print(f"{self.nome} subiu para o nível {self.level}!")