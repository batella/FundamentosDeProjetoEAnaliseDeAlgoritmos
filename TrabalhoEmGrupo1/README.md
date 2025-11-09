# Fundamentos de Projeto e Análise de Algoritmos
**Alunos:** Caio Batella, Raul Fernandes Goulart, Ian Nascimento Rocha  
**Professor:** João Paulo Carneiro Aramuni  
**Disciplina:** Fundamentos de Projeto e Análise de Algoritmos – PUC Minas  
**Descrição:** Implementação do algoritmo A* para resolução de labirintos.

---

## 1. Nome da Atividade
**Atividade:** Implementação do Algoritmo A* (Busca Heurística)

---

## 2. Descrição do Projeto

Este projeto implementa o **algoritmo A\*** (*A-star*), um dos métodos de busca heurística mais eficientes para encontrar o **menor caminho entre dois pontos** em um grafo ou matriz  neste caso, aplicado a um **labirinto**.

O algoritmo utiliza uma função heurística (distância de Manhattan) para estimar o custo restante até o destino e priorizar os caminhos mais promissores, equilibrando **exploração** e **otimização**.

O programa permite que o usuário insira um labirinto linha por linha, com símbolos representando o início, o fim, os espaços livres e os obstáculos.  
Em seguida, o algoritmo encontra e exibe o **menor caminho possível** entre o ponto inicial `S` e o ponto final `E`.

---

## 3. Estrutura e Funcionamento

### 3.1. Representação do Labirinto
O labirinto é representado como uma **matriz bidimensional** (lista de listas), onde cada célula pode conter:

| Símbolo | Significado |
|----------|-------------|
| `S` | Ponto inicial (*Start*) |
| `E` | Ponto final (*End*) |
| `0` | Espaço livre (caminho possível) |
| `1` | Obstáculo (caminho bloqueado) |

### 3.2. Heurística de Manhattan
A heurística utilizada é a **distância de Manhattan**, definida como:

\[
h(x, y) = |x - x_{final}| + |y - y_{final}|
\]

Essa função mede a distância entre dois pontos apenas em movimentos horizontais e verticais (sem diagonais), adequada para labirintos em grade.

### 3.3. Lógica do Algoritmo A\*
O A* combina o **custo real (g)** do caminho percorrido com uma **estimativa (h)** da distância até o objetivo, minimizando:

\[
f(n) = g(n) + h(n)
\]

Passos principais:
1. Localiza os pontos `S` (início) e `E` (fim) na matriz;  
2. Cria uma **fila de prioridade (heap)** com o ponto inicial e sua estimativa de custo;  
3. Em cada iteração:
   - Seleciona o nó com menor valor de `f(n)` (custo total estimado);
   - Gera seus vizinhos (cima, baixo, esquerda, direita);
   - Atualiza o custo acumulado `g` e a heurística `h` de cada vizinho;
   - Marca o caminho mais promissor até alcançar o destino;  
4. Quando o ponto final é encontrado, reconstrói o **caminho percorrido**;  
5. Caso não exista solução, retorna a mensagem `"Sem solução"`.

## 4. Como Rodar

### Pré-requisitos
- **Python 3.8** ou superior instalado;
- Nenhuma biblioteca externa necessária (somente o módulo padrão `heapq`).

## Exemplo de Execução

- Entrada:
  
|S 0 1 0|
|0 0 0 0|
|1 1 0 E|

- Saída:

  Menor caminho (em coordenadas): [(0,0), (1,0), (1,1), (1,2), (2,2), (2,3)]
Labirinto com o caminho destacado:

S * 1 0
0 * * *
1 1 * E



## 5. Análise de Complexidade
5.1. Complexidade Temporal

- Melhor caso: O(n)  quando o destino está próximo do ponto inicial.

- Pior caso: O(n log n)  quando é necessário explorar quase todo o labirinto.

- Geral: O algoritmo é eficiente pois evita percorrer caminhos improváveis graças à heurística de Manhattan.

5.2. Complexidade Espacial

Mantém listas de nós visitados e abertos;

Complexidade espacial: O(n), proporcional ao número de células do labirinto.

## 6. Conclusão

- A implementação do Algoritmo A* demonstra como heurísticas podem otimizar a busca de caminhos em grafos e matrizes.
- A abordagem é amplamente utilizada em IA, jogos, robótica móvel e sistemas de navegação, equilibrando custo e desempenho para alcançar resultados eficientes.





