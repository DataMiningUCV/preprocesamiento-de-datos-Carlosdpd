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

#with pd.option_context('display.max_rows', 999, 'display.max_columns', 3):

#Nos situamos en el directorio de los datos
os.chdir("/home/carlos/Escritorio/Mineria_datos")

#Leemos nuestro dataframe
data_frame_org = pd.read_csv("data.csv")

#Para no perder al dataframe original, creamos un segundo, que es el que modificaremos
#Renombramos todos los indices para una mas facil manipulacion

indices = ["Solicitud", "Periodo", "Cedula", "Fecha_nac", "Edad", "Estado_Civil", "Sexo", "Escuela", "Ano_Ingreso_UCV", "Modalidad_Ingreso", "Semestre_Actual", "Modificacion_Dir", "Motivo_Mod", "Num_Materias_Sem_Ant", "Num_Materias_Aprob_Sem_Ant", "Num_Materias_Ret_Sem_Ant", "Num_Materias_Rep_Sem_Ant", "Promedio_Pond", "Eficiencia", "Motivo_Rep", "Num_Mats_Actual", "Tesis_Trabajo_Actual", "Num_Ocasion_Trabajo_Tesis", "Procedencia", "Res_Actual", "Personas_Vive_Act", "Tipo_Vivienda", "Monto_Alq", "Dir_Res", "Contrajo_Matrimonio", "Benef_Adc", "Benef_Adc_Año_Motivo", "Trabaja", "Trabajo_Act_Frec", "Monto_Beca", "Aporte_Resp_Econ", "Aporte_Fam", "Ing_Horas", "Ing_Total", "Alimentacion", "Transporte_P", "Gastos_Medicos", "Gastos_Odont", "Gastos_Pers", "Alquiler_Renta", "Mats_Est", "Recreacion", "Otros_Gastos", "Total_Egresos", "Resp_Econ","R_E_Carga_Fam","Ingreso_Resp_Econ", "R_E_Otros_Ing", "R_E_Ing_total", "R_E_Vivienda","R_E_Alimentacion", "R_E_Transporte", "R_E_Gastos_Medicos", "R_E_Gastos_Odont", "R_E_Gastos_Educ", "R_E_Servicios_Basicos", "R_E_Condominio", "R_E_Otros_Gastos1", "R_E_Total_Egresos", "Opinion", "Sugerencias"]
data_frame = pd.read_csv('./data.csv', sep=',',skiprows = 1, names = indices)
#Pasaremos a limpiar un poco los datos 
#Eliminaremos algunas columnas redundantes
#La columna "Contrajo Matrimonio" se eliminara puesto que el dato de estado civil ya nos otorga esa informacion
del data_frame['Contrajo_Matrimonio']
#Esta columna se elimina por considerarse demasiado especifica y de poca importancia puesto que la zona ya es suficiente informacion la cual se encuentra en la columna de Procedencia
del data_frame['Dir_Res']
#Estas dos columnas a continuacion se eliminan por dos motivos principales: El primero es que tienen informacion demasiado complicada de estandarizar y la segunda es que posse muy pocas instancias como para encontrar informacion relevante a medida que se desarrolle el proceso
del data_frame['Benef_Adc_Año_Motivo']
del data_frame['Trabajo_Act_Frec']


#QUE HACER CON COLUMNAS RARAS POR AHI
#-----------------------------------
#------------------------------------
#------------------------------------


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
data_frame.Estado_Civil = data_frame.Estado_Civil.replace({'Soltero (a)': '0'})
data_frame.Estado_Civil = data_frame.Estado_Civil.replace({'Casado (a)': '1'})
data_frame.Estado_Civil = data_frame.Estado_Civil.replace({'Viudo (a)': '2'})
data_frame.Estado_Civil = data_frame.Estado_Civil.replace({'Unido (a)': '3'})
data_frame.Estado_Civil = data_frame.Estado_Civil.astype(int)


#Estandarizando sexo
#POSIBLE DISCRIMINACION A COMUNIDADES LGBT
data_frame.Sexo = data_frame.Sexo.replace({'Femenino' : '0'})
data_frame.Sexo = data_frame.Sexo.replace({'Masculino' : '1'})
data_frame.Sexo = data_frame.Sexo.astype(int)


#Estandarizando escuelas
data_frame.Escuela = data_frame.Escuela.replace({'Enfermería' : '0'})
data_frame.Escuela = data_frame.Escuela.replace({'Bioanálisis' : '1'})
data_frame.Escuela = data_frame.Escuela.astype(int)

#Columna de ingreso. Nada que hacer

#Manipulando Modalidad_Ingreso
#?????????????????????????????

#Columna semestre
#?????????????????????????????

#Modificacion de direccion
data_frame.Modificacion_Dir = data_frame.Modificacion_Dir.replace({'No':'0'})
data_frame.Modificacion_Dir = data_frame.Modificacion_Dir.replace({'Si':'1'})
data_frame.Modificacion_Dir = data_frame.Modificacion_Dir.astype(int)

#Motivo_Mod
#NO SE QUE HACER AQUI AUN

#Numero de materias inscritas
#Ya son enteros

#Num materias aprobadas
#Ya son enteros

#Num materias retiradas
#hay un mas de 10 por ahi. revisar

#num materias reprobadas
#ya son enteros

#Promedio_Pond hay 0.6 por ahi. revisar
i=0
for x in data_frame.Promedio_Pond:
    if x > 20:
        data_frame.Promedio_Pond[i] = x/1000
    i=i+1
        
#Eficiencia
i=0
for x in data_frame.Eficiencia:
    if x > 1 and x < 999:
        data_frame.Eficiencia[i] = x*10
        
    if x > 1001 and x < 9999:
        data_frame.Eficiencia[i] = x/10000        
        
    if x > 10000 and x < 20000:
        data_frame.Eficiencia[i] = x/100000

    if x == 1000:
        data_frame.Eficiencia[i] = x/1000
    
    if x == 10000:
        data_frame.Eficiencia[i] = x/10000


    i=i+1
    

data_frame.Eficiencia[134] = data_frame.Eficiencia[134]/1000
data_frame.Eficiencia[162] = data_frame.Eficiencia[162]/1000

#Logrado. Pero esta pasando algo RARISIMO. REVISAR

#Motivo_ rep
#No se que hacer con esto

#Numero de materias actualmente

#-------Hacer cosas

#Tesis_Trabajo_Actual
data_frame.Tesis_Trabajo_Actual = data_frame.Tesis_Trabajo_Actual.replace({'No':'0'})
data_frame.Tesis_Trabajo_Actual = data_frame.Tesis_Trabajo_Actual.replace({'Si':'1'})
data_frame.Tesis_Trabajo_Actual = data_frame.Tesis_Trabajo_Actual.astype(int)

#Num_Ocasion_Trabajo_Tesis S ASUME QUE PRIMERA VEZ Y ESPACIO VACIO SON PRIMERA VEZ QUE SE PRESENTA LA TESIS/TRABAJO
data_frame.Num_Ocasion_Trabajo_Tesis.fillna(0, inplace=True)
data_frame.Num_Ocasion_Trabajo_Tesis = data_frame.Num_Ocasion_Trabajo_Tesis.replace({'Primera vez':'0'}, regex=True)
data_frame.Num_Ocasion_Trabajo_Tesis = data_frame.Num_Ocasion_Trabajo_Tesis.replace({'Segunda vez': '1'}, regex=True)
data_frame.Num_Ocasion_Trabajo_Tesis = data_frame.Num_Ocasion_Trabajo_Tesis.replace({'Más de dos': '2'}, regex=True)
data_frame.Num_Ocasion_Trabajo_Tesis = data_frame.Num_Ocasion_Trabajo_Tesis.astype(int)

#Procedencia, 0 Libertador Caracas,1 Sucre, 2 Chacao, 3 Baruta, 4 Hatillo 5 Estado Miranda, 6 afueras
data_frame.Procedencia = data_frame.Procedencia.replace({'Municipio Libertador Caracas':'0'})
data_frame.Procedencia = data_frame.Procedencia.replace({'Municipio Sucre':'1'})
data_frame.Procedencia = data_frame.Procedencia.replace({'Municipio Chacao':'2'})
data_frame.Procedencia = data_frame.Procedencia.replace({'Municipio Baruta':'3'})
data_frame.Procedencia = data_frame.Procedencia.replace({'Municipio El Hatillo':'4'})
data_frame.Procedencia = data_frame.Procedencia.replace({'Valles del Tuy':'5'})
data_frame.Procedencia = data_frame.Procedencia.replace({'Altos Mirandinos':'5'})
data_frame.Procedencia = data_frame.Procedencia.replace({'Guarenas - Guatire':'5'})
data_frame.Procedencia = data_frame.Procedencia.replace({'Barlovento':'5'})


i=0
for x in data_frame.Procedencia:
    if x != '0' and x != '1' and x != '2' and x != '3' and x != '4' and x != '5' :
        data_frame.Procedencia[i] = 6
        
    i=i+1

data_frame.Procedencia = data_frame.Procedencia.astype(int)
#Res_Actual en este caso 6 = No responde. HACER ALGO LUEGO ---------------------------
data_frame.Res_Actual = data_frame.Res_Actual.replace({'Municipio Libertador Caracas':'0'})
data_frame.Res_Actual = data_frame.Res_Actual.replace({'Municipio Sucre':'1'})
data_frame.Res_Actual = data_frame.Res_Actual.replace({'Municipio Chacao':'2'})
data_frame.Res_Actual = data_frame.Res_Actual.replace({'Municipio Baruta':'3'})
data_frame.Res_Actual = data_frame.Res_Actual.replace({'Municipio El Hatillo':'4'})
data_frame.Res_Actual = data_frame.Res_Actual.replace({'Valles del Tuy':'5'})
data_frame.Res_Actual = data_frame.Res_Actual.replace({'Altos Mirandinos':'5'})
data_frame.Res_Actual = data_frame.Res_Actual.replace({'Guarenas - Guatire':'5'})
data_frame.Res_Actual = data_frame.Res_Actual.replace({'Barlovento':'5'})


i=0
for x in data_frame.Res_Actual:
    if x != '0' and x != '1' and x != '2' and x != '3' and x != '4' and x != '5' :
        data_frame.Res_Actual[i] = 6
        
    i=i+1

data_frame.Res_Actual = data_frame.Res_Actual.astype(int)
#Personas_Vive_Act 0 es familiares directos, 1 es conyuge, 2 solo/a, 3 amigos/residencia est, 4 dueño apart
i=0
for x in data_frame.Personas_Vive_Act:
    data_frame.Personas_Vive_Act[i] = x.lower()
    i=i+1

i=0
for x in data_frame.Personas_Vive_Act:
    if 'madre' in x:
        data_frame.Personas_Vive_Act[i] = 0
        
    if 'padre' in x:
        data_frame.Personas_Vive_Act[i] = 0
        
    if 'abuel' in x:
        data_frame.Personas_Vive_Act[i] = 0
    
    if 'ma' in x:
        data_frame.Personas_Vive_Act[i] = 0
        
    if 'pat' in x:
        data_frame.Personas_Vive_Act[i] = 0
    
    if 'her' in x:
        data_frame.Personas_Vive_Act[i] = 0
        
    if 'pri' in x:
        data_frame.Personas_Vive_Act[i] = 0
    
    if 'esp' in x:
        data_frame.Personas_Vive_Act[i] = 1
        
    if 'sol' in x:
        data_frame.Personas_Vive_Act[i] = 2
    
    if 'ami' in x:
        data_frame.Personas_Vive_Act[i] = 3
        
    if 'cia' in x:
        data_frame.Personas_Vive_Act[i] = 3
        
    if 'comp' in x:
        data_frame.Personas_Vive_Act[i] = 3
        
    if 'inq' in x:
        data_frame.Personas_Vive_Act[i] = 3
        
    if 'apart' in x:
        data_frame.Personas_Vive_Act[i] = 4
    i=i+1

data_frame.Personas_Vive_Act = data_frame.Personas_Vive_Act.astype(int)

#Tipo_Vivienda
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Quinta o casa quinta':'0'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Apartamento en edifico':'1'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Casa en barrio urbano':'2'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Habitación alquilada':'3'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Casa en barrio rural':'4'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Apartamento en quinta - casa quinta o casa':'0'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Residencia estudiantil':'3'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Casa de vecindad':'2'})
#Esto no se debe hacer, revisar luego
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'casa':'2'})

i=0
for x in data_frame.Tipo_Vivienda:
    if x != '0' and x != '1' and x != '2' and x != '3' and x != '4' :
        data_frame.Tipo_Vivienda[i] = 5
        
    i=i+1

data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.astype(int)

#Monto_Alq
data_frame.Monto_Alq = data_frame.Monto_Alq.fillna(0)
data_frame.Monto_Alq = data_frame.Monto_Alq.replace({' bs': ''}, regex=True)
#No se debe hacer REVISAR LUEGO ---------------------------------------------
data_frame.Monto_Alq[115]=150
data_frame.Monto_Alq = data_frame.Monto_Alq.astype(int)

#Benef_Adc
data_frame.Benef_Adc = data_frame.Benef_Adc.replace({'No':'0'})
data_frame.Benef_Adc = data_frame.Benef_Adc.replace({'Si':'1'})
data_frame.Benef_Adc = data_frame.Benef_Adc.astype(int)

#Trabaja 
data_frame.Trabaja = data_frame.Trabaja.replace({'No':'0'})
data_frame.Trabaja = data_frame.Trabaja.replace({'Si':'1'})
data_frame.Trabaja = data_frame.Trabaja.astype(int)

#Monto_Beca revisar para busscar outlyers
data_frame.Monto_Beca
#-------------- CONTINUARA PRONTO!!!!!!


    

