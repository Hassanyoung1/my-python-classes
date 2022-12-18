while True:
    s  = input('Enter my name :')
    if s == 'quit':
         break
    if len(s) < 3:
        print('too small')
        continue
    print('Input is of sufficient lenght')
else:
    print('done')
