chances=1
print("...you have total 9 chances of guessing the number... \n")
while (True):
    if chances<9 :
        n = int(input("guess the number: "))
        if n < 20:
            print("guess a greater number")
            print("you are left with",9-chances,"more chances to guess the number \n")
            chances = chances+1
            continue
        elif n >= 20 and n < 29:
            print("guess a little greater")
            print("you are left with", 9 - chances, "more chances to guess the number \n")
            chances = chances + 1
            continue
        elif n > 29 and n <= 38:
            print("guess a little smaller")
            print("you are left with", 9 - chances, "more chances to guess the number \n")
            chances = chances + 1
            continue
        elif n > 38:
            print("guess a smaller number")
            print("you are left with", 9 - chances, "more chances to guess the number \n")
            chances = chances + 1
            continue
        else:
            print("congratulations! you guessed it right! \n")
            print("you took", chances, "chances for guessing the number")
            break
    elif chances==9:
        n = int(input("guess the number: "))
        if n < 20:
            print("Alas! you couldn\'t guess it right \n")
            chances = chances + 1
            continue
        elif n >= 20 and n < 29:
            print("Alas! you couldn\'t guess it right \n")
            chances = chances + 1
            continue
        elif n > 29 and n <= 38:
            print("Alas! you couldn\'t guess it right \n")
            chances = chances + 1
            continue
        elif n > 38:
            print("Alas! you couldn\'t guess it right \n")
            chances = chances + 1
            continue
        else:
            print("congratulations! you guessed it right! \n")
            print("you took",chances,"chances for guessing the number")
            break
    else:
        print("you ran out of chances. GAME OVER!")
        break
