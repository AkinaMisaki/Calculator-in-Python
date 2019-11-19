x = 0
y = 0
math = input('1-Soma, 2-subtração, 3-multiplicação, 4-divisão, 5-potenciação, 6-radiciação, 7-IMC ')
if math == '1':
    x = input('Coloque o primeiro numero da soma:')
    y = input('Coloque o segundo numero da soma:')
    print('Resultado:',float(x) + float(y))
if math == '2':
    x = input('Coloque o primeiro numero da subtração:')
    y = input('Coloque o segundo numero da subtração:')
    print('Resultado:',float(x) - float(y))
if math == '3':
    x = input('Coloque o primeiro numero da multiplição:')
    y = input('Coloque o segundo numero da multiplicação:')
    print('Resultado:',float(x) * float(y))
if math == '4':
    x = input('Coloque o primeiro numero da divisão:')
    y = input('Coloque o segundo numero da divisão:')
    print('Resultado:',float(x) / float(y)) 
if math == '5':
    x = input('Coloque o primeiro numero da potenciação:')
    y = input('Coloque o segundo numero da potenciação:')
    print('Resultado:',float(x) ** float(y))
if math == '6':
    x = input('Coloque o primeiro numero da radiciação:')
    y = input('Coloque o segundo numero da radiciação:')
    print('Resultado:',float(x) // float(y))
if math == '7':
    x = input('Coloque sua altura(m):' )
    y = input('Coloque seu peso(Kg):' )
    alt2 = float(x) ** 2
    print('Resultado:', float(y) / float(alt2))
    print('Menos do que 18,5-Abaixo do peso')     
    print('Entre 18,5 e 24,9-Peso normal')
    print('Entre 25 e 29,9-Sobrepeso')
    print('Mais do que 40-Obesidade grau 3')
    print('Entre 35 e 39,9-Obesidade grau 2')
    print('Entre 30 e 34,9-Obesidade grau 1')
input()
exit
