H, M = map(int, input().split())

def alarm(H, M): 
    if M >= 45: 
        M -= 45
    else:
        M += 15  # 60 - 45
        H -= 1
        if H < 0:
            H = 23
    print(H, M)

alarm(H, M)
