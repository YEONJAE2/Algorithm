V = int(input())
ab_list = str(input())
a = ab_list.count('A')
b = ab_list.count('B')

if a > b:
     print("A")
elif b > a:
     print("B")
else: 
     print('Tie')
