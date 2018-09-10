# 装饰器模式

装饰器模式多用于给某个特定模块添加额外功能。

python中定义装饰器的格式如下:
```python
    def decorater_name(inner_func):
            # 为创建修饰器提供便利，保留被修饰函数的__name__和__doc__属性
	    @functools.wraps(inner_func)
	    def decorater(*args):
	        # 进行一系列执行函数inner_func()前的操作
	   
	        inner_func()
	        
	        # 进行一系列执行函数inner_func()后的操作
        return decorater
```
- 多个装饰器模式嵌套是有顺序的
```python
@decorate1
@decorate2
def myfun():
    pass

等价于 decorate1(decorate2(myfun))
```