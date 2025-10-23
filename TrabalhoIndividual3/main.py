def is_hamiltonian_path(graph, path, visited, n):
    if len(path) == n:
        return True

    last_node = path[-1]
    for neighbor in graph[last_node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)

            if is_hamiltonian_path(graph, path, visited, n):
                return True

            path.pop()
            visited[neighbor] = False

    return False

def find_hamiltonian_path(graph):
    n = len(graph)

    for start in range(n):
        path = [start]
        visited = [False] * n
        visited[start] = True

        if is_hamiltonian_path(graph, path, visited, n):
            return path

    return None

def main():
    print("Digite o número de vértices:")
    n = int(input())

    print("Digite o número de arestas:")
    m = int(input())

    graph = {i: [] for i in range(n)}

    print("Digite as arestas no formato 'u v' (sem aspas), onde u e v são vértices conectados (de 0 até n-1):")
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # Remover esta linha se o grafo for orientado

    path = find_hamiltonian_path(graph)
    if path:
        print("Caminho Hamiltoniano encontrado:", path)
    else:
        print("Não existe Caminho Hamiltoniano.")

if __name__ == "__main__":
    main()
