# Bowser's Big Blast — Python Simulation

Simulação em Python baseada no minigame **Bowser's Big Blast**, com o objetivo de analisar se a posição inicial de um jogador influencia sua probabilidade de vitória.

O programa executa milhares de partidas, registra o vencedor de cada uma e calcula a porcentagem de vitórias de cada jogador.

## Tecnologias utilizadas

* Python
* Random

## Como funciona

A simulação reproduz a dinâmica do minigame:

* 4 jogadores começam em uma ordem definida.
* A rodada começa com 5 botões.
* Um dos botões é escolhido aleatoriamente como o detonador.
* Cada jogador escolhe um botão aleatoriamente.
* O jogador que escolher o detonador é eliminado.
* Após uma eliminação, a quantidade de botões é reduzida.
* O processo continua até restar apenas um jogador.
* O vencedor é registrado e uma nova partida é iniciada.

## Análise

Após a execução das partidas, o programa calcula a porcentagem de vitórias de cada jogador.

A quantidade de partidas pode ser alterada através da variável:


qtd_jogos = 10000


O objetivo é utilizar a simulação para observar se existe alguma diferença significativa na taxa de vitória de acordo com a posição inicial do jogador.

## Objetivo do projeto

Este projeto foi desenvolvido como um exercício de Python e simulação de probabilidades, utilizando programação para investigar um problema por meio da execução repetida de partidas.
