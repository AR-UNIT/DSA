def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    def process():
        # Write your code here
        arrays = []
        for i in range(N):
            if C[i] == "P":
                arrays.append(C[i:i + Y + 1 + Y])
        print(arrays)

        def getPossiblePhotosCount(array):
            res = 0
            # get all the P indexes
            Ps = [i for i, x in enumerate(array) if x == "P"]
            # get all the B indexes
            Bs = [i for i, x in enumerate(array) if x == "B"]
            for p in Ps:
                for b in Bs:
                    if (b - p > X and p < b):
                        arr = array[p:b + 1]
                        As = [i for i, x in enumerate(arr) if x == "A"]
                        # check if there is any A contained between P and B
                        for a in As:
                            if a - p >= X and b - a >= X and b - a <= Y and a - p <= Y:
                                res += 1
                            print(p,a,b)
            return res

        count = 0
        for a in arrays:
            count += getPossiblePhotosCount(a)
        print(count)
        return count

    count = process()
    C = C[::-1]
    count += process()

    print(count)
    return count

N = 10
C = "PABABAPBAP"
X = 1
Y = 3


# N = 5
# C = "APABA"
# X = 1
# Y = 2

# N = 5
# C = "APABA"
# X = 2
# Y = 3

# N = 8
# C = ".PBAAP.B"
# X = 1
# Y = 3

# N = 12
# C = "PAB.BAP.APB."
# X = 3
# Y = 3

# N = 10
# C = "B.PA.AB.P."
# X = 3
# Y = 3

# N = 9
# C = "AP.BA.PB."
# X = 3
# Y = 3


# N = 38
# C = "P.A.B.P.B.A.A.P.B.P.A.B.A.P.B.A.A.P.B."
# X = 3
# Y = 3

getArtisticPhotographCount(N, C, X, Y)
