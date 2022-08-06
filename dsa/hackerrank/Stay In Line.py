x = int(input())

arr=[]
for _ in range(x):
    c=list(input().strip().split())
    if c[0]=='in':
        arr.append(c[1])
    elif c[0]=='out':
        del arr[0]

n = int(input())
try :
    print(arr[n])
except Exception:
    print('ERROR')
