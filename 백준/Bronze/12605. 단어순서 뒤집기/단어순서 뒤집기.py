N = int(input())

for i in range(N): 
    sentence = input()
    words = sentence.split()
    print(f"Case #{i+1}: {' '.join(words[::-1])}")
