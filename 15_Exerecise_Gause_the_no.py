# Exrexise 3  -- Gause the number

n=18
i=0
while(i<=9):
    i+=1
    if i>=9:
        print("Game Over ..... You all ready use all no of guess")
        break
    elif i<=9:
        print(9-i,"th Attempt left the guessing the number")
        num=int(input("Enter your guess Number : "))
        if n == num:
            print("Congratulation, You Win !!!! you are correctly guess the number")
            break
        elif n >= num:
            print("your number is smaller than guessing number")
        elif  n <= num:
            print("Your no is greater than the guessing number")

    else:
        continue