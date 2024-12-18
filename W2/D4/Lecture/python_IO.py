#Oldschool method of accessing API
# f = open('sample.txt','r+')
# content = f.read()
# print(content)
# f.close() #manually close the file.

# try:
#     f = open('sample.txt','r+')
#     content = f.read()
#     print(content)
# finally:
#     f.close()

############################################
#NewSchool Version of using the word "with"

with open('sample1.txt', 'a+', encoding= 'utf-8') as f:
    for i in range (10):
        f.write(f'this is line {i}\n')
content = f.read()
print(content)

