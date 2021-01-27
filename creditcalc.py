import argparse
import math

# Check if the argument --type is correct
def check_type(typee):
    if typee:
        pass
    else:
        print("Incorrect parameters")


# Check if --payment argument is correct
def check_payment(payment, typee):
    if typee == "diff" and payment:
        print("Incorrect parameters")

def calculating_payments(principal, periods, interest, month):
    return (principal / periods) + (interest / (12 * 100)) * (principal - ((principal * (month - 1)) / periods))

def last_payment(principal, periods):
    return (principal - (periods - 1) * (math.ceil(principal / periods)))

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

check_type(typee)
check_payment(payment, typee)


# Crear una función pa esto
month = 1
payment_total = 0

while month != (periods + 1):  
    payment_monthly = calculating_payments(principal, periods, interest, month)
    print(f"Month {month}: payment is {math.ceil(payment_monthly)}")
    payment_total += math.ceil(payment_monthly)
    month += 1

pt = payment_total - principal
print(f"Overpayment = {int(pt)}")