# -*- coding: utf-8 -*-
# desafio6.py — Desafios da Fase 6
# Rode com: python desafio6.py

from mapa import mapa_romenia, heuristica_bucareste
from fase6_a_estrela import resumo_fronteira


def busca_com_contador(inicio, objetivo, grafo, heuristica, mostrar=True):
    """Versão da busca A* que também devolve o número de iterações do laço while."""
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    explorados = set()
    iteracao = 0

    if mostrar:
        print(f'--- Busca A* de {inicio} para {objetivo} ---')

    while fronteira:
        iteracao += 1
        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        if mostrar:
            print(
                f'{iteracao}. Expandindo: {cidade_atual} | '
                f'g(n)={g_atual}, h(n)={heuristica[cidade_atual]} '
                f'-> f(n)={f_atual}'
            )

        if cidade_atual == objetivo:
            return caminho, g_atual, iteracao

        if cidade_atual in explorados:
            continue
        explorados.add(cidade_atual)

        for vizinho, custo_estrada in grafo.get(cidade_atual, []):
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

        if mostrar:
            fronteira.sort(key=lambda no: no[0])
            print('   fronteira:', resumo_fronteira(fronteira))

    return None, float('inf'), iteracao

h_zero = {cidade: 0 for cidade in mapa_romenia}
caminho_h0, custo_h0, it_h0 = busca_com_contador(
    'Arad', 'Bucharest', mapa_romenia, h_zero, mostrar=False
)
print('--- Desafio 1 e 3: heurística zero (h=0) ---')
print('Caminho:', ' -> '.join(caminho_h0))
print(f'Custo: {custo_h0} km | Iterações do while: {it_h0}')

print('\n--- Desafio 2 e 3: outras origens até Bucharest ---')
for origem in ['Lugoj', 'Mehadia', 'Eforie']:
    caminho, custo, it = busca_com_contador(
        origem, 'Bucharest', mapa_romenia, heuristica_bucareste, mostrar=False
    )
    print(
        f'{origem:<10} {custo:>4} km | {it:>2} iterações | '
        f'{" -> ".join(caminho)}'
    )
