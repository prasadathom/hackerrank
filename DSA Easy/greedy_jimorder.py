def jimOrders(orders):
    total = {}
    for i in range(len(orders)):
        total[i + 1] = sum(orders[i])
    return [item[0] for item in sorted(total.items(), key=lambda x: x[1])]

#a god way to optimize size and code
