n, k = map(int, raw_input().split())
circle = list(range(1, n+1))
josephus = list()
delIndex = 0

for i in range(n):
    circleLen = n-i
    delIndex = delIndex + k - 1
    if delIndex >= circleLen:
        delIndex = delIndex % circleLen
    josephus.append(circle.pop(delIndex))
josephus = map(str, josephus)

print("<{}>".format(", ".join(josephus)))