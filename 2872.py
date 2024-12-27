from collections import defaultdict


class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        print(edges)
        adjacencyList = defaultdict(list)
        for elem in edges:
            node1, node2 = elem[0], elem[1]
            adjacencyList[node1].append(node2)
            adjacencyList[node2].append(node1)

        print(adjacencyList)
        # res is number of components after valid splits, usint list to represent so that I can access it in dfs func
        res = [0]

        def dfs(cur, parent):
            '''
            calculate the total sum of subtree rooted at current node,
            this is done by traversing to all possible edges from current node,
            except for going back to the parent node, to stop infinite loop
                infinite loop is avoided by simply not going to parent because,
                    the graph is a tree, so there are no cycles, acyclic graph,
                    so no need to maintain a visited set to stop revisiting nodes
            this is building up sum from bottom up
            '''

            # since we only want to consider the subtree from current node,
            # we have to set the total to equal value of current node
            # when we recurse upwards, it would be in or after the for loop below, so total in that node's subtree
            # would be maintained
            total = values[cur]
            for child in adjacencyList[cur]:
                if child != parent:
                    total += dfs(child, cur)

            if total % k == 0:
                res[0] += 1

            # returning total of current subtree upwards
            return total

        dfs(0, -1)
        return res[0]
