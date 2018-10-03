## 责任链模式

特点：
- 使多个对象都有机会处理请求，从而避免请求的发送者和接受者之间的耦合关系，
- 将多个处理事件的对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理请求为止。


#### 抽象处理角色
```python
from abc import ABC, abstractmethod


class Handler(ABC):
	def __init__(self, name):
		self.next_handler = None
		self.name = name

	@abstractmethod
	def handle_request(self):
		pass

	def set_next_handler(self, next_handler):
		self.next_handler = next_handler

	def get_next_handler(self):
		return self.next_handler


```

#### 具体处理角色
```python
class ConcreteHandler(Handler):

	def handle_request(self):
		if self.get_next_handler() != None:
			print(self.name + "放过请求")
			self.get_next_handler().handle_request()
		else:
			print(self.name + "处理请求")

```

#### 客户端类发送请求
```python
if __name__ == '__main__':
	# 请求处理对象链
	handler1 = ConcreteHandler("处理对象1")
	handler2 = ConcreteHandler("处理对象2")
	handler3 = ConcreteHandler("处理对象3")
	handler1.set_next_handler(handler2)
	handler2.set_next_handler(handler3)

	# 处理请求
	handler1.handle_request()

```

### 纯的与不纯的责任链模式
一个纯的责任链模式要求一个具体的处理者对象只能在两个行为中选择一个：
1. 承担责任，
2. 把责任推给下家。

不允许出现某一个具体处理者对象在承担了一部分责任后又 把责任向下传的情况。


- 在一个纯的责任链模式里面，一个请求必须被某一个处理者对象所接收；
- 在一个不纯的责任链模式里面，一个请求可以最终不被任何接收端对象所接收。
- 纯的责任链模式的实际例子很难找到，一般看到的例子均是不纯的责任链模式的实现。



