def solution(nums):
    N = len(nums)
    
    pick = N // 2
    
    K = len(set(nums))
    
    return min(K, pick)
