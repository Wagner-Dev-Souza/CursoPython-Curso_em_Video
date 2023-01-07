import sys


# Função para encontrar o comprimento da subsequência crescente mais longa
def LIS(arr, i, n, prev):
    # Caso base: nada resta
    if i == n:
        return 0

    # caso 1: exclua o elemento atual e processe o
    # elementos restantes
    excl = LIS(arr, i + 1, n, prev)

    # caso 2: inclua o elemento atual se for maior
    # do que o elemento anterior em LIS
    incl = 0
    if arr[i] > prev:
        incl = 1 + LIS(arr, i + 1, n, arr[i])

    # retorna o máximo das duas opções acima
    return max(incl, excl)


if __name__ == '__main__':
    arr = [9, 9, 4, 2]

    print('The length of the LIS is', LIS(arr, 0, len(arr), -sys.maxsize))