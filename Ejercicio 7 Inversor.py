invercionInicial = float(input('Cual va a ser su invecion inicial?: '))
interesAnual = float(input('Cual va a ser el interes anual?: '))
tiempoDeInvecion = float(input('Indique que cantidad la cantidad de anios a invertir: '))

total = (invercionInicial*(interesAnual*tiempoDeInvecion/100))
print(f'Capital obtenido {total}')