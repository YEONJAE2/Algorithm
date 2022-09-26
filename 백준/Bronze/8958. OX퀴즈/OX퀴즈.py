T = int(input())
for i in range(T) :
    O_X = list(input())
    score = 0
    sum = 0
    for j in O_X:
        if j == "O":
            score += 1
            sum += score
        else :
            score = 0
    print(sum)