N = int(input())
money_list = []
for i in range(N):
    a, b, c = map(int, input().split())
    if a==b==c:
        money = 10000 + a * 1000
    elif a==b!=c:
        money = 1000+a*100
    elif a==c!=b:
        money = 1000+a*100
    elif b==c!=a:
        money = 1000+b*100    
    else:
        max_number = max([a,b,c])
        money = max_number*100
    money_list.append(money)


print(max(money_list))