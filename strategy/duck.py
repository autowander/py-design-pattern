from quack import Quack						#引入两种策略
from flyWithWings import FlyWithWings


class Duck(object):
	
	def __init__(self, flyBehavior, quackBehavior):
		self.quackBehavior_ = quackBehavior
		self.flyBehavior_ = flyBehavior
	
	def performQuack(self):
		self.quackBehavior_.quack()		#执行制定behavior的策略
	
	def performFly(self):
		self.flyBehavior_.fly()			#执行制定behavior的策略
	
	def display(self):
		pass

	def swim(self):
		print('ALL ducks float, even decos!')
	
		
class MallardDuck(Duck):

	def __init__(self):
		super().__init__(FlyWithWings(), Quack())		#传入策略
														#不同的鸭子可以传入不同的策略
	def display(self):
		print("I'm a real Mallard duck")
		
		
class MiniDuckSimulator():
	def main():
		mallard = MallardDuck()
		mallard.performFly()
		mallard.performQuack()
		mallard.display()
		
		
if __name__ == "__main__":
	MiniDuckSimulator.main()