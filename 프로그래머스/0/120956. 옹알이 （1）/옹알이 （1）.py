def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for word in babbling:
        checked = word
        
        while checked: 
            for s in sounds:
                if checked.startswith(s):
                    checked = checked.replace(s, "", 1)
                    break  
            else: 
                break
        else:
            answer += 1
    return answer