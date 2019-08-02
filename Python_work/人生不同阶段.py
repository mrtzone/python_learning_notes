age=65
if age<2:
	message='他是婴儿'
elif age<4:
	message='他正在蹒跚学步'
elif age<13:
	message='他是儿童'
elif age<20:
	message='他是青少年'
elif age<65:
	message='他是成年人'
else:
	message='他是老人'
print(message)