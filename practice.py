"Day 1"
"""
##Write programs that:
##Calculate area of a rectangle
##print('What is the length?')
##length=input('>')
##print('What is the width?')
##width=input('>')
##print('The area of this rectangle is '+ str(int(length)*int(width)))
##Convert temperature (F to C)
##print('What is the temp in F degrees?')
##F=input('>')
##print('The temp in C is'+str((int(F)-32)/1.8))
##Concatenate user's first and last name
##print('What is your first name?')
##f_name=input('>')
##print('What is your last name?')
##l_name=input('>')
##print('Hello '+f_name+' '+l_name)
"""
'Day 2'
'''
##Write programs that:
##Check if number is even/odd
##print('Pick a number')
##g_num=input('>')
##if int(g_num)%2==0:
## print('That number is even')
##else:
## print('That number is odd')
##Validate user age (must be 18+)
##print('How old are you?')
##u_age=input('>')
##if int(u_age) >= 18:
## print('Access granted')
##else:
## print('Access denied')
##Grade calculator (A, B, C, D, F based on score)
print('What was you score?')
stu_score=input('>')
if int(stu_score)>=90:
    print('You got an A!')
elif int(stu_score)>=80:
    print('You got a B!')
elif int(stu_score)>=70:
    print('You got a C')
elif int(stu_score)>=60:
    print('You got a D')
else:
    print('You got an F')
# Create a number guessing game:
# 1. Program picks random number 1-100
# 2. User has 7 tries to guess
# 3. Give "higher" or "lower" hints
# 4. Track number of attempts

import random
initial_num=random.choice(range(1,101))
guesses=[]
print('I"m thinking of a number between 1 and 100, can you guess which number?')
guess=int(input('>'))
while len(guesses)<8:
    guesses.append(guess)
    if guess == initial_num:
        print('Wow you guessed right!')
        break
    elif guess < initial_num:
        print(f'It"s higher then that. Guess again.You have {7-len(guesses)} guesses left.')
        guess = int(input('>'))
    elif guess > initial_num:
        print(f'It"s lower then that. Guess again.You have {7-len(guesses)} guesses left.')
        guess = int(input('>'))
print(f'You"re out of guesses. The number was {initial_num}')
'''
'Day 3'

##Build a simple to-do list manager:
##Add tasks
##Remove tasks
##View all tasks
##Mark tasks complete
# Our two lists start empty
tasks = []
statuses = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. See all tasks")
    print("2. Add a task")
    print("3. Mark a task as DONE")
    print("4. Remove a task")
    print("5. Exit")

    choice = input("What do you want to do? ")

    if choice == "1":
        print("\nYour List:")
        # We look through the list by number (0, 1, 2...)
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i], "[", statuses[i], "]")

    elif choice == "2":
        new_task = input("What is the task? ")
        tasks.append(new_task)
        statuses.append("Not Done")
        print("Task added!")

    elif choice == "3":
        number = input("Which task number is finished? ")
        # We turn the string "1" into the number 1, then subtract 1
        index = int(number) - 1
        statuses[index] = "Done"
        print("Great job finishing that!")

    elif choice == "4":
        number = input("Which task number should we delete? ")
        index = int(number) - 1
        # .pop() removes the item from the list
        tasks.pop(index)
        statuses.pop(index)
        print("Task deleted.")

    elif choice == "5":
        print("See you later!")
        break
##Daily Exercise:
# Create a student grade tracker:
# 1. Store student names and grades in lists
# 2. Calculate class average
# 3. Find highest and lowest grades
# 4. List students above average

'Day 4'
"""
##Begin building a CSV data analyzer:
##Store records as list of dictionaries
##Basic statistics (count, sum)
##Daily Exercise:
# Create an inventory system:
# 1. Store items: {name: quantity, price}
# 2. Add new items
# 3. Update quantities
# 4. Calculate total inventory value
# 5. Find items below minimum stock
"""
'Day 5'
"""
Refactor previous exercises into functions
Create utility functions:
Data validation
Calculations
Formatting
Build a small function library

 Create a data cleaning module:
# 1. Function to remove extra whitespace
# 2. Function to validate email format
# 3. Function to standardize phone numbers
# 4. Function to convert data types
# Test each function with sample data
"""
'Day 6'
"""
Build a log file analyzer:
Read log file line by line
Count error vs warning messages
Extract timestamps
Handle missing files gracefully

Create a data backup tool:
# 1. Read data from input file
# 2. Process/transform data
# 3. Write to backup file with timestamp
# 4. Handle file not found errors
# 5. Log success/failure

"""