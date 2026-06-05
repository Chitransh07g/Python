#prices = [7, 1, 5, 3, 6, 4] # expected: 5
#prices = [7, 1, 5, 3, 6, 4, 35]  # expected: 34
prices = [7, 6, 5, 4, 3, 2, 1]
#prices = [7, 3, 5, 1, 4, 2]      # expected: 3

last = len(prices)
profit = 0
minimum = min(prices)
for price in prices:
    if price <= minimum and prices.index(price) < (last -1):
        buy_day = price
        alo = prices[prices.index(price): ] 
        profit = (max(alo))- buy_day
        break 

if profit > 0 :
    print (f"Your profit is :-{profit}")
else :
    print(f"Sorry")    