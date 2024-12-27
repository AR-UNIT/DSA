days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

# [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 30), (11, 31)]
n = len(days)

print(list(enumerate(days)))

# chosen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
chosen = [11]
# chosen = [19]

def checkValidChosen(chosen):
    if len(chosen) == 1 and days[chosen[0]-1] >= 30:
        return False
    for i in range(len(chosen)-1):
        if days[chosen[i+1]-1] - days[chosen[i]-1] > 30:
            return False
    return True

print(checkValidChosen(chosen))

print(float("inf"))




