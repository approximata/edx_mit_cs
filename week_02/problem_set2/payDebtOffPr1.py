#!/usr/bin/python3
def pay_debt_off_pr(balance, annualInterestRate, monthlyPaymentRate):
    monthly_intrest = annualInterestRate / 12
    month = 0

    while month < 12:
        minimum_pay_month = balance * monthlyPaymentRate
        unpaid_balance = balance - minimum_pay_month
        intrest = unpaid_balance * monthly_intrest
        balance = unpaid_balance + intrest
        # print(round(balance, 2))
        month += 1
    return round(balance, 2)

print(pay_debt_off_pr(484, 0.2, 0.04))
