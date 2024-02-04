coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(total):
    count_coins = {}
    for coin in coins:
        count = total // coin
        if count > 0:
            count_coins[coin] = count
        total = total - coin * count
    return count_coins

print(find_coins_greedy(113))