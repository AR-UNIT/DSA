def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    res = 0
    for i, cell in enumerate(C):
        for j in range(X, Y + 1):
            for k in range(X, Y + 1):
                if (i + j + k) >= N:
                    break
                if ''.join([cell, C[i + j], C[i + j + k]]) in ('PAB', 'BAP'):
                    res += 1
    print(res)
    return res


N = 10
C = "PABABAPBAP"
X = 1
Y = 3
getArtisticPhotographCount(N, C, X, Y)
