# utils/sistemabatalha.py

from utils.funcoes import pausa, espacamento
import random

def batalha(player, inimigo):
    espacamento()
    print(f"Batalha iniciada! {player.nome} vs {inimigo.nome}")
    
    while player.vida_atual > 0 and inimigo.vida > 0:
        print(f"\n{player.nome}: {player.vida_atual}/{player.vida_max} HP")
        print(f"{inimigo.nome}: {inimigo.vida} HP")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Fugir")
        
        acao = input("Escolha sua ação: ")
        
        if acao == '1':
            dano = max(0, player.ataque - inimigo.defesa + random.randint(-2, 5))
            inimigo.vida -= dano
            print(f"Você causou {dano} de dano ao {inimigo.nome}!")
        elif acao == '2':
            print("Você se defende, reduzindo dano do próximo ataque!")
            player.defesa += 5
        elif acao == '3':
            print("Você fugiu!")
            return
        else:
            print("Ação inválida!")
            continue
        
        pausa(1)
        
        if inimigo.vida <= 0:
            print(f"Você derrotou o {inimigo.nome} e ganhou {inimigo.xp} XP!")
            player.xp += inimigo.xp
            if player.xp >= 100:
                player.subir_level()
                player.xp = 0
            break
        
        dano_inimigo = max(0, inimigo.ataque - player.defesa // 3)
        player.vida_atual -= dano_inimigo
        print(f"O {inimigo.nome} atacou e causou {dano_inimigo} de dano!")
        
        if acao == '2':
            player.defesa -= 5
        
        pausa(1)

