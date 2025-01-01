# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

def main():
    my_list = [1,2,3,4]
    print('Initial List:',(my_list))

    item = int(input(f'Enter a number to insert: '))
    index = int(input('Enter the index: '))
    my_list.insert(index,item)
    print('Updated List:',(my_list))

if __name__ == "__main__":
    main()

# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

def main():
    my_string = input('Enter a string: ')
    count = my_string.count(' ')
    print('Number of spaces:', count)


if __name__ == "__main__":
    main()

# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

def main():
    my_string = input('Enter a string: ')
    upper = sum(1 for c in my_string if c.isupper())
    lower = sum(1 for c in my_string if c.islower())
    print('Number of upper case letters:', upper)
    print('Number of lower case letters:', lower)

if __name__ == "__main__":
    main()

# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:
def main():
    my_list = [1,5,4,2]
    total = 0
    for i in my_list:
        total += i
    print('Sum:', total)

if __name__ == "__main__":
    main()

# Exercise 5
# Instructions
# Write a function to find the max number in a list
def main():
    my_list = [0,1,3,50]
    print('Max number:', max(my_list))

# Exercise 6
# Instructions
# Write a function that returns factorial of a number
def main():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
n = 24
result = factorial(n)
print('Factorial:', result)  

if __name__ == "__main__":
    main()

# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):
def list_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

result = list_count(['a', 'a', 't', 'o'], 'a')
print(result) 

# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

def norm(lst):
    squared_sum = sum(x**2 for x in lst)
    return squared_sum**0.5
lst = [1, 2, 2]
result = norm(lst)
print('result:',result)

# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

def is_mono(array):
    increasing = decreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            increasing = False
        if array[i] > array[i-1]:
            decreasing = False

    return increasing or decreasing

print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))


# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

def find_longest_word(words):
    longest_word = ''
    max_length = 0

    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word
words = ['Hello', 'World', 'I', 'am', 'here']
result = find_longest_word(words)
print(result)


# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def filter_list(lst):
    integers = []
    strings = []

    for item in lst:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)

    return integers, strings

lst = [1, 'apple', 3, 'banana', 7, 'cherry']
integers, strings = filter_list(lst)
print('Integers:', integers)
print('Strings:', strings)

# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

def is_palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]
print(is_palindrome('radar'))
print(is_palindrome('John'))


# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:
def sum_over_k(sentence, k):
    return sum(len(word) > k for word in sentence.split())

sentence = 'Do or do not there is no try'
k = 2
print(sum_over_k(sentence, k))
# >>>sentence = 'Do or do not there is no try'
# >>>k=2
# >>>sum_over_k(sentence,k)
# >>>3


# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):


def dict_avg(d):
    return sum(d.values()) / len(d)
print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1})) 
# >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
# >>>3


# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

def common_div(a, b):
    return [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
print(common_div(10, 20)) 

# >>>common_div(10,20)
# >>>[2,5,10]


# Exercise 16
# Instructions
# Write a function that test if a number is prime:

# >>>is_prime(11)
# >>>True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11)) 

# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:
def weird_print(lst):
    return [value for index, value in enumerate(lst) if index % 2 == 0 and value % 2 == 0]

print(weird_print([1, 2, 2, 3, 4, 5]))
# >>>weird_print([1,2,2,3,4,5])
# >>>[2,4]


# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

def type_count(**kwargs):
    type_counts = {}
    for value in kwargs.values():
        t = type(value).__name__
        type_counts[t] = type_counts.get(t, 0) + 1
    return ', '.join(f"{t}: {count}" for t, count in type_counts.items())

print(type_count(a=1, b='string', c=1.0, d=True, e=False))

# >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
# >>>int: 1, str:1 , float:1, bool:2


# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.

# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def my_split(string, delimiter=' '):
    result = []
    current = ''
    for char in string:
        if char == delimiter:
            if current:
                result.append(current)
                current = ''
        else:
            current += char
    if current:
        result.append(current)
    return result

print(my_split('hello world'))           
print(my_split('a,b,c,d', delimiter=','))

# Exercise 20
# Instructions
# Convert a string into password format.

# Example:
# input : "mypassword"
# output: "***********"

def to_password_format(string):
    return '*' * len(string)
print(to_password_format("mypassword")) 