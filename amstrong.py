a=input("enter the value to chek amstrong number ")
s=0
while(a>0):
	c=a%10
	s=s+(c*c*c)
	a=a/10
if(a==s):
	print("number is amsrong")
else:
	print("number is not amstrong")

	

