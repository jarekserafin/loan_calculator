# read READ.ME for informations about this program

import argparse
import math

parser = argparse.ArgumentParser(description="This program calculates important loan staff")
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
_type = args.type
payment = args.payment
principal = args.principal
periods = args.periods
interest = args.interest
parameters = [args.type, args.payment, args.principal, args.periods, args.interest]
if interest is not None:
    interest = float(interest)
if payment is not None:
    payment = float(payment)
if principal is not None:
    principal = float(principal)
if periods is not None:
    periods = int(periods)
number_of_parameters = 0
invalid_input = False
for parameter in parameters:
    if parameter is not None:
        number_of_parameters += 1
# print("number = " + str(number_of_parameters))
if interest is None:
    invalid_input = True
elif _type not in ["annuity", "diff"]:
    invalid_input = True
elif _type == "diff":
    if payment is not None:
        invalid_input = True
    if principal is not None and periods is not None and number_of_parameters == 4:
        P = principal
        n = periods
        i = interest / (12 * 100)
        monthly = list()
        for m in range(n):
            m += 1
            D = math.ceil(P / n + i * (P - P * (m - 1) / n))
            monthly.append(D)
        overpayment = int(math.fsum(monthly) - P)
        x = 1
        for month in monthly:
            print("Month " + str(x) + ": payment is " + str(month))
            x += 1
        print()
        print("Overpayment = " + str(overpayment))
elif _type == "annuity":
    if number_of_parameters != 4:
        invalid_input = True
    else:
        if periods is None:
            i = interest / (12 * 100)
            all_months = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
            # all_months = math.ceil(principal / payment)
            if all_months > 11:
                years = math.floor(all_months / 12)
                months = all_months % 12
                if months == 0:
                    print("It will take " + str(years) + " years to repay this loan!")
                else:
                    print("It will take " + str(years) + " years and " + str(months) + " months to repay this loan!")
            else:
                if all_months == 1:
                    print("It will take " + str(all_months) + " month to repay this loan!")
                else:
                    print("It will take " + str(all_months) + " months to repay this loan!")
            overpayment = int(all_months * payment - principal)
            print("Overpayment = " + str(overpayment))
        elif principal is None:
            i = interest / (12 * 100)
            periods = int(periods)
            P = math.floor(payment / ((i * math.pow((1 + i), periods)) / (math.pow((1 + i), periods) - 1)))
            print("Your loan principal = " + str(P) + "!")
            overpayment = int(periods * payment - P)
            print("Overpayment = " + str(overpayment))
        elif payment is None:
            i = interest / (12 * 100)
            periods = int(periods)
            principal = float(principal)
            A = math.ceil(principal * ((i * math.pow((1 + i), periods)) / (math.pow((1 + i), periods) - 1)))
            print("Your monthly payment = " + str(A) + "!")
            overpayment = periods * A - principal
            overpayment = int(overpayment)
            print()
            print("Overpayment = " + str(overpayment))
if invalid_input:
    print("Incorrect parameters")
