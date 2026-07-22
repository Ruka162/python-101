keep_going = 'y'
while keep_going.upper() == 'Y':
    wholesale_cost = float(input('Enter the wholesale cost: '))
    retail_price = wholesale_cost * 2.5
    print(f'The commission is: ${retail_price:.2f}')
    keep_going = input('Do you want to calculate another' + \
                       ' commission? (Enter y for yes n for no): ')