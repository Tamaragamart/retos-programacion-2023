
def calcular_puntos(palabra):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    combis = {}
    value = 1
    for letra in letras:
        combis[letra]= value
        value += 1

    

    puntos = 0
    for letra in palabra:
        letra = letra.upper()
        if letra in combis:
            puntos += combis[letra]

    return puntos

puntos = 0
while puntos <100:
    
    palabra = input('Dime una palabra').upper()
    puntospalabra = calcular_puntos(set(palabra))
    puntos += puntospalabra
    print(f'La palabra {palabra} tiene {puntospalabra} puntos. Tienes {puntos} puntos.')

    if puntos >= 100:
        print(f'¡Enhorabuena! Has conseguido {puntos} puntos.')

        break



