# composite
i=int(input())
c=0

for s in range(i):
    if s%2==0:
        c+=1
if c>2:
    print('yes')
else:
    print('no')
