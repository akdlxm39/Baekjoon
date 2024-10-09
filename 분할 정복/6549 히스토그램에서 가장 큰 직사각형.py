import sys
input = sys.stdin.readline

def main():
    while True:
        N, *histogram = list(map(int, input().split()))
        if N == 0:
            break
        answer = divide(histogram, 0, N-1)
        print(answer)

def divide(A, l, r):
    if l == r:
        return A[l]
    m = (l+r)//2
    answer = max((divide(A, l, m)), (divide(A, m+1, r)))
    i = j = m
    h = A[m]
    answer = max(answer, h)
    while i > l or j < r:
        if j < r and (i == l or A[i - 1] <= A[j + 1]):
            j += 1
            h = min(h, A[j])
        else:
            i -= 1
            h = min(h, A[i])
        answer = max(answer, h * (j - i + 1))
    return answer

main()


# def main():
#     while True:
#         N, *histogram = list(map(int, input().split()))
#         if N == 0:
#             break
#         answer = [0]
#         solution(N, histogram, answer)
#         print(answer[0])
        
# def solution(N, A, answer):
#     s = []
#     for i in range(N):
#         while s and A[s[-1]] > A[i]:
#             tmp = s.pop()
#             answer[0] = max(answer[0], (i-(s[-1]if s else -1)-1)*A[tmp])
#         s.append(i)
#     while s:
#         tmp = s.pop()
#         answer[0] = max(answer[0], (N-(s[-1]if s else -1)-1)*A[tmp])

# main()