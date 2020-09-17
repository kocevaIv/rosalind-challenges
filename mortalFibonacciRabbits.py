# returns the number of rabbits pairs after n months if they die after m months
def wabbitSeason(n, m):
    rabbit_pairs=[1,1]
    for month in range(2,n):
        if month < m:
            rabbit_pairs.append(rabbit_pairs[month-1]+rabbit_pairs[month-2])
        else:
            rabbit_pairs.append(sum(rabbit_pairs[month-m:-1]))
    return rabbit_pairs