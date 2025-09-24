n = int(input())

def check_good_or_bad():
    for _ in range(n):
        name = input()
        lower_name = name.lower()
        g_count = lower_name.count('g')
        b_count = lower_name.count('b')
    
        if g_count > b_count:
            print(f"{name} is GOOD")
        
        elif b_count > g_count:
            print(f"{name} is A BADDY")
        
        else:
            print (f"{name} is NEUTRAL")
    
check_good_or_bad()