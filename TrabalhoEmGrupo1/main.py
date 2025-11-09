import heapq

# Função para calcular a heurística de Manhattan
def heuristica(x, y, x_final, y_final):
    return abs(x - x_final) + abs(y - y_final)

# Função para o Algoritmo A*
def a_star(labirinto):
    inicio = final = None
    linhas = len(labirinto)
    colunas = len(labirinto[0])

    # Localiza S e E
    for i in range(linhas):
        for j in range(colunas):
            if labirinto[i][j] == 'S':
                inicio = (i, j)
            elif labirinto[i][j] == 'E':
                final = (i, j)

    if not inicio or not final:
        return "Sem solução"

    movimentos = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # A* (f, g, posição)
    h_inicial = heuristica(inicio[0], inicio[1], final[0], final[1])
    open_list = [(h_inicial, 0, inicio)]
    
    came_from = {}
    g_score = {inicio: 0}

    while open_list:
        _, g, atual = heapq.heappop(open_list)

        if atual == final:
            caminho = []
            while atual in came_from:
                caminho.append(atual)
                atual = came_from[atual]
            caminho.append(inicio)
            return caminho[::-1]

        ax, ay = atual
        for dx, dy in movimentos:
            nx, ny = ax + dx, ay + dy
            
            if 0 <= nx < linhas and 0 <= ny < colunas and labirinto[nx][ny] != '1':
                g_vizinho = g + 1
                
                if (nx, ny) not in g_score or g_vizinho < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = g_vizinho
                    f_vizinho = g_vizinho + heuristica(nx, ny, final[0], final[1])
                    heapq.heappush(open_list, (f_vizinho, g_vizinho, (nx, ny)))
                    came_from[(nx, ny)] = atual

    return "Sem solução"

# Função para destacar o caminho no labirinto
def exibir_labirinto_com_caminho(labirinto, caminho):
    for x, y in caminho:
        if labirinto[x][y] not in ('S', 'E'):
            labirinto[x][y] = '*'
    for linha in labirinto:
        print(' '.join(linha))

# Função para ler a matriz de entrada
def ler_matriz():
    print("Por favor, insira o labirinto linha por linha.")
    print("Use 'S' para o ponto inicial, 'E' para o ponto final, 0 para espaços livres e 1 para obstáculos.")

    matriz = []
    valido = {'0', '1', 'S', 'E'}

    while True:
        linha = input("Digite uma linha (ou pressione Enter para terminar): ").strip()
        if linha == "":
            break
        linha_lista = linha.split()
        
        if all(c in valido for c in linha_lista):
            matriz.append(linha_lista)
        else:
            print("Linha inválida. Por favor, insira apenas 0, 1, S ou E.")

    return matriz

# Leitura da entrada e execução
def main():
    labirinto = ler_matriz()

    if not labirinto:
        print("Labirinto vazio. Encerrando o programa.")
        return

    caminho = a_star(labirinto)
    
    if caminho == "Sem solução":
        print(caminho)
    else:
        print(f"Menor caminho (em coordenadas): {caminho}")
        print("Labirinto com o caminho destacado:")
        exibir_labirinto_com_caminho(labirinto, caminho)

if __name__ == "__main__":
    main()
