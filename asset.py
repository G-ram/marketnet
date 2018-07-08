
import random
import string
import numpy as np

class Asset(object):
	def __init__(self, symbol, price, quantity):
		self.symbol = symbol
		self.price = price
		self.quantity = quantity
		self.outstanding = quantity

	def __str__(self):
		return "%s=> $%f, Total: %d outstanding: %d" % (
			self.symbol, self.price, self.quantity, self.outstanding)

def gen_asset():
	outstanding = random.randint(100, 1000)
	symbol = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
	price = random.uniform(1, 100)
	return Asset(symbol, price, outstanding)

class Position(object):
	def __init__(self, asset, quantity, price):
		self.asset = asset
		self.quantity = quantity
		self.price = price

class Transaction(object):
	def __init__(self, asset, quantity, buy_price, sell_price, buyer, sellers):
		self.asset = asset
		self.quantity = quantity
		self.buy_price = buy_price
		self.sell_price = sell_price
		self.buyer = buyer
		self.sellers = sellers

	def gain_loss(self):
		if self.sell_price is None: return 0
		return self.quantity * (self.sell_price - self.buy_price)

	def percent_gain_loss(self):
		if self.sell_price is None: return 0
		return (self.sell_price / self.buy_price)

class Market(object):
	def __init__(self):
		pass