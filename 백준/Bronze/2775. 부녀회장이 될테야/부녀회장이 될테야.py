arr = [[i for i in range(15)] for j in range(15)]
# print(arr)
for i in range(1,15):
    for j in range(1,15):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    print(arr[k][n])

