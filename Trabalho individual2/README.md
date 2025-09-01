## Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select) em Python - Caio Batella

## 1. Descrição do projeto

### Lógica do Algoritmo MaxMin Select (linha a linha)

```python
def max_min_select(arr, low, high):
    # Define a função principal recursiva. Recebe:
    # arr: lista de números inteiros.
    # low: índice inicial da sublista.
    # high: índice final da sublista.

    if low == high:
        # Caso base 1: se há apenas um elemento, ele é tanto o maior quanto o menor.
        return arr[low], arr[low]

    if high == low + 1:
        # Caso base 2: se há dois elementos, compara diretamente.
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide a lista ao meio
    mid = (low + high) // 2

    # Chamada recursiva para cada metade
    max1, min1 = max_min_select(arr, low, mid)
    max2, min2 = max_min_select(arr, mid + 1, high)

    # Combinação dos resultados parciais
    final_max = max(max1, max2)
    final_min = min(min1, min2)

    return final_max, final_min


if __name__ == "__main__":
    # Entrada do usuário: números separados por espaço
    entrada = input("Digite os números separados por espaço: ")
    numeros = list(map(int, entrada.strip().split()))

    if not numeros:
        # Verifica se a lista está vazia
        print("Lista vazia. Digite pelo menos um número.")
    else:
        # Chamada da função MaxMin Select
        maior, menor = max_min_select(numeros, 0, len(numeros) - 1)
        print(f"Maior elemento: {maior}")
        print(f"Menor elemento: {menor}")
```


## 2. Como Executar o Projeto

### Pré-requisitos
- Python 3 instalado.

### Passos:
1. Salve o código em um arquivo `main.py`.
2. No terminal, execute:
   ```bash
   python main.py
   ```
3. Insira o array com os números separados por um espaço quando solicitado.\
 Exemplo: 2 3 45 1 8 11

4. O programa exibirá o maior e o menor elemento do array.

## 3. Relatório Técnico



Este relatório apresenta uma análise detalhada da complexidade do algoritmo **MaxMin Select**, implementado de forma recursiva com divisão e conquista.

---

### Contagem de Operações (Comparações)

O algoritmo busca encontrar **simultaneamente** o maior e o menor elemento em uma lista de `n` elementos.

#### Abordagem Ingênua (para comparação):

- Para encontrar o menor: `n - 1` comparações.
- Para encontrar o maior: `n - 1` comparações.
- **Total**: `2n - 2` comparações.

#### Abordagem com MaxMin Select:

- O algoritmo divide a lista em duas partes e resolve recursivamente.
- Para **cada par de elementos**, faz 1 comparação para identificar o maior e o menor.
- Ao combinar os resultados das duas metades, realiza **2 comparações**: uma para os maiores e outra para os menores.

#### Exemplo de contagem:

Para `n = 8`:

1. Divide o problema em duas metades de 4 elementos.
2. Cada metade é dividida até chegar em subproblemas de tamanho 1 ou 2.
3. Cada par gera 1 comparação.
4. A cada combinação, são feitas 2 comparações (1 para o maior, 1 para o menor).

#### Fórmula Geral:

- Quando `n` é par:
  - Número total de comparações ≈ `3n / 2 - 2`
- Quando `n` é ímpar:
  - O número de comparações é um pouco maior, mas ainda é `O(n)`.

#### Conclusão:

A contagem de operações mostra que o número total de comparações cresce linearmente com o tamanho da entrada. Portanto, a complexidade é: O(n)

## Aplicação do Teorema Mestre

Considere a recorrência para o algoritmo *MaxMin Select*:\
 T(n) = 2T(n/2) + O(1)

### Etapas da Análise

-   Identifique os parâmetros da fórmula:

 T(n) = a ⋅ T(n / b) + f(n) 

-   **a = 2**

-   **b = 2**

-   **f(n) = O(1)**

-   Cálculo de log_b a:\
    \`log₂(2) = 1 ⇒ p = 1\`

-   Comparação de f(n) com n\^p:\
    \`f(n) = O(1)\` é \`O(n\^0)\`, e **0 \< 1**, ou seja:\
    \`f(n) = O(n\^(p - ε))\` para algum ε \> 0

-   Caso do Teorema Mestre:\
    Este é o **Caso 1** do Teorema Mestre.

------------------------------------------------------------------------

## Conclusão com Teorema Mestre

\`\`\` T(n) = Θ(n) \`\`\`

Ou seja, a complexidade assintótica também é **linear** pela aplicação
formal do Teorema Mestre.