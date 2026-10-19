class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # returning maxprofit i can earn, 0 if no profit possible
        # keep a counter of the minimum sell price
        # keep a counter of the maximum sell price indez so far, updating as I      traverse

        #check to see if the maxprofit increases, if so, updated sell index

        # keep track ofn the sell value as current index

        #returning the MAX profit as a value, which two indices give maxProfit


        min_price = prices[0];
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
            
            if prices[i] < min_price:
                min_price = prices[i]
        return max_profit




        