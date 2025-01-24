import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6+5)

def preorder(inorder, postorder, size, ini, posti):
    idx = postorder[posti+size-1] - ini
    print(inorder[ini+idx], end=' ')
    if idx != 0:
        preorder(inorder, postorder, idx, ini, posti)
    if size-idx-1 != 0:
        preorder(inorder, postorder, size-idx-1, ini+idx+1, posti+idx)

def main():
    n = int(input())
    inorder = list(map(int, input().split()))
    inorder_dict = dict((x, i) for i, x in enumerate(inorder))
    postorder = list(map(int, input().split()))
    postorder = [inorder_dict[x] for x in postorder]
    preorder(inorder, postorder, n, 0, 0)

if __name__ == "__main__":
    main()
#           A
#       B       C
#     D   E   F
#              G
#
# pre:  A B D E C F G
#
# in:   D B E A F G C
# post: D E B G F C A