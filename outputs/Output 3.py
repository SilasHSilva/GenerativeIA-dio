import random

# Função para criar o tabuleiro
def criar_tabuleiro(tamanho):
    return [["~" for _ in range(tamanho)] for _ in range(tamanho)]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro, mostrar_navios=False):
    for linha in tabuleiro:
        if mostrar_navios:
            print(" ".join(linha))
        else:
            print(" ".join("X" if celula == "N" else celula for celula in linha))

# Função para posicionar navios no tabuleiro
def posicionar_navios(tabuleiro, quantidade):
    for _ in range(quantidade):
        while True:
            linha = random.randint(0, len(tabuleiro) - 1)
            coluna = random.randint(0, len(tabuleiro[0]) - 1)
            if tabuleiro[linha][coluna] == "~":
                tabuleiro[linha][coluna] = "N"
                break

# Função para jogar o jogo
def jogar_batalha_naval():
    tamanho = 5
    quantidade_navios = 3
    tentativas = 10

    # Configuração do jogo
    tabuleiro = criar_tabuleiro(tamanho)
    posicionar_navios(tabuleiro, quantidade_navios)

    print("Bem-vindo ao Batalha Naval!")
    print(f"O tabuleiro é de tamanho {tamanho}x{tamanho}.")
    print(f"Existem {quantidade_navios} navios escondidos. Boa sorte!\n")

    while tentativas > 0:
        imprimir_tabuleiro(tabuleiro)
        print(f"Tentativas restantes: {tentativas}\n")

        # Entrada do jogador
        try:
            linha = int(input("Digite a linha (0 a 4): "))
            coluna = int(input("Digite a coluna (0 a 4): "))
            if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
                print("Coordenadas fora do limite! Tente novamente.\n")
                continue
        except ValueError:
            print("Entrada inválida! Use apenas números.\n")
            continue

        # Verificar se acertou um navio
        if tabuleiro[linha][coluna] == "N":
            print("Parabéns! Você acertou um navio!")
            tabuleiro[linha][coluna] = "H"  # H de "Hit" (acerto)
            quantidade_navios -= 1
            if quantidade_navios == 0:
                print("Você afundou todos os navios! Vitória!")
                break
        elif tabuleiro[linha][coluna] == "~":
            print("Água! Tente novamente.")
            tabuleiro[linha][coluna] = "A"  # A de "Água"
        else:
            print("Você já tentou essa posição. Tente outra.")

        tentativas -= 1

    if tentativas == 0 and quantidade_navios > 0:
        print("Fim de jogo! Você usou todas as tentativas.")
        print("Os navios estavam nas seguintes posições:")
        imprimir_tabuleiro(tabuleiro, mostrar_navios=True)

# Iniciar o jogo
jogar_batalha_naval()