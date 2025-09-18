k, q, l, b, n, p = list(map(int, input().split()))

def check_piece_one(p): 
    if p == 0: 
        return 1
    elif p > 1:
        return -(p-1)   
    else: 
        return 0

def check_piece_two(p): 
    if p == 0: 
        return 2
    elif p > 2:
        return -(p-2)  
    elif 0 < p < 2:
        return 2-p
    else: 
        return 0
    
def check_piece_pawn(p):
    if p == 0:
        return 8
    elif p > 8:
        return -(p-8)
    elif 0< p < 8: 
        return 8-p
    else: 
        return 0

print(
check_piece_one(k),
check_piece_one(q),
check_piece_two(l),
check_piece_two(b),
check_piece_two(n),
check_piece_pawn(p))