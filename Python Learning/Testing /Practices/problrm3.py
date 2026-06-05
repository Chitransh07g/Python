import os

# Specify the directory you want to list
directory = '.'  # Use '.' for the current directory, or specify another path

# Get the list of files and directories in the specified directory
contents = os.listdir(directory)

# Print the contents
print("Contents of the directory:", directory)
for item in contents:
    print(item)
