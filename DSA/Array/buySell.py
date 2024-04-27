'''
Input: prices = [7,1,5,3,6,4]
Output: 5

'''

prices = [7,2,5,3,6,4]
#=====================================================================================================================================
# python way

buy = min(prices)
sell = max(prices[prices.index(buy):])

print(sell - buy)

#=====================================================================================================================================
# actual way

buy, sell = 111111111,-1
for num in range(len(prices)):
    if buy > prices[num] :
        buy = prices[num]


for j in range(prices.index(buy),len(prices)):
    if sell < prices[j] :
        sell = prices[j]


print(sell-buy)