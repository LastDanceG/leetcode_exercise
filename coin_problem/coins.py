# -*- coding: utf-8 -*-
import time


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


if __name__ == '__main__':

    import sys
    sys.setrecursionlimit(10000)

    start = time.time()
    print coin_combine([1, 2, 5, 10], 1000)
    print time.time() - start
