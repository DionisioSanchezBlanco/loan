import argparse
import math

# Check if the argument --type is correct
def check_type(typee):
    if typee:
        pass
    else:
        return 0


# Check if --payment argument is correct
def check_payment(payment, typee):
    if typee == "diff" and payment:
        return 0


# Begin Formulas
# Monthly payment formula
def calculating_payments(principal, periods, interest, month):
    return (principal / periods) + (interest / (12 * 100)) * (principal - ((principal * (month - 1)) / periods))

# Annuity formula
def annuity_calculating_payments(principal, periods, interest):
    nominal_interest = interest / (100 * 12)
    return principal * (nominal_interest * math.pow(1 + nominal_interest, periods) / (math.pow(1 + nominal_interest, periods) - 1))

# Annuity formula monthly
def annuity_calculating_payments_monthly(payment, periods, interest):
    nominal_interest = interest / (100 * 12)
    return payment / (nominal_interest * math.pow(1 + nominal_interest, periods) / (math.pow(1 + nominal_interest, periods) - 1))

def periods_calculating(principal, payment, interest):
    nominal_interest = interest / (100 * 12)
    return math.log(payment / (payment - nominal_interest * principal), 1 + nominal_interest)    

# End Formulas


def last_payment(principal, periods):
    return (principal - (periods - 1) * (math.ceil(principal / periods)))

def calc_monthly_payments(principal, periods, interest):

    month = 1
    payment_total = 0

    while month != (periods + 1):  
        payment_monthly = calculating_payments(principal, periods, interest, month)
        print(f"Month {month}: payment is {math.ceil(payment_monthly)}")
        payment_total += math.ceil(payment_monthly)
        month += 1

    pt = payment_total - principal
    print(f"\nOverpayment = {int(pt)}")

# Annuity with principal
def calc_annuity_payments(principal, periods, interest):
    annuity_payment = 0

    annuity_payment = annuity_calculating_payments(principal, periods, interest)
    print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
    
    pta = (math.ceil(annuity_payment) * periods) - principal
    print(f"\nOverpayment = {int(pta)}")    

# Annuity but monthly payment
def calc_annuity_payments_monthly(payment, periods, interest):

    month = 1
    payment_total = 0
    loan_principal = 0

    loan_principal = annuity_calculating_payments_monthly(payment, periods, interest)
    print(f"Your annuity payment = {math.ceil(loan_principal)}!")
    
    pta = (payment * periods) - loan_principal
    print(f"\nOverpayment = {int(pta)}")    


# Calc periods to pay
def calc_periods(principal, payment, interest):
    periods_pay = periods_calculating(principal, payment, interest)
    years_pay = math.ceil(periods_pay / 12)
    print(f"It will take {years_pay} years to repay this loan!")

    annuity_payment = 0

    annuity_payment = annuity_calculating_payments(principal, periods_pay, interest)
    
    pta = (math.ceil(annuity_payment) * math.ceil(periods_pay)) - principal
    print(f"\nOverpayment = {int(math.ceil(pta))}")        


# Description about the script functionality
parser = argparse.ArgumentParser(description="Payments calculator")

# Add arguments
parser.add_argument("--type", choices=["diff", "annuity"])
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)

# Reading arguments from command line
args = parser.parse_args()
typee = args.type
payment = args.payment
principal = args.principal
periods = args.periods
interest = args.interest

# Check the number of arguments
list_arguments = [typee, payment, principal, periods, interest]
number_arguments = 0
negative_number = False

for argum in list_arguments:
    if argum != None:
        number_arguments += 1
        if type(argum) == float and argum < 0:
            negative_number = True   

if number_arguments < 4:
    print("Incorrect parameters.")
else:
    if check_type(typee) == 0 or check_payment(payment, typee) == 0:
        print ("Incorrect parameters")
    elif negative_number:
         print ("Incorrect parameters")
    else:
        if typee == 'annuity':
            if principal == None:
                calc_annuity_payments_monthly(payment, periods, interest)
            elif periods == None:
                calc_periods(principal, payment, interest)
            else:
                calc_annuity_payments(principal, periods, interest)
        else:
            calc_monthly_payments(principal, periods, interest)
           