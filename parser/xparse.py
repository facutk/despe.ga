from BeautifulSoup import BeautifulSoup
import json

html=open("vuelos.html","rb").read()

info = []
soup = BeautifulSoup(html)
vuelos = soup.findAll('div', {'class': 'destination-info'})

nombre_ciudad = None
for vuelo in vuelos:
    info_city = vuelo.findAll('div', {'class': 'info-city'})
    for data in info_city:
        nombres_city = data.findAll('span')
        for nombre_city in nombres_city:
            if(nombre_city.contents):
                nombre_ciudad = nombre_city.contents[0]
    
    
    info_price = vuelo.find('span', {'class': 'price'}).contents[0]
    info.append( {'city': nombre_ciudad, 'price':info_price} )
    #print "%s $%s"%( nombre_ciudad, info_price )
    #print info_price
    #print nombre_ciudad
    #print vuelo
    #break

salida_json = json.dumps( info )
print salida_json
