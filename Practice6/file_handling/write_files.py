# Open (or create) 'b.txt' in write mode ('w')
# This will overwrite any existing content in the file
f = open('b.txt', 'w')

# Write a specific string of text into the file
f.write('it is first line in file')

# Get the current position of the file pointer
# This tells you how many bytes have been written so far
print(f.tell()) 

# Close the file to ensure the data is saved to the disk
f.close()