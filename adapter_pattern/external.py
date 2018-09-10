"""
	外部组件及其接口
"""
class Synthesizer:
	def __init__(self, name):
		self._name = name

	def __str__(self):
		return "Synthesizer ==> {} ".format(self._name)

	def play(self):
		print("The Synthesizer {} is playing a electronic song!".format(self._name))


class Human:
	def __init__(self, name):
		self._name = name

	def __str__(self):
		return "Human ==> {} ".format(self._name)

	def sing(self):
		print("The Human {} is singing a song!".format(self._name))