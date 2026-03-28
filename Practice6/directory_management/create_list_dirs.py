import os

# Define a list of directory paths to be created
dirts = ['proj', 'proj/exist.txt', 'proj/mayfile']

for d in dirts:
    # Create the directory; exist_ok=True prevents errors if it already exists
    os.makedirs(d, exist_ok=True) 
    print(f'created: {d}')

# Check if the specified path exists in the current working directory
if os.path.exists('anyfils'): 
    print('this file exists')
else:
    # Execute this if the path 'anyfils' cannot be found
    print('this file do not exists')

# Rename the directory/file from the first argument to the second argument
os.rename('proj/mayfile', 'proj/myfile')