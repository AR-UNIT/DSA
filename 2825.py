import string

alphabet = string.ascii_lowercase
letters = list(alphabet)
print(letters, len(letters))

print(ord("a"))
print(ord("z"))

# str1 = "abc"
# str2 = "ad"
# str1 = "ab"
# str2 = "d"
str1 = "zc"
str2 = "ad"
# str1 = "dby"
# str2 = "z"

ords1 = [ord(x) for x in str1]
ords2 = [ord(x) for x in str2]

print(str1, ords1)
print(str2, ords2)

from collections import defaultdict

enumerated_list = enumerate(ords1)
enumerated_dict = defaultdict(list)

# for index,elem in enumerated_list:
#     enumerated_dict[elem].append(index)
#
# '''
# enumerated_dict contains number -> sorted index of instances
# '''
# print(enumerated_dict)
#
# for c in ords2:
#     if enumerated_dict[c] or enumerated_dict[c-1]:



i = 0 # itr for ords2
j = 0 # itr for ords1

while i < len(ords2) and j < len(ords1):
    if ords2[i] == ords1[j] or (ords2[i] == ords1[j] + 1) or (ords2[i] == 97 and (ords1[j] == 122)):
        i += 1
    j += 1

print(i, i == len(ords2))

