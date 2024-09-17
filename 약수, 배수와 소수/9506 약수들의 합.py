import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    factors = []
    for x in range(1, n):
        if n % x == 0:
            factors.append(x)
    if n == sum(factors):
        print(f"{n} = {' + '.join(map(str, factors))}")
    else:
        print(f"{n} is NOT perfect.")
