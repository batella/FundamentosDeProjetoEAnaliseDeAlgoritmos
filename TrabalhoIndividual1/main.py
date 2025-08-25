def karatsuba(x, y):
    # Caso base otimizado: usa multiplicação normal para números pequenos pois não vale a pena usar karatsuba para valores pequenos
    if x < 10000 or y < 10000:
        return x * y

    # Calcula o número de dígitos dos maiores operandos, divide por 2 e guarda em m
    n = max(x.bit_length(), y.bit_length())
    m = n // 2

    # Converte m de bits para número de base 10 aproximado
    m10 = 10 ** (m // 3)  # fator de conversão baseado em log(2)/log(10)

    high1, low1 = divmod(x, m10)
    high2, low2 = divmod(y, m10)

    z0 = karatsuba(low1, low2)
    z2 = karatsuba(high1, high2)
    z1 = karatsuba(low1 + high1, low2 + high2) - z2 - z0

    return (z2 * m10**2) + (z1 * m10) + z0

def main():
    try:
        x = int(input("Digite o primeiro número inteiro: "))
        y = int(input("Digite o segundo número inteiro: "))
        resultado = karatsuba(x, y)
        print(f"\nResultado da multiplicação: {x} * {y} = {resultado}")
    except ValueError:
        print("Por favor, digite apenas números inteiros válidos.")

if __name__ == "__main__":
    main()
