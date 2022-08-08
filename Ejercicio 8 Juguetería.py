clown = 112
wrist = 75

clownsSold = int(input('how many clown did you sell: '))
dollSold = int(input('how many dolls did you sell: '))

overallWeight = clownsSold * clown + dollSold * wrist

print(f'El peso total del paquete es {overallWeight}')