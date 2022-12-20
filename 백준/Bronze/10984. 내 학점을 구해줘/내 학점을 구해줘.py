for _ in range(int(input())):
    credit = 0
    total = 0
    for _ in range(int(input())):
        c, g = map(float, input().split())
        credit += int(c)
        total += c * g
    GPA = total / credit
    print(credit, '%.1f'%GPA)