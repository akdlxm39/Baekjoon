import sys
input = sys.stdin.readline

def main():
    string = input().rstrip()
    prefixsum = [[0]*26]
    for c in string:
        prefixsum.append(list(prefixsum[-1]))
        prefixsum[-1][ord(c)-97] += 1
    Q = int(input())
    for _ in range(Q):
        a, l, r = input().split()
        l, r = int(l), int(r)
        print(prefixsum[r+1][ord(a)-97] - prefixsum[l][ord(a)-97])

main()