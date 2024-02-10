'''Vamos al FSY
Si Cumples 14 año en el 2024 Acompañanops al FSY
Jovenes menoires de 14 años e mayores de 18 años no seran aceptados en este FSY
'''
nombre=input('Hola, como te llamas? ')
nacimiento=float(input('Cual es tu año de nacimiento: '))

edad=2024-nacimiento

if edad < 14:
    print('Estimado ',nombre,'actualmente tienes ',edad, 'años, lamentablemente no tienes la edad para participar en el FSY 2024 ')

elif 14 <= edad < 18:
    print('Estimado ',nombre,'actualmente tienes ',edad, 'años, Felicitacioes!!! tienes la edad para participar en el FSY 2024 ')

if edad >= 18:
    print('Estimado ',nombre,'actualmente tienes ',edad, 'años, lamentablemente superas la edad para participar en el FSY 2024, pide a tu lider para participar como Asesor')
