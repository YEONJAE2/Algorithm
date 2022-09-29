T = int(input()) # 테스트 케이스 숫자
for _ in range(T): 
    N = int(input()) # 비교할 학교 수
    max = 0
    for _ in range(N): 
        name, num = input().split()
        num = int(num)
        if num > max:
            max = num
            result = name
    print(result)