import sys
import time

f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
             break
        priint(line, end='')
        sys.stdout.flush()
        print('Press ctrl+c now')
        time.slepp(2)
except IOError:
    print('Could not find file poem.text')
except KeyboardInterrupt:
    print('!! Y ou cancelled the reading from the filee. ')
finally:
    if f:
        f.close()
    print('(Cleaning up: closed the file)')
