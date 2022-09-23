bowl = list(str(input()))
sum = 10
for i in range (1,len(bowl)) :
     if bowl[i-1] == bowl[i] :
          sum += 5
     else : sum += 10
print(sum)