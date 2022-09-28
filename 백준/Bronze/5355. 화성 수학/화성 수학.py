T = int(input())
for i in range(T):
    mars_math = list(map(str,input().split()))
    result = float(mars_math[0])
    for j in mars_math:
        if j =="@":
            result *= 3
        elif j =="%":
            result += 5
        elif j =="#":
            result -= 7

    print("%0.2f" % result)