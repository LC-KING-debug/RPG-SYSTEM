# classes/inimigos.py

class Orc:
    def __init__(self):
        self.nome = 'Orc'
        self.vida = 17
        self.defesa = 6
        self.xp = 25
        self.ataque = 4


class Goblin:
    def __init__(self):
        self.nome = 'Goblin'
        self.vida = 10
        self.defesa = 3
        self.xp = 8
        self.ataque = 2


class Elfo:
    def __init__(self):
        self.nome = 'Elfo'
        self.vida = 14
        self.defesa = 4
        self.xp = 19
        self.ataque = 6


class MortoVivo:
    def __init__(self):
        self.nome = 'Morto-Vivo'
        self.vida = 20
        self.defesa = 13
        self.xp = 21
        self.ataque = 5


class Golem:
    def __init__(self):
        self.nome = 'Golem'
        self.vida = 40
        self.defesa = 20
        self.xp = 40
        self.ataque = 10