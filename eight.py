def maxUniqueSplit(s):
    """
    :type s: str
    :rtype: int
    """

    split_entries = list()

    res = list()
    n = len(s)

    def split(string, i, split_entries):

        if string in split_entries:
            return

        # if we reached the end of the string, we can return
        if i == n:
            # print(res)
            if(len(string) == n):
                res.append(string)
            else:
                res.append(split_entries[:])
            return


        split_entries.append(string)
        split(string, i + 1, split_entries)

        include_char_string = string + s[i]

        split(include_char_string, i+1, split_entries)

    split("", 0, split_entries)
    print(res)
    length_of_elements = list(map(lambda x: len(x), res))
    return max(length_of_elements)
s = "ababccc"
print(maxUniqueSplit(s))
