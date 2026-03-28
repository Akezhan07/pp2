import os
import shutil

f = open('fir.txt','a')
os.makedirs('folder',exist_ok=True)
shutil.move('fir.txt','folder/fir.txt')
print('done!')
f.close()