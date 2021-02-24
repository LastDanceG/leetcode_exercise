# -*- coding: utf-8 -*-
from __future__ import print_function
import time


# 斐波那契数列自顶向下递归
def helper(memory, n):

    if n == 1 or n == 2:
        memory[n] = 1
    if memory[n] != 0:
        return memory[n]
    memory[n] = helper(memory, n-1) + helper(memory, n-2)
    # print(memory[1:n])
    return memory[n]


def fib(n):
    if n < 0:
        return 0
    else:
        memory = [0] * (n + 1)
        memory[n] = helper(memory, n)
        return memory[n]


# 自下向上解法，dp数组迭代解法的优化，空间复杂度为O(1)
def fib2(n):
    if n == 1 or n == 2:
        return 1
    pre, current = 1, 1
    for i in range(3, n + 1):
        _sum = pre + current
        pre = current
        current = _sum
    return current


# dp数组迭代解法
def fib3(n):

    if n < 0:
        return 0
    if n == 1 or n == 2:
        return 1
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':

    start = time.time()
    for i in range(1, 50):
        print(fib2(i), end=',')
    print(time.time() - start)
