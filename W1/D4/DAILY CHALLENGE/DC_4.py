# Given a “Matrix” string:

#     7ii
#     Tsx
#     h%?
#     i #
#     sM 
#     $a 
#     #t%
#     ^r!

# Matrix: A matrix is a two-dimensional array. It is a grid of numbers arranged in rows and columns.
# To reproduce the grid, the matrix should be a 2D list, not a string



# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix.

#convert a string to a list - Done
#create a list in a list aka a Matrix - Done
#read each column from top to bottom, starting from the leftmost column. Reference each index [0],[1],[2].
#Then replace every group of symbols between two alpha characters by a space. Make a space between end letter and beginning letter with a space.
#Then take the alpha characters and create a list for the decrypted message string.

m_string = '''7ii
Tsx
h%?
i #
 sM 
 $a 
#t%
^r!
'''
my_list = m_string.splitlines()
n_cols = 3
n_rows = 8
Secret_message = []
matrix = [list(row) for row in my_list]

for row in range(len(matrix[0])):
    for col in matrix:
        char = col[row]
        if char.isalpha(): #How to detect a letter vs symbol in a string https://stackoverflow.com/questions/40097590/detect-whether-a-python-string-is-a-number-or-a-letter
            Secret_message.append(char)
print(Secret_message)

        

    
    
   
    
    