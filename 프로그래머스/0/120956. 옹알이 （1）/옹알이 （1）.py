sounds = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    answer = 0
    
    for word in babbling:
        used = set()
        for s in sounds:
            if s in word and s not in used:
                used.add(s)
        
        index = 0
        while index < len(word):
            matched = False
            possible = True

            for s in used:
                if word[index:index+len(s)] == s:
                    index += len(s)
                    matched = True
                    break
                
            if not matched:
                possible = False
                break
        
        if possible:
            answer += 1
            
    return answer