""" 
@author Jayesh Mann
@created 22-09-2021
"""

m = 10**4
n = 10**2
# dynamic programming table pre-computation
table = [[None for _ in range(m+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i <= 1 or j <= 1:
            table[i][j] = 1

for i in range(n+1):
    for j in range(m+1):
        if i < 2 or j < 2:
            pass
        elif i > j:
            table[i][j] = table[j][j]
        elif i == j:
            table[i][j] = 2*table[i][j-1]
        else:
            table[i][j] = 2*table[i][j-1] - table[i][j-i-1]


def solve(x, y):
    # ans is precomputed using dp table modulo 10^9 + 7
    return table[y][x] % (10**9 + 7)


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    # read a list of integers, 2 in this case
    # also, list(map(int, input().split(" "))) does the same thing
    c, b = [int(s) for s in input().split(" ")]
    print("{}".format(solve(c, b)))
