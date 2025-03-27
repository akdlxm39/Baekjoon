import sys
from bisect import bisect_left
input = sys.stdin.readline

# class LIS:
#     def __init__(self, num=None):
#         self.num = num
#         self.child_list = []
#         self.child_list_size = 0
#         self.max_depth = 0
#
#     def add(self, node: 'LIS'):
#         flag = False
#         for i in range(self.child_list_size):
#             child = self.child_list[i]
#             if child.num < node.num:
#                 depth = child.add(node)
#                 if self.max_depth < depth:
#                     self.max_depth = depth
#                 flag = True
#             elif child.num == node.num:
#                 flag = True
#             elif child.max_depth == 0:
#                 self.child_list[i] = node
#                 flag = True
#         if not flag:
#             self.child_list.append(node)
#             self.max_depth += 1
#             self.child_list_size += 1
#         return self.max_depth+1
#
#     def __str__(self, flag=True):
#         ret = ""
#         if flag:
#             ret += str(self.max_depth) + "\n"
#         else:
#             ret += str(self.num) + " "
#         if self.child_list_size:
#             ret += max(self.child_list, key=lambda x: x.max_depth).__str__(False)
#         return ret
#
# def main():
#     n = int(input())
#     root = LIS()
#     for num in map(int, input().split()):
#         root.add(LIS(num))
#     print(root)

def main():
    n = int(input())
    num_list = input().split()
    stack = []
    dp = [0] * n
    for i in range(n):
        num = int(num_list[i])
        if not stack or stack[-1] < num:
            stack.append(num)
            dp[i] = len(stack)
        else:
            index = bisect_left(stack, num)
            stack[index] = num
            dp[i] = index+1
    cnt = len(stack)
    ans = [""]*cnt
    for i in range(n-1,-1,-1):
        if dp[i] == cnt:
            cnt -= 1
            ans[cnt] = num_list[i]
    print(len(ans), ' '.join(ans), sep='\n')

if __name__ == "__main__":
    main()