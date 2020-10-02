# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 21:22:16 2020

@author: oscar
"""
#Parte del codigo para poder abrir el archivo csv
import csv

lista_datos = []

with open("synergy_logistics_database.csv","r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
        lista_datos.append(linea)
        
        

#Interfaz con la que el usurio podra interactuar con la informacion
print("EL SIGUIENTE PROGRAMA MUESTRA \n Opción 1) Rutas de importación y exportación. \n Opción 2) Medio de transporte utilizado. \n Opción 3) Valor total de importaciones y exportaciones. \n")
accion = input("QUE ACCION DESEA REALIZAR? (Escriba 1,2 o 3:  ")

#GENERAR RUTAS DE EXPORTACIÓN E IMPORTACIONES OPCION 1

def opcion1():
    #aqui se accede al indice de las exportaciones para poder usar esos datos y sacar los paises que las hacen y las reciben ademas de la informacionde cuanto generan
    direccion = "Exports"
    contador = 0
    rutas_contadas = []
    conteo_rutas = []
    dinero_ruta = 0
    a=0
    b=1
    #for que recorre la lista y la ordena para sacar los datos
    for ruta in lista_datos:
        if ruta[1] == direccion:
            ruta_actual = [ruta[2], ruta[3]]
            
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[2],movimiento[3]]:
                        contador +=1
                        dinero_ruta += int(movimiento[9])
                        
                rutas_contadas.append(ruta_actual)
                formato_ideal = [ruta[2],ruta[3], contador, dinero_ruta]
                conteo_rutas.append(formato_ideal)
                contador = 0
                dinero_ruta = 0
     #Se ordena la lista para poder obtener los indices adecuados y posteriormete poder obtener los 10 primeros           
    conteo_rutas.sort(reverse = True, key = lambda x:x[2])
    for top in conteo_rutas:
        if a<10:
            print(b," La ruta",top[0]," a ", top[1], "cuenta con: ", top[2]," Exportaciones ")
            b+=1
            a+=1
        
    
      #esta parte del codigo accede a la importaciones para poder sacar los paises involucrados y lo que han generado  
    direccion1 = "Imports"
    contador1 = 0
    rutas_contadas1 = []
    conteo_rutas1 = []
    dinero_ruta1 = 0
    a1=0
    b1=1
    #el for nos permite al igual que en la otra parte del codigo obtener los indices adecuados
    for ruta1 in lista_datos:
        if ruta1[1] == direccion1:
            ruta_actual1 = [ruta1[2], ruta1[3]]
            
            if ruta_actual1 not in rutas_contadas1:
                for movimiento1 in lista_datos:
                    if ruta_actual1 == [movimiento1[2],movimiento1[3]]:
                        contador1 +=1
                        dinero_ruta1 += int(movimiento1[9])
                        
                rutas_contadas1.append(ruta_actual1)
                formato_ideal = [ruta1[2],ruta1[3], contador1, dinero_ruta1]
                conteo_rutas1.append(formato_ideal)
                contador1 = 0
                dinero_ruta1 = 0
        #se ordenan de mayor a menor para poder representar la informacion y se seleccionan los que seran mostrados        
    conteo_rutas1.sort(reverse = True, key = lambda x:x[2])
    for top1 in conteo_rutas1:
        if a1<10:
            print(b1," La ruta",top1[0]," a1 ", top1[1], "cuenta con: ", top1[2]," Importaciones")
            b1 +=1
            a1 +=1

#esta parte del codigo esta en proceso

def opcion2():
    print("Disculpe las molestias, aun no esta disponible. GRACIAS!")



#GENERAR RUTAS DE EXPORTACIÓN E IMPORTACIONES PARA CONCER LOS QUE APORTAN EL 80% OPCION 3
# la parte 3 es muy similar a las enteriores con la diferencia de que en la parte final del codigo se agrega un apartado para
# poder calcular el porcentaje de y el equivalente al 80% asi como los paises que lo conforman
def opcion3():
    
    direccion = "Exports"
    contador = 0
    rutas_contadas = []
    conteo_rutas = []
    dinero_ruta = 0
    dinero_total = 0
    for ruta in lista_datos:
        if ruta[1] == direccion:
            ruta_actual = [ruta[2], ruta[3]]
            
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[2],movimiento[3]]:
                        contador +=1
                        dinero_ruta += int(movimiento[9])
                        
                rutas_contadas.append(ruta_actual)
                formato_ideal = [ruta[2],ruta[3], contador, dinero_ruta]
                conteo_rutas.append(formato_ideal)
                dinero_total += dinero_ruta
                contador = 0
                dinero_ruta = 0
    conteo_rutas.sort(reverse = True, key = lambda x:x[3])
    nomas80 = 0
    paises80 = []
    porcentaje80 = int(dinero_total) * 0.8
    for porce in conteo_rutas:
        nomas80 += porce[3]
        if nomas80 < porcentaje80:
            ideal_format = porce[0],porce[3]
            paises80.append(ideal_format)
    for paises in paises80:
        print("Los paises que aportan el 80% de las exportaciones son: ", paises[0],"Con un: ", int(paises[1])/int(dinero_total) * 100, "% del total \n")
        
    #esta parte del codigo nos muestra los paises que aportan el 80% del ingreso de la aportaciones y su respectivo porcentaje
    direccion1 = "Imports"
    contador1 = 0
    rutas_contadas1 = []
    conteo_rutas1 = []
    dinero_ruta1 = 0
    dinero_total1 = 0
    for ruta1 in lista_datos:
        if ruta1[1] == direccion1:
            ruta_actual1 = [ruta1[2], ruta1[3]]
            
            if ruta_actual1 not in rutas_contadas1:
                for movimiento1 in lista_datos:
                    if ruta_actual1 == [movimiento1[2],movimiento1[3]]:
                        contador1 +=1
                        dinero_ruta1 += int(movimiento1[9])
                        
                rutas_contadas1.append(ruta_actual1)
                formato_ideal = [ruta1[2],ruta1[3], contador1, dinero_ruta1]
                conteo_rutas1.append(formato_ideal)
                dinero_total1 += dinero_ruta1
                contador1 = 0
                dinero_ruta1 = 0
                
    conteo_rutas1.sort(reverse = True, key = lambda x:x[2])                
    
    nomas800 = 0
    paises800 = []
    porcentaje800 = int(dinero_total1) * 0.8
    for porce in conteo_rutas:
        nomas800 += porce[3]
        if nomas800 < porcentaje800:
            ideal_format1 = porce[0],porce[3]
            paises800.append(ideal_format1)
    for paises1 in paises800:
        print("Los paises que aportan el 80% de las importaciones son: ", paises1[0],"Con un: ", int(paises1[1])/int(dinero_total1) * 100, "% del total \n")
          
        
 #parte dle codigo que activa la funcion respectiva de la parte del codigo que se requiere y fue seleccionado.       
        
if accion == "1":
    opcion1()
    

if accion == "2":
    opcion2()
    

if accion == "3":
    opcion3()
    
