line = "Create a program that reads a file and writes a modified version to a new file."
with open("assignment.txt", "w") as file:
    file.write(line)

# This script reads a file 
with open("assignment.txt", "r") as file:
    content = file.read()
    
# Convert to upper case
upper = content.upper()

#Write the modified content to a new file
with  open("done.txt", "w") as file:
    file.write("Upper Case  content:" + "\n" + upper)