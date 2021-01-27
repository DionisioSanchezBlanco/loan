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

def nominal_interest_rate(loan_percent):
    return loan_percent / (12 * 100)

def number_months (monthly_money, interest, loan_principal):
    return math.log(monthly_money / (monthly_money - interest * loan_principal), 1 + interest)

def monthly_payment (interest, loan_percent, loan_principal, periods):
    return loan_principal * ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))

def quantiy_loan (interest, loan_percent, periods, annuity):
    return annuity / ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
# Main

print('''What do you want to calculate?
type "n" - for number of monthly payments,
type "a" - for annuity monthly payment amount,
type "p" - for loan principal:''')
option = input()

if option == 'n':
    print("Enter the loan principal:")
    loan_principal = int(input())
    print('Enter the monthly payment:')
    monthly_money = int(input())
    print('Enter the loan interest:')
    loan_percent = float(input())

    interest = nominal_interest_rate(loan_percent)
    months = number_months(monthly_money, interest, loan_principal)
    number_years = round(months) / 12
    rest_months = math.ceil(months) % 12

    if rest_months == 0:
        if number_years != 1:
            print(f"It will take {round(number_years)} years to repay this loan!")
        else:
            print(f"It will take {round(number_years)} year to repay this loan!")
    else:
        if number_years == 0:
            if rest_months != 1:
                print(f"It will take {rest_months} months to repay this loan!")
            else:
                print(f"It will take {rest_months} month to repay this loan!")
        else:
            if rest_months != 1 and number_years == 1:
                print(f"It will take {round(number_years)} year {rest_months} months to repay this loan!")
            elif rest_months == 1 and number_years == 1:
                print(f"It will take {round(number_years)} year {rest_months} month to repay this loan!")
            elif rest_months == 1 and number_years != 1:
                print(f"It will take {round(number_years)} years {rest_months} month to repay this loan!")
            else:
                print(f"It will take {round(number_years)} years {rest_months} month to repay this loan!")
        
elif option == 'a':
    print("Enter the loan principal:")
    loan_principal = int(input())
    print('Enter the number of periods:')
    periods = int(input())
    print('Enter the loan interest:')
    loan_percent = float(input())

    interest = nominal_interest_rate(loan_percent)
    quantity_monthly = monthly_payment (interest, loan_percent, loan_principal, periods)
    print(f'Your monthly payment = {math.ceil(quantity_monthly)}!')
else:
    # Last example. Loan principal
    print("Enter the annuity payment:")
    annuity = float(input())
    print('Enter the number of periods:')
    periods = int(input())
    print('Enter the loan interest:')
    loan_percent = float(input())
    
    interest = nominal_interest_rate(loan_percent)
    result_loan = quantiy_loan (interest, loan_percent, periods, annuity)
    print(f'Your loan principal = {round(result_loan)}!')
