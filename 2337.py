class Solution(object):

    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        print("start=", start)
        print("target=", target)
        start_elems = list()
        target_elems = list()
        for elem in start:
            if elem != "_":
                start_elems.append(elem)
        for elem in target:
            if elem != "_":
                target_elems.append(elem)

        if start_elems != target_elems:
            return False

        starts = dict()
        starts["L"] = []
        starts["R"] = []
        for i, elem in enumerate(start):
            if elem == "L":
                starts["L"].append(i)
            if elem == "R":
                starts["R"].append(i)
        print("starts=", starts)

        targets = dict()
        targets["L"] = []
        targets["R"] = []
        for i, elem in enumerate(target):
            if elem == "L":
                targets["L"].append(i)
            if elem == "R":
                targets["R"].append(i)
            """
            The subsequence formed by removing _ should be same for start and target for them to be interconvertible.
            In the target, no L should be righter than the corresponding L in start and no R should be lefter than the corresponding R in start.
            """
        print("targets=", targets)
        for r_start, r_target in zip(starts["R"], targets["R"]):
            if r_start > r_target:
                return False

        for l_start, l_target in zip(starts["L"], targets["L"]):
            if l_start < l_target:
                return False
        return True


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

# this will not 
start = "_R"
target = "R"
'''
object = Solution()
print(object.canChange(start, target))
