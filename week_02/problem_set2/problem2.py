#!/usr/bin/python3
def pay_debt_off_pr(balance, annualInterestRate):
    monthly_intrest = annualInterestRate / 12
    fixed_monthly_pay = 0
    original_balance = balance

    while balance > 0:
        month = 0
        fixed_monthly_pay += 10
        balance = original_balance
        print(fixed_monthly_pay, 'fixed')
        while month < 12:
            unpaid_balance = balance - fixed_monthly_pay
            intrest = unpaid_balance * monthly_intrest
            balance = unpaid_balance + intrest
            print(round(balance, 2))
            month += 1
            round(balance, 2)
    return fixed_monthly_pay

print(pay_debt_off_pr(4773, 0.2))
