# -*- coding: utf-8 -*-
import time


# 动态规划，自顶向下解决凑领钱的问题
def coin_combine(coins, amount):
    """
    :param coins: a list, contain coins type, for example: [1, 2, 5]
    :param amount: target amount, int, for example: 100
    :return: minimum combine num
    """

    memory = dict()

    def dp(n):
        if n in memory:
            return memory[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n - coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
            memory[n] = res if res != float('INF') else -1
        return memory[n]
    return dp(amount)


# 动态规划，自底向上解决凑领钱的问题
def coins_combine(coins_list, amount):
    """
    des see function coin_combine's func_doc
    """
    dp = [amount+1] * (amount + 1)
    dp[0] = 0

    for i in range(len(dp)):
        for coin in coins_list:
            if i - coin < 0:
                continue
            else:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return -1 if dp[amount] == amount + 1 else dp[amount]


if __name__ == '__main__':

    start = time.time()
    print coin_combine([1, 2, 5, 10], 100)
    print time.time() - start

    start1 = time.time()
    print coins_combine([1, 2, 5], 100)
    print time.time() - start1
