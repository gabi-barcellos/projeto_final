"""
Autoras:  Gabriela Barcellos e Rebeca Marconi
Date: 04/03/2021
Version: 3
Last update: 04/03/2021
"""
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
from sys import argv

programaPrincipal = sys.argv[0]
arquivo = sys.argv[1]


with pd.ExcelFile(arquivo) as xlsx:
    df = pd.read_excel(xlsx)



#df1 = df[['Target_Name','CT']]
#print(df1)

coefb = 58.53223295
coefm = (-3.397186047)
QT = 10**((df['CT'] - coefb) / coefm)
df['Quantity']=QT

colunas_data = {'Sample_Name':df['Sample_Name'], 'Target_Name':df['Target_Name'], 'Stage':df['Stage'], 'CT':df['CT'], 'Quantity':df['Quantity']}
df_q = pd.DataFrame(colunas_data, columns=['Sample_Name', 'Target_Name', 'Stage', 'CT', 'Quantity'])
print(df_q)

df_q.to_excel("df_q.xlsx")


valor_maximo = df['Quantity'].max()
print("Esse foi o maior Quantity: {}".format(valor_maximo))

maximo = df['Quantity'].max()

print(df[df['Quantity'] == maximo])