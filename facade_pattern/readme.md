# 外观模式

外观模式常用来将一些复杂的内部逻辑包装成一个简单的接口，供客户端使用。一定程度上可达到解耦的好处。

ps:

python中实现抽象父类需使用abc模块，抽象函数通过@abc.abstractmethod修饰器修饰。

可调用`Base.register(Sub)`或`类继承`的方式来实现具体类

具体类必须实现用@abc.abstractmethod修饰的方法