# Função iterativa para encontrar o comprimento da subsequência crescente mais longa
# de uma determinada lista
def LIS(arr):
    # caso básico
    if not arr:
        return 0

    # Lista # para armazenar soluções de subproblemas. `L[i]` armazena o comprimento
    # da subsequência crescente mais longa que termina com `arr[i]`
    L = [0] * len(arr)

    # a subsequência crescente mais longa que termina em `arr[0]` tem comprimento 1
    L[0] = 1

    # começa a partir do segundo elemento da lista
    for i in range(1, len(arr)):
        # faz para cada elemento na sublista `arr[0…i-1]`
        for j in range(i):
            # encontre a subsequência crescente mais longa que termina com `arr[j]`
            # onde `arr[j]` é menor que o elemento atual `arr[i]`
            if arr[j] < arr[i] and L[j] > L[i]:
                L[i] = L[j]

        # incluem `arr[i]` no LIS
        L[i] = L[i] + 1

    # retorna a subsequência crescente mais longa (com comprimento máximo)
    return max(L)


if __name__ == '__main__':
    arr = [9, 9, 4, 2]
    print('The length of the LIS is', LIS(arr))