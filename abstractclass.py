from abc import ABC,abstractmethod
from random import *

class TradeBot:
	def get_data(self,item:str):
		data = [50000,30000,40000,100000]		
		return choice(data)
		
		
	@abstractmethod		
	def profit_trade(self):
		pass
	
	@abstractmethod		
	def lose_trade(self):
		pass
	
	def confirm(self,item):
		item_price = self.get_data(item)
		profit_trade = self.profit_trade()
		lose_trade = self.lose_trade()
		profit = item_price/100
		
		if profit_trade:	
			total = item_price+profit
			print('profit -',profit)
			print('you sold your item with price',total)		
		else:	
			total = item_price - profit
			print('lose -',profit)
			print('you sold your item with price',total)		
			
	
class NormalTradeBot(TradeBot):
		def profit_trade(self):
			
		def lose_trade(self):
			return True
					
		
k = NormalTradeBot()
k.lose_trade()
k.confirm('k')
	