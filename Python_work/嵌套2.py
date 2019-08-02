aliens=[]
for aliens_numbers in range(0,30):
	new_alien={'color':'yellow','point':5,'speed':'fast'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['point']=10
		alien['speed']='medium'
	elif alien['color']=='yellow':
		alien['color']='red'
		alien['point']='1000'
		alien['speed']='fasts'
for alien in aliens[0:5]:
	print(alien)
print('\n\n\n'+"...")
