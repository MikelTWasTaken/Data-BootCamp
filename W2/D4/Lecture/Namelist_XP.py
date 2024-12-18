# Download this text file http://www.practicepython.org/assets/nameslist.txt and do the following steps


# Read the file line by line
# Read only the 5th line of the file
# Read only the 5 first characters of the file
# Read all the file and return it as a list of strings. Then split each word
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"

############################################

# Read the file line by line
with open('/Users/teitelbaumsair/Desktop/DI_Bootcamp/W2/D4/nameslist.txt', 'r',encoding = 'utf-8') as f:
    lines = f.readlines()
print(lines)

# Read only the 5th line of the file
fifth_line = lines[4] # Indexing starts from 0, so the 5th line is at index 4
print(fifth_line)

# Read only the 5 first characters of the file
with open('/Users/teitelbaumsair/Desktop/DI_Bootcamp/W2/D4/nameslist.txt', 'r', encoding = 'utf-8') as f:
    first_5_chars = f.readline(5)
print(first_5_chars)
# Read all the file and return it as a list of strings. Then split each word
with open('/Users/teitelbaumsair/Desktop/DI_Bootcamp/W2/D4/nameslist.txt', 'r', encoding = 'utf-8') as f:
    content = f.read()  # Read all the content
    words = content.split()
print(words)

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
darth_count = words.count('Darth')
luke_count = words.count('Luke')
lea_count = words.count('Lea')

# Append your first name at the end of the file
with open('/Users/teitelbaumsair/Desktop/DI_Bootcamp/W2/D4/nameslist.txt', 'a', encoding = 'utf-8') as f:
    first_5_chars = f.write('\nTeitelbaum')

# Append "SkyWalker" next to each first name "Luke"
updated_lines = []
with open('/Users/teitelbaumsair/Desktop/DI_Bootcamp/W2/D4/nameslist.txt', 'r+', encoding = 'utf-8') as f:
    for line in f:
        updated_line = line.replace("Luke", "Luke SkyWalker")
        updated_lines.append(updated_line)

print(f"5th line: {fifth_line.strip()}")
print(f"First 5 characters: {first_5_chars}")
print(f"Occurrences of 'Darth': {darth_count}")
print(f"Occurrences of 'Luke': {luke_count}")
print(f"Occurrences of 'Lea': {lea_count}")