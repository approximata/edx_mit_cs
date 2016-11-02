
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

    us_num = int(us_num)
    ten_digit = us_num // 10
    digit = us_num % 10

    if ten_digit == 0:
        return trans.get(str(us_num))
    elif us_num == 10:
        return 'shi'
    elif us_num > 10 and us_num < 20:
        return str('shi ' + trans.get(str(digit)))
    elif us_num >= 20 and digit == 0:
        return str(trans.get(str(ten_digit)) + ' shi')
    else:
        return str(trans.get(str(ten_digit)) + ' shi ' + trans.get(str(digit)))


print(convert_to_mandarin('36'))
