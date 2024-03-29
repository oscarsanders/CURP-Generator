# Requisitos para generar curp 2022:
# -Nombre completo
# -Fecha nacimiento
# -Lugar nacimiento
# -Genero M/H
# -Numero aleatorio

vocales = ["A","E","I","O","U"]
consonantes = ["B","C","D","F","G","H","J","K","L",
               "M","N","Ñ","P","Q","R","S","T","V","W","X","Y","Z"]
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L",
               "M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# Estados de México
entidades = {
    "AGUASCALIENTES" : 'AS',
    "BAJA CALIFORNIA":'BC',
    "BAJA CALIFORNIA SUR" : 'BS',
    "CAMPECHE" : 'CC',
    "COAHUILA" : 'CL',
    "COLIMA" : 'CM',
    "CHIAPAS" : 'CS',
    "CHIHUAHUA" : 'CH',
    "CIUDAD DE MÉXICO" : 'DF',
    "DURANGO" : 'DG',
    "GUANAJUATO" : 'GT',
    "GUERRERO" : 'GR',
    "HIDALGO" : 'HG',
    "JALISCO" : 'JC',
    "MÉXICO" : 'MC',
    "MICHOACÁN" : 'MN',
    "MORELOS" : 'MS',
    "NAYARIT" : 'NT',
    "NUEVO LEÓN" : 'NL',
    "OAXACA" : 'OC',
    "PUEBLA" : 'PL',
    "QUERÉTARO" : 'QT',
    "QUINTANA ROO" : 'QR',
    "SAN LUIS POTOSÍ" : 'SP',
    "SINALOA" : 'SL',
    "SONORA" : 'SR',
    "TABASCO" : 'TC',
    "TAMAULIPAS" : 'TS',
    "TLAXCALA" : 'TL',
    "VERACRUZ" : 'VZ',
    "YUCATÁN" : 'YN',
    "ZACATECAS" : 'ZS',
    "EXTRANJERO" : 'NE'
}

curp = []

# lista vacia para nombre completo
nombre_full = []

ap_paterno = input("Apellido Paterno: ").upper()
nombre_full.append(ap_paterno)

ap_materno = input("Apellido Materno: ").upper()
nombre_full.append(ap_materno)

nombres = input("Nombre(s): ").upper().split()

nombre_full = nombre_full + nombres
# print(nombre_full)

fecha = []
year = input("Año de nacimiento: ")
fecha.append(year)

month = int(input("Mes de nacimiento (numero): "))
if month <= 9:
    month = "0"+str(month)
fecha.append(str(month))

day = int(input("Dia de nacimiento (numero): "))
if day <= 9:
    day = "0"+str(day)
fecha.append(str(day))

# Entidad federativa (estado de la republica)
state = input("Entidad federativa de nacimiento (estado): ").upper()

# Ciudad natal
city = input("Ciudad de nacimiento: ").upper()

#Genero
genero = input("Seleccione genero Mujer (M) / Hombre (H): ").upper()

# Numero aleatorio para 
# los ultimos dos espacios
from random import randint
n1 = str(randint(0, 9))
n2 = str(randint(0, 9))

#Generar CURP
#1/18
curp = ap_paterno[0]
#2/18
for vocal in vocales:
    for letra in ap_paterno:
        if letra == vocal:
            curp = curp + letra
    break
#3/18    
curp = curp + ap_materno[0]
#4/18
curp = curp + nombre_full[2][0]
#6/18
curp = curp + year[2:]
#8/18
curp = curp + str(month)
#10/18
curp = curp + str(day)
#11/18
curp = curp + genero
#13/18
for entidad in entidades:
    if entidad == state:
        curp = curp + entidades[state]
#14/18 
for vocal in vocales:
    for letra in ap_paterno[1:]:
        if letra != vocal:
            curp = curp + letra
            break
    break
#15/18
for vocal in vocales:
    for letra in ap_materno[1:len(ap_materno)-1]:
        if letra in vocales:
            continue
        elif vocal != letra:
            curp = curp + letra
            break
    break
#16/18
for vocal in vocales:
    for letra in nombre_full[2]:
        if letra in vocales:
            continue
        elif vocal != letra:
            curp = curp + letra
            break
    break
#18/18
curp = curp + n1 + n2

print(f"Tu clave CURP es: {curp}")
print("NOTA: Los dos ultimos digitos \
\n      pueden no ser los correctos.")

