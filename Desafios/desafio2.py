# -*- coding: utf-8 -*-
# desafio2.py — Desafios da Fase 2
# Rode com: python desafio2.py

from fase2_caminhos import custo_do_caminho, mostrar_g_h_f
caminho_desafio2 = [
    'Arad',
    'Timisoara',
    'Lugoj',
    'Mehadia',
    'Drobeta',
    'Craiova',
    'Pitesti',
    'Bucharest'
]

# --- PASSO 1: custo total do caminho ---
print('--- Custo total do caminho ---')
custo_total = custo_do_caminho(caminho_desafio2)
print(f'Caminho: {" -> ".join(caminho_desafio2)}')
print(f'Custo total: {custo_total} km')

# --- PASSO 2: mostrar g(n), h(n) e f(n) para cada cidade ---
print('\n--- Valores de g(n), h(n) e f(n) ---')
mostrar_g_h_f(caminho_desafio2)
