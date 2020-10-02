import math
import argparse

stage_1 ='''loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

write your code here
print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)'''
stage_2 = '''def number_payments(total):
    payment = int(input("Enter the monthly payment:"))
    if total / payment == 1:
        print("It will take 1 month to repay the loan")
    else:
        time = ceil(total / payment)
        print(f"It will take {int(time)} months to repay the loan")


def amount_payments(total):
    number = int(input("Enter the number of months:"))
    monthly = total / number
    if total % number == 0:
        print(f"Your monthly payment = {int(monthly)}")
    else:
        last_payment = total - (number - 1) * ceil(monthly)
        print(f"Your monthly payment = {ceil(monthly)} and the last payment = {last_payment}.")


principal = int(input("Enter the loan principal:"))
option = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")
if option == "m":
    number_payments(principal)
elif option == "p":
    amount_payments(principal)
'''
stage_3 = '''
def convert(number):
    if number < 2:
        return "1 month"
    elif number < 12:
        return f"{number} months"
    elif number == 12:
        return "1 year"
    elif number % 12 == 0:
        return f"{number / 12} years"
    else:
        return f"{number // 12} years and {number % 12} months"


def monthly():
    p = int(input("Enter the loan principal:"))
    a = float(input("Enter the monthly payment:"))
    loan_int = float(input("Enter the loan interest:"))
    i = loan_int / (12 * 100)
    n = math.ceil(math.log(a / (a - i * p), 1 + i))
    print(f"It will take {convert(n)} to repay this loan!")


def annuity():
    p = int(input("Enter the loan principal:"))
    n = int(input("Enter the number of periods:"))
    loan_int = float(input("Enter the loan interest:"))
    i = loan_int / (12 * 100)
    a = p * (i * pow(1 + i, n))/(pow(1 + i, n) - 1)
    print(f"Your monthly payment = {math.ceil(a)}!")


def loan():
    a = float(input("Enter the annuity payment:"))
    n = int(input("Enter the number of periods:"))
    loan_int = float(input("Enter the loan interest:"))
    i = loan_int / (12 * 100)
    p = a / ((i * pow(1 + i, n))/(pow(1 + i, n) - 1))
    print(f"Your loan principal = {math.floor(p)}!")


option = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for the loan principal:""")
if option == "n":
    monthly()
elif option == "a":
    annuity()
elif option == "p":
    loan()'''


def convert(number):
    if number < 2:
        return "1 month"
    elif number < 12:
        return f"{number} months"
    elif number == 12:
        return "1 year"
    elif number % 12 == 0:
        return f"{int(number / 12)} years"
    else:
        return f"{int(number // 12)} years and {int(number % 12)} months"


def monthly(p1, a1, loan_int):
    i1 = loan_int / (12 * 100)
    n1 = math.ceil(math.log(a1 / (a1 - i1 * p1), 1 + i1))
    print(f"It will take {convert(n1)} to repay this loan!")
    print("Overpayment = {}".format(math.ceil(a1 * n1 - p1)))


def annuity(p2, n2, loan_int):
    i2 = loan_int / (12 * 100)
    a2 = p2 * (i2 * pow(1 + i2, n2))/(pow(1 + i2, n2) - 1)
    print(f"Your annuity payment = {math.ceil(a2)}!")
    print("Overpayment = {}".format(math.ceil(a2) * n2 - p2))


def loan(a3, n3, loan_int):
    i3 = loan_int / (12 * 100)
    p3 = a3 / ((i3 * pow(1 + i3, n3))/(pow(1 + i3, n3) - 1))
    print(f"Your loan principal = {math.floor(p3)}!")
    print("Overpayment = {}".format(math.ceil(a3 * n3 - p3)))


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", help="Choose option to calculate", type=str)
parser.add_argument("-p", "--payment", type=int)
parser.add_argument("-pr", "--principal", type=int)
parser.add_argument("-pe", "--periods", type=int)
parser.add_argument("-i", "--interest", type=float)

args = parser.parse_args()

n = args.periods
p = args.principal
pa = args.payment
inter = args.interest

if args.type is None:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif args.type == "annuity":
    if args.principal is None:
        loan(pa, n, inter)
    elif args.payment is None:
        annuity(p, n, inter)
    elif args.periods is None:
        monthly(p, pa, inter)
elif args.type == "diff":
    i = inter / (12 * 100)
    over = 0
    for m in range(1, n+1):
        d = p / n + i * (p - (p * (m - 1) / n))
        print("Month {}: payment is {}".format(m, math.ceil(d)))
        over += math.ceil(d)
    print("Overpayment = {}".format(over - p))
else:
    print("Incorrect parameters")
