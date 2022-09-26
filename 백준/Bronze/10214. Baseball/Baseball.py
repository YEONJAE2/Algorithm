T = int(input())
for i in range(T):#테스트 돌리기 위함
    Y_sum = 0
    K_sum = 0
    for j in range(9): # 입력 위함
        y,k = map(int,input().split())
        Y_sum += y
        K_sum += k

    if Y_sum > K_sum :
        print("Yonsei")
    elif Y_sum < K_sum :
        print("Korea")
    else :
        print("Draw")