number = 15
running = True

while running :
    guess = int(input('Enter An Integer : '))

    if guess == number:
        print("Congratulation, Omo elewa. :")


    elif guess < number :
        print("No, if is a higher than that")
        running = False


    else :
        print('No, it is a little lower than that')
else:
    print('The while loop is over')
    print ('Done')
