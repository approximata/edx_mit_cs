#!/usr/bin/python3
monthly_intrest = annualInterestRate / 12
original_balance = balance
fixed_monthly_pay_min = balance/12
fixed_monthly_pay_max = (balance*((1+monthly_intrest)**12))/12


while round(balance, 2) != 0.00:
    balance = original_balance
    month = 0
    fixed_monthly_pay = round((fixed_monthly_pay_min + fixed_monthly_pay_max)/2, 4)
    while month < 12:
        unpaid_balance = balance - fixed_monthly_pay
        intrest = unpaid_balance * monthly_intrest
        balance = unpaid_balance + intrest
        month += 1
    if balance > 0:
        fixed_monthly_pay_min = fixed_monthly_pay
    else:
        fixed_monthly_pay_max = fixed_monthly_pay
print(round(fixed_monthly_pay, 2))
print('yolo')
