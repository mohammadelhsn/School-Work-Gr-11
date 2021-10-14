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
    sum = 0
    for i in nums:
        sum += i
    return sum / len(nums)

# Assign average to avg variable

avg = findAverage()

# Print out the results

print(f"Here is the average of {num1}, {num2}, {num3} and {num4}: Average: {avg}")