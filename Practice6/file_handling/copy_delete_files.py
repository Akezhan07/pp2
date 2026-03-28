import os

if os.path.exists("c.txt"):
    os.remove('c.txt')
else:
    print('this file does not exists')

os.rmdir('somethings')
