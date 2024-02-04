def find_min_coins(amount, coins):
    dp_table = [float('inf')] * (amount + 1)
    dp_table[0] = 0

    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp_table[i - coin] + 1 < dp_table[i]:
                dp_table[i] = dp_table[i - coin] + 1
                coin_used[i] = coin

    result = {}
    remaining_amount = amount
    while remaining_amount > 0:
        coin = coin_used[remaining_amount]
        result[coin] = result.get(coin, 0) + 1
        remaining_amount -= coin

    return result

coins = [50, 25, 10, 5, 2, 1]
amount = 113
result = find_min_coins(amount, coins)
print(result)
