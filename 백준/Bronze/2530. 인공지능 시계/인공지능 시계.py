H,M,S = map(int, input().split())
timer = int(input())

S += timer
M += S//60
H += M//60

H %= 24
M %= 60
S %= 60

print(H, M, S)