# Função iterativa para encontrar a subsequência crescente mais longa de uma determinada lista
def findLIS(arr):
    # caso básico
    if not arr:
        return []

    # LIS[i] armazena a subsequência crescente mais longa da sublista
    # `arr[0…i]` que termina com `arr[i]`
    LIS = [[] for _ in range(len(arr))]

    # LIS[0] denota a subsequência crescente mais longa terminando em `arr[0]`
    LIS[0].append(arr[0])

    # começa a partir do segundo elemento da lista
    for i in range(1, len(arr)):

        # faz para cada elemento na sublista `arr[0…i-1]`
        for j in range(i):

            # encontre a subsequência crescente mais longa que termina com `arr[j]`
            # onde `arr[j]` é menor que o elemento atual `arr[i]`

            if arr[j] < arr[i] and len(LIS[j]) > len(LIS[i]):
                LIS[i] = LIS[j].copy()

        # inclui `arr[i]` em `LIS[i]`
        LIS[i].append(arr[i])

    # `j` irá armazenar o índice de LIS
    j = 0
    for i in range(len(arr)):
        if len(LIS[j]) < len(LIS[i]):
            j = i

    # LIS de impressão
    print(LIS[j])


if __name__ == '__main__':
    arr = [9, 9, 4, 2]
    findLIS(arr)