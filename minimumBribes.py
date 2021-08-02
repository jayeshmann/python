# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    count = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            return "Too chaotic"
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                count += 1
    return count


print(minimumBribes([1, 2, 3, 5, 4, 6, 7, 8]))
