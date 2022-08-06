import itertools as itt
n,m = map(int,raw_input().strip().split())
person_arr=[]
max_score=0
count=0
for i in range(n):
    person = map(int,raw_input().strip().split())
    person_arr.append(person)

for j in itt.combinations(person_arr,3):
    team_score = sum(sum(k) for k in j)
    if team_score>max_score:
        max_score=team_score
        count=1
    elif team_score==max_score:
        count+=1

print(max_score)
print(count)
