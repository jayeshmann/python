
"""
input1: number of intersection
input2: number of path
input3: 2d array representing paths
input4: array representing damage at each intersection

output: minimum damage

input1: 8
input2: 11
input3: [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[3,1],[4,7],[5,2],[5,7],[6,5]]
input4: [1,1,5,1,11,10,2,1]

output: 12
"""


def maze(input1, input2, input3, input4):
    # create graph
    graph = {}
    for i in range(input1):
        graph[i] = []
    for i in range(len(input3)):
        graph[input3[i][0]].append(input3[i][1])
        graph[input3[i][1]].append(input3[i][0])

    # create dp table
    dp = {}
    for i in range(input1):
        dp[i] = [0] * input2
    dp[0][0] = input4[0]
    for i in range(1, input1):
        dp[i][0] = dp[i-1][0] + input4[i]

    # create bfs
    queue = [0]
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if dp[v][0] >= dp[i][0]:
                queue.append(i)
                dp[i][0] = dp[v][0] + input4[i]

    # find minimum
    return min(dp[-1])
