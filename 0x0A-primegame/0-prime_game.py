#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    Maria, Ben = 0, 0
    n = max(nums)
    primes = [True for t in range(1, n + 1, 1)]
    primes[0] = False
    for i, prime in enumerate(primes, 1):
        if i == 1 or not prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for t, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        Ben += primes_count % 2 == 0
        Maria += primes_count % 2 == 1
    if Maria == Ben:
        return None
    if Maria > Ben:
        return "Maria"
    else:
        return "Ben"
