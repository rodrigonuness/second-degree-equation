thin: str = 'c'
while(thin == 'c' or thin == 'C'):
    print('Ax² + Bx + C= 0\n')
    a = int(input('Type A: '))
    b = int(input('Type B: '))
    c = int(input('Type C: '))

    j: str = 'oi0'

    if (a != 0):
        if (c == 0):
            j = 'incomplete'
        elif (b == 0):
            j = 'incomplete'
        elif (b != 0 and c != 0):
            j = 'complete'
    else:
        j = 'do not exist'

    print(a, 'x² + ', b, 'x + ', c, '= 0\n')

    print('is ', j)

    al: float = (b ** 2) - (4 * a * c)

    print('Delta is:', al)
    if (al < 0):
        print('There is no real root\n')
    else:
        print('There is real root: \n')
    baske1 = -(b) + (al ** (1 / 2))
    baske2 = 2 * a
    print(baske1, '/', baske2, '=')
    print('x = ±',baske1 / baske2)
    thin = str(input('FOR CONTINUE PRESS C OR c, FOR OUT PRESS S ou s.........'))
