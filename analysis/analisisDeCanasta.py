#1 Importar paquete o paquetes con los que voy a analizar la información

import pandas as pd

def analizarCanastaBasica():
    #archivo def para llamarlo e importarlo en el main
 
    #2. Sin importar la fuente (sql, xls, JSON, csv...)
 #crear tabla tabulada que se llama DATAFRAME
 Tabla=pd.read_csv('./data/bdcanasta.csv')
 
 #print(Tabla)

 #3. Aplico filtros para limpiar o seleccionar datos

 #print(Tabla.head(20)) #primeros N registros
 #print(Tabla.tail())
 print(Tabla.describe())

