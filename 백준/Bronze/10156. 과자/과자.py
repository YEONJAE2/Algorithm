k, N, M = map(int,input().split())
money = -1*(M - (k*N))
if money < 0:
   money = 0
print(money)