#Author : Isuru Nuwanthilaka
#version : 7
n=int(raw_input())
pack_arr=[]

for _ in range(n):
    pack_arr.append(int(raw_input()))

for i in range(n-1):
    for j in range(1,n-i,1):
        if pack_arr[i]+pack_arr[i+j]<=5:
            pack_arr[i]+=pack_arr[i+j]
            pack_arr[i+j]=0
                       
for k in pack_arr:
    print(k)

if len(pack_arr)==0:
    print(0)
