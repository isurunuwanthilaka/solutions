def minion_game(string):
    # your code goes here
    l = len(string)
    stuart,kevin = 0 , 0
    for i in range(l):
        count=l-i
        if string[i] in ('A','E','I','O','U',):
            kevin+=count
        else:
            stuart+=count
    if stuart==kevin:
        print("Draw")
    elif stuart>kevin:
        print("Stuart "+str(stuart))
    else:
        print("Kevin "+str(kevin))
if __name__ == '__main__':
    s =input()
    minion_game(s)
