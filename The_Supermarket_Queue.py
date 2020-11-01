def queue_time(customers, n):
    l = [0] * n
    for i in customers:
        l[l.index(min(l))] += i
    return max(l)


print(queue_time([], 2))

print(queue_time([2, 2, 3, 3, 4, 4], 2))
