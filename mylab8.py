def backpack(maxWeight, weight, cost, n):
    bp = [[0 for x in range(maxWeight+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(maxWeight+1):
            if i == 0 or j == 0:
                bp[i][j] = 0
            elif weight[i-1] <= j:
                bp[i][j] = max(cost[i-1] + bp[i-1][j-weight[i-1]], bp[i-1][j])
            else:
                bp[i][j] = bp[i-1][j]
    return bp

weight = [1, 3, 4, 1, 1]
cost = [1500, 2000, 3000, 2000, 1000]
maxWeight = 4
n = len(weight)
bp = backpack(maxWeight, weight, cost, n)
print(bp[n][maxWeight])