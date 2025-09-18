a, b = map(int, input().split())
seq = []

i = 1
while len(seq) < b: 
    seq.extend([i] * i)
    i += 1

answer = sum(seq[a-1:b])
print(answer)