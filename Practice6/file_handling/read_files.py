# Open the file 'a.txt' in read-only mode ('r')
f = open("a.txt", "r")

# Read and print only the first 6 characters from the file
print(f.read(6)) 

# Read all remaining lines in the file and return them as a list of strings
print(f.readlines())

# Close the file to free up system resources
f.close()