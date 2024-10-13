import sys
input = sys.stdin.readline
import heapq
# from collections import deque

# class heap:
#     def __init__(self, value=None):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.size = int(self.value is not None)
#     def get(self):
#         q = deque()
#         result = []
#         q.append(self)
#         while q:
#             cur = q.popleft()
#             result.append(cur.value)
#             if cur.left is not None:
#                 q.append(cur.left)
#             if cur.right is not None:
#                 q.append(cur.right)
#         return [self.size] + result
#     def push(self, value):
#         if self.value is None:
#             self.value = value
#         elif self.value[0] < value[0] or (self.value[0] == value[0] and self.value[1] <= value[1]):
#             if self.left is None:
#                 self.left = heap(value)
#             elif self.right is None:
#                 self.right = heap(value)
#             elif self.left.size <= self.right.size:
#                 self.left.push(value)
#             else:
#                 self.right.push(value)
#         else: #self.value[0] > value[0]
#             tmp, self.value = self.value, value
#             if self.left is None:
#                 self.left = heap(tmp)
#             elif self.right is None:
#                 self.right = heap(tmp)
#             elif self.left.size <= self.right.size:
#                 self.left.push(tmp)
#             else:
#                 self.right.push(tmp)
#         self.size += 1
#     def pop(self):
#         if self.size == 0:
#             return (0, 0)
#         tmp = self.value
#         if self.left is not None and self.right is not None:
#             if self.left.value[0] < self.right.value[0] or (self.left.value[0] == self.right.value[0]  and self.left.value[1] <= self.right.value[1]):
#                 self.value = self.left.pop()
#                 if self.left.size == 0:
#                     self.left = None
#             else:
#                 self.value = self.right.pop()
#                 if self.right.size == 0:
#                     self.right = None
#         elif self.left is not None:
#             self.value = self.left.pop()
#             if self.left.size == 0:
#                 self.left = None
#         elif self.right is not None:
#             self.value = self.right.pop()
#             if self.right.size == 0:
#                 self.right = None
#         else:
#             self.value = None
#         self.size -= 1
#         return tmp

def main():
    N = int(input())
    heap = []
    for _ in range(N):
        x = int(input())
        if x:
            heapq.heappush(heap, (abs(x), x))
        else:
            print(heapq.heappop(heap)[1] if heap else 0)
    # h = heap()
    # for _ in range(N):
    #     x = int(input())
    #     if x:
    #         h.push((abs(x), x))
    #     else:
    #         print(h.pop()[1])
    #     print(h.get())

main()