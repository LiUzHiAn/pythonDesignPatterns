"""
	工厂模式和建造者模式的区别：

	1.在工厂模式下，会立即返回一个创建好的对象；而在建造者模式下，仅在需
		要时客户端代码才显式地请求指挥者返回最终的对象
	2.工厂模式以单个步骤创建对象，而建造者模式以多个步骤创建对象，
		并且几乎始终会使用一个指挥者。

"""

"""工厂模式"""
Mini14 = "1.4GHz Mac mini"


class AppleFactory:
	class MacMini14:
		def __init__(self):
			self._memory = 4
			self._hdd = 500
			self._gpu = "Intel HD Graphics 5000"

		def __str__(self):
			return "memory:{},hdd:{},gpu:{},".format(self._memory, self._hdd, self._gpu)

	def build_computer(self, model):
		if model == Mini14:
			return self.MacMini14()
		else:
			print("对不起，我没法生产" + model)
			return None


def main_1():
	apple_factory = AppleFactory()
	model = input("你需要什么型号的电脑？")
	computer = apple_factory.build_computer(model)
	print(computer)


"""建造者模式"""


class Computer:

	def __init__(self, serial_number):
		self.serial = serial_number
		self._memory = None  # 单位为GB
		self._hdd = None  # 单位为GB
		self._gpu = None

	def __str__(self):
		return "memory:{},hdd:{},gpu:{},".format(self._memory, self._hdd, self._gpu)


# 专门配某种电脑的厂商
class ComputerBuilder:
	def __init__(self):
		self.computer = Computer('AG23385193')

	def add_memory(self, memory):
		self.computer._memory = memory

	def add_hdd(self, hdd):
		self.computer._hdd = hdd

	def add_gpu(self, gpu):
		self.computer._gpu = gpu


class HardwareEngineer:
	def __init__(self):
		self._builder = None

	def construct_computer(self, memory, hdd, gpu):
		self._builder = ComputerBuilder()
		self._builder.add_memory(memory)
		self._builder.add_hdd(hdd)
		self._builder.add_gpu(gpu)

	@property
	def computer(self):
		return self._builder.computer


def main_2():
	engineer = HardwareEngineer()
	engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
	computer = engineer.computer
	print(computer)


if __name__ == '__main__':
	main_2()
