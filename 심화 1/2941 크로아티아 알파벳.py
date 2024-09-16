import sys
input = sys.stdin.readline
S = input().rstrip()
X = len(S.replace('c=', 'x').replace('c-', 'x').replace('dz=', 'x').replace('d-', 'x').replace('lj', 'x').replace('nj', 'x').replace('s=', 'x').replace('z=', 'x'))
print(X)