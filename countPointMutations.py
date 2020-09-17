def countPointMutations(s, t):
    countMutations = 0
    for index in range(0, len(s)):
        if s[index] != t[index]:
            countMutations += 1
    return countMutations
