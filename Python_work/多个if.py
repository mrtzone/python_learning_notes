餐馆麻辣洋芋=['辣椒','酱油','葱花','蔬菜']
顾客=['辣椒','西红柿','葱花']
for 顾客点的 in 顾客:
	if 顾客点的 in 餐馆麻辣洋芋:
		print('添加'+顾客点的)
	else:
		print('抱歉，这个我们无法提供')
print('你的点完了')
