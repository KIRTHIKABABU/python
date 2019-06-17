#kd2805
str1,str2=input().split()
c=0
if len(str1)>len(str2):
  str1,str2=str2,str1
j=0
while j<len(str1):
  c+=(ord(str2[j])-ord(str1[j]))
  j+=1
for j in range(j,len(str2)):
  c+=ord(str2[j])-ord('a')+1
print(c)
