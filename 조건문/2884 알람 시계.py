H, M = map(int, input().split())
if M < 45:
    print((H-1)%24, (M-45)%60)
else:
    print(H, (M-45))