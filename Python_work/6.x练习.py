nums={
    'lala':1,
    'kaka':1,
    'sasa':3,
    'jojo':4,
    'momo':5,
    'popo':6,
    }
print(str(nums)+'\n')
for name,num in nums.items():
	print(str(name.title())+'最喜欢的数字是'+str(num)+'\n')
for wel in nums:
	print(wel)
friend=['lala','jojo']
for name in nums:
	if name in friend:
		print('nihao'+str(name))
	else:
		print('buyaode'+str(name))
if 'hihi' not in nums:
	print('kailai')
print(nums.keys())
for name in sorted(nums.keys()):
	print(name)
print('\n')
for name in set(nums.values()):
	print(name)
for name in nums:
	print(str(name.title())+'来了')

未包含=['popoopo','disaj','dsaf']
for 未包含的 in 未包含:
	if 未包含的 not in nums.keys():
		print(str(未包含的.title())+'快来吧')
	else:
		print('finished')

