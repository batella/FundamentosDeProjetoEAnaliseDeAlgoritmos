# Implementação do Algoritmo de Karatsuba em Python

## 1. Descrição do Projeto

Este projeto implementa o **algoritmo de Karatsuba** para multiplicação eficiente de dois números inteiros grandes, usando a técnica de **dividir para conquistar**.

### Linha a linha da função `karatsuba(x, y)`:

```python
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
```
- **Caso base**: se qualquer número tiver apenas um dígito, retorna a multiplicação direta para evitar recursão infinita.

```python
    n = max(len(str(x)), len(str(y)))
    m = n // 2
```
- Determina o número de dígitos dos operandos e divide o maior pela metade (parte inteira).

```python
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)
```
- Separa cada número em **parte alta** e **parte baixa**, com base nos dígitos.

```python
    z0 = karatsuba(low1, low2)
    z2 = karatsuba(high1, high2)
    z1 = karatsuba(low1 + high1, low2 + high2) - z2 - z0
```
- Realiza três multiplicações recursivas:
  - `z0` = produto das partes baixas.
  - `z2` = produto das partes altas.
  - `z1` = produto das somas das partes (low+high) subtraindo `z2` e `z0`.

```python
    return (z2 * 10**(2*m)) + (z1 * 10**m) + z0
```
- Combina os resultados usando o deslocamento adequado em base 10 e retorna o produto final.

## 2. Como Executar o Projeto

### Pré-requisitos
- Python 3 instalado.

### Passos:
1. Salve o código em um arquivo `main.py`.
2. No terminal, execute:
   ```bash
   python main.py
   ```
3. Insira os dois números inteiros quando solicitado.
4. O programa exibirá o resultado da multiplicação.

## 3. Relatório Técnico

### 3.1. Complexidade Ciclomática

A complexidade ciclomática é dada por:

\[ M = E - N + 2P \]

Onde:
- **E** = número de **arestas** (transições possíveis no fluxo),
- **N** = número de **nós** (blocos de decisão ou comando),
- **P** = componentes conexos (aqui, **P = 1**).

####  Fluxo de Controle

1. Início da função.
2. Checagem do **caso base** `if x < 10 or y < 10`: decisão.
   - Se verdadeiro → multiplica e retorna (ramo 1).
   - Se falso → continua (ramo 2).
3. Cálculo de `n`, `m`.
4. Divisão em `high1`, `low1`, `high2`, `low2`.
5. Chamada recursiva para `z0`.
6. Chamada recursiva para `z2`.
7. Chamada recursiva para `z1`.
8. Combinação e retorno.

#### Construção do Grafo

- **Nós (N)**: 9
- **Arestas (E)**: 10
- **P = 1**

\[ M = 10 - 9 + 2 * 1 = 3 \]

A função possui **3 caminhos independentes**:
1. Entrada → caso base → retorno.
2. Entrada → recursão → caminhos recursivos → retorno.
3. Fluxo interno de operações após condição.

### 3.2. Complexidade Assintótica

#### Temporal (T(n))

Karatsuba segue a recorrência:

\[ T(n) = 3T(n/2) + O(n) \]

Pela relação mestre:

T(n) = O(n^(log₂ 3)) ≈ O(n^1.585)


#### Melhor Caso
- Quando pelo menos um dos números de entrada tem apenas um dígito.
- O algoritmo retorna imediatamente com uma multiplicação direta.
- **Complexidade:** \( O(1) \)

#### Caso Médio e Pior Caso
- Quando ambos os números têm muitos dígitos.
- O algoritmo realiza todas as divisões e chamadas recursivas.
- **Complexidade:** \( \Theta(n^{\log₂ 3}) -> approx \Theta(n^{1.585}) \)

#### Espacial (S(n))

- Espaço por chamada recursiva: \( O(n) \)
- Profundidade da recursão: \( O(\log n) \)
- Espaço total: \( O(n \log n) \)
