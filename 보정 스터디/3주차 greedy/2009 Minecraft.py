import sys
input = sys.stdin.readline

def main():
    M = int(input())
    Hp = [input().rstrip()  for _ in range(M)]
    Rp = [input().rstrip()  for _ in range(M)]
    Cp = [input().rstrip() for _ in range(M)]
    Mp = [[['0'] * M for _ in range(M)] for _ in range(M)]
    H = [['0'] * M for _ in range(M)]
    R = [['0'] * M for _ in range(M)]
    C = [['0'] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            for k in range(M):
                if Hp[j][k] == '1' and Rp[i][k] == '1' and Cp[i][j] == '1':
                    Mp[i][j][k] = H[j][k] = R[i][k] = C[i][j] = '1'
    for i in range(M):
        for j in range(M):
            if H[i][j] != Hp[i][j] or R[i][j] != Rp[i][j] or C[i][j] != Cp[i][j]:
                print("NO")
                return
    print("YES")
    for p in Mp:
        for l in p:
            print(''.join(l))
    return

if __name__ == "__main__":
    main()