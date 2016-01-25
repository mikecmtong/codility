def solution(A):
    min_price = 300000
    max_profit = 0
    
    for price in A:
        temp_profit = price - min_price
        if temp_profit < 0:
            min_price = price
        elif temp_profit > max_profit:  
            max_profit = temp_profit
    return max_profit
