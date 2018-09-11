"""
	享元模式

	对象之间共享数据
"""
import random
from enum import Enum


class TreeType(Enum):
	apple_tree = 1
	orange_tree = 2
	banana_tree = 3


class Tree:
	# 共享对象的缓存池
	pool = dict()

	# __new__函数先于__init__函数执行，创建一个类实例返回。
	# __new__主要对类属性进行配置
	# __init__对创建好的实例的属性进行配置
	def __new__(cls, tree_type):
		obj = cls.pool.get(tree_type, None)
		# 如果享元还未被创建
		if not obj:
			obj = object.__new__(cls)
			obj.tree_type = tree_type
			# 保存到缓存池
			cls.pool[tree_type] = obj
		return obj

	# 渲染函数
	def render(self, age, x, y):
		print("我即将渲染一棵树，种类 ==> {}，年龄 ==> {}，位置 ==> ({},{})".format(self.tree_type, age, x, y))


def main():
	# 随机种子
	rnd = random.Random()
	age_min, age_max = 1, 30  # 单位为年
	min_point, max_point = 0, 100
	tree_counter = 0

	# 产生10棵苹果树
	for _ in range(10):
		t1 = Tree(TreeType.apple_tree)
		t1.render(rnd.randint(age_min, age_max),
				  rnd.randint(min_point, max_point),
				  rnd.randint(min_point, max_point))
		tree_counter += 1

	# 产生5棵香蕉树
	for _ in range(5):
		t2 = Tree(TreeType.banana_tree)
		t2.render(rnd.randint(age_min, age_max),
				  rnd.randint(min_point, max_point),
				  rnd.randint(min_point, max_point))
		tree_counter += 1

	# 产生3棵橘子树
	for _ in range(3):
		t3 = Tree(TreeType.orange_tree)
		t3.render(rnd.randint(age_min, age_max),
				  rnd.randint(min_point, max_point),
				  rnd.randint(min_point, max_point))
		tree_counter += 1

	print("总共渲染树的数目 ==> {}".format(tree_counter))
	print("总共实例化树对象的数目 ==> {}".format(len(Tree.pool)))

	t4 = Tree(TreeType.apple_tree)
	t5 = Tree(TreeType.banana_tree)
	t6 = Tree(TreeType.apple_tree)

	# 根据id的值就知道数据是否共享
	print('{} == {}? {}'.format(id(t4), id(t6), id(t4) == id(t6)))
	print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))


if __name__ == '__main__':
	main()
