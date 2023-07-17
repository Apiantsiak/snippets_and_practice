def queue_time(customers, n):
    tills = [0] * n
    for customer in customers:
        tills[tills.index(min(tills))] += customer
    return max(tills)


if __name__ == '__main__':
    queue_time([2, 2, 3, 3, 4, 4], 2)
