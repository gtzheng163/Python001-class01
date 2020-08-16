#作业一：
# 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
# list
# tuple
# str
# dict
# collections.deque

容器序列: list, tuple, dict
扁平序列: str, collections.deque
可变序列: list, dict
不可变序列: str, tuple, collections.deque


# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。

def mymap(func,list1):
    for i in list1:
        yield func(i)


# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

import time

def timer(func,*args,**kwargs):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print(f'{func.__name__}运行时间: {end_time - start_time}')
    return wrapper

@timer
def mytest(n):
    time.sleep(n)

mytest(2)
