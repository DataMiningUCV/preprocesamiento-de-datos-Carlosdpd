# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este archivo temporal se encuentra aquí:
/home/carlos/.spyder2/.temp.py
"""
#Paquetes e importanciones
import pandas as pd
import matplotlib.pyplot as plt
import os

#Nos situamos en el directorio de los datos
os.chdir("/home/carlos/Escritorio/Mineria_datos")

#Leemos nuestro dataframe
data_frame_org = pd.read_csv("data.csv")

#Para no perder al dataframe original, creamos un segundo, que es el que modificaremos
#Renombramos todos los indices para una mas facil manipulacion

indices = ["Solicitud", "Periodo", "Cedula", "Fecha_Nac", "Edad", "Estado_Civil", "Sexo", "Escuela", "Ano_Ingreso_UCV", "Modalidad_Ingreso", "Semestre_Actual", "Modificacion_Dir", "Motivo_Mod", "Num_Materias_Sem_Ant", "Num_Materias_Aprob_Sem_Ant", "Num_Materias_Ret_Sem_Ant", "Num_Materias_Rep_Sem_Ant", "Promedio_Pond", "Eficiencia", "Motivo_Rep", "Num_Mats_Actual", "Tesis_Trabajo_Actual", "Num_Ocasion_Trabajo_Tesis", "Procedencia", "Res_Actual", "Personas_Vive_Act", "Tipo_Vivienda", "Monto_Alq", "Dir_Res", "Contrajo_Matrimonio", "Benef_Adc", "Benef_Adc_Año_Motivo", "Trabaja", "Trabajo_Act_Frec", "Monto_Beca", "Aporte_Resp_Econ", "Aporte_Fam", "Ing_Horas", "Ing_Total", "Alimentacion", "Transporte_P", "Gastos_Medicos", "Gastos_Odont", "Gastos_Pers", "Alquiler_Renta", "Mats_Est", "Recreacion", "Otros_Gastos", "Total_Egresos", "Resp_Econ","R_E_Carga_Fam","Ingreso_Resp_Econ", "R_E_Otros_Ing", "R_E_Ing_total", "R_E_Vivienda","R_E_Alimentacion", "R_E_Transporte", "R_E_Gastos_Medicos", "R_E_Gastos_Odont", "R_E_Gastos_Educ", "R_E_Servicios_Basicos", "R_E_Condominio", "R_E_Otros_Gastos1", "R_E_Total_Egresos", "Opinion", "Sugerencias"]
data_frame = pd.read_csv('./data.csv', sep=',',skiprows = 1, names = indices)
#Pasaremos a limpiar un poco los datos 
#Eliminaremos algunas columnas redundantes
#Se elimina la columna edad puesto que ya se tiene la fecha de nacimiento
del data_frame['Edad']
#La columna "Contrajo Matrimonio" se eliminara puesto que el dato de estado civil ya nos otorga esa informacion
del data_frame['Contrajo_Matrimonio']
#Esta columna se elimina por considerarse demasiado especifica y de poca importancia puesto que la zona ya es suficiente informacion la cual se encuentra en la columna de Procedencia
del data_frame['Dir_Res']
#Estas dos columnas a continuacion se eliminan por dos motivos principales: El primero es que tienen informacion demasiado complicada de estandarizar y la segunda es que posse muy pocas instancias como para encontrar informacion relevante a medida que se desarrolle el proceso
del data_frame['Motivo_Rep']
del data_frame['Benef_Adc_Año_Motivo']
del data_frame['Trabajo_Act_Frec']
del data_frame['Motivo_Mod']
#Se eliminan las siguientes columnas puesto que esa informacion puede ser calculada usando otras columnas
del data_frame['Ing_Total']
del data_frame['Total_Egresos']
del data_frame['R_E_Ing_total']
del data_frame['R_E_Total_Egresos']
#Las siguientes columnas se eliminan por su elevada complejidad para poder convertir a dato numero y su poca relevancia en el proceso de mineria
del data_frame['Opinion']
del data_frame['Sugerencias']


#Solicitudes a enteros
data_frame.Solicitud = data_frame.Solicitud.astype(int)

#Estandarizamos periodos academicos
i=0
for x in data_frame.Periodo:
    data_frame.Periodo[i] = x.lower()
    i=i+1

i=0
for x in data_frame.Periodo:
    if 'i' and '15' in x:
        data_frame.Periodo[i] = 'I-2015'
        
    if 'ii' and '14'in x:
        data_frame.Periodo[i] = 'II-2014'
    #Usamos este valor por ser la moda y reemplazamos el periodo que no esta especificado(Sacamos la moda usando .mode)
    if 'semes' in x:
        data_frame.Periodo[i] = 'II-2014'
    
    i=i+1



#Estos ultimos valores se arreglan "a mano" por su irregularidad
data_frame.Periodo[149] = 'II-2014'
data_frame.Periodo[143] = 'II-2014'
data_frame.Periodo[1] = 'II-2014'
data_frame.Periodo[63] = 'II-2014'

#En la columna cedula pasamos todos los datos a enteros
data_frame.Cedula = data_frame.Cedula.astype(int)

#Corrigiendo fechas de nacimiento
i=0

for x in data_frame.Fecha_Nac:
    if len(x) == 8:
        data_frame.Fecha_Nac[i] = data_frame.Fecha_Nac[i][:6]+ '19' + data_frame.Fecha_Nac[i][6:]    
        
    
    i=i+1
    
data_frame.Fecha_Nac = data_frame.Fecha_Nac.replace({'-': '/'}, regex=True)
data_frame.Fecha_Nac = data_frame.Fecha_Nac.replace({' ': '/'}, regex=True)

data_frame.Fecha_Nac[12] = '10/05/1989'
data_frame.Fecha_Nac[42] = '18/05/1992'



#Estandarizando estados civiles
data_frame.Estado_Civil = data_frame.Estado_Civil.replace({'Soltero (a)': '0'})
data_frame.Estado_Civil = data_frame.Estado_Civil.replace({'Casado (a)': '1'})
data_frame.Estado_Civil = data_frame.Estado_Civil.replace({'Viudo (a)': '2'})
data_frame.Estado_Civil = data_frame.Estado_Civil.replace({'Unido (a)': '3'})
data_frame.Estado_Civil = data_frame.Estado_Civil.astype(int)

#Se puede observar algunos outliers que representas personas que no estan solteras
plt.scatter(data_frame['Cedula'], data_frame['Estado_Civil'])
plt.show()

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
data_frame.Modalidad_Ingreso = data_frame.Modalidad_Ingreso.replace({'Prueba Interna y/o propedéutico':'0'})
data_frame.Modalidad_Ingreso = data_frame.Modalidad_Ingreso.replace({'Asignado OPSU':'1'})
i=0

for x in data_frame.Modalidad_Ingreso:
    if 'Convenios' in x:
        data_frame.Modalidad_Ingreso[i] = 2
        
    i=i+1
    
data_frame.Modalidad_Ingreso = data_frame.Modalidad_Ingreso.astype(int)
#Se observa en esta grafica que los valores atipicos corresponden a la modalidad de ingreso por convenios
plt.scatter(data_frame['Cedula'], data_frame['Modalidad_Ingreso'])
plt.show()
#Columna semestre
i=0

for x in data_frame.Semestre_Actual:
    if '1' in x:
        data_frame.Semestre_Actual[i] = 1
    
    if '10' in x:
        data_frame.Semestre_Actual[i] = 10
        
    if '2' in x:
        data_frame.Semestre_Actual[i] = 2
        
    if '3' in x:
        data_frame.Semestre_Actual[i] = 3
    
    if '4' in x:
        data_frame.Semestre_Actual[i] = 4
        
    if '5' in x:
        data_frame.Semestre_Actual[i] = 5
        
    if '6' in x:
        data_frame.Semestre_Actual[i] = 6
    
    if '7' in x:
        data_frame.Semestre_Actual[i] = 7
        
    if '8' in x:
        data_frame.Semestre_Actual[i] = 8

    if '9' in x:
        data_frame.Semestre_Actual[i] = 9

    i=i+1

data_frame.Semestre_Actual = data_frame.Semestre_Actual.astype(int)

#Modificacion de direccion
data_frame.Modificacion_Dir = data_frame.Modificacion_Dir.replace({'No':'0'})
data_frame.Modificacion_Dir = data_frame.Modificacion_Dir.replace({'Si':'1'})
data_frame.Modificacion_Dir = data_frame.Modificacion_Dir.astype(int)

#Numero de materias inscritas
data_frame.Num_Materias_Sem_Ant = data_frame.Num_Materias_Sem_Ant.astype(int)


#Num materias aprobadas
data_frame.Num_Materias_Aprob_Sem_Ant[1] = 10
data_frame.Num_Materias_Aprob_Sem_Ant = data_frame.Num_Materias_Aprob_Sem_Ant.astype(int)
#Se observa un solo alumno el cual aprobo 10 materias el semestre anterior, separandose bastante de la nube de puntos de la parte inferior de la grafica
plt.scatter(data_frame['Cedula'], data_frame['Num_Materias_Aprob_Sem_Ant'])
plt.show()


#Num materias retiradas
data_frame.Num_Materias_Ret_Sem_Ant = data_frame.Num_Materias_Ret_Sem_Ant.astype(int)


#Num materias reprobadas
data_frame.Num_Materias_Rep_Sem_Ant = data_frame.Num_Materias_Rep_Sem_Ant.astype(int)

#Promedio_Pond
i=0
for x in data_frame.Promedio_Pond:
    if x > 20:
        data_frame.Promedio_Pond[i] = x/1000
    i=i+1
    

#Reemplazamos el valor atipico con la media     
data_frame.Promedio_Pond[6] = 12
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

#Numero de materias actualmente


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
#Curiosamente se observa que los outliers de esta columna son los residentes de la ciudad de Caracas
plt.scatter(data_frame['Procedencia'], data_frame['Cedula'])
plt.show()

#Res_Actual en este caso 6 = No responde. 
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

data_frame.Personas_Vive_Act[189] = 0

data_frame.Personas_Vive_Act =data_frame.Personas_Vive_Act.astype(int)
#Es notable que la menor cantidad de puntos se situa en el punto definido como "Apartamentos" donde viven la menor proporcion de los estudiantes
plt.scatter(data_frame['Personas_Vive_Act'], data_frame['Cedula'])
plt.show()
#Tipo_Vivienda
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Quinta o casa quinta':'0'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Apartamento en edifico':'1'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Casa en barrio urbano':'2'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Habitación alquilada':'3'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Casa en barrio rural':'4'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Apartamento en quinta - casa quinta o casa':'0'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Residencia estudiantil':'3'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'Casa de vecindad':'2'})
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.replace({'casa':'2'})

i=0
for x in data_frame.Tipo_Vivienda:
    if x != '0' and x != '1' and x != '2' and x != '3' and x != '4' :
        data_frame.Tipo_Vivienda[i] = 5
        
    i=i+1
    
data_frame.Tipo_Vivienda[31]= 5
data_frame.Tipo_Vivienda = data_frame.Tipo_Vivienda.astype(int)
#Se observa que la mayoria de los estudiantes viven en apartamentos de edificios mientras que uno solo se ubica en otro lugar, el numero 5 coincide con "Conserjeria" que es el lugar donde vive este estudiante
plt.scatter(data_frame['Tipo_Vivienda'], data_frame['Cedula'])
plt.show()
#Monto_Alq
data_frame.Monto_Alq = data_frame.Monto_Alq.fillna(0)
data_frame.Monto_Alq = data_frame.Monto_Alq.replace({' bs': ''}, regex=True)

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

#Monto_Beca 
#Se observa un clarisimo valor atipico en el monto de las becas, se puede deber a un error de tipeo
plt.scatter(data_frame['Monto_Beca'], data_frame['Cedula'])
plt.show()


#Aporte_Resp_Econ
data_frame.Aporte_Resp_Econ = data_frame.Aporte_Resp_Econ.fillna(0)
data_frame.Aporte_Resp_Econ = data_frame.Aporte_Resp_Econ.astype(int)

#Aporte_Fam
data_frame.Aporte_Fam = data_frame.Aporte_Fam.fillna(0)
data_frame.Aporte_Fam = data_frame.Aporte_Fam.astype(int)


#Ing_Horas
data_frame.Ing_Horas = data_frame.Ing_Horas.fillna(0)
data_frame.Ing_Horas = data_frame.Ing_Horas.astype(int)


#Alimentacion
data_frame.Alimentacion = data_frame.Alimentacion.fillna(0)
data_frame.Alimentacion = data_frame.Alimentacion.astype(int)


#Transporte_P
data_frame.Transporte_P = data_frame.Transporte_P.fillna(0)
data_frame.Transporte_P = data_frame.Transporte_P.astype(int)
#Podemos observar dos valores que sugieren que gastan bastante dinero en transporte, seria interesante revisar esas cedulas y ver su direccion actual. Tal vez podria notarse que viven en una poblacion alejada a la universidad
plt.scatter(data_frame['Transporte_P'], data_frame['Cedula'])
plt.show()


#Gastos_Medicos
data_frame.Gastos_Medicos = data_frame.Gastos_Medicos.fillna(0)
data_frame.Gastos_Medicos = data_frame.Gastos_Medicos.astype(int)

#Gastos_Odont
data_frame.Gastos_Odont = data_frame.Gastos_Odont.fillna(0)
data_frame.Gastos_Odont = data_frame.Gastos_Odont.astype(int)

#Gastos_Pers
data_frame.Gastos_Pers = data_frame.Gastos_Pers.fillna(0)
data_frame.Gastos_Pers = data_frame.Gastos_Pers.astype(int)

#Alquiler_Renta
data_frame.Alquiler_Renta = data_frame.Alquiler_Renta.fillna(0)
data_frame.Alquiler_Renta = data_frame.Alquiler_Renta.astype(int)

#Mats_Est
data_frame.Mats_Est = data_frame.Mats_Est.fillna(0)
data_frame.Mats_Est = data_frame.Mats_Est.astype(int)

#Recreacion
data_frame.Recreacion = data_frame.Recreacion.fillna(0)
data_frame.Recreacion = data_frame.Recreacion.astype(int)
#Se observa un valor atipico de un estudiante que podria estar gastando demas en actividades recreativas
plt.scatter(data_frame['Recreacion'], data_frame['Cedula'])
plt.show()

#Otros_Gastos
data_frame.Otros_Gastos = data_frame.Otros_Gastos.fillna(0)
data_frame.Otros_Gastos = data_frame.Otros_Gastos.astype(int)

#Resp_Econ
data_frame.Resp_Econ = data_frame.Resp_Econ.replace({'Madre':'1'})
data_frame.Resp_Econ = data_frame.Resp_Econ.replace({'Padre':'2'})
data_frame.Resp_Econ = data_frame.Resp_Econ.replace({'Ambos padres':'3'})
data_frame.Resp_Econ = data_frame.Resp_Econ.replace({'Familiares':'4'})
data_frame.Resp_Econ = data_frame.Resp_Econ.replace({'Usted mismo':'5'})
data_frame.Resp_Econ = data_frame.Resp_Econ.replace({'Cónyugue':'6'})
i=0
for x in data_frame.Resp_Econ:
    if x != '0' and x != '1' and x != '2' and x != '3' and x != '4' and x != '5' and x != '6' :
        data_frame.Resp_Econ[i] = 7
        
    i=i+1

#tuve que hacerlo a mano, algunos se pusieron algunos no
data_frame.Resp_Econ[26] = 7
data_frame.Resp_Econ[52] = 7
data_frame.Resp_Econ[96] = 7
data_frame.Resp_Econ[117] = 7
data_frame.Resp_Econ[146] = 7
data_frame.Resp_Econ[184] = 7
data_frame.Resp_Econ = data_frame.Resp_Econ.astype(int)


#Se observa que la mayoria de los responsables economicos son madres o padres. Mientras que el menos comun es la autosuficiencia economica de los estudiantes
plt.scatter(data_frame['Resp_Econ'], data_frame['Cedula'])
plt.show()

#R_E_Carga_Fam
data_frame.R_E_Carga_Fam = data_frame.R_E_Carga_Fam.fillna(0)
data_frame.R_E_Carga_Fam = data_frame.R_E_Carga_Fam.astype(int)



#Ingreso_Resp_Econ
data_frame.Ingreso_Resp_Econ = data_frame.Ingreso_Resp_Econ.fillna(0)
data_frame.Ingreso_Resp_Econ = data_frame.Ingreso_Resp_Econ.replace({'bs':''}, regex=True)
data_frame.Ingreso_Resp_Econ = data_frame.Ingreso_Resp_Econ.replace({' ':''}, regex=True)
data_frame.Ingreso_Resp_Econ = data_frame.Ingreso_Resp_Econ.replace({',':''}, regex=True)
data_frame.Ingreso_Resp_Econ = data_frame.Ingreso_Resp_Econ.astype(float)

#Podemos observar que la mayoria no conoce el ingreso mensual de su responsable economico
plt.scatter(data_frame['Cedula'], data_frame['Ingreso_Resp_Econ'])
plt.show()

#R_E_Otros_Ing
data_frame.R_E_Otros_Ing[180] = 0
data_frame.R_E_Otros_Ing = data_frame.R_E_Otros_Ing.replace({'bs':''}, regex=True)
data_frame.R_E_Otros_Ing = data_frame.R_E_Otros_Ing.replace({' ':''}, regex=True)
data_frame.R_E_Otros_Ing = data_frame.R_E_Otros_Ing.replace({',':''}, regex=True)
data_frame.R_E_Otros_Ing = data_frame.R_E_Otros_Ing.fillna(0)
data_frame.R_E_Otros_Ing = data_frame.R_E_Otros_Ing.astype(float)



#R_E_Vivienda
data_frame.R_E_Vivienda = data_frame.R_E_Vivienda.replace({'bs':''}, regex=True)
data_frame.R_E_Vivienda = data_frame.R_E_Vivienda.replace({' ':''}, regex=True)
data_frame.R_E_Vivienda = data_frame.R_E_Vivienda.replace({',':''}, regex=True)
data_frame.R_E_Vivienda[5] = 0
data_frame.R_E_Vivienda = data_frame.R_E_Vivienda.fillna(0)
data_frame.R_E_Vivienda = data_frame.R_E_Vivienda.astype(int)


#R_E_Alimentacion
data_frame.R_E_Alimentacion = data_frame.R_E_Alimentacion.replace({'bs':''}, regex=True)
data_frame.R_E_Alimentacion = data_frame.R_E_Alimentacion.fillna(0)
data_frame.R_E_Alimentacion = data_frame.R_E_Alimentacion.astype(int)

#R_E_Transporte
data_frame.R_E_Transporte = data_frame.R_E_Transporte.replace({'bs':''}, regex=True)
data_frame.R_E_Transporte = data_frame.R_E_Transporte.fillna(0)
data_frame.R_E_Transporte = data_frame.R_E_Transporte.astype(int)

#R_E_Gastos_Medicos
data_frame.R_E_Gastos_Medicos = data_frame.R_E_Gastos_Medicos.replace({'bs':''}, regex=True)
data_frame.R_E_Gastos_Medicos = data_frame.R_E_Gastos_Medicos.fillna(0)
data_frame.R_E_Gastos_Medicos = data_frame.R_E_Gastos_Medicos.astype(float)

#R_E_Gastos_Odont
data_frame.R_E_Gastos_Odont[96]=0
data_frame.R_E_Gastos_Odont = data_frame.R_E_Gastos_Odont.replace({'bs':''}, regex=True)
data_frame.R_E_Gastos_Odont = data_frame.R_E_Gastos_Odont.fillna(0)
data_frame.R_E_Gastos_Odont = data_frame.R_E_Gastos_Odont.astype(int)


#R_E_Gastos_Educ
data_frame.R_E_Gastos_Educ = data_frame.R_E_Gastos_Educ.fillna(0)
data_frame.R_E_Gastos_Educ = data_frame.R_E_Gastos_Educ.astype(int)

#R_E_Servicios_Basicos
data_frame.R_E_Servicios_Basicos = data_frame.R_E_Servicios_Basicos.replace({'bs':''}, regex=True)
data_frame.R_E_Servicios_Basicos = data_frame.R_E_Servicios_Basicos.fillna(0)
data_frame.R_E_Servicios_Basicos = data_frame.R_E_Servicios_Basicos.astype(int)


#R_E_Condominio
data_frame.R_E_Condominio = data_frame.R_E_Condominio.replace({'bs':''}, regex=True)
data_frame.R_E_Condominio = data_frame.R_E_Condominio.fillna(0)
data_frame.R_E_Condominio = data_frame.R_E_Condominio.astype(float)


#R_E_Otros_Gastos1
data_frame.R_E_Otros_Gastos1 = data_frame.R_E_Otros_Gastos1.fillna(0)
data_frame.R_E_Otros_Gastos1 = data_frame.R_E_Otros_Gastos1.astype(float)
#Estas dos instancia son removidas por su terrible manera de imputar datos NECESARIOS para lo que seria un sistema de becas
data_frame = data_frame.drop(data_frame.index[19])  
data_frame = data_frame.drop(data_frame.index[153])  

data_frame.to_csv('minable.csv')
