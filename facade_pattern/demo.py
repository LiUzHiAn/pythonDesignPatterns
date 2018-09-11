"""
	外观模式可以将复杂的内部再包装，将一些必要的接口暴露给客户端
"""

# “abc” refers "Abstract base class"
from abc import ABCMeta, abstractmethod


# 表示计算机的各种服务的抽象类
class Server(metaclass=ABCMeta):
	@abstractmethod
	def boot(self):
		pass

	@abstractmethod
	def kill(self, restart=True):
		pass


# 文件服务
class FileServer(Server):
	def __init__(self):
		self.name = "FileServer"

	def boot(self):
		print("boot the {}".format(self.name))

	def kill(self, restart=True):
		print("kill the {}".format(self.name))

	def other_file_function(self, job):
		print("do file job :{} in the {}".format(job, self.name))


# 进程服务
class ProcessServer(Server):
	def __init__(self):
		self.name = "ProcessServer"

	def boot(self):
		print("boot the {}".format(self.name))

	def kill(self, restart=True):
		print("kill the {}".format(self.name))

	def other_process_function(self, job):
		print("do process job:{} in the {}".format(job, self.name))


# 外观类
# 将文件服务和进程服务进行封装
class OperatingSystem:
	def __init__(self):
		self.fs = FileServer()
		self.ps = ProcessServer()

	def start(self):
		self.fs.boot()
		self.ps.boot()

	# 文件服务的其他操作
	def do_file_operation(self, job):
		self.fs.other_file_function(job)

	# 进程服务的其他操作
	def do_process_oeration(self, job):
		self.ps.other_process_function(job)


def main():
	os = OperatingSystem()
	# 启动各项服务
	os.start()
	os.do_file_operation("add a new file")
	os.do_process_oeration("show process info")


if __name__ == '__main__':
	main()
