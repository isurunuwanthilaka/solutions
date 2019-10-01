arr=[1,1]
n=5
for i in range(2*n-1):
    arr.append(arr[-1]+arr[-2])
print arr[-1]*arr[-2]


##check http://austinrochford.com/posts/2013-11-01-generating-functions-and-fibonacci-numbers.html
##
##then see that n th fibonacci nugget is f(2n)*f(2n+1) 
for i in range(1,31):
    arr=[1,4]
    for i in range(2*i-1):
        arr.append(arr[-1]+arr[-2])
    print arr[-1]*arr[-2]
