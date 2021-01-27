# Loan
import math

# Functions
def months_payment(loan_principal, monthly_money):
    return round(loan_principal / monthly_money)

def money_payment(loan_principal, months_to_pay):
    if loan_principal % months_to_pay == 0:
        return loan_principal / months_to_pay
    else:
        return math.ceil(loan_principal / months_to_pay)

def last_payment(loan_principal, months_to_pay):
    return (loan_principal - (months_to_pay - 1) * (math.ceil(loan_principal / months_to_pay)))


# Main
print("Enter the loan principal:")
loan_principal = int(input())

print('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')
option = input()

if option == 'm':
    print('Enter the monthly payment:')
    monthly_money = int(input())
    months_to_pay = months_payment(loan_principal, monthly_money)
    if months_to_pay != 1:
        print(f"\nIt will take {months_to_pay} months to repay the loan")
    else:
        print(f"\nIt will take {months_to_pay} month to repay the loan")
else:
    print('Enter the number of months:')
    months_to_pay = int(input())
    money_per_month = money_payment(loan_principal, months_to_pay)
    last_month = last_payment(loan_principal, months_to_pay)
    if last_month != money_per_month:
        print(f'\nYour monthly payment = {money_per_month} and the last payment = {last_month}')
    else:
        print(f'\nYour monthly payment = {money_per_month}')
    

