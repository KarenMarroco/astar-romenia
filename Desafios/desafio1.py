# -*- coding: utf-8 -*-
# desafio1.py — Desafios da Fase 1
# Rode com: python desafio1.py

from mapa import mapa_romenia, heuristica_bucareste

# --- PASSO 1: cidades com uma estrada ---
print('--- Cidades com uma estrada ---')
for cidade, vizinhos in mapa_romenia.items():
    if len(vizinhos) == 1:
        print(f'{cidade:<10} vizinho = {vizinhos[0][0]:<10} custo = {vizinhos[0][1]:>4} km')

# --- PASSO 2: cidades com h(n) < 200km ---
print()
print('--- Cidades com h(n) < 200km ---')
for cidade, h in heuristica_bucareste.items():
    if h < 200:
        print(f'{cidade:<10} h(n) = {h:>4} km')

# --- PASSO 3: estrada mais longa do mapa ---
maior_custo = 0
estrada_mais_longa = ''

for cidade, vizinhos in mapa_romenia.items():
    for vizinho, custo in vizinhos:
        if custo > maior_custo:
            maior_custo = custo
            estrada_mais_longa = f'{cidade} - {vizinho}'

print('\n--- Estrada mais longa do mapa ---')
print(f'{estrada_mais_longa}: {maior_custo} km')
