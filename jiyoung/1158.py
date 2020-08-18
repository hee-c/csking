n , index = input().split()

i = 1
p = []

while( i<= int(n)):
    p.append(i)
    i=i+1

i = -1

arr = []

while p :
    i = i+int(index)
    if(i >= len(p)):
        i = i%len(p)

    arr.append(p[i])
    del p[i]
    i = i-1


print("<", end="")
for i in range(0,int(n),1):
    if(i != int(n)-1):
        print(arr[i],end=', ')
    else:
        print(arr[i],end='>')