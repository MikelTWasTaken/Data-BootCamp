# Exercise 1 : Student Grade Summary
# Instructions
# You are given a dictionary containing student names as keys and lists of their grades as values. Your task is to create a summary report that calculates the average grade for each student, assigns a letter grade, and determines the class average.
# Initial Data:

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# Requirements:
# Calculate the average grade for each student and store the results in a new dictionary called student_averages.
# Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
# A: >= 90
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60

def grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"
    

grade_avg = {}
for key, value in student_grades.items():
    grade_avg[key] = sum(value)/ float(len(value))

print(grade_avg)

# Calculate the class average (the average of all students’ averages) and print it.
class_avg = {}
for key, value in grade_avg.items():
    class_avg[key] = sum(value)/float(len(value))

print(class_avg)

grade_avg = {}
for key, value in student_grades.items():
    avg_score = sum(value) / float(len(value))  # Calculate the average grade
    letter_grade = grade(avg_score)  # Assign the letter grade based on the average
    grade_avg[key] = (avg_score, letter_grade)  # Store both average and letter grade

# Print the name, average grade, and letter grade for each student
for student, (avg_score, letter_grade) in grade_avg.items():
    print(f"{student}: Average Grade = {avg_score:.2f}, Letter Grade = {letter_grade}")



# 🌟 Exercise 2 : Advanced Data Manipulation and Analysis
# Instructions
# In this exercise, you will analyze data from a hypothetical online retail company to gain insights into sales trends and customer behavior. The data is represented as a list of dictionaries, where each dictionary contains information about a single purchase.



# sales_data = [
#     {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
#     {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
#     {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
#     {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
#     {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
#     {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
#     {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
# ]


# Tasks:
# Total Sales Calculation: Calculate the total sales for each product category (i.e., the total revenue generated from each type of product). Use a loop to iterate through the data and a dictionary to store the total sales for each product.

# Customer Spending Profile: Determine the total amount spent by each customer. Use a dictionary to maintain the sum of amounts each customer has spent.

# Sales Data Enhancement:

# Add a new field to each transaction called “total_price” that represents the total price for that transaction (quantity * price).
# Use a loop to modify the sales_data list with this new information.
# High-Value Transactions:

# Using list comprehension, create a list of all transactions where the total price is greater than $500.
# Sort this list by the total price in descending order.
# Customer Loyalty Identification:

# Identify any customer who has made more than one purchase, suggesting potential loyalty.
# Use a dictionary to count purchases per customer, then use a loop or comprehension to identify customers meeting the loyalty criterion.
# Bonus: Insights and Analysis:

# Calculate the average transaction value for each product category.
# Identify the most popular product based on the quantity sold.
# Provide insights into how these analyses could inform the company’s marketing strategies.
