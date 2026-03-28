import os

# Check if the file 'c.txt' exists in the current directory
if os.path.exists("c.txt"):
    # Delete the file 'c.txt' permanently
    os.remove('c.txt')
else:
    # Print a message if the file was not found
    print('this file does not exists')

# Remove the directory named 'somethings'
# Note: This function only works if the directory is empty
os.rmdir('somethings')