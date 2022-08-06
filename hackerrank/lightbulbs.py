n=map(int,list(str(int(raw_input()))))
c=2**(len(n)-1)
ar=[]
for i in range(len(n)):
    ar.append(0)
if len(n)>=2:
    ar[0]=1
    ar[1]=1
    k=1
    while k<len(n):
        if n[k]!=ar[k]:
            if k+1<len(n):
                ar[k+1]=1
            c+=2**(len(n)-1-k)
            

        k+=1
    print c
elif len(n)==0:
    print 0
elif len(n)==1 and n[0]==0:
    print 0
elif len(n)==1 and n[0]==1:
    print 1
    
