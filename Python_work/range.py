#for value in range(1,101,3):
	#print(value)
#numbers=list(range(1,11,2))
#print(numbers)
squares=[]
for value in range(1,100,3):
	square=value**2
	squares.append(square)
print(squares)
最小值=min(squares)
最大值=max(squares)
总和=sum(squares)
print("最大值为"+str(最大值)+"\n最小值为"+str(最小值)+"\n总和为"+str(总和))