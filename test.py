def knapsack(W, weight, cost, n):
    K = [ [0 for x in range(W + 1)] for x in range(n + 1) ]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i - 1] <= j:
                K[i][j] = max(cost[i - 1] + K[i - 1][j - weight[i-1]], K[i - 1][j] ) 
            else:
                K[i][j] = K[i - 1][j] 
    return K 

weight = [1, 3, 4]
cost = [1500, 2000, 3000]
maxWeight = 4
n = len(weight)
bp = knapsack(maxWeight, weight, cost, n)
print(bp)