from collections import namedtuple

n = int(input())
string = ' '.join(input().strip().split())
Student = namedtuple('Student',string)

tot = 0.0

for _ in range(n):
    i = input().strip().split()
    print(i)
    s = Student(i[0],i[1],i[2],i[3])
    tot+=int(s.MARKS)

print('%.2f'%(tot/n))
    
