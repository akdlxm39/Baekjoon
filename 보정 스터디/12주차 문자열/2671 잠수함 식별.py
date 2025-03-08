import sys
input = sys.stdin.readline

# state input
#       0   1
# S0:   0   0  sink_state
# S1:   2   3  init_state
# S2:   0   1
# S3:   4   0
# S4:   5   0
# S5:   5   6
# S6:   2   7
# S7:   8   7
# S8:   5   1

def main():
    state_table = [(0, 0),(2, 3), (0, 1), (4, 0), (5, 0), (5, 6), (2, 7), (8, 7), (5, 1)]
    s = input().rstrip()
    state = 1
    for c in s:
        if not state:
            break
        state = state_table[state][int(c)]
    if state == 1 or state == 6 or state == 7:
        print("SUBMARINE")
    else:
        print("NOISE")

if __name__ == "__main__":
    main()