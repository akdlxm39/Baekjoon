import sys
input = sys.stdin.readline
xlist, ylist = [], []
for _ in range(3):
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)
xlist.sort()
ylist.sort()
x = xlist[0] + xlist[2] - xlist[1]
y = ylist[0] + ylist[2] - ylist[1]
print(x, y)