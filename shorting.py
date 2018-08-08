arr = [10, 7, 25, 1, 5, 2,100,2,34,17,76,34]
length=len(arr) -1 

i = 0
while i < len(arr):
	i=i+1
	j= 0
	while j < length:
		a=arr[j]
		b=arr[j+1]
		if a > b:
			arr[j]=b
			arr[j+1]=a
			
		else:
			arr[j]=a
			arr[j+1]=b
		j=j+1

print arr
	   
