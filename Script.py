# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este archivo temporal se encuentra aquí:
/home/carlos/.spyder2/.temp.py
"""
#Paquetes e importanciones
import pandas as pd
import numpy as np
import os
import csv

#Nos situamos en el directorio de los datos
os.chdir("/home/carlos/Escritorio/Mineria_datos")

#Leemos nuestro dataframe
data_frame_org = pd.read_csv("data.csv")

#Para no perder al dataframe original, creamos un segundo, que es el que modificaremos
data_frame = data_frame_org.copy(deep=True)

#Renombramos algunos indices para mayor comprension

data_frame.rename(columns = {data_frame.columns[0]:'Numero.Solicitud'}, inplace=True)
data_frame.rename(columns = {data_frame.columns[1]:'Periodo.Renovacion'}, inplace=True)
#Se cambia un indice un tanto confuso
data_frame.rename(columns = {data_frame.columns[22]:'Numero.Ocasiones.Que.Cursa.Tesis.Trabajo.Grado'}, inplace=True)
#Se cambia un error en el indice
data_frame.rename(columns = {data_frame.columns[21]:'Estás.realizado.tesis...trabajo.de.grado.o.pasantías.de.grado.'}, inplace=True)
