def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        checked = word
        is_possible = True

        while checked:
            for s in sounds:
                if checked.startswith(s):
                    checked = checked.replace(s, "", 1)
                    break
            else:
                is_possible = False
                break

        if is_possible:
            answer += 1

    return answer
