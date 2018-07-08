import torch
import torch.nn as nn

import asset

class Actor(object):
	class DQN(nn.Module):
		def __init__(self):
			pass
		def forward(self):
			pass

	def __init__(self):
		self.target = self.DQN()
		self.policy = self.DQN()
		self.positions = {}
		self.transactions = []
		# self.optimizer = optim.RMSprop(policy_net.parameters())

	def move(self, device):
		# self.target.to(device)
		# self.policy.to(device)
		# self.target_net.load_state_dict(policy_net.state_dict())
		# self.target_net.eval()
		self.device = device

	def train(self, device):
		if self.device is None or device != self.device:
			self.move(device)

	def test(self, device):
		pass

	def buy(self, a, quantity, price, sellers):
		self.positions[a.symbol] = asset.Position(a, quantity, price)
		self.transactions.append(
			asset.Transaction(a, quantity, price, None, self, sellers))

	def sell(self, a, quantity, price, buyer):
		if quantity > self.positions[a.symbol].quantity:
			quantity = self.positions[a.symbol].quantity
			print "Trying to sell more than actor owns"

		self.positions[a.symbol].quantity -= quantity
		buy_price = self.positions[a.symbol].price
		self.transactions.append(
			asset.Transaction(a, quantity, buy_price, price, buyer, [self]))

	def performance(self):
		total_gain_loss = 0.
		total_bought = 0.
		total_sold = 0.
		for t in transactions:
			total_gain_loss += t.gain_loss()
			total_bought += t.quanity * t.buy_price
			total_sold += t.quantity * t.total_sold

		return total_gain_loss, total_bought / total_sold


