# -*- coding: utf-8 -*-
# desafio5.py — Desafios da Fase 5
# Rode com: python desafio5.py

from mapa import mapa_romenia, heuristica_bucareste

def busca_a_estrela(inicio, objetivo, modo='normal'):
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:
        # Ordena a fronteira pelo valor de f e retira o nó com menor f
        if modo == 'gulosa_h':
            fronteira.sort(key=lambda no: heuristica_bucareste[no[2]])
        else:
            fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho_atual = fronteira.pop(0)

        # Verifica se o objetivo foi alcançado
        if modo != "objetivo_ao_gerar" and cidade_atual == objetivo:
            return caminho_atual, g_atual

        if cidade_atual in explorados:
            continue
        explorados.add(cidade_atual)

        # Expande o nó atual
        for vizinho, custo in mapa_romenia[cidade_atual]:
            novo_g = g_atual + custo
            novo_caminho = caminho_atual + [vizinho]

            if modo == 'objetivo_ao_gerar' and vizinho == objetivo:
                return novo_caminho, novo_g

            if vizinho in explorados:
                continue

            novo_f = novo_g + heuristica_bucareste[vizinho]
            fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

    return None, float('inf')  # Retorna None se não houver caminho

for nome, modo in [('Busca A* normal', 'normal'), ('Busca gulosa (h)', 'gulosa_h'), ('objetivo ao gerar filho', 'objetivo_ao_gerar')]:
    caminho, custo = busca_a_estrela('Arad', 'Bucharest', modo=modo)
    print(f'\n{nome}:')
    if caminho:
        print(f'Caminho encontrado: {" -> ".join(caminho)} com custo {custo} km')
