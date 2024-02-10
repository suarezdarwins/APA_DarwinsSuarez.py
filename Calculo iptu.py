'''plano diretor de desenvolvimento urbano
de uma cidade determina qual é o percentual de área máximo destinado para garagem em
relação à área total do terreno da casa, dependendo da localização deste terreno na cidade:
• Para a zona norte da cidade, o percentual máximo é de 25%;
• Para as zonas leste e oeste da cidade, o percentual máximo é de 30%;
• Para a zona sul, menos povoada, o percentual máximo é de 40%.
Quien este dentro del padrón será excento del IPTU'''

ancho_t=float(input('Indique el ancho en metros del terreno: '))
largo_t=float(input('Indique el largo en metros del terreno: '))
ancho_g=float(input('Indique el ancho en metros del garage: '))
largo_g=float(input('Indique el largo en metros del garage: '))

area_t = ancho_t * largo_t
area_g = ancho_g * largo_g

porcentaje = ((area_g)/(area_t))*100

zona=input('Indique su region: Norte=1, Este=2, Sur=3 : ')

print('Su inmueble esta localizano na Zona: ',zona)
print('Su porcentual de ocupacion es de: ', porcentaje,'%')

if zona=='1' and porcentaje<=25:
    print('Su inmueble esta dentro del plano y será insento ')
    
elif zona=='2' and porcentaje<=30:
    print('Su inmueble esta dentro del plano y será insento ')
    
elif zona=='3' and porcentaje<=40:
    print('Su inmueble esta dentro del plano y será insento ')
    
else:
    print('Su inmueble esta fuera del plano, deberá pagar el IPTU equivalente')


