import xlsxwriter
import base64

# Informacion
archivo_grupos = "grupos.csv"
archivo_carreras = "carreras.csv"

# Agrear ordenados de mayor a menor y eliminar los excedentes 
def AgregarDePana(Bucket, valor, gnumber, grupos):
    # Flag de si entró el valor o no.
    flag = False
    # Si está vacío lo agregamos así nomá
    length = len(Bucket[gnumber])
    if length == 0:
        Bucket[gnumber].append(valor)
    else:
        for v in range(length):
            if valor[1] > Bucket[gnumber][v][1]:
                Bucket[gnumber].insert(v, valor)
                flag = True
                break
        # Si no ha entrado el valor, y el arreglo en la bucket es menor al máximo de vacantes por grupo, entonces lo agregamos al final
        if(not flag and length < grupos[gnumber-1][2]):
            Bucket[gnumber].append(valor)
    
    # Revisamos si el diccionario modificado tiene más vacantes de lo disponible, eliminamos el último
    if length > grupos[gnumber-1][6]:
        del Bucket[gnumber][-1]
    return Bucket
    
def CargarDatos():
    grupos = []
    carreras = []
    #Cargar los grupos de carreras agrupados por ponderaciones.
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
    file = open(archivo_carreras, "r")
    for line in file:
        string = line.split(",")
        for i in range(1,3):
            string[i] = int(string[i])
        carreras.append(string)
    file.close()
    return grupos, carreras

#Parsear postulantes
def ParseData(buckets, grupos, datos):
    print(datos)
    datos = datos.split('\n')
    for line in datos:
        string = line.split(";")
        # Pasar a int
        if(not string[0].isdigit()):
            continue
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
        #buckets = 
        AgregarDePana(buckets, valor, grupom, grupos)
    #return buckets
#print(buckets)

def EscribirExcel(buckets, carreras, nombre):
    excel = xlsxwriter.Workbook(nombre)
    for item in carreras:
        worksheets = []
        worksheets.append(excel.add_worksheet(item[0]))
        row = 0
        contador = 0
        col = 0
        vacantes = item[1]
        lista = list(buckets[item[-1]])
        for b in range(len(lista)): # El grupo al que pertenecen las carreras está al final; V es la tupla
            if(row == vacantes):
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

# Recibe el nombre del archivo y retorna el string en b64 | Debería pedir los datos en vez del nombre.
def EncodeFile(archivo_out):
    data = open(archivo_out, 'rb').read()
    base64_encoded = base64.b64encode(data)
    #file = open("archivo.bin", 'wb').write(base64_encoded)
    return base64_encoded

# Recibe datos en b64 y los decodifica.
def Decode(data):
    #data = open("holiwi.bin", 'rb').read()
    base64_decoded = 0
    base64.decode(data, base64_decoded)
    return base64_decoded
