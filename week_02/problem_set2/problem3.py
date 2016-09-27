#!/usr/bin/python3
def pay_debt_off_pr3(balance, annualInterestRate):
    monthly_intrest = annualInterestRate / 12

    original_balance = balance
    fixed_monthly_pay_min = balance/12
    fixed_monthly_pay_max = (balance*((1+monthly_intrest)**12))/12
    print(fixed_monthly_pay_min)
    print(fixed_monthly_pay_max)

    count = 0

    while round(balance, 2) != 0.00:
        count += 1
        print(count, 'count')
        balance = original_balance
        month = 0
        fixed_monthly_pay = round((fixed_monthly_pay_min + fixed_monthly_pay_max)/2, 4)
        print(fixed_monthly_pay, 'fixed')
        while month < 12:
            unpaid_balance = balance - fixed_monthly_pay
            intrest = unpaid_balance * monthly_intrest
            balance = unpaid_balance + intrest
            print(round(balance, 2))
            month += 1
        if balance > 0:
            fixed_monthly_pay_min = fixed_monthly_pay
        else:
            fixed_monthly_pay_max = fixed_monthly_pay
    return round(fixed_monthly_pay, 2)

print(pay_debt_off_pr3(320000, 0.2))
