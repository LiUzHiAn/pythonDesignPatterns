class Event:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name


# 抽象处理类
class Widget:
	def __init__(self, parent=None):
		self.parent = parent

	def handle(self, event):
		handler = "handle_{}".format(event)
		# 如果自己有处理请求的办法，就自己处理
		if hasattr(self, handler):
			method = getattr(self, handler)
			method(event)
		# 如果有上一级，则传给上一级（父类）
		elif self.parent:
			self.parent.handle(event)
		# 如果有默认处理方法
		elif hasattr(self, "handle_default"):
			self.handle_default(event)


# 该类只处理close事件和defaul事件
class MainWindow(Widget):
	def handle_close(self, event):
		print("MainwWindow处理：{}事件".format(event))

	def handle_default(self, event):
		print("MainwWindow默认处理：{}事件".format(event))


# 该类只处理paint事件
class SendDialog(Widget):
	def handle_paint(self, event):
		print("SendDialog处理：{}事件".format(event))


# 该类只处理down事件
class MsgText(Widget):
	def handle_down(self, event):
		print("MsgText：{}事件".format(event))


# 客户端请求消息
if __name__ == '__main__':
	mw = MainWindow()
	sd = SendDialog(mw)
	msg = MsgText(sd)

	for e in ["close", "paint", "down", "default"]:
		event = Event(e)
		print('\nSending event -{}- to MainWindow'.format(event))
		mw.handle(event)
		print('Sending event -{}- to SendDialog'.format(event))
		sd.handle(event)
		print('Sending event -{}- to MsgText'.format(event))
		msg.handle(event)
