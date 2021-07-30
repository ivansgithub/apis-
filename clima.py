import requests
import json 

key="your_key"
with open ('sucursales_sol_360.csv') as sucursales:
    for f in sucursales:
        a=f.split(';')
        
        
        ciudad=a[1]
        provincia=a[0]
        
       
        ciudad_cod=requests.utils.quote(ciudad)
        provincia_cod=requests.utils.quote(provincia)
        try:
    
            url ='http://api.openweathermap.org/data/2.5/weather?q='+ ciudad_cod + ',Argentina&lang=es&appid='+key
            objeto=json.loads(requests.get(url).text)
         
        
            a =objeto.get('weather')[0].get('description')
            print(ciudad.replace('\n','') +', '+ a)

        except:
            print(ciudad.replace('\n','') +', '+ 'n/a')
