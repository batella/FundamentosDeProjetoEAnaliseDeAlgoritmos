import heapq

# Função para calcular a heurística de Manhattan
def heuristica(x, y, x_final, y_final):
    return abs(x - x_final) + abs(y - y_final)

# Função para o Algoritmo A*
def a_star(labirinto):
    # Encontre as posições de 'S' (início) e 'E' (final)
    inicio = None
    final = None
    linhas = len(labirinto)
    colunas = len(labirinto[0])

    for i in range(linhas):
        for j in range(colunas):
            if labirinto[i][j] == 'S':
                inicio = (i, j)
            elif labirinto[i][j] == 'E':
                final = (i, j)

    if not inicio or not final:
        return "Sem solução"  # Se não houver 'S' ou 'E'

    # Movimentos possíveis (cima, esquerda, baixo, direita) em ordem fixa
    movimentos = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # A* (algoritmo de busca)
    open_list = []
    heapq.heappush(open_list, (0 + heuristica(inicio[0], inicio[1], final[0], final[1]), 0, inicio))  # f, g, posição
    came_from = {}  # Para reconstruir o caminho
    g_score = {inicio: 0}
    
    while open_list:
        _, g, atual = heapq.heappop(open_list)

        if atual == final:
            # Reconstruir o caminho
            caminho = []
            while atual in came_from:
                caminho.append(atual)
                atual = came_from[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho

        for movimento in movimentos:
            vizinho = (atual[0] + movimento[0], atual[1] + movimento[1])

            # Verifique se a célula vizinha está dentro dos limites e se não é um obstáculo
            if 0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas and labirinto[vizinho[0]][vizinho[1]] != '1':
                # Cálculo do custo g para o vizinho
                g_vizinho = g + 1
                if vizinho not in g_score or g_vizinho < g_score[vizinho]:
                    g_score[vizinho] = g_vizinho
                    f_score = g_vizinho + heuristica(vizinho[0], vizinho[1], final[0], final[1])
                    heapq.heappush(open_list, (f_score, g_vizinho, vizinho))
                    came_from[vizinho] = atual

    return "Sem solução"

# Função para destacar o caminho no labirinto
def exibir_labirinto_com_caminho(labirinto, caminho):
    for x, y in caminho:
        if labirinto[x][y] != 'S' and labirinto[x][y] != 'E':
            labirinto[x][y] = '*'
    for linha in labirinto:
        print(' '.join(str(celula) for celula in linha))

# Função para ler a matriz de entrada
def ler_matriz():
    print("Por favor, insira o labirinto linha por linha.")
    print("Use 'S' para o ponto inicial, 'E' para o ponto final, 0 para espaços livres e 1 para obstáculos.")
    matriz = []
    
    while True:
        try:
            linha = input("Digite uma linha (ou pressione Enter para terminar): ")
            if linha == "":
                break  # Termina a entrada se a linha estiver vazia
            linha_lista = linha.split()
            if all(item in ['0', '1', 'S', 'E'] for item in linha_lista):
                matriz.append(linha_lista)
            else:
                print("Linha inválida. Por favor, insira apenas 0, 1, S ou E.")
        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")
    
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
        print(f'Menor caminho (em coordenadas): {caminho}')
        print('Labirinto com o caminho destacado:')
        exibir_labirinto_com_caminho(labirinto, caminho)

if __name__ == "__main__":
    main()
