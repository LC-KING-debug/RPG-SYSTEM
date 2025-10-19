from utils.funcoes import pausa

def coletar_dados_jogador():
    while True:
        try:
            nome = input("Digite o nome do seu personagem: ")
            idade = int(input("Digite a sua idade: "))
            break
        except ValueError:
            print("Digite um número para a idade")
    
    return nome, idade

def escolhalugar(nome_jogador):  # DEVE receber o parâmetro
    print("Missões foram concedidas à você jovem {}".format(nome_jogador))
    print("Escolha um dos 3 lugares para explorar:")
    print("Carregando...")
    pausa()
    print('''1 - Terra de Oogrest
2 - Vale das sombras
3 - Ilha Morta''')
    
    while True:
        try:
            escolha_do_lugar = int(input("Digite o número referente ao lugar: "))
            if escolha_do_lugar in [1, 2, 3]:
                break
            else:
                print("Digite apenas 1, 2 ou 3")
        except ValueError:
            print("Digite apenas os números referente ao lugar (1,2,3)")
    
    if escolha_do_lugar == 1:
        print("então o jogador(a) {} vai para a Terra de Oogrest? ".format(nome_jogador))
    elif escolha_do_lugar == 2:
        print("então o jogador(a) {} vai para o Vale das Sombras? ".format(nome_jogador))
    else:
        print("então o jogador(a) {} vai para A Ilha Morta? ".format(nome_jogador))
    
    input("Aperte ENTER para continuar")
    pausa()