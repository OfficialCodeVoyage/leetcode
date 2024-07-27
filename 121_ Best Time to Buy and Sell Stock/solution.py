# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#


def sellstock(prices):
    # counter = max(prices)
    # postocut = 0
    # price_to_buy = 0
    # for i in prices:
    #     if i < counter:
    #         counter = i
    #         postocut = prices[i]
    #         price_to_buy = i
    #
    # newlist = prices[postocut:]
    # max_val = max(newlist)
    # profit = max_val - price_to_buy
    # return profit

    # counter = max(prices)
    # postocut = min(prices)
    # pos = 0
    # for i, price in enumerate(prices):
    #     if price == postocut:
    #         pos = i
    # newlist = prices[pos:]
    # max_val = max(newlist)
    # profit = max_val - postocut
    # return profit

    #using 2 pointers approach
    max_profit = 0
    lenght_list = len(prices)
    pointer1 = 0
    pointer2 = 1

    while pointer2 < lenght_list:
        if prices[pointer1] > prices[pointer2]:
            pointer1 = pointer2

        else:
            check_profit = prices[pointer2] - prices[pointer1]
            if check_profit > max_profit:
                max_profit = check_profit
        pointer2 += 1


    return max_profit


# prices = [7,1,5,3,6,4]
#
# prices = [7, 6, 4, 3, 1]

prices = [2, 1, 4]

#prices = [2, 4, 1]

print(sellstock(prices))
