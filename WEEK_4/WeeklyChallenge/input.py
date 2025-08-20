# Read the contents of input.txt, process it, and write to output.txt

# Step 1: Read the contents of input.txt
with open('input.txt', 'r') as f:
    content = f.read()

# Step 2: Count the number of words
word_count = len(content.split())

# Step 3: Convert all text to uppercase
processed_content = content.upper()

# Step 4: Write the processed text and the word count to output.txt
with open('output.txt', 'w') as f:
    f.write(processed_content)
    f.write(f"\nWord Count: {word_count}\n")

# Print a success message
print("The file output.txt has been created successfully.")
