import ccxt
conn = ccxt.kraken()
prices = conn.fetchTickers()

class Coin:
    def __init__(self, abbr, name):
        self.name = name
        self.pair = abbr + "/USD"
    def get_price(self):
        return prices[self.pair]['last']
    def __repr__(self):
        s1 = f"The Price of {self.name} is:".ljust(35, ' ')
        s2 = "${:8,.2f}".format(self.get_price())
        return s1 + s2
        #return f"the price of {self.name} is {self.get_price()}."


coins = [
        Coin('BTC', 'Bitcoin'),
        Coin('BCH', 'Bitcoin Cash'),
        Coin('ETH', 'Ethereum'),
        Coin('LTC', 'Litecoin Cash')
]
print(' ')
for c in coins:
    print(c)
print(' ')
