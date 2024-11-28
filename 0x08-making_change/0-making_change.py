#!/usr/bin/python3
""" determine fewest number of coins needed to meet
a given amount total
"""


def makeChange(coins, total):
    """ calc how much change the total will require """
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        count = 0
        for i in coin:
            while(total >= i):
                count += 1
                total -= i
        if total == 0:
            return count
        return -1
