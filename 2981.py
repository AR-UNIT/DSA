class Solution(object):
    def getAllSubarrays(self, s):
        r_limit = len(s)
        all_subarrays = []
        visited = set()

        def backtrack(L, R):
            if (L, R) in visited:
                return
            print("backtrack(" + str(L) + "," + str(R) + ")")
            # Base case: If indices are out of bounds, stop recursion
            if R > r_limit:
                return

            if L < R:
                all_subarrays.append(s[L:R])
                visited.add((L, R))
                print(s[L:R])

            if R < r_limit and (R == 0 or s[R] == s[R - 1]):
                backtrack(L, R + 1)
            else:
                backtrack(L + 1, L + 2)

            '''
            only making a backtrack call to start search from next index of earliest R, where R is just right of L,
            this starts the recursion from L+1, L+1, instead, (i.e) similar to starting from (0,0), (1,1), xetc,
            and avoids doing repeated decision tree steps if we did (L+1, R), and (L, R+1) 
            '''
            if R == L + 1:
                backtrack(L + 1, L + 1)

            print("recursing out of: " + "backtrack(" + str(L) + "," + str(R) + ")")

        backtrack(0, 0)
        return all_subarrays
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        subarrays = self.getAllSubarrays(s)
        counts = Counter(subarrays)
        prev_len = 0
        res = ""
        for subarray, count in counts.items():
            if count >= 3 and prev_len < len(subarray):
                prev_len = len(subarray)
                res = subarray
        return -1 if res == "" else res





# string = "abcdef"
# string = "aaaa"
# string = "abcaba"
string = "fafff"
# string = "abc"
# string = "abcd"
# string = "abb"
object = Solution()
# print(object.getAllSubarrays(string))
print(object.maximumLength(string))
