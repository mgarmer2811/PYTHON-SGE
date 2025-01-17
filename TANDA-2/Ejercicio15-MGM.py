try:
    num1 = float(input('Bro dame un numero porfa\n'))
    num2 = float(input('Dame otro numero porfis\n'))
    operacion = input('Que operacion quieres hacer? (+,-,x,/)\n')

    if ((operacion != '+') and (operacion != '-') and (operacion != 'x') and (operacion != '/')):
        raise ValueError

    if num2 > num1:
        aux = num1
        num1 = num2
        num2 = aux

    resultado = 0

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == 'x':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2
    
    print('El resultado de la operacion es: ', resultado)

except ValueError:
    print('Alguno de los parametros es incorrecto')