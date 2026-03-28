import os

dirts = ['proj','proj/exist.txt','proj/mayfile']
for d in dirts:
    os.makedirs(d, exist_ok = True) # ex need if i had any fils with name in dirts
    print(f'created:{d} ')

if os.path.exists('anyfils'): #find that file is exists or not
    print('this file exists')
else:
    print('this file do not exists')


os.rename('proj/mayfile','proj/myfile') # it is work if file is empty




