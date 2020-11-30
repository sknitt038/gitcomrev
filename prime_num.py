def primenumber(num):
	f=0
	if(num>=2):
		for i in range(2,num):
			if num%i==0:
				f=1
				break
	if(f==1):
		print("Not a prime")
	else:
		print("prime", num)



if __name__=="__main__":
	print("Enter the nnumber")
	num=int(input("Enter the nnumber: "))
	primenumber(num)
