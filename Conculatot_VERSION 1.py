print('---Канкулятор---')
while True:
    num1 = float(input('Ведите первое число\n'))
    try:
        error = int(num1)
    except ValueError:
        print('Пожалуйста введите цифру!')
    operatiom = input('Выберите знак + или -\n')
    num2 = float(input('Ведите второе число\n'))
    if operatiom == '+':
        print(num1 + num2)
    elif operatiom == '-':
        print(num1 - num2)
