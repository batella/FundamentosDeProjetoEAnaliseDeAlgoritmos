# Identificação e Preenchimento de Regiões em um Grid 2D  
### Algoritmo Flood Fill (DFS Iterativo)

Este projeto implementa um sistema capaz de identificar e preencher automaticamente todas as regiões conectadas em um grid 2D composto por células navegáveis (`0`) e obstáculos (`1`), utilizando o algoritmo Flood Fill.

O usuário informa:

- as dimensões do grid  
- os valores de cada linha  
- uma coordenada inicial  

O programa preenche essa região inicial com uma cor (número) específica. Em seguida, todas as demais regiões navegáveis desconectadas também são preenchidas com cores diferentes.

Esse tipo de problema é comum em:

- jogos 2D  
- algoritmos de segmentação de imagem  
- sistemas de preenchimento gráfico  
- análises de caminhos e agrupamento de terrenos  

## Objetivo do Projeto

Resolver o problema de conseguir detectar  automaticamente regiões de zeros conectados em um grid e atribuir a cada região uma cor distinta (um identificador numérico crescente), permitindo visualizar facilmente os agrupamentos de células navegáveis.

A solução:

- marca a região conectada à célula inicial com `2`;  
- percorre o grid;  
- cada vez que encontra um zero não preenchido, aplica novamente o Flood Fill com um novo identificador.  

## Introdução ao Problema

Considere um mapa representado por uma matriz, onde:

- `0` representa terreno livre (navegável);  
- `1` representa um obstáculo.  

O objetivo é identificar todas as áreas de terreno livre conectadas ortogonalmente (cima, baixo, esquerda e direita).  
Cada área conectada deve receber uma cor própria.

## Funcionamento do Algoritmo Flood Fill (Implementado)

A solução utiliza DFS iterativo com uma pilha (`stack`), evitando problemas de estouro de recursão.

Fluxo do algoritmo:

1. Começa na célula inicial informada pelo usuário.  
2. Verifica se ela é navegável (`0`).  
3. Caso positivo, essa célula é colocada na pilha.  
4. Enquanto houver células na pilha:
   - Remove uma célula da pilha.  
   - Verifica se está dentro dos limites e se é navegável.  
   - Marca essa célula com a cor atual.  
   - Adiciona seus vizinhos ortogonais à pilha.  
5. Quando a primeira região termina, o programa percorre o grid por completo:
   - Ao encontrar um `0`, executa novamente o Flood Fill com uma nova cor.  

## Como Executar o Projeto

### 1. Verifique se o Python 3 está instalado

```bash
python --version
```

### 2. Salve o código em um arquivo, por exemplo:

```
flood_fill.py
```

### 3. Execute o programa

```bash
python flood_fill.py
```

### 4. Forneça as informações solicitadas:

- número de linhas  
- número de colunas  
- linhas do grid  
- coordenadas iniciais  

## Exemplos de Funcionamento

### Exemplo 1

Entrada:

```
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
```

Coordenadas iniciais:

```
(0, 0)
```

Saída:

```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

### Exemplo 2

Entrada:

```
0 1 0 0
0 1 1 0
0 0 0 1
1 1 0 0
```

Coordenadas iniciais:

```
(2, 1)
```

Saída:

```
5 1 5 5
5 1 1 5
5 5 5 1
1 1 6 6
```

### Exemplo 3

Entrada:

```
0 1 0 0 1 0 0
0 1 0 1 1 0 1
0 0 0 1 0 0 0
1 1 0 1 0 1 0
0 0 0 0 0 0 1
```

Coordenadas iniciais:

```
(2, 2)
```

Saída possível:

```
2 1 3 3 1 4 4
2 1 3 1 1 4 1
2 2 3 1 5 5 5
1 1 3 1 5 1 5
6 6 6 6 6 6 1
```

## Conclusão

Este projeto ilustra o processo de identificar regiões conectadas em grades 2D, utilizar DFS de forma iterativa e colorir cada área com tonalidades distintas. Além disso, o algoritmo pode ser ampliado para incluir a consideração de conexões diagonais, gerar visualizações coloridas mais ricas ou integrar-se a interfaces gráficas para uma experiência mais completa.
