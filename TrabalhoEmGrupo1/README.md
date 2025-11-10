# Fundamentos de Projeto e Análise de Algoritmos
**Alunos:** Caio Batella, Raul Fernandes Goulart, Ian Nascimento Rocha e Rodrigo Diniz Carvalho

**Professor:** João Paulo Carneiro Aramuni  
**Disciplina:** Fundamentos de Projeto e Análise de Algoritmos – PUC Minas  
**Descrição:** Implementação do algoritmo A* para resolução de labirintos.

---

## 1. Nome da Atividade
**Atividade:** Implementação do Algoritmo A* (Busca Heurística)

---

## 2. Introdução

Este projeto tem como objetivo implementar o **algoritmo A\*** (*A-star*), um dos mais importantes métodos de **busca heurística** usados em **Inteligência Artificial**, **robótica** e **jogos digitais** para encontrar o **menor caminho entre dois pontos** em um grafo ou matriz.

O algoritmo utiliza uma função heurística (neste caso, a **distância de Manhattan**) para estimar o custo restante até o destino e escolher o caminho mais promissor a cada passo.

O problema abordado é o de **resolução de labirintos**, onde o usuário define um ponto inicial (`S`), um ponto final (`E`), espaços livres (`0`) e obstáculos (`1`).  
O programa processa essa matriz e retorna o **menor caminho possível** entre `S` e `E`, destacando visualmente o percurso encontrado.

---

## 3. Estrutura e Funcionamento

### 3.1. Representação do Labirinto

O labirinto é representado como uma **matriz bidimensional**, onde cada célula pode conter:

| Símbolo | Significado |
|----------|-------------|
| `S` | Ponto inicial (*Start*) |
| `E` | Ponto final (*End*) |
| `0` | Espaço livre (caminho possível) |
| `1` | Obstáculo (caminho bloqueado) |

---

### 3.2. Heurística de Manhattan

A heurística adotada é a **distância de Manhattan**, calculada pela fórmula:

\[
h(x, y) = |x - x_{final}| + |y - y_{final}|
\]

Essa função mede a distância entre dois pontos considerando apenas movimentos horizontais e verticais, sem diagonais ideal para ambientes em grade, como labirintos.

---

### 3.3. Funcionamento do Algoritmo A\*

O algoritmo A* combina o **custo real (g)** com a **estimativa heurística (h)**, buscando minimizar:

\[
f(n) = g(n) + h(n)
\]

**Etapas principais:**
1. Identificar os pontos `S` e `E` na matriz.  
2. Inserir o ponto inicial em uma **fila de prioridade** (heap).  
3. Em cada iteração:
   - Selecionar o nó com o menor valor de `f(n)`.  
   - Expandir seus vizinhos (cima, baixo, esquerda, direita).  
   - Atualizar o custo real `g` e a estimativa `h`.  
   - Marcar o caminho mais promissor até alcançar o destino.  
4. Quando `E` é encontrado, reconstruir o caminho percorrido.  
5. Caso não exista solução, exibir `"Sem solução"`.

---

## 4. Como Rodar

### Pré-requisitos
- **Python 3.8** ou superior instalado;
- Nenhuma biblioteca externa necessária (apenas o módulo padrão `heapq`).

### Execução

1. Execute o arquivo principal no terminal:

   ```bash
   python main.py
   
2. Insira o labirinto linha por linha conforme o modelo abaixo.

3. Pressione Enter em uma linha vazia para encerrar a entrada.
 
4. O programa exibirá o menor caminho e o labirinto com o trajeto destacado.

## 5. Exemplo de Execução

### Entrada

| Linha | Conteúdo |
|-------|-----------|
| 1 | S 0 1 0 |
| 2 | 0 0 0 0 |
| 3 | 1 1 0 E |

---

### Saída Esperada

| Tipo de Saída | Conteúdo |
|----------------|-----------|
| **Menor caminho (em coordenadas)** | `[(0,0), (1,0), (1,1), (1,2), (2,2), (2,3)]` |
| **Labirinto com o caminho destacado** |  S * 1 0, 0 * * * , 1 1 * E |

---

## 6. Análise de Complexidade

### 6.1. Complexidade Temporal
- **Melhor caso:** `O(n)`  quando o destino está próximo do ponto inicial.  
- **Pior caso:** `O(n log n)`  quando é necessário explorar quase todo o labirinto.  
- O uso da heurística de Manhattan torna o algoritmo mais eficiente ao evitar caminhos improváveis.

### 6.2. Complexidade Espacial
O algoritmo mantém listas de nós abertos e visitados.  
Complexidade espacial: `O(n)`, proporcional ao número de células do labirinto.

---

## 7. Conclusão

A implementação do **Algoritmo A\*** demonstra como heurísticas podem otimizar a busca de caminhos em grafos e matrizes.  
Essa abordagem é amplamente utilizada em áreas que exigem **eficiência e precisão**, como:
- **Sistemas de navegação autônoma;**
- **Planejamento de trajetórias de robôs;**
- **IA em jogos (pathfinding);**
- **Roteamento em redes.**

O projeto evidencia o equilíbrio entre **custo e desempenho**, mostrando a importância da heurística de Manhattan na tomada de decisões durante o processo de busca.




