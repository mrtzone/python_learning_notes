def users(first,last,**na):
	profile = {}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in na.items():
		profile[key]=value
	return profile

u = users('ds','dsa',do='d',dasdas='dda')

print(u)