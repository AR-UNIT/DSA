class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """

    def getAllSubsets(self, s):
        def backtrack(start, path):
            # Append the current path as a string to all_strings
            all_strings.append("".join(path))

            for j in range(start, len(s)):
                # Avoid duplicates if the same character is encountered consecutively
                if j > start and s[j] == s[j - 1]:
                    continue
                path.append(s[j])  # Include the current character
                backtrack(j + 1, path)  # Recurse with the next character
                path.pop()  # Backtrack: remove the last character


        s = ''.join(sorted(s))  # Sort to handle duplicates and ensure order
        all_strings = []
        backtrack(0, [])
        return all_strings

# string = "abcdef"
string = "abc"
object = Solution()
print(object.getAllSubsets(string))
