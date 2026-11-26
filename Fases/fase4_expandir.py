# -*- coding: utf-8 -*-
# fase4_expandir.py — Fase 4: transformar a expansão em função e repetir à mão.
# Rode com: python fase4_expandir.py

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: função que mostra a fronteira de forma resumida -----
def mostrar_fronteira(fronteira):
    """Imprime cada nó da fronteira como Cidade(f=...)."""
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={f})')
    print(' fronteira:', ', '.join(partes))

# ---- PASSO 3: função que expande um nó -----
def expandir_no(no, explorados):
    """devolve uma lista de nós filhos, pulando os já explorados."""
    f, g, cidade, caminho = no
    filhos = []
    for vizinho, custo_estrada in mapa_romenia[cidade]:
        if vizinho in explorados:
            continue
        novo_g = g + custo_estrada
        novo_h = heuristica_bucareste[vizinho]
        novo_f = novo_g + novo_h
        novo_caminho = caminho + [vizinho]
        filhos.append((novo_f, novo_g, vizinho, novo_caminho))
    return filhos

#---- PASSO 4: testar a função expandir_no -----
inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

# ----- PASSO 5: repetir a expansão à mão -----
for rodada in range(3):
    print()
    print(f'Rodada {rodada + 1}:')
    mostrar_fronteira(fronteira)
    no = fronteira.pop(0)
    f, g, cidade, caminho = no
    print(' nó retirado:', cidade, 'f =', f, 'g =', g, 'caminho =', caminho)
    explorados.add(cidade)
    filhos = expandir_no(no, explorados)
    print(' filhos gerados:', [filho[2] for filho in filhos])
    fronteira.extend(filhos)
    fronteira.sort(key=lambda no: no[0])
