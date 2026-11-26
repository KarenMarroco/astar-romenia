# -*- coding: utf-8 -*-
# a_estrela.py — Fase 6: o programa completo da busca A*.
# Rode com: python a_estrela.py
#
# f(n) = g(n) + h(n)
# g(n): km já percorridos desde a origem até n (custo real)
# h(n): km em linha reta de n até Bucareste (estimativa, heurística)
# f(n): estimativa do custo total do caminho que passa por n

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: funções de apoio para imprimir -----
def resumo_fronteira(fronteira):
    """texto curto com a fronteira: Cidade(f) separadas por vírgula."""
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={f})')
    return ', '.join(partes)

# ---- PASSO 3: a busca A*, recebendo o grafo e a heurística -----
def busca_astar(inicio, objetivo, grafo, heuristica, mostrar=True):
    """busca A* em grafo. devolve (caminho, custo) do melhor caminho, ou (None, infinito). cada nó da fronteira é uma tupla (f, g, cidade, caminho); o f fica na posição 0 para que a fronteira seja ordenada por f(n)."""
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    explorados = set()
    interacoes = 0
    if mostrar:
        print(f'Início da busca A* de {inicio} a {objetivo}:')

    while fronteira:
        interacoes += 1
        fronteira.sort(key=lambda no: no[0])
        f, g, cidade, caminho = fronteira[0]
        if mostrar:
            print(f'Interação {interacoes}: nó retirado = {cidade}, f = {f}, g = {g}, caminho = {caminho}')
            print(f'Fronteira: {resumo_fronteira(fronteira)}')

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
        for vizinho, custo_estrada in grafo[cidade]:
            if vizinho not in explorados:
                novo_g = g + custo_estrada
                novo_f = novo_g + heuristica[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

        if mostrar:
            fronteira.sort(key=lambda no: no[0])
            print(f'Fronteira após expandir {cidade}: {resumo_fronteira(fronteira)}')

    return None, float('inf')

# ----- PASSO 4: o programa principal -----
def main():
    inicio = 'Arad'
    objetivo = 'Bucharest'
    caminho, custo = busca_astar(inicio, objetivo, mapa_romenia, heuristica_bucareste)
    print()
    print('--- Resultado ---')
    if caminho is None:
        print(f'Não foi encontrado caminho de {inicio} a {objetivo}.')
    else:
        print(f'Caminho encontrado de {inicio} a {objetivo}:', ' -> '.join(caminho))
        print('Custo total =', custo, 'km')
        print('passos =', len(caminho) - 1, 'estradas')
    # teste de regressão: o livro diz 418 k, em 4 passos
    if custo == 418 and len(caminho) - 1 == 4:
        print('Teste de regressão OK: custo = 418 km, passos = 4')
    else:
        print('Teste de regressão falhou: custo =', custo, 'passos =', len(caminho) - 1)
    
    print()
    print('--- Outras origens (sem rastro) ---')
    for origem in ['Timisoara','Oradea','Craiova','Iasi']:
        caminho, custo = busca_astar(origem, objetivo, mapa_romenia, heuristica_bucareste, mostrar=False)
        print(f'{origem:<10} custo = {custo:>4} km ', ' -> '.join(caminho))

# ----- PASSO 5: só roda o main quando o arquivo é executado diretamente -----
if __name__ == '__main__':
    main()
