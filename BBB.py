import random

qtd_jogos = 10000


def minigame():
    jogadores = ['Yoshi', 'Toad', 'Luigi', 'Mario']

    # Começamos com 5 botões
    qtd_botoes = 5

    # Índice do jogador que começa
    indice = 0

    while len(jogadores) > 1:

        # Cria os botões da rodada
        botoes = list(range(qtd_botoes))

        # Escolhe aleatoriamente qual botão é o detonador
        bomba = random.choice(botoes)

        # Continua a rodada até alguém ser eliminado
        while True:

            jogador = jogadores[indice]

            # Jogador escolhe um dos botões disponíveis
            escolha = random.choice(botoes)

            if escolha == bomba:
                # Jogador foi eliminado
                jogadores.remove(jogador)

                # Diminui a quantidade de botões
                qtd_botoes -= 1

                # Se sobrou apenas um jogador, ele venceu
                if len(jogadores) == 1:
                    break

                # O próximo jogador começa a nova rodada
                if indice >= len(jogadores):
                    indice = 0

                break

            else:
                # Jogador sobreviveu.
                # Ele vai para o final da fila.
                indice += 1

                if indice >= len(jogadores):
                    indice = 0

    return jogadores[0]


# Contagem das vitórias
resultados = {
    'Yoshi': 0,
    'Toad': 0,
    'Luigi': 0,
    'Mario': 0
}


# Simulação
for i in range(qtd_jogos):

    vencedor = minigame()

    resultados[vencedor] += 1


# Calculando as porcentagens
total = sum(resultados.values())

print(f'Total de jogos: {total}')
print()
print('Porcentagem de vitórias:')

for jogador, vitorias in resultados.items():

    porcentagem = (vitorias / total) * 100

    print(f'{jogador}: {porcentagem:.2f}%')
