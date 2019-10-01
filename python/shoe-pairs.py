n=input()
arr=[]
for _ in xrange(n):
    arr.append(raw_input().strip().split())
arr.sort()
c=0
while len(arr)>1:
    a=arr.pop(0)
    if a[1]=='L':
        a[1]='R'
    else:
        a[1]='L'
    if a in arr:
        c+=1
        arr.remove(a)

print c
