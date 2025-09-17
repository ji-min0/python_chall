num = int(input())

black = set()
for i in range(num):
    x, y = map(int,input().split())
    for w in range(x, x+10):
        for h in range(y, y+10):
            black.add((w,h))

black_area = len(black)
print(black_area)