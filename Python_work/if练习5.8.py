current_users=['ali','kila','faloi','poloe','vikol']
new_users=['Ali','Aas','Dasfa','Poloe','Fs']
for new_user in new_users:
	if new_user.lower() in current_users:
		print(new_user+'次用户名已被占用，请换一个')
	else:
		print(new_user+'此用户名未被使用')