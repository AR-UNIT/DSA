class Solution(object):
    def moveRight(self, start):
        i = len(start)-1
        while i >= 0:
            val = start[i]
            if val == "R" and i+1<len(start) and start[i+1] == "_":
                j = i+1
                while j+1 < len(start) and start[j+1] == "_":
                    j += 1
                start[i] = "_"
                start[j] = "R"
            else:
                i -= 1
        return start

    def moveLeft(self, start):
        i = 0
        while i < len(start):
            val = start[i]
            if val == "L" and i-1>-1 and start[i-1] == "_":
                j = i-1
                while j-1 > -1 and start[j-1] == "_":
                    j -= 1
                start[i] = "_"
                start[j] = "L"
            else:
                i += 1
        return start

    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        print("start =", start)
        start = list(start)
        start = self.moveRight(start)
        print("shifted_right_start =", "".join(start))
        start = self.moveLeft(start)
        print("shifted_left_start =", "".join(start))

        print("target =", target)
        target = list(target)
        target = self.moveRight(target)
        print("shifted_right_target =", "".join(target))
        target = self.moveLeft(target)
        print("shifted_left_start =", "".join(target))

        # target_elems = list()
        # for elem in target:
        #     if elem == "R":
        #         target_elems.append(elem)
        # return start_elems == target_elems


'''
if its an L, then ignore all "_" that came before it
'''

# start = "_L__R__R_"
# target = "L______RR"

'''
transformed
start = "L__RR"
target = "L______RR"
'''
#
# start = "_L__R__R_"'''
# transformed
# start = "_L__R__R_"
# '''
# target = "_L___R__R"
# start = "R_L_"
# target = "__LR"

'''
transformed
start = "RL_"
target = "LR"
'''

start = "_R"
target = "R_"
'''
transformed
start = "_R"
target = "R"
'''
object = Solution()
print(object.canChange(start, target))

