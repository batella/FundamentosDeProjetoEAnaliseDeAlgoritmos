def flood_fill(grid, x, y, color):
    n = len(grid)
    m = len(grid[0])
    stack = [(x, y)]

    while stack:
        i, j = stack.pop()

        # Evita chamadas de verificação repetidas
        if 0 <= i < n and 0 <= j < m and grid[i][j] == 0:
            grid[i][j] = color

            # Adiciona vizinhos
            stack.append((i - 1, j))
            stack.append((i + 1, j))
            stack.append((i, j - 1))
            stack.append((i, j + 1))


def preencher_todas_as_regioes(grid, x_inicial, y_inicial):
    n = len(grid)
    m = len(grid[0])
    color = 2

    # Preenche região inicial
    if 0 <= x_inicial < n and 0 <= y_inicial < m and grid[x_inicial][y_inicial] == 0:
        flood_fill(grid, x_inicial, y_inicial, color)
        color += 1

    # Preenche outras regiões
    for i in range(n):
        linha = grid[i]  # otimização: acesso direto
        for j in range(m):
            if linha[j] == 0:
                flood_fill(grid, i, j, color)
                color += 1

    return grid


def imprimir_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))
    print()


def main():
    # Entrada dimensões
    n = int(input("Digite o número de linhas do grid (n): "))
    m = int(input("Digite o número de colunas do grid (m): "))

    print("Digite o grid linha por linha, separando os valores com espaço (ex: 0 1 0 0):")

    grid = []
    for i in range(n):
        while True:
            linha = list(map(int, input(f"Linha {i}: ").split()))
            if len(linha) == m:
                grid.append(linha)
                break
            print("Número de colunas incorreto. Digite novamente.")

    # Entrada coordenadas
    x = int(input("Digite a coordenada x inicial: "))
    y = int(input("Digite a coordenada y inicial: "))

    print("\nGrid inicial:")
    imprimir_grid(grid)

    preencher_todas_as_regioes(grid, x, y)

    print("Grid preenchido:")
    imprimir_grid(grid)


if __name__ == "__main__":
    main()
