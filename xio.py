#coding = utf-8
'''设置'''
import random
import time 
import sys

#初始化游戏
real_c = ''
real_u = ''
attack_c = 0
defence_c = 0
attack_u = 0
defence_u = 0	
xios = [0,0]
tianbos = [0,0]
spec_c = 10
spec_u = 10
#设定玩家可用的所有招式
usable_u= ['xio','摸摸','雷扒','三砍','五合体','虎合体','地波','天波','超防']
#设定电脑初始可用招式
usable_a = ['摸摸']
usable_d = ['地波','天波']
state = ['usable_a','usable_d','xio']

'''组件:方法'''
#招式(电脑)
def xio(pos):
	global defence_u, defence_c, xios
	if pos == 0:
		defence_c = 0.1
		xios[0] = xios[0]+1	
	else:
		defence_u = 0.1
		xios[1] = xios[1]+1
def dibo(pos):
	global defence_u, defence_c, xios
	if pos == 0 :
		defence_c = 1
	else:
		defence_u = 1
def tianbo(pos):
	global defence_u, defence_c, xios
	if pos == 0:
		defence_c = 1
		tianbos[0] = tianbos[0] + 1
	else:
		global defence_u, xios
		tianbos[1]=tianbos[1]+1
		defence_u = 1
		spec_u = 2
def chaofang(pos):
	global defence_u, defence_c, xios
	if pos == 0:
		defence_c = 9
		xios[0] = xios[0]-1
	else:
		defence_u = 9
		xios[1]=xios[1]-1
def leiba(pos):
	global attack_u, attack_c, xios
	if pos == 0:
		attack_c = 0.3
		xios[0] = xios[0]-0.3
	else:
		attack_u = 0.3
		xios[1] = xios[1] - 0.3
	
def momo(pos):
	global attack_u, attack_c, xios
	if pos == 0:
		attack_c = 1
		xios[0] = xios[0]-1
	else:
		attack_u = 1
		xios[1] =  xios[1] - 1
def sankan(pos):
	global attack_u, attack_c, xios
	if pos == 0:
		attack_c = 3
		if tianbos[0] >= 5:
			tianbos[0] = tianbos[0] - 5
		else:
			xios[0] = xios[0]-3
	else:
		attack_u = 3
		if tianbos[1] >= 5:
			tianbos[1] = tianbos[1] - 5
		else:
			xios[1] = xios[1]-3
def wuhe(pos):
	global attack_u, attack_c, xios
	if pos == 0:
		attack_c = 5
		xios[0] = xios[0]-5
	else:
		attack_u = 5
		xios[1] = xios[1]-5
		
def huhe(pos):
	global attack_u, attack_c, xios
	if pos == 0:
		attack_c = 10
		xios[0] = xios[0]-10
	else:
		attack_u = 10
		xios[1] = xios[1]-10
		
#状态组件
def Start():	
	print("输入'xio'以开始游戏")
	start=input(str("你："))
	if start=='xio':
		xios[1] = xios[1]+1              
		print('电脑：xio')
		xios[0] = xios[0]+1
		turn()
	else:
		Sstart()

def over():
	end = input('输入任意键退出游戏\n')
	sys.exit

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
			xio(0)
			print('电脑:xio')
		elif get == '雷扒' :
			leiba(0)
			print('电脑:雷扒')
		elif get == '摸摸' :
			momo(0)
			print('电脑:摸摸')
		elif get == '三砍' :
			sankan(0)
			print('电脑:三砍')
		elif get == '五合体' :
			wuhe(0)
			print('电脑:五合体')
		elif get == '虎合体' :
			huhe(0)
			print('电脑:虎合体')
	elif go == 'usable_d':
		get = random.choice(usable_d)	
		if get == '天波':
			tianbo(0)
			print('电脑:天波')
		if get == '地波':
			dibo(0)
			print('电脑:地波')
		if get == '超防':
			chaofang(0)
			print('电脑:超防')
	elif go == 'xio':
		xio(0)
		print('电脑:xio')

def user():
	global attack_c, attack, defence_c, defence, real_c, real_u
	#接受用户输入
	usr = input(str('你：'))
	if usr == 'xio' or usr == 'x':
		xio(1)
		real_u = 'xio'
	elif usr == '摸摸' or usr == 'm':
		momo(1)
		real_u = '摸摸'
	elif usr == '三砍' or usr == 's':
		sankan(1)
		real_u = '三砍'
	elif usr == '雷扒' or usr == 'l':
		leiba(1)
		real_u = '雷扒'
	elif usr == '五合体' or usr == 'w':
		wuhe(1)
		real_u = '五合体'
	elif usr == '虎合体' or usr == 'h':
		huhe(1)
		real_u = '虎合体'
	elif usr == '地波' or usr == 'd':
		dibo(1)
		real_u = '地波'
	elif usr == '天波' or usr == 't':
		tianbo(1)
		real_u = '天波'
	elif usr == '超防' or usr == 'c':
		chaofang(1)
		real_u = '超防'
	else:
		print('无法判断输入，请重新输入')
		turn()

def turn():
	global attack_c, attack_u, defence_c, defence_u, real_c, real_u, usable_u
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
	if xios[1] < 0 or real_u not in usable_u:
		print('你爆死')
		over()
	elif attack_u > attack_c and attack_c != 0  or attack_u > defence_c and defence_c != 0 or real_u == '雷扒' and real_c == '天波':
		print('你赢了')
		over()
	elif attack_c > attack_u and attack_u != 0 or attack_c > defence_u and defence_u != 0 or real_u == '天波' and real_c == '雷扒':
		print('你输了')
		over()
	else:
		#初始化
		real_c = ''
		real_u = ''
		attack_c = 0
		defence_c = 0
		attack_u = 0
		defence_u = 0
		#显示比分
		print(xios)
		#递归下一轮
		turn()
		
print('版本号:1.1.2')
Start()

	
	
		
		
		
