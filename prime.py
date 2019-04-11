n=input("enter a value")
i=2
f=0
if(n==1):
	print("it is a composite number")
if(n==2):	 
	print("it is a prime number")
while(i<=n/2):
	if(n%i==0):
           f=f+1
        i=i+1
if(f>0):
	print("n is not prime")
else:
	print("n is prime number")

