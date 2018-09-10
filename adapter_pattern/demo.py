from adapter_pattern.external import Human, Synthesizer

# 新的需求组件
class Computer:
	def __init__(self, name):
		self._name = name

	def __str__(self):
		return "Computer ==> {} ".format(self._name)

	def execute(self):
		print("The computer {} is running!".format(self._name))


# 适配器
class Adapter:

	# adapted_obj是将要被适配的对象
	# adapted_method是适配的函数字典，key为客户端调用的代码，value是组件提供的接口
	def __init__(self, adapted_obj, adapted_methods):
		self._adapted_obj = adapted_obj
		self.__dict__.update(adapted_methods)

	def __str__(self):
		return str(self._adapted_obj)


def main():
	syth = Synthesizer("Moog")
	human = Human("Bob")

	objs = [Computer("Apple")]
	objs.append(Adapter(syth, dict(execute=syth.play)))
	objs.append(Adapter(human, dict(execute=human.sing)))

	for item in objs:
		print(str(item))
		item.execute()


if __name__ == '__main__':
	main()
