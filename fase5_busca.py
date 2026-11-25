# -*- coding: utf-8 -*-
# fase5_busca.py — Fase 5: o laço while que repete a expansão até chegar.
# Rode com: python fase5_busca.py

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: função de busca A* -----
def busca_astar(inicio, objetivo):
    """devolve (caminho, custo) do melhor caminho, ou (None, infinito)."""
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:
        #escolhe o nó com menor f(n)
        no = fronteira.pop(0)
        f, g, cidade, caminho = no

        # teste de objetivo: feito ao retirar o nó, não ao gerar
        if cidade == objetivo:
            return caminho, g

        #cidade já explorada por um caminho melhor: descarta
        if cidade in explorados:
            continue
        explorados.add(cidade)

        #gerar filhos e colocar na fronteira
        for vizinho, custo_estrada in mapa_romenia[cidade]:
            if vizinho not in explorados:
                novo_g = g + custo_estrada
                novo_f = novo_g + heuristica_bucareste[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf')

# ----- PASSO 3: chamar a função e mostrar o resultado -----
caminho, custo = busca_astar('Arad', 'Bucharest')
if caminho is None:
    print('Não foi encontrado caminho de Arad a Bucharest.')
else:
    print('Caminho encontrado de Arad a Bucharest:', ' -> '.join(caminho))
    print('Custo total =', custo, 'km')
    print('passos =', len(caminho) - 1, 'estradas')