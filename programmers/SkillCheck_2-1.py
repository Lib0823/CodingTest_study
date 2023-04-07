# 프로그래머스 스킬체크 2-1

# 자연수 n이 주어졌을 때 3개의 조건에 맞는 숫자를 반환하시오.
# 1. n의 다음 큰 숫자는 n보다 큰 자연수이다.
# 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같다.
# 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 이다.

# algorithm : 자연수 n의 2진수를 구한다 -> '1'의 갯수를 count한다 -> n을 1증가하고 2진수를 구한다음 '1'을 count하여 비교한다 -> '1'의 갯수가 똑같을 시 숫자 반환 

# self-feedback : 하나씩 if문으로 비교하며 돌리는 것이 매우 비효율적이다.
#                 switch나 반복문으로 하면 좋을 것 같다.

def solution(n):
    arr = ['0','0','0','0','0','0','0']
    arr2 = ['0','0','0','0','0','0','0']
    nn = n
    
    # 2진수 구함
    if n >= 64: 
        arr[0] = '1'
        n -= 64
    if n >= 32: 
        arr[1] = '1'
        n -= 32
    if n >= 16: 
        arr[2] = '1'
        n-= 16
    if n >= 8: 
        arr[3] = '1'
        n -=8
    if n >= 4: 
        arr[4] = '1'
        n -= 4
    if n >= 2: 
        arr[5] = '1'
        n -= 2
    if n >= 1: 
        arr[6] = '1'
        n -= 1
        
        
    cnt = arr.count('1')    
        
    while True:
        nn += 1
        nnn = nn
        
        arr2 = ['0','0','0','0','0','0','0']
        # 2진수 구하기
        if nnn >= 64: 
            arr2[0] = '1'
            nnn -= 64
        if nnn >= 32: 
            arr2[1] = '1'
            nnn -= 32
        if nnn >= 16: 
            arr2[2] = '1'
            nnn-= 16
        if nnn >= 8: 
            arr2[3] = '1'
            nnn -=8
        if nnn >= 4: 
            arr2[4] = '1'
            nnn -= 4
        if nnn >= 2: 
            arr2[5] = '1'
            nnn -= 2
        if nnn >= 1: 
            arr2[6] = '1'
            nnn -= 1
            
        cnt2 = arr2.count('1')
        
        if cnt == cnt2:
            return nn


