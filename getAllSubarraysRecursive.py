def getAllSubarrays(s):
    r_limit = len(s)
    all_subarrays = []

    def backtrack(L, R):
        print("backtrack(" + str(L) + "," + str(R) + ")")
        # Base case: If indices are out of bounds, stop recursion
        if R > r_limit:
            return

        if L < R:
            all_subarrays.append(s[L:R])
            print(s[L:R])

        backtrack(L, R + 1)

        '''
        only making a backtrack call to start search from next index of earliest R, where R is just right of L,
        this starts the recursion from L+1, L+1, instead, (i.e) similar to starting from (0,0), (1,1), etc,
        and avoids doing repeated decision tree steps if we did (L+1, R), and (L, R+1) 
        '''
        if R == L + 1:
            backtrack(L + 1, L + 1)

    backtrack(0, 0)
    return all_subarrays
