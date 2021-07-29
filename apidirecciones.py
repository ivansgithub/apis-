import requests
import pprint
import json
#contenido=requests.get(url)

direccion=input("ingrese la direccion:")

localidad='caba'


direccion_formato= requests.utils.quote(direccion + ', ' +  localidad)


url='http://servicios.usig.buenosaires.gob.ar\
/normalizar/?geocodificar=True&direccion='+direccion_formato

dir_normalizada=json.loads(requests.get(url).text)

#pprint.pprint(dir_normalizada)

print("direccion:",dir_normalizada['direccionesNormalizadas'][0]['direccion'])
print("nombre:",dir_normalizada['direccionesNormalizadas'][0]['nombre_calle'])
print("altura:", dir_normalizada['direccionesNormalizadas'][0]['altura'])
print("localidada:",dir_normalizada['direccionesNormalizadas'][0]['nombre_localidad'])
print("coorx:",dir_normalizada['direccionesNormalizadas'][0]['coordenadas']['x'])
print("coory:",dir_normalizada['direccionesNormalizadas'][0]['coordenadas']['y'])








