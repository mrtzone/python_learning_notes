rivers={
    'changjiang':'china',
    'huanghe':'china',
    'zhujiang':'china'
    }
for river,country in rivers.items():
	print(str(river.title())+'属于'+str(country.title()))
for river in rivers:
	print(river)
for country in set(rivers.values()):
	print(country)