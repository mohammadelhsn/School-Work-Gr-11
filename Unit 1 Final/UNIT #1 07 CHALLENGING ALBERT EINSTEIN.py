#############################################################################
#Author: Mohammad El-Hassan
#Description: UNIT #1 07 CHALLENGING ALBERT EINSTEIN
#Date Created: 2021/10/26
#Date Modified: 2021/10/26
#############################################################################

# Tell the user the instructions

print("Here is a number, `1089` remember this number! You will give me any 3 digit number and I will give you 1089 by simply reversing, adding and subtracting!")

# Ask for user input

num = int(input("Enter a 3 digit number: "))

# Reversing the number

def reverse(num):
    nums = []
    for i in range(0, 3):
        nums.append(num % 10)
        num = num // 10
    return "".join(str(v) for v in nums)

# Calculations and reversed nums

num_reversed = reverse(num)
new_num = abs(int(num_reversed)) - int(num)
new_reversed = int(reverse(new_num))
total = new_num + new_reversed

# Output nums

print("The number you entered is:", num)
print("The reversed number is:", num_reversed)
print("The new number is:", new_num)
print("The new reversed number is:", new_reversed)
print("The total is:", total)
