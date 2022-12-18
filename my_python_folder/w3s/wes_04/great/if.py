number = 23
guess = int(input('Enter an interger : '))
if guess == number:
    print('Congratulation, you guessed it.')
    print('(but you do not win any prizes)')


elif guess < number :
    print ('No,it\'s a little higher than that')

else:
    print("ali go to school")
    print("No, it's a little lower than that")

print('Done')
