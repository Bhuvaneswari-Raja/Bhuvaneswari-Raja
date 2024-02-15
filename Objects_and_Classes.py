import sys
import random

class Bot():

	def init(self, color, version):
		self.color = color
		self.version_no = version

	def add_nums(self, num1, num2):
		return num1 + num2

	def subtract_nums(self, num1,num2):
		return num1 - num2

	def bot_talk(self):
		print("hello homosapien! How are you doing?")

	def do_math(self,num1,num2):
		x = self.add_nums 

bot = Bot()
print(bot.add_nums(1,2))
print(bot.subtract_nums(1,2))
bot.bot_talk()
