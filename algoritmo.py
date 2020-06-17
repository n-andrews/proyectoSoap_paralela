def AgregarDePana(Bucket, valor, gnumber):
    # Flag de si entró el valor o no.
    flag = False
    # Si está vacío lo agregamos así nomá
    length = len(Bucket(gnumber))
    if length == 0:
        Bucket[gnumber].append(valor)
    else:
        for v in range(len(Bucket[gnumber])):
            if valor[1] > Bucket[grupom][i][1]:
                Bucket[grupom].insert(v, valor)
                flag = True
                break
        # Si no ha entrado el valor, y el arreglo en la bucket es menor al máximo de vacantes, entonces lo agregamos al final
        if(not flag and len(Bucket[gnumber]) < grupos[gnumber-1][2]):
            Bucket[gnumber].append(valor)
    
    # Revisamos si el diccionario modificado tiene más vacantes de lo disponible, eliminamos el último
    if length > grupos[gnumber-1][2]:
        del Bucket[gnumber][-1]
#Cargar los grupos de carreras agrupados por ponderaciones.
grupos = []
file = open("grupos.csv", "r")
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
file = open("carreras.csv", "r")
for line in file:
    string = line.split(",")
    for i in range(1,3):
        string[i] = int(string[i])
    carreras.append(string)
file.close()

#Parsear postulantes
buckets = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
datos = []
file = open("mini.csv", "r")
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
    buckets[grupom].append(valor)
file.close
print(buckets)