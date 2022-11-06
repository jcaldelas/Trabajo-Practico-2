#Definicon de funciones
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
        
    with open('monthly_average_SATL.csv', 'w') as ejercicio_3:
        for promedio in promedios:
            ejercicio_3.write(promedio)
    
monthly_average('SATL', diccionario)
def max_gain(nombre_accion, diccionario, fecha_venta):
    precio = 0
    valor_max = 0
    maximos_anteriores = []
    posicion = 0
    for i, fechas in enumerate(diccionario['Date']):
        if fechas == fecha_venta:
            for x, valores in enumerate(diccionario[nombre_accion]):
                if x == i:
                    precio = valores          
                    for d, precios in enumerate(diccionario[nombre_accion]):
                        if d <= x:
                            maximos_anteriores.append(precios)
                            valor_max = max(maximos_anteriores)
                            posicion =maximos_anteriores.index(valor_max)
    dia_optimo = diccionario['Date'][posicion] 
    precio_venta2 = diccionario[nombre_accion][posicion]
    print(precio_venta2)
    print(dia_optimo)                 
    return dia_optimo

    
max_gain('MELI', diccionario, '2021-06-06')

def report_max_gains(diccionario, fecha_venta):
    fecha = input('Ingresar fecha en formato AÑO-MES-DIA: ')
