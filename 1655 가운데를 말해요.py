import heapq
n = int(input())
left_heap = [-int(input())]
right_heap = []
switch = True
l = (int(input()) for _ in range(n-1))
print(-left_heap[0])
for x in l:
    if switch:
        heapq.heappush(right_heap, x if x>=-left_heap[0] else -heapq.heappushpop(left_heap, -x))
    else:
        heapq.heappush(left_heap, -x if x<=right_heap[0] else -heapq.heappushpop(right_heap, x))
    switch = not switch
    print(-left_heap[0])