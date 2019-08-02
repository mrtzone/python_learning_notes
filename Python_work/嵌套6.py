users={
    'liuliu':{
        'first':'zhao',
        'last':'jin',
        'aihao':'play',
        },
    'huhu':{
        'first':'zhang',
        'last':'ting',
        'aihao':'diaoyu',
        }
    }
for usersname,fullname in users.items():
	print('\n'+'用户名为:'+str(usersname.title()))
	print('全称为：'+str(fullname['first'])+'\t'+str(fullname['last']))
	print('爱好为：'+str(fullname['aihao']))