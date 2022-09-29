n = int(input()) #라운드 수 입력
c_score = s_score = 100 # 기본점수 100
for _ in range(n): 
    c,s = map(int,input().split()) #창영, 상덕의 주사위 숫자
    if c > s :
        s_score -= c
    elif c < s:
        c_score -= s
    else:
        pass
print(c_score)
print(s_score)

