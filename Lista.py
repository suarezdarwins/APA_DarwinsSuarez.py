numero= int(input('digite el numero a factorial '))

fatorial = 1
for termo in range (1,(numero + 1)):
    fatorial *= termo

print ('El factorial de '+ str(numero)+'! es: '+ str (fatorial))
