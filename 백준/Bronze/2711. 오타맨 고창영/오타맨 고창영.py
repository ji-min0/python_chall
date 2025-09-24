T = int(input())

for _ in range(T):
    test_case = input().split()
    wrong_position = int(test_case[0])
    sentence = list(test_case[1])
    
    sentence.pop(wrong_position - 1)
    
    print(''.join(sentence))
