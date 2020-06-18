import xlsxwriter

# Informacion
archivo_grupos = "grupos.csv"
archivo_carreras = "carreras.csv"

# Nombre de los archivos (debug)
archivo_datos = "ejemplo.csv"

def AgregarDePana(Bucket, valor, gnumber):
    # Flag de si entró el valor o no.
    flag = False
    # Si está vacío lo agregamos así nomá
    length = len(Bucket[gnumber])
    if length == 0:
        Bucket[gnumber].append(valor)
    else:
        for v in range(length):
            if valor[1] > Bucket[grupom][v][1]:
                Bucket[grupom].insert(v, valor)
                flag = True
                break
        # Si no ha entrado el valor, y el arreglo en la bucket es menor al máximo de vacantes por grupo, entonces lo agregamos al final
        if(not flag and length < grupos[gnumber-1][2]):
            Bucket[gnumber].append(valor)
    
    # Revisamos si el diccionario modificado tiene más vacantes de lo disponible, eliminamos el último
    if length+1 >= grupos[gnumber-1][6]:
        del Bucket[gnumber][-1]

#Cargar los grupos de carreras agrupados por ponderaciones.
grupos = []
file = open(archivo_grupos , "r")
for line in file:
    string = line.split(",")
    for i in range(1,8):
        if(i < 6):
            string[i] = int(string[i])/100
        else:
            string[i] = int(string[i])
    grupos.append(string)
file.close()

#Cargar los nombres de las carreras
carreras = []
file = open(archivo_carreras, "r")
for line in file:
    string = line.split(",")
    for i in range(1,3):
        string[i] = int(string[i])
    carreras.append(string)
file.close()

#Parsear postulantes
buckets = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
datos = []
file = open(archivo_datos, "r")
for line in file:
    string = line.split(";")
    # Pasar a int
    for i in range(7):
        string[i] = int(string[i])

    valor = []
    valor.append(string[0]) # Agregar el rut

    # Debido a que la utem permite ciencias o historia, sacamos el menor puntaje entre los 2.
    if(string[5] >= string[6]):
        del string[6]
    else:
        del string[5]

    # Ponderar
    maximo = 0
    grupom = 0
    for g in grupos:
        suma = 0
        for i in range(1,6):
            suma += string[i] * g[i]
        if(suma > maximo):
            maximo = suma
            grupom = g[-1]
    valor.append(maximo) # Agregar el puntaje ponderado maximo
    # Funcion auxiliar: agregar de pana. (Ordenados)
    #buckets[grupom].append(valor)
    AgregarDePana(buckets, valor, grupom)

file.close()
print(buckets)

#def EscribirExcel:
excel = xlsxwriter.Workbook('holiwi.xlsx')
for item in carreras:
    worksheets = []
    worksheets.append(excel.add_worksheet(item[0]))
    row = 0
    contador = 0
    col = 0
    vacantes = item[-2]
    lista = list(buckets[item[-1]])
    for b in range(len(lista)): # El grupo al que pertenecen las carreras está al final; V es la tupla
        if(row == item[1]):
            break
        worksheets[-1].write(row, col, lista[0][0]) # Debemos acceder al ultimo worksheet; y al primer elemento de la lista (mayor) 
        worksheets[-1].write(row, col+1, lista[0][1]) # 0 y 1 son rut y ptje ponderado
        # Eliminamos el primer elemento y avanzamos el puntero
        row += 1
        del lista[0]
        contador += 1
    # También debemos sacar los elementos de la bucket
    del buckets[item[-1]][:contador]


excel.close()