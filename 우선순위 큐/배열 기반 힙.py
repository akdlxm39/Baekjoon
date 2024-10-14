import sys
input = sys.stdin.readline

class heap:
    def __init__(self):
        self.array = []
        self.size = 0
    def push(self, value):
        self.array.append(value)
        self.size += 1
        self.heapify_up(self.size-1)

    def pop(self):
        if self.size == 0:
            return 0
        if self.size == 1:
            self.size = 0
            return self.array.pop()
        result = self.array[0]
        self.array[0] = self.array.pop()
        self.size -= 1
        self.heapify_down()
        return result

    def heapify_up(self, idx):
        while idx > 0 and self.array[idx] < self.array[(idx-1)//2]:
            self.array[idx], self.array[(idx-1)//2] = self.array[(idx-1)//2], self.array[idx]
            idx = (idx-1)//2

    def heapify_down(self):
        idx = 0
        while idx*2+1 < self.size:
            right = idx*2+2
            smallest = idx*2+1
            if right < self.size and self.array[smallest] > self.array[right]:
                smallest = right
            if self.array[idx] <= self.array[smallest]:
                break
            self.array[idx], self.array[smallest] = self.array[smallest], self.array[idx]
            idx = smallest

def main():
    N = int(input())
    h = heap()
    for _ in range(N):
        x = int(input())
        if x:
            h.push(x)
        else:
            print(h.pop())

main()