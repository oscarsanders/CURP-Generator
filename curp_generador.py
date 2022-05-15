#!/usr/bin/env python
# coding: utf-8
# Los datos necesarios para generar la CURP en Mexico son:
# https://es.wikipedia.org/wiki/Clave_%C3%9Anica_de_Registro_de_Poblaci%C3%B3n
# https://www.dof.gob.mx/nota_detalle_popup.php?codigo=5526717#:~:text=La%20CURP%20se%20genera%20a,y%20validaci%C3%B3n%20que%20realicen%20los

import curp_functions as curpf
from random import randint

alfabeto_ingles = ["A","B","C","D","E","F","G","H","I","J","K","L",
               "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L",
               "M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]               

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
    "MEXICO" : 'MC',
    "MICHOACÁN" : 'MN',
    "MORELOS" : 'MS',
    "NAYARIT" : 'NT',
    "NUEVO LEÓN" : 'NL',
    "OAXACA" : 'OC',
    "PUEBLA" : 'PL',
    "QUERETARO" : 'QT',
    "QUINTANA ROO" : 'QR',
    "SAN LUIS POTOSI" : 'SP',
    "SINALOA" : 'SL',
    "SONORA" : 'SR',
    "TABASCO" : 'TC',
    "TAMAULIPAS" : 'TS',
    "TLAXCALA" : 'TL',
    "VERACRUZ" : 'VZ',
    "YUCATAN" : 'YN',
    "ZACATECAS" : 'ZS',
    "EXTRANJERO" : 'NE'
}

curp = ""

nombre = input("Nombre(s): ").upper()

apellido_paterno = input("Apellido paterno: ").upper()

apellido_materno = input("Apellido materno: ").upper()

ano_nacimiento = input("Año de nacimiento: ")

mes_nacimiento = input("Mes de nacimiento (numero 01-12): ")

dia_nacimiento = input("Dia de nacimiento (01-31): ")

genero = input("Sexo: Mujer(M)/Hombre(H): ").upper()

entidad = input("Entidad federativa de nacimiento: ").upper()

curp += curpf.curp_1_2(apellido_paterno) + curpf.curp_3(apellido_materno)

curp += curpf.curp_4(nombre)

curp += curpf.curp_5to10(ano_nacimiento, mes_nacimiento, dia_nacimiento)

curp += genero + entidades[entidad] 

curp += curpf.curp_14(apellido_paterno) + curpf.curp_15(apellido_materno) + curpf.curp_16(curpf.name_list(nombre))

if int(ano_nacimiento) <= 1999:
    ch17 = str(randint(0,9))
else:
    ch17 = alfabeto[randint(0, len(alfabeto)-1)]

ch18 = str(randint(0,9))

curp += ch17 + ch18

print(curp)




