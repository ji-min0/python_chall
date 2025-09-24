"""
피드백
max 값을 1000000으로 고정하지 말고 입력에서 최댓값 받기
print에서 바로 1 빼주기
"""


N = int(input())
nums = []
max_num = 0

for i in range(N):
    now_num = int(input())
    nums.append(now_num)
    if now_num > max_num:
        max_num = now_num

counts = [0] * (max_num + 1)
for num in nums:
    counts[num] += 1

for now_num in nums:
    total_taps = 0
    
    for j in range(1, int(now_num ** 0.5) + 1):
        if now_num % j == 0:
            total_taps += counts[j]
            
            if j * j != now_num:
                total_taps += counts[now_num // j]

    print(total_taps - 1)