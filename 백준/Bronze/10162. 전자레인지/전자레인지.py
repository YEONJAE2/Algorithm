time = int(input())
button1 = button2 = button3 = 0
if time %10 != 0: 
    print(-1)
else:
    button1 = time//300
    button2 = (time%300)//60
    button3 = (time%300)%60//10
    print(button1, button2, button3)