from bisect import bisect_left

days = [1,4,6,7,8,20]
costs = [2,7,15]


def mincostTickets(days, costs):
    """
    :type days: List[int]
    :type costs: List[int]
    :rtype: int
    """

    n = len(days)

    # storing day-> min cost required to travel upto this day, building solution bottom up
    dp = dict()

    # i is the index for days, which day are we on in dfs
    # when building dp solution, we can only return use [i] as key for dp, because
    #           i,total is not possible pair, because total is running amount, and expected result of dp
    #           BUT BETTER TO MAKE DP[I]
    from bisect import bisect_left
    def dfs(i, total):
        if i >= n:
            return total


        ## simply adding a if (i in dp) call here does not work because storing in dp[i] is not storing the
        ##          max value for every 
        # if (i in dp):
        #     return dp[i]

        next_day_index_1 = bisect_left(days, days[i] + 1)
        # dfs(next_day, total + costs[0])

        next_day_index_7 = bisect_left(days, days[i] + 7)
        # dfs(next_day, total + costs[1])

        next_day_index_30 = bisect_left(days, days[i] + 30)
        # dfs(i+30, total + costs[2])

        dp[i] = min(dfs(next_day_index_1, total + costs[0]), dfs(next_day_index_7, total + costs[1]),
                    dfs(next_day_index_30, total + costs[2]))
        print(dp)
        return dp[i]

    dfs(0, 0)
    print("Final DP:")
    print(sorted(dp.items()))
print(mincostTickets(days,costs))