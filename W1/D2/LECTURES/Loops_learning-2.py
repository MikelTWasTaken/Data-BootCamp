#FOR LOOP
#syntax
# for i in x:
    #what you want to happen each time each itteration in this sequence.
#    print(i)

students = ['Alex','Steve','Sara','Dave']
for each_student in students:
    print(f'Welcome', (each_student)) #include an f so that the message loops around in each element of the variable.
#when you print, each iteration of the for loop will create a new line.

#I want to check if a student is russian and then to say "dobre utra"

students = ['Alex','Steve','Sara','Dave'] #in this case you want to make a distinguishing difference in the greeting.
for each_student in students:
    if each_student == 'Dave':
        print(f'Dobre Utra', (each_student))
    else:
        print('Welcome',(each_student))

#LOOPING THROUGH A RANGE. RANGE IS ANOTHER BUILD METHOD.
for i in range(1,10): #i is not a name or element it is the number of the iteration.
#first number is where to start and last number is where to stop. If you do not put in an endpoint
#it will say that it is missing an argument and will give an error.    
    print('Hello There!')

for i in range(1,len(students)): #you can also print len of a list
    print(f'Hello There {i}')

#FOR ENNUMERATE - loop prints the index and the value
#0 Alex
#1 Steve
#2 Sara
#3 Dave
for i, each_student in enumerate(students):
    print(i,each_student)

# #WHILE Loops
# While loops differ from for loops, they have what we call an indefinite iteration cycle. What that means is that the number of times they execute isn’t defined by the length of a given list but by a specific breakpoint that will stop the loop’s execution when it is hit.
# A while loop is defined somewhat similarly to a conditional statement. The loop will keep running as long as the set condition is True and stop when this condition evaluates to False.
# The while loop runs as long as (or while) a certain condition is true.
# It will execute all the instructions in the loop, then test the condition, if the condition is still True, it will rerun the loop, and again until the condition becomes false.

my_nums = [1,2,3,4,5,6,77]
print(sum(my_nums)) #this is the fastest way to do it

output = 0 #this is what happens behind the scenes of print(sum(my_nums)) above.
for i in range (len(my_nums)):
    output += my_nums[i]
    print(output)

i = 0
while i < 10:
    print(f'Hi,{i}')
    i += 1
#if we want to ask a nuser to add all family members, we can use a while loop. 
#way 1
family = [] #its an empty list because it needs to be added to.
members = input("Write Family Member Name. Press 'q' to finish: ")  #add in a commmand to end the loop because you don't knwo how may family members there are.
while members != 'q':
    members = input("Write Family Member Name. Press 'q' to finish: ")
    family.append(members)

#way 2
family = []
Keep_Asking = True #this is a boolean flag. It was initiated in true so the program can ask.

while Keep_Asking:
    members = input("Write Family Member Name. Press 'q' to finish: ")
    if members == 'q':
        Keep_Asking = False
    else:
        family.append(members)

