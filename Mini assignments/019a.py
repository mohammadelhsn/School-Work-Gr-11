#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignment 4
#Date Created: 2021/10/12
#Date Modified: 2021/10/12
#############################################################################

# Imports

# Constants

# Define numbers to go into the array / list

num1 = 90
num2 = 85
num3 = 74
num4 = 68

# Make the list of numbers

nums = [num1, num2, num3, num4]

# Make this function to loop through the list add the numbers and divide 
# by the length of the list / array 

def findAverage():

    # Define sum variable

    sum = 0

    # For every number in the list of numbers, add it to the total 
    
    for i in nums:
        sum += i

    # Divide by the total by the length of the list to get the average

    return (sum / len(nums))

# Assign average to avg variable

avg = findAverage()

# Print out the results

print(f"Here is the average of {num1}, {num2}, {num3} and {num4}: Average: {avg}")