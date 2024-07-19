while True:
    num1 = int(input('Enter 1-number: '))
    operator = input('Enter operator: ')
    num2 = int(input('Enter 2-number: '))

    if operator == '+':
        print(f'{num1} + {num2} = {num1+num2}')
    elif operator == '-':
        print(f'{num1} - {num2} = {num1-num2}')
    elif operator == '/':
        print(f'{num1} / {num2} = {num1/num2}')
    elif operator == '*':
        print(f'{num1} * {num2} = {num1*num2}')
    elif operator == 'false':
        break
    else:
        print('Error!')