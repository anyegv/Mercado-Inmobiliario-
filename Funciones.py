import json
#CODIGO PARA ABRIR LOS JSON, SE DEBE INTRODUCIR EL NOMBRE DEL JSON A ABRIR AL LLAMAR LA FUNCIÓN
def open_json(json_name):
    with open((fr"D:\UNIVERSIDAD\PROYETO INMOBILIARIA\{json_name}.json"), "r", encoding="utf-8") as f:
            datos = json.load(f)
    return(datos)

alq=open_json("Alquileres") #GUARDAR LOS DATOS DEL JSON DE ALQUILERES EN UNA VARIABLE PARA TRABAJO POSTERIOR
#GUARDAR LOS DATOS DEL JSON DE Casas por Cuarto EN UNA VARIABLE PARA TRABAJO POSTERIOR

#EXTRAER UNA LISTA CON LOS PRECIOS DE LOS ALQUILERES
def precios_alquileres():
    precios=[]
    for index in range (len(alq)):
        precios.append(alq[index]['percio'])
    return precios

#ESTA FUNCIÓN ESTÁ PREPARADA PARA LA GRÁFICA DE SCATTER, FUNCIONA PARA OBTENER UNA LISTA DE INDICES PARA LAS CASAS EN CORRESPONDENCIA A LOS SERVICIOS (introducir "casas" o "servicios" al llanar la función)
def servicios_alquileres(x:str):
    servicios=[]
    for i in range(len(alq)):
        servicios.append(list((alq[i]["servicios"]).values()))
    
    casas_serv=[]
    serv_true=[]
    for i in range(len(servicios)):
        aux=[]
        aux2=[]
        for j in range(len(servicios[i])):
            if servicios[i][j]==True:
                aux.append(j)
                aux2.append(i)
        serv_true.append(aux)
        casas_serv.append(aux2)
    if x=="casas":
        return casas_serv
    elif x=="servicios":
        return serv_true
    else: print("ERROR.....Introduzca: 'casas' o 'servicios'")