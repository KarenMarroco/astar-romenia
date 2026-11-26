# 🗺️ Busca A* na Romênia (`astar-romenia`)

Implementação passo a passo do algoritmo de busca informada **A\*** (*A-Star*) em Python para encontrar a rota de menor custo entre **Arad** e **Bucareste** (`Bucharest`).

> **Disciplina:** Engenharia de Software — Laboratório de Python  

---

## 🎯 Sobre o Problema e o Algoritmo

O objetivo é encontrar o caminho mais curto (menor quilometragem) no mapa rodoviário da Romênia combinando a distância real já percorrida com uma estimativa heurística admissível (distância em linha reta até Bucareste):

$$f(n) = g(n) + h(n)$$

* **$g(n)$:** custo real acumulado desde a cidade de origem até o nó $n$ (em km).
* **$h(n)$:** distância estimada em linha reta do nó $n$ até `Bucharest`.
* **$f(n)$:** custo total estimado da viagem passando por $n$.

---

## 📂 Estrutura do Projeto (Fases)

O desenvolvimento foi dividido em 6 fases incrementais e seus respectivos desafios práticos:

| Fase | Arquivo(s) | Descrição |
| :--- | :--- | :--- |
| **Fase 0** | `README.md`, `.gitignore` | Configuração do ambiente (Python, Git, VS Code) e criação do repositório. |
| **Fase 1** | `mapa.py`, `fase1_explorar.py`, `desafio1.py` | Estruturação do grafo (`dict`, `list`, `tuple`) e da heurística $h(n)$. |
| **Fase 2** | `fase2_caminhos.py`, `desafio2.py` | Cálculo de custo de estradas, caminhos completos e valores $g(n)$, $h(n)$ e $f(n)$. |
| **Fase 3** | `fase3_fronteira.py`, `desafio3.py` | Criação do nó de busca `(f, g, cidade, caminho)` e ordenação da fronteira. |
| **Fase 4** | `fase4_expandir.py`, `desafio4.py` | Função `expandir()` e controle de cidades visitadas com o conjunto `explorados` (`set`). |
| **Fase 5** | `fase5_busca.py`, `desafio5.py` | Implementação completa do laço `while` da busca A\* e teste de objetivo ao retirar o nó. |
| **Fase 6** | `a_estrela.py`, `desafio6.py` | Programa final com rastro detalhado, teste de regressão, `main()` e outras origens. |

---
