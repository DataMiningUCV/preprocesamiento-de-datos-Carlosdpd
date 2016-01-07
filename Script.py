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
#Renombramos todos los indices para una mas facil manipulacion

indices = ["Solicitud", "Periodo", "Cedula", "Fecha_nac", "Edad", "Estado_Civil", "Sexo", "Escuela", "Ano_Ingreso_UCV", "Modalidad_Ingreso", "Semestre_Actual", "Modificacion_dir", "Motivo_mod", "Num_Materias_Sem_Ant", "Num_Materias_Aprob_Sem_Ant", "Num_Materias_Ret_Sem_Ant", "Num_Materias_Rep_Sem_Ant", "Promedio_Pond", "Eficiencia", "Motivo_Rep", "Num_Mats_Actual", "Tesis_Trabajo_Actual", "Num_Ocasion_Trabajo_Tesis", "Procedencia", "Res_Actual", "Personas_Vive_Act", "Tipo_Vivienda", "Monto_Alq", "Dir_Res", "Contrajo_Matrimonio", "Benef_Adc", "Benef_Adc_Año_Motivo", "Trabaja", "Trabajo_Act_Frec", "Monto_Beca", "Aporte_Resp_Econ", "Aporte_Fam", "Ing_Horas", "Ing_Total", "Alimentacion", "Transporte_P", "Gastos_Medicos", "Gastos_Odont", "Gastos_Pers", "Alquiler_Renta", "Mats_Est", "Recreacion", "Otros_Gastos", "Total_Egresos", "Resp_Econ","Carga_Fam","Ingreso_Resp_Econ", "Otros_Ing", "Ing_total", "Vivienda","Alimentacion1", "Transporte1", "Gastos_Medicos1", "Gastos_Odont1", "Gastos_Educ", "Servicios_Basicos", "Condominio", "Otros_Gastos1", "Total_Egresos1", "Opinion", "Sugerencias"]
data_frame = pd.read_csv('./data.csv', sep=',',skiprows = 1, names = indices)
#Pasaremos a limpiar un poco los datos 


#Solicitudes a enteros
data_frame.Solicitud = data_frame.Solicitud.astype(int)

#Estandarizamos periodos academicos

#En la columna cedula pasamos todos los datos a enteros
data_frame.Cedula = data_frame.Cedula.astype(int)

#Corrigiendo fechas de nacimiento


#Limpiando la columna de la edad, removiendo el string años,AÑOS para utilizar solo valores numericos
data_frame.Edad =  data_frame.Edad.replace({'años': ''}, regex=True)
data_frame.Edad =  data_frame.Edad.replace({'AÑOS': ''}, regex=True)
data_frame.Edad =  data_frame.Edad.replace({' ': ''}, regex=True)
#Los convertimos a enteros
data_frame.Edad = data_frame.Edad.astype(int)

#Estandarizando estados civiles

#Estandarizando sexo

#Estandarizando escuelas

#-------------- CONTINUARA PRONTO!!!!!! GOD BLESS AMERICA
