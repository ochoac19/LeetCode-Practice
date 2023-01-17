class Buy_Sell:
    def maxProfit(self, prices: list[int]) -> int:
        
        buy, sell = 0, 1
        max_profit= 0
        
        while sell < len(prices):
            #
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]     #Calculates profit between two points 
                max_profit = max(max_profit, profit)     #Returns the highest of the new profit or old profit.
            
            else:
                buy = sell  #sets the buy pointer to the new min
            sell += 1 #Increments to compare
            
        return max_profit
    print (maxProfit(None, [7,1,5,3,6,4] ))
        