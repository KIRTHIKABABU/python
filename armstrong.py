# kirthika281197
num=int(input())
sum=0
temp=num
while(temp>0):
    result=temp%10
    sum+=result**3
    temp//=10
if(num==sum):
    print("yes")
else:
    print("no")
