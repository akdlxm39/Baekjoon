import sys
input = sys.stdin.readline

def main():
    arr = list(map(int, input().split()))
    n = len(arr)-1
    dp = [((0, 0), 0), ((0, 0), 0)]
    for i, x in enumerate(arr, 2):
        left = dp[i-2]
        right = dp[i-1]
        next_foot = (x, left[0][1])
        cost1 = left[1] + (4 if abs(left[0][0]-x)==2 else 3 if left[0][0] != 0 else 2)
        cost2 = right[1] + (4 if abs(right[0][0]-x)==2 else 3 if right[0][0] != 0 else 2)

if __name__ == "__main__":
    main()