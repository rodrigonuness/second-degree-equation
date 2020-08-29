repeat: str = 'c'
while(repeat == 'c' or repeat == 'C'):
    print('Ax² + Bx + C= 0\n')
    a = int(input('Type A: '))
    b = int(input('Type B: '))
    c = int(input('Type C: '))

    info: str = 'none'

    if (a != 0):
        if (c == 0):
            info = 'incomplete'
        elif (b == 0):
            info = 'incomplete'
        elif (b != 0 and c != 0):
            info = 'complete'
    else:
        info = 'do not exist'

    print(a, 'x² + ', b, 'x + ', c, '= 0\n')

    print('is ', info)

    baske: float = (b ** 2) - (4 * a * c)

    print('Delta is:', baske)
    if (baske < 0):
        print('There is no real root\n')
    else:
        print('There is real root: \n')
    baske1 = -(b) + (baske ** (1 / 2))
    baske2 = 2 * a
    print(baske1, '/', baske2, '=')
    print('x = ±',baske1 / baske2)
    repeat = str(input('FOR CONTINUE PRESS C OR c, FOR OUT PRESS S ou s.........'))
