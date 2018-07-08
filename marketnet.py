import argparse
import json
import random

import asset
import actor

MAX_TRANSACTIONS = 3

def main(args):
	with open(args.config, 'r') as f:
		config = json.load(f)

	market = asset.Market()
	assets = [asset.gen_asset() for _ in xrange(config['assets'])]
	actors = [actor.Actor() for _ in xrange(config['actors'])]
	for a in assets:
		movement_mean = random.uniform(-1.0, 1.0)
		movement_std_dev = random.uniform(0.1, 2.0)
		for _ in xrange(config['memory']):
			for _ in xrange(0, random.randint(0, MAX_TRANSACTIONS)):
				buyer, seller = random.sample(range(config['actors']), 2)
				change = random.normalvariate(movement_mean, movement_std_dev)
				settle_price = (1 + change / 100.) * a.price
				if a.symbol not in actors[seller].positions:
					quantity = random.randint(0, a.outstanding)
					a.outstanding -= quantity
					actors[buyer].buy(a, quantity, settle_price, [market])
				elif actors[seller].positions[a.symbol].quantity > 0:
					shares = a.outstanding + actors[seller].positions[a.symbol].quantity
					quantity = random.randint(0, shares)
					if quantity > actors[seller].positions[a.symbol].quantity: 
						quantity_from_seller = actors[seller].positions[a.symbol].quantity
					else:
						quantity_from_seller = quantity
					a.outstanding -= (quantity - quantity_from_seller)
					a.price = settle_price
					actors[buyer].buy(a, quantity, settle_price, [actors[seller], market])
					actors[seller].sell(a, quantity_from_seller, settle_price, actors[buyer])
				a.price = settle_price
		print a

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--config',
		type=str,
		help='Configuration file')
	parser.add_argument(
		'--num_gpus',
		type=int,
		default=0,
		help='Number of CUDA devices available')
	args = parser.parse_args()
	main(args)