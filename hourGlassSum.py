
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    result = []
    for i in range(0, 4):
        for j in range(0, 4):
            sum_hourglass = sum(arr[i][j:j+3]) + \
                arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            result.append(sum_hourglass)
    return max(result)
