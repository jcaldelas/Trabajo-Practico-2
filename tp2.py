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

def monthly_average(accion, diccionario):
    lista_sinrepetir = []
    lista_anos = []
    diccionario.get(accion)
    dias = diccionario.get('Date')
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
        print(resultado)
        
prueba = monthly_average('SATL', read_file('PRACTICAS/bolsa.csv'))
with open('monthly_average_SATL.csv', 'w') as archivo:
    archivo.write(prueba)