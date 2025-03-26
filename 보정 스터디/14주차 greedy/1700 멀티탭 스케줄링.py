import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))
    using = []
    ans = 0
    for i, x in enumerate(seq):
        if x in using:
            pass
        elif len(using) < n:
            using.append(x)
        else:
            l = []
            for j, y in enumerate(using):
                if y not in seq[i:]:
                    using[j] = x
                    break
                l.append((seq.index(y, i), j))
            else:
                using[max(l)[1]] = x
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()