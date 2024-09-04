import sys
input = sys.stdin.readline
import heapq
n = int(input())
l = [int(input()) for _ in range(n)]
left_heap = [-l[0]]
right_heap = []
switch = True
answer = [-left_heap[0]]
for x in l[1:]:
    if switch:
        heapq.heappush(right_heap, x if x>=-left_heap[0] else -heapq.heappushpop(left_heap, -x))
    else:
        heapq.heappush(left_heap, -x if x<=right_heap[0] else -heapq.heappushpop(right_heap, x))
    switch = not switch
    answer.append(-left_heap[0])
print('\n'.join(map(str, answer)))