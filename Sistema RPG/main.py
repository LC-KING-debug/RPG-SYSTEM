# main.py
from utils.entrada import escolhalugar
from classes.herois import Mago, Cavaleiro, Arqueiro
from classes.inimigos import Orc, Goblin, Elfo, MortoVivo, Golem
from utils.sistemabatalha import batalha
from utils.funcoes import espacamento, pausa
from utils.entrada import coletar_dados_jogador
import random

espacamento()
print('✦✦✦=BEM-VINDO AO MEU SISTEMA DE RPG=✦✦✦')
espacamento()
pausa(1)

# CORREÇÃO: Armazena o retorno da função
nome_jogador, idade_jogador = coletar_dados_jogador()

# CORREÇÃO: Passa o nome como parâmetro
escolhalugar(nome_jogador)

print("Escolha sua classe:")
print("1 - Mago\n2 - Cavaleiro\n3 - Arqueiro")
classe = int(input("Digite o número da classe: "))
player = Mago() if classe == 1 else Cavaleiro() if classe == 2 else Arqueiro()
print(f"Você escolheu a classe {player.__class__.__name__}!")
pausa(1)

inimigos_list = [Orc(), Goblin(), Elfo(), MortoVivo(), Golem()]
inimigo = random.choice(inimigos_list)
print(f"Um {inimigo.nome} apareceu!")

batalha(player, inimigo)