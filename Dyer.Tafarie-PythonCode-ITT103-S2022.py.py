#Author: Tafarie Dyer
#Date created: April 30, 2022
#Course: ITT103
#Purpose: The purpose of this Python Program is to provide JamEx Limited with the exact commission figure received by a sales person from each specified classes and undetermined sales person.

def saleCal():

    if Class == '1' and sales_amount <= 1000:
        commission_rate = .06
        commission = sales_amount * commission_rate
    elif Class == '1' and sales_amount > 1000:
        commission_rate = .07
        commission = sales_amount * commission_rate
    elif Class == '2' and sales_amount < 1000:
        commission_rate = .04
        commission = sales_amount * commission_rate
    elif Class == '2' and sales_amount > 1000:
        commission_rate = .06
        commission = sales_amount * commission_rate
    elif Class == '3':
        commission_rate = .045
        commission = sales_amount * commission_rate
        
    print('the commission is', commission)
    return


Welcome = input('Welcome to JamEx Ltd Commission Calculator, press enter on your keyboard to continue')
salesperson_num = input('Please enter salesperson_num')
sales_amount = input('Enter sales person sales_amount')
sales_amount = int(sales_amount)
Class = input ('Dont forget to enter the class you belong to, please enter this now')

while Class != '1' and Class != '2' and Class != '3':
    Class = input('salesperson class undetermined, please enter a valid Class!')
saleCal()

# saleCal = [Welcome,salesperson_num, sales_amount, Class]


Rerun = ('Yes')
prompt = input('Wish to calculate another salesperson commission?')

while prompt == Rerun:
    Welcome = input('Welcome to JamEx Ltd Commssion Calculator, press enter on your keyboard to continue')
    salesperson_num = input('Please enter salesperson_num')
    sales_amount = input('Enter sales person sales_amount')
    sales_amount = int(sales_amount)
    Class = input ('Dont forget to enter the class you belong to, please enter this now')

    while Class != '1' and Class != '2' and Class != '3':
     Class = input('salesperson class undetermined, please enter a valid Class!')
    saleCal()
    input('Wish to calculate another salesperson commission?')

if prompt != Rerun: 
    print('thank you and good bye')



# input('Would like to calculate another salesperson commission?')
#input (yes to loop, no to terminate the program)
#once an invalid message is recieved program is to output error and restart

