#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/09/30
#Date Modified: 2021/09/30
#############################################################################

rate = float(input('What is your rate of pay? '))
hours = float(input("How many hours did you work? "))
gross_pay = rate * hours
ei = round(gross_pay * 0.0158, 2)
cpp = round(gross_pay * 0.0545, 2)
tax = round(ei + cpp, 2)
net = round(gross_pay - tax, 2)
yearly_pay = round(gross_pay * 50, 2)
yearly_deductions = tax * 50

print(f"Gross pay: ${gross_pay}")
print(f"Employement insurance Deduction: ${ei}")
print(f"CPP deductions: ${cpp}")
print(f"Total deductions: ${tax}")
print(f"Net Pay (after deductions): ${net}")
print(f"Yearly pay at that rate: ${yearly_pay}")
print(f"Yearly deductions ${yearly_deductions}")