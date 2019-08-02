alien_0={'x':0,'y':25,'speed':'medium'}
print('这个机器人向x方向移动：'+str(alien_0['x']))
if alien_0['speed']=='slow':
	x_in=1
elif alien_0['speed']=='medium':
	x_in=2
elif alien_0['speed']=='fast':
	x_in=3
alien_0['x']=alien_0['x']+x_in
print('这个新的机器人向x方向移动距离为：'+str(alien_0['x']))