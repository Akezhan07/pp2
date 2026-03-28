import os
import shutil

# Open (or create) 'fir.txt' in append mode ('a')
f = open('fir.txt', 'a')

# Create a directory named 'folder'; avoid errors if it already exists
os.makedirs('folder', exist_ok=True)

# Move 'fir.txt' from the current directory into the 'folder' directory
shutil.move('fir.txt', 'folder/fir.txt')

# Inform the user that the operation was successful
print('done!')

# Close the file object to free up system resources
f.close()