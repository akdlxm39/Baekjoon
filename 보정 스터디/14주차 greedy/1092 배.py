import sys
input = sys.stdin.readline

def upper_bound(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] > x:
            l = m+1
        else:
            r = m-1
    return l

def main():
    n = int(input())
    cranes = sorted(map(int, input().split()), reverse=True)
    m = int(input())
    boxes = sorted(map(int, input().split()), reverse=True)
    if cranes[0] < boxes[0]:
        print(-1)
        return
    counts = []
    i, cur = 1, 0
    while cur < m and i < n:
        pre, cur = cur, upper_bound(boxes, cranes[i])
        counts.append(cur - pre)
        i += 1
    if cur != m:
        counts.append(m-cur)
    h = remain = 0
    for w, cur_cnt in enumerate(counts, 1):
        cur_cnt -= remain
        if cur_cnt > h:
            cur_cnt -= h
            h += (cur_cnt-1)//w+1
            remain = (w-cur_cnt%w) if cur_cnt%w else 0
        else:
            remain = h-cur_cnt
    print(h)

if __name__ == "__main__":
    main()