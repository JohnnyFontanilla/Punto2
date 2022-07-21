import mysql.connector as mysql
import json
import pandas as pd

#conexion a base de datos
sql_connet = mysql.connect(user='root', password='1234', host='localhost',port='3306',database='Prueba2',auth_plugin='mysql_native_password' )

#conexion a excel
df=pd.read_excel('Punto2.xlsx', sheet_name='Hoja 1')
df_dic=df.to_dict()

#conexion a MySql
mycursor = sql_connet.cursor()
query = 'insert into datos (Cedula,Nombres,Direccion,Latitud,Longitud,Ciudad,Descripcion) values (%s,%s,%s,%s,%s,%s,%s)'

for i in range(0,2):
    cedula = str(df_dic['Cédula'][i])
    nombres = df_dic['Nombres'][i]
    Direccion = df_dic["Dirección"][i]
    Datos_json = json.loads(df_dic["Data"][i])
    latitud = Datos_json['latitude']
    longitud = Datos_json['longitude']
    ciudad = Datos_json['city']
    descricion = Datos_json['description']

    value = (cedula, nombres, Direccion, latitud, longitud, ciudad, descricion)
    mycursor.execute(query, value)
    sql_connet.commit()