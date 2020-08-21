h, m = input().split()

h = int(h)
m = int(m)

if(m<45):
    if(h==0):
        h = 24

    h = h-1
    m = m+15
else:
    m = m-45

print(h,m)
