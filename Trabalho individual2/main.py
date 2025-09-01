def max_min_select(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2
    max1, min1 = max_min_select(arr, low, mid)
    max2, min2 = max_min_select(arr, mid + 1, high)

    final_max = max(max1, max2)
    final_min = min(min1, min2)

    return final_max, final_min


if __name__ == "__main__":
    entrada = input("Digite os números separados por espaço: ")
    numeros = list(map(int, entrada.strip().split()))
    
    if not numeros:
        print("Lista vazia. Digite pelo menos um número.")
    else:
        maior, menor = max_min_select(numeros, 0, len(numeros) - 1)
        print(f"Maior elemento: {maior}")
        print(f"Menor elemento: {menor}")
