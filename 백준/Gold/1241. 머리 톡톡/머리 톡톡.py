N = int(input())
max_s = 1000000

s = [0] * N
counts = [0] * (max_s + 1)

for i in range(N):
    num = int(input())
    s[i] = num
    counts[num] += 1

for i in range(N):
    now = s[i]
    total_taps = 0

    for j in range(1, int(now ** 0.5) + 1):
        if now % j == 0:
            total_taps += counts[j]

            if j * j != now:
                total_taps += counts[now // j]

    total_taps -= 1

    print(total_taps)