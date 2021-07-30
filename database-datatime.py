import requests
from io import StringIO
import csv
import sqlite3
from datetime import datetime

def get_time():
   ahora = datetime.now()
   hora = ahora.strftime("%H:%M:%S")
   return hora

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/oferta-gastronomica/oferta_gastronomica.csv'
bajada = requests.get(url).text
csv = csv.reader(StringIO(bajada))
next(csv)






conexion = sqlite3.connect('nuevabase.db')

cursor = conexion.cursor()




contador = 0
print("Hora de comienzo:", get_time())
for linea in csv:
   sql = "INSERT INTO bar(latitud, longitud, nombre, direccion, comuna) VALUES(?,?,?,?,?)"
   cursor.execute(sql, (linea[1], linea[0], linea[3], linea[13], linea[15][7:]))
   contador += 1
   print(contador, "Valor cargado")

print("Hora de finalización:", get_time())
conexion.commit()
conexion.close()


cursor.execute("SELECT * FROM bar")
  
# fetch all the matching rows 
result = cursor.fetchall()
  
# loop through the rows
for row in result:
    print(row)
    print("\n")
