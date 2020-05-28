#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: 王鹏飞
# 邮箱: wpfei973@163.com
# 时间: 2020-05-28 09:41:49
# 描述: xxxx

def fun():
	print("这是一个测试文件")
fun()


class One():
	def __init__(self, name, age, sex):
		"""构造函数
		创建init初始化函数
		Arguments:
			name {[str]} -- 姓名
			age {[int]} -- 年龄
			sex {[str]} -- 性别
		"""
		self.name = name 
		self.age = age
		self.sex = sex

	@property
	def age(self):
		return self.__age
	@age.setter
	def age(self,value):
		if value < 20 or value > 30:
			raise ValueError("年龄不符")
		else:
			self.__age = value 
	
	def __str__(self):
		return self.name
	
	def pri_mes(self):
		print("姓名:" + self.name + "  年龄:" + str(self.age) + "  性别:" + self.sex)


o1 = One("王鹏飞", 23, "男")
print(o1)
o1.pri_mes()