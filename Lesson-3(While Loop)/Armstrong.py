num=int(input("Enter a number to check: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if num==sum:
    print(num," is a armstrong number")
else:
    print(num," is not an armstrong number")