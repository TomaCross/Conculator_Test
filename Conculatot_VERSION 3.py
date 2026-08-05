print('---Канкулятор---')
while True:
    try:
        num1 = float(input('Ведите первое число\n'))
    except ValueError:
        print('Пожалуйста введите цифру!')
        continue
    operatiom = int('Выберите знак + или -\n')
        if operatiom == '+' or operatiom == '-':
            continue
        else:
            break
    try:
        num2 = float(input('Ведите второе число\n'))
    except ValueError:
        print('Пожалуйста введите цифру!')
        continue
    if operatiom == '+':
        print(num1 + num2)
    elif operatiom == '-':
        print(num1 - num2)
