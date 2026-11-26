# -*- coding: utf-8 -*-
# desafio3.py — Desafios da Fase 3
# Rode com: python desafio3.py

from mapa import mapa_romenia, heuristica_bucareste

# fronteira apos expandir Arad
fronteira = [
    (449, 75, 'Zerind',['Arad','Zerind']),
    (393, 140, 'Sibiu',['Arad','Sibiu']),
    (447, 118, 'Timisoara',['Arad','Timisoara'])
]

# --- PASSO 1: ordernar por f, retirar Sibiu e expadir seus vizinhos ---
fronteira.sort(key=lambda no: no[0])
no_sibiu = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho_atual = no_sibiu

for vizinho, custo in mapa_romenia[cidade_atual]:
    g_vizinho = g_atual + custo
    h_vizinho = heuristica_bucareste[vizinho]
    f_vizinho = g_vizinho + h_vizinho
    caminho_vizinho = caminho_atual + [vizinho]
    fronteira.append((f_vizinho, g_vizinho, vizinho, caminho_vizinho))
fronteira.sort(key=lambda no: no[0])
print('--- Fronteira ordenada por f ---')
for item in fronteira:
    print(f'Cidade: {item[2]}, f: {item[0]}, g: {item[1]}, Caminho: {" -> ".join(item[3])}')

# --- PASSO 2: ordernar pela mesma fronteira por g (no[1]) ---
fronteira.sort(key=lambda no: no[1])
primeiro_por_g = fronteira.pop(0)
print('--- Fronteira ordenada por g ---')
for item in fronteira:
    print(f'Cidade: {item[2]}, f: {item[0]}, g: {item[1]}, Caminho: {" -> ".join(item[3])}')
