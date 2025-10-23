
# Caminho Hamiltoniano em Python 
Autor: Caio Batella

##  Descrição do Projeto

Este projeto implementa um algoritmo em Python para verificar a existência de um **Caminho Hamiltoniano** em um grafo. Um Caminho Hamiltoniano é um caminho que passa por **todos os vértices exatamente uma vez**, sem repetições.

### Lógica do Algoritmo (linha a linha)

- Define a função recursiva que tenta construir um Caminho Hamiltoniano.

```python
def is_hamiltonian_path(graph, path, visited, n):
```
- Se o caminho atual já passou por todos os vértices, é um caminho válido.

```python
    if len(path) == n:
        return True
```
- Pega o último vértice do caminho e explora seus vizinhos.

```python
    last_node = path[-1]
    for neighbor in graph[last_node]:
```
- Visita o vizinho não visitado e o adiciona ao caminho.

```python
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
```
- Chama recursivamente para continuar a busca.

```python
            if is_hamiltonian_path(graph, path, visited, n):
                return True
```
- Se a busca falhar, desfaz a escolha (backtracking).

```python
            path.pop()
            visited[neighbor] = False
```
- Se nenhum caminho válido foi encontrado, retorna falso.

```python
    return False
```
- Função principal que tenta encontrar um caminho Hamiltoniano a partir de cada vértice.

```python
def find_hamiltonian_path(graph):
```
- Inicializa a busca a partir de cada vértice do grafo.

```python
    n = len(graph)
    for start in range(n):
        path = [start]
        visited = [False] * n
        visited[start] = True
```
- Retorna o caminho encontrado, se existir.

```python
        if is_hamiltonian_path(graph, path, visited, n):
            return path
```
- Se nenhum caminho Hamiltoniano for encontrado, retorna `None`.

```python
    return None
```
- Função principal de execução do programa com entrada do usuário.

```python
def main():
```
- Lê o número de vértices.

```python
    print("Digite o número de vértices:")
    n = int(input())
```
- Lê o número de arestas.

```python
    print("Digite o número de arestas:")
    m = int(input())
```
- Inicializa o grafo como lista de adjacência.

```python
    graph = {i: [] for i in range(n)}
```
- Lê as arestas e monta o grafo.

```python
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # grafo não orientado
```
- Executa o algoritmo e imprime o resultado.

```python
    path = find_hamiltonian_path(graph)
    if path:
        print("Caminho Hamiltoniano encontrado:", path)
    else:
        print("Não existe Caminho Hamiltoniano.")
```


---

##  Como Executar o Projeto

1. Instale o Python (versão 3.6 ou superior).
2. Salve o arquivo como `main.py`.
3. Execute no terminal:

```bash
python main.py
```

4. Insira os dados do grafo conforme solicitado (exemplo):

```
Digite o número de vértices:
4
Digite o número de arestas:
5
Digite as arestas no formato 'u v':
0 1
0 2
1 2
1 3
2 3
```

---

##  Relatório Técnico

###  Análise da Complexidade Computacional

####  Classes P, NP, NP-Completo e NP-Difícil

1. O problema do Caminho Hamiltoniano pertence à classe **NP-Completo**.
2. Justificativa:
   - Está em NP porque, dado um caminho, podemos verificar em tempo polinomial se ele é Hamiltoniano.
   - É NP-Completo porque é **tão difícil quanto os problemas mais difíceis de NP**.
   - Relaciona-se diretamente ao Problema do Caixeiro Viajante (TSP), que também é NP-Completo. A diferença é que o TSP exige um ciclo com custo mínimo, enquanto o Caminho Hamiltoniano busca apenas um caminho.

---

###  Análise da Complexidade Assintótica de Tempo

1. **Complexidade Temporal**: O algoritmo de backtracking tem complexidade **O(n!)**, onde `n` é o número de vértices.
2. Justificativa:
   - Para cada vértice, tentamos colocá-lo em cada posição possível no caminho → permutações.
   - O método de análise é **contagem de operações recursivas** com base na profundidade e ramificação da recursão.

---

###  Aplicação do Teorema Mestre

1. **Não é possível aplicar o Teorema Mestre** diretamente.
2. Justificativa:
   - O Teorema Mestre aplica-se a **recorrências do tipo divisão e conquista**, como `T(n) = aT(n/b) + f(n)`.
   - Este algoritmo é **puramente recursivo com backtracking**, não uma divisão regular de problemas.

---

###  Análise dos Casos de Complexidade

1. **Pior Caso**:
   - Todos os caminhos possíveis são testados até concluir que não existe caminho Hamiltoniano.
   - Complexidade: O(n!) — extremamente custoso para grafos grandes.

2. **Melhor Caso**:
   - O primeiro caminho testado já é Hamiltoniano.
   - Complexidade: O(n) — a recursão é mínima.

3. **Caso Médio**:
   - Depende da estrutura do grafo e da ordem dos vizinhos.
   - Complexidade prática entre O(n) e O(n!), mas tende ao pior caso em grafos densos e grandes.

4. **Impacto no desempenho**:
   - Em grafos pequenos, o algoritmo funciona bem.
   - Em grafos maiores, rapidamente se torna inviável sem otimizações (como poda ou heurísticas).
