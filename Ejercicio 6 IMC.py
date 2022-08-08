peso = int(input('Indique cual es su peso en kg, ejemplo: 60kg : '))
altura = float(input('Indique cual es su altura en metros, ejemplo:1.70m : '))

imc = round( peso / altura ** 2 , 2 )

print(f'Su imc es de {imc} ')