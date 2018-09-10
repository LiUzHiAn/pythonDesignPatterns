"""
	以下是工厂方法模式的示例。

	假设需要根据不同文件格式解析文件内容，我们可以根据文件的格式定义不同连接器

	然后再利用一个工厂方法来维护解析器
"""
import json
import xml.etree.ElementTree as eTree


# json解析类
class JsonConnector:
	def __init__(self, filepath):
		self.data = dict()
		with open(filepath, mode="r", encoding="utf-8") as f:
			self.data = json.load(f)

	@property
	def parse_data(self):
		return self.data


# xml解析类
class XMLConnector:
	def __init__(self, filepath):
		self.tree = eTree.parse(filepath)

	@property
	def parse_data(self):
		return self.tree


# 工厂方法
def connector_factory(filepath):
	if filepath.endswith(".json"):
		connector = JsonConnector
	elif filepath.endswith(".xml"):
		connector = XMLConnector
	else:
		raise ValueError("Cannot connect to *** {} ***".format(filepath))
	return connector(filepath)


# 对工厂方法包装
def connect_to(filepath):
	factory = None
	try:
		factory = connector_factory(filepath)
	except ValueError as e:
		print(e)
	return factory


def main_1():
	# 异常测试
	sqlite_factory = connect_to("test.sq3")
	print("\n")

	# json factory
	json_factory = connect_to("test.json")
	print(json_factory)
	json_data = json_factory.parse_data
	print("found: {} donuts".format(len(json_data)))
	print("\n")
	for item in json_data:
		print("name: {}".format(item["name"]))
		print("price: ${}".format(item["ppu"]))
		for topping in item["topping"]:
			print("id: {}".format(topping["id"]))
			print("type: {}".format(topping["type"]))
		print("\n")

	# xml factory
	xml_factory = connect_to("test.xml")
	xml_data = xml_factory.parse_data
	liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
	for liar in liars:
		print("First name: {}".format(liar.find("firstName").text))
		print("Last name: {}".format(liar.find("lastName").text))
		for num in liar.find("phoneNumbers"):
			print("phone number ({}):".format(num.attrib['type']), num.text)


"""
	以下是抽象工厂模式的示例。
	
	抽象工厂是对工厂方法的衍生。通常一开始时使用工厂方法，因为它更简单。如果后来发现应用需要许多工厂方法，那么将创建
	一系列对象的过程合并在一起更合理，从而最终引入抽象工厂。
	
	有一个游戏，分别面向小孩和成人
"""

"""面向小孩的"""


class Frog:
	def __init__(self, name):
		self._name = name

	def __str__(self):
		return self._name

	def interact_with(self, obstacle):
		print('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))


class Bug:
	def __str__(self):
		return "a bug"

	def action(self):
		return "eats it"


class FrogWorld:
	def __init__(self, player_name):
		print(self)
		self._player_name = player_name

	def __str__(self):
		return '\n\n\t------ Frog World-------'

	def make_character(self):
		return Frog(self._player_name)

	def make_obstacle(self):
		return Bug()


"""面向成人的"""


class Wizard:
	def __init__(self, name):
		self._name = name

	def __str__(self):
		return self._name

	def interact_with(self, obstacle):
		print('{} the Wizard encounters {} and {}!'.format(self, obstacle, obstacle.action()))


class Ork:
	def __str__(self):
		return "an evil ork"

	def action(self):
		return "kills it"


class WizardWorld:
	def __init__(self, player_name):
		print(self)
		self._player_name = player_name

	def __str__(self):
		return '\n\n\t------ Wizard World-------'

	def make_character(self):
		return Wizard(self._player_name)

	def make_obstacle(self):
		return Ork()


"""抽象工厂"""


class GameEnvironment:
	def __init__(self, factory):
		self._hero = factory.make_character()
		self._obstacle = factory.make_obstacle()

	def play(self):
		self._hero.interact_with(self._obstacle)


# 函数validate_age()提示用户提供一个有效的年龄。
# 如果年龄无效，则会返回一个元组，其第一个元素设置为False。
# 如果年龄没问题，元素的第一个元素则设置为True
def validate_age(name):
	try:
		age = int(input("Welcom {}. How old are you? ".format(name)))
	except ValueError as e:
		print("The input age is invalid, please try again...")
		return (False, -1)
	return (True, age)


def main_2():
	name = input("Hello, What's your name? ")
	age_valid = False
	while not age_valid:
		age_valid, age = validate_age(name)
	# 其实这条语句就相当于一个工厂方法调用
	game = FrogWorld if age < 18 else WizardWorld
	gameEnvironment = GameEnvironment(game(name))
	gameEnvironment.play()


if __name__ == '__main__':
	main_2()

"""
	总结:两种模式都可以用于以下几种场景： 
		(a)想要追踪对象的创建时，
		(b)想要将对象的创建与使用解耦时，
		(c)想要优化应用的性能和资源占用时
		
	Time:2018/9/3 21:31
	Andy
"""
