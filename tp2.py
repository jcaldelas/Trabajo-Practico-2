#Definicon de funciones
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


def str2datetime(date, fmt="%Y-%m-%d"):
    if isinstance(date, str):
        return datetime.strptime(date, fmt)
    elif isinstance(date, (list, np.ndarray)):
        output = []
        for d in date:
            output.append(datetime.strptime(d, fmt))
        if isinstance(date, np.ndarray):
            output = np.array(output)
        return output

def read_file(nombre_del_archivo):
    diccionario = {}
    with open(nombre_del_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for x in range(0, len(lineas)):
            lineas[x] = lineas[x].strip()
        claves = lineas[0]
        claves = claves.split(',')

        for i, u in enumerate(claves):
            lista = []
            for h in range(1, len(lineas)):
                datos = lineas[h]
                datos = datos.split(',')
                if i == 0:
                    lista.append(datos[i])
                else: 
                    lista.append(float(datos[i]))
            diccionario[claves[i]] = lista
    return diccionario
diccionario = read_file('Trabajo-Practico-2/bolsa.csv')    

def monthly_average(accion, diccionario):
    lista_sinrepetir = []
    lista_anos = []
    diccionario.get(accion)
    dias = diccionario.get('Date')
    promedios = []
    for x, i in enumerate(dias):
        date = dias[x].split('-')
        lista_anos.append(date[0] + date[1])
        for j in lista_anos:
            if j not in lista_sinrepetir:
                lista_sinrepetir.append(j)
    for n in lista_sinrepetir:
        lista_promedio = []
        for m, l in enumerate(lista_anos):
            if n == l:
                lista_promedio.append(diccionario[accion][m])
            suma = sum(lista_promedio)
            largo = len(lista_promedio)
        resultado = suma / largo
        resultado = str(resultado)
        promedios.append(resultado)
    
    return lista_anos, promedios
        
fechas, promedios = monthly_average('SATL', diccionario)
with open('monthly_average_SATL.csv', 'w') as ejercicio_3:
    for promedio in promedios:
        ejercicio_3.write(promedio)



def max_gain(nombre_accion, diccionario, fecha_venta):
    precio = 0
    valor_max = 0
    maximos_anteriores = []
    posicion = 0
    for i, fechas in enumerate(diccionario['Date']):
        if fechas == fecha_venta:
            for x, valores in enumerate(diccionario[nombre_accion]):
                if x == i:
                    for d, precios in enumerate(diccionario[nombre_accion]):
                        if d <= x:
                            maximos_anteriores.append(precios)
                            valor_min = min(maximos_anteriores)
                            posicion = maximos_anteriores.index(valor_min)             
    dia_optimo = diccionario['Date'][posicion]
    indice_precio_venta = 0
    for indice, fecha in enumerate(diccionario['Date']):
        if fecha == fecha_venta:
            indice_precio_venta = indice
    precio_compra = diccionario[nombre_accion][posicion]
    precio_venta = diccionario[nombre_accion][indice_precio_venta]
    ganancia = (precio_venta - precio_compra) / precio_compra
    return ganancia, dia_optimo
max_gain('MELI', diccionario, '2022-06-06')


def report_max_gains(diccionario, fecha_venta):
    with open('resumen_mejor_compra.txt', 'w') as archivo:
        acciones = list(diccionario.keys())
        maximos = []
        for i, nombre in enumerate(acciones):
            if i > 0:
                maximos.append(max_gain(nombre, diccionario, fecha_venta))
        l = 1
        if i > 0:
            for max in maximos:
                info = str(acciones[l]) + ' genera una ganancia de ' + str(list(max)[0]) + '% habiendo comprado en ' + str(list(max)[1]) + ' y vendiendose en ' + str(fecha_venta)
                archivo.write(info + '\n')
                l += 1
report_max_gains(diccionario, '2022-06-06')

def plot_price(nombre_accion, diccionario, start = '2021-10-04', end = '2022-09-28'):
    idx_start = diccionario["Date"].index(start)
    idx_end = diccionario["Date"].index(end)
    x_data = str2datetime(diccionario["Date"])[idx_start:idx_end]
    y_data = diccionario[nombre_accion][idx_start: idx_end]
    plt.plot(x_data, y_data, 'g')
    plt.savefig(f'price_{nombre_accion}.png')
    plt.title(f'Graficos de precio de la acción {nombre_accion}')
    plt.xlabel('Fechas')
    plt.ylabel('Precios')
    plt.grid(True)
    plt.show()


def monthly_average_bar_plot(nombre_accion, diccionario):
    fechas, promedios = monthly_average(nombre_accion, diccionario)

    
monthly_average_bar_plot('MELI', diccionario)





