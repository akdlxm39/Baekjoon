import sys
input = sys.stdin.readline

def merge_sort(A, l, r, list):
    if l >= r:
        return A
    m = (l + r)//2
    merge_sort(A, l, m, list)
    merge_sort(A, m+1, r, list)
    merge(A, l, m, r, list)

def merge(A, l, m, r, list):
    i, j = l, m + 1
    tmp = []
    while i <= m and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= m:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    for i, x in enumerate(tmp):
        A[l+i] = x
        list.append(x)

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    answer = []
    merge_sort(A, 0, len(A)-1, answer)
    print(answer[K-1] if len(answer) >= K else -1)
main()