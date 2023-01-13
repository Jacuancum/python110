print ('Please answer the question below from 1 to 10 Rate')

ok_loan = False 

loan_size = int(input ('How large is the loan? '))
credit_history = int(input ('How good is your credit history? '))
income = int(input ('How high is your income? '))
down_payment = int(input ('How large is your down payment? '))

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        ok_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            ok_loan = True
        else:
            ok_loan = False
    else:
        ok_loan = False        

else:
    if credit_history < 4:
        ok_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            ok_loan = True
        elif income >= 4 and down_payment >= 4:
            ok_loan = True
        else:
            ok_loan = False


if ok_loan:
    print('Yes, you can have this loan.')
else:
    print('No, you can not loan this money.')