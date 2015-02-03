def dp_make_change(coinValueList, change, minCoins, coinsUsed):
	for cents in range(change+1):
		coinCount = cents
		newCoin = 1
		for j in [c for c in coinValueList if c <= cents]:
			if minCoins[cents-j]+1 < coinCount:
				coinCount = minCoins[cents-j]+1
				newCoin = j
		minCoins[cents] = coinCount
		coinsUsed[cents] = newCoin
	return minCoins[change]

def print_coins(coinsUsed, change):
	coin = change
	while coin > 0:
		thisCoin = coinsUsed[coin]
		print thisCoin
		coin = coin - thisCoin

amount = 63
coinList = [1, 5, 10, 21, 25]
coinsUsed = [0]*(amount+1)
coinCount = [0]*(amount+1)

print "Making change for ",amount," requires:"
print dp_make_change(coinList, amount, coinCount, coinsUsed)," coins!!!"
print "The coins used are:"
print_coins(coinsUsed, amount)
print "The used coins list is as follows:"
print coinsUsed