"""
	基于Memoization的递归可以大大提升性能，此时可以自定义一个memorize修饰器
"""
import functools


def memorize(fn):
	# 缓存字典
	know = dict()

	# 为创建修饰器提供便利，保留被修饰函数的__name__和__doc__属性
	@functools.wraps(fn)
	def memoizer(*args):
		# 如果缓存字典中已经存在
		if args in know:
			return know[args]
		# 如果缓存字典中不存在
		else:
			know[args] = fn(*args)
			return know[args]

	return memoizer


@memorize
# 返回前n个数的和
def nsum(n):
	assert (n >= 0), "n must be >=0"
	return n if n == 0 else n + nsum(n - 1)


@memorize
# 返回斐波那契数列的第n个数
def fib(n):
	assert (n >= 0), "n must be >=0"
	return n if n in (0, 1) else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
	from timeit import Timer

	measures = [
		{"exec": "fib(100)", "import": "fib", "func": fib},
		{"exec": "nsum(100)", "import": "nsum", "func": nsum},
	]
	for item in measures:
		t = Timer(
			item["exec"],
			"from __main__ import {}".format(item["import"])
		)
		print("name: {}, doc: {}, executing: {}, time:{}". \
			  format(item["func"].__name__, item["func"].__doc__, item["exec"], t.timeit()))
