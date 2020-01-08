#coding = utf-8
'''设置'''
import random
import time 
import sys

#初始化游戏
attack_c = 0
defence_c = 0
attack_u = 0
defence_u = 0	
xios = [0,0]
tianbos = [0,0]

#设定电脑初始可用招式
usable_a = ['摸摸']
usable_d = ['地波','天波']
state = ['usable_a','usable_d','xio']

'''组件:方法'''
#招式(电脑)
def xio_c():
	print('电脑:xio')
	global defence_c, xios
	defence_c = 0.1
	xios[0] = xios[0]+1	
def dibo_c():
	global defence_c, xios
	defence_c = 1
	print('电脑:地波')
def tianbo_c():
	global defence_c, xios
	defence_c = 1
	tianbos[0] = tianbos[0] + 1
	print('电脑:天波')
def chaofang_c():
	global defence_c, xios
	defence_c = 9
	xios[0] = xios[0]-1
	print('电脑:超防')
def leiba_c():
	global attack_c, xios
	attack_c = 0.3
	xios[0] = xios[0]-0.3
	print('电脑:雷扒')
def momo_c():
	global attack_c, xios
	attack_c = 1
	xios[0] = xios[0]-1
	print('电脑:摸摸')
def sankan_c():
	global attack_c, xios
	attack_c = 3
	if tianbos[0] >= 5:
		tianbos[0] = tianbos[0] - 5
	else:
		xios[0] = xios[0]-3
	print('电脑:三砍')
def wuhe_c():
	global attack_c, xios
	attack_c = 5
	xios[0] = xios[0]-5
	print('电脑:五合体')
def huhe_c():
	global attack_c, xios
	attack_c = 10
	xios[0] = xios[0]-10
	print('电脑:虎合体')
#招式(玩家)
def xio_u():
	global defence_u, xios
	defence_u = 0.1
	xios[1] = xios[1]+1
def dibo_u():
	global defence_u, xios
	defence_u = 1
def tianbo_u():
	global defence_u, xios
	tianbos[1]=tianbos[1]+1
	defence_u = 1
def chaofang_u():
	global defence_u, xios
	defence_u = 9
	xios[1] = xios[1]-1
def leiba_u():
	global attack_u, xios
	attack_u = 0.3
	xios[1] =  xios[1] - 1/3
def momo_u():
	global attack_u, xios
	attack_u = 1
	xios[1] = xios[1]-1
def sankan_u():
	global attack_u, xios
	attack_u = 3
	if tianbos[1] >= 5:
		tianbos[1] = tianbos[1] - 5
	else:
		xios[1] = xios[1]-3
def wuhe_u():
	global attack_u, xios
	attack_u = 5
	xios[1] = xios[1]-5
def huhe_u():
	global attack_u, xios
	attack_u = 10
	xios[1] = xios[1]-10

def cpu():
	#控制不爆死
	global usable_a, usable_d, attack_c, defence_c, state
	if xios[0] < 0.3:
		usable_a = ['xio']
		usable_d = ['地波','天波']
	elif xios[0] < 1:
		usable_a = ['雷扒']
		usable_d = ['地波','天波']
	elif xios[0] < 3:
		usable_a = ['摸摸','雷扒']
		usable_d = ['地波','天波','超防']
	elif xios[0] < 5:
		usable_a = ['摸摸','雷扒','三砍']
		usable_d = ['地波','天波','超防']
	elif xios[0] < 10:
		usable_a = ['摸摸','雷扒','三砍','五合体']
		usable_d = ['地波','天波','超防']	
	else:
		usable_a = ['摸摸','雷扒','三砍','五合体','虎合体']
		usable_d = ['地波','天波','超防']
	if xios[1] < 3  and '超防' in usable_d:
		usable_d.remove('超防')
	else:
		pass
	#出招式
	go = random.choice(state)
	if go == 'usable_a' and usable_a is not None:
		get = random.choice(usable_a)
		if get == 'xio' or get == 'x':
			xio_c()
		elif get == '雷扒' or get == 'leiba':
			leiba_c()
		elif get == '摸摸' or get == 'momo':
			momo_c()
		elif get == '三砍' or get == 'sankan':
			sankan_c()
		elif get == '五合体' or get == '':
			wuhe_c()
		elif get == '虎合体':
			huhe_c()
	elif go == 'usable_d':
		get = random.choice(usable_d)	
		if get == '天波':
			tianbo_c()
		if get == '地波':
			dibo_c()
		if get == '超防':
			chaofang_c()
	elif go == 'xio':
		xio_c()

def user():
	global attack_c, attack_u, defence_c, defence_u
	#接受用户输入
	usr = input(str('你：'))
	if usr == 'xio' or usr == 'x':
		xio_u()
	elif usr == '摸摸' or usr == 'momo':
		momo_u()
	elif usr == '三砍' or usr == 'sa':
		sankan_u()
	elif usr == '雷扒' or usr == 'l':
		leiba_u()
	elif usr == '五合体' or usr == 'w':
		wuhe_u()
	elif usr == '虎合体' or usr == 'h':
		huhe_u()
	elif usr == '地波' or usr == 'd':
		dibo_u()
	elif usr == '天波' or usr == 't':
		tianbo_u()
	elif usr == '超防' or usr == 'c':
		chaofang_u()
	else:
		print('无法判断输入，请重新输入')
		turn()
def turn():
	global attack_c, attack_u, defence_c, defence_u
	#调用用户出招式
	user()
	#调用电脑给出招式
	cpu()	
	'''判断'''
	#全转浮点数
	attack_c = float(attack_c)
	attack_u = float(attack_u)
	defence_c = float(defence_c)
	defence_u = float(defence_u)
	#判断输赢
	if xios[1] < 0:
		print('你爆死')
		print(xios)
		over = input('输入任意键退出游戏')
		sys.exit()
	elif attack_u > attack_c and attack_c != 0  or attack_u > defence_c and defence_c != 0:
		print('你赢了')
		over = input('输入任意键退出游戏')
		sys.exit()
	elif attack_c > attack_u and attack_u != 0 or attack_c > defence_u and defence_u != 0:
		print('你输了')
		over = input('输入任意键退出游戏')
		sys.exit()
	elif attack_u > attack_c and attack_c == 0 or attack_c > attack_u and attack_u == 0 or attack_c > defence_u and defence_u ==0 and attack_u > defence_c and defence_c == 0 or attack_u == attack_c or defence_u == defence_c:
		attack_c = 0
		defence_c = 0
		attack_u = 0
		defence_u = 0
		print(xios)
		turn()
		
		
	
print("输入'xio'以开始游戏")
print('版本号:1.1.0开源版')
start=input(str("你："))
if start=='xio':
	xios[1] = xios[1]+1              
	print('电脑：xio')
	xios[0] = xios[0]+1
turn()
	
	
		
		
		
