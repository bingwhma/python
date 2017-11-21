import eventlet

def func(*args, **kwargs):
	print("------------start--------------")
	return 0

gt = eventlet.spawn(func)

# 真正开始执行
gt.wait()