s = "abbca"
n = len(s)
res = []
totalAppeal = 0

def calculateAppeal(substring):
    count = dict()
    for c in substring:
        if c in count:
            continue
        else:
            count[c] = 1

    substringAppeal = 0
    for key, value in count.items():
        substringAppeal += value
    return substringAppeal


for i in range(0, n):
    for j in range(n - i):
        substring = s[j:j + i + 1]
        # if substring not in res:
        res.append(substring)
        calculateAppeal(substring)
        totalAppeal += calculateAppeal(substring)

print(res)
print(totalAppeal)