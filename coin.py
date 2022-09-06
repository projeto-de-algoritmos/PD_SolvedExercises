class Solution:
    def coinChange(coins, amount):
    
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]

    ## Entradas
    coins = [2]
    amount = 3

    print(coinChange(coins, amount))