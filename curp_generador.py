#!/usr/bin/env python
# coding: utf-8

# #### Los datos necesarios para generar la CURP en Mexico son:
# 
# https://es.wikipedia.org/wiki/Clave_%C3%9Anica_de_Registro_de_Poblaci%C3%B3n
# 
# 
# https://www.dof.gob.mx/nota_detalle_popup.php?codigo=5526717#:~:text=La%20CURP%20se%20genera%20a,y%20validaci%C3%B3n%20que%20realicen%20los
# 
# « Presiciones »
# - ~~Primera letra del primer apellido.~~
# - ~~Primera vocal del primer apellido.~~
# - ~~Primera letra del segundo apellido.~~
# - Primera letra del nombre de pila: Se tomará en cuenta el primer nombre 
#   («exceptuando los nombres compuestos cuando a estos se antepongan los nombres 
#   de MARÍA o JOSÉ, entre otros, en cuyo caso se usará el segundo nombre.»).
# - ~~Fecha de nacimiento sin espacios en orden de año (dos dígitos), mes y día. 
#   Ejemplo: 960917 (1996, septiembre 17).~~
# - ~~Letra del sexo o género (H para Hombre, o M para Mujer).~~
# - ~~Dos letras correspondientes a la entidad federativa de nacimiento 
#   (en caso de haber nacido fuera del país, se marca como NE, «Nacido en el 
#   Extranjero»; véase el Catálogo de claves de entidades federativas).~~
# - ~~Primera consonante interna (después de la primera letra) del primer apellido.~~
# - ~~Primera consonante interna del segundo apellido.~~
# - Primera consonante interna del nombre de pila.
# - Dígito del 0 al 9 para fechas de nacimiento hasta el año 1999 y de la A a la Z
#   para fechas de nacimiento a partir del 2000, asignado por la SEGOB para evitar 
#   registros repetidos.
# - Dígito verificador, para comprobar la integridad.
# 
# __Excepciones__
# 
# Habitualmente, los primeros dos caracteres de la clave son las dos primeras letras del primer apellido, pero en caso de que un primer apellido tenga una consonante como segunda letra, se asignará entonces la primera vocal que se encuentre en el apellido. Por ejemplo, si una persona se llamara Romina Orozco Castillo, sus primeros cuatro caracteres de la CURP serían: OOCR, ya que la segunda letra de «Orozco» es consonante.
# 
# Tampoco la letra Ñ se asigna en la CURP. Un claro ejemplo es el apellido Peña. En casos como este es necesario reemplazar, en la clave, la letra «Ñ» por el carácter «X».
# 
# Cuando una persona tenga dos nombres y su primer nombre sea María, en el caso de mujeres, o José, en el caso de hombres, el cuarto carácter se tomará de la primera letra del segundo nombre, en vez del primero. Esto debido a que los nombres «María» y «José» son muy comunes y generarían muchos duplicados. Por ejemplo: si la persona se llama María Fernanda Escamilla Arroyo, los primeros cuatro caracteres serán EAAF (María no cuenta para formar el cuarto carácter).
# 
# Otra excepción en la cual sería necesario utilizar «X» sería el caso de personas que no cuentan con segundo apellido, o algunos extranjeros en cuyos países el segundo apellido es inexistente.
# 
# Por ejemplo, un hombre proveniente de Irlanda cuyos nombres son Brian Donall y su único apellido es Plunkett nació el 21 de octubre de 1957 y, como no nació en ninguna entidad mexicana, las dos claves correspondientes serán «NE» (Nacido en el Extranjero), y su CURP podría ser: PUXB571021HNELXR00. Se usarían, aquí, la «X» por no tener segundo apellido, ni mucho menos primera consonante del mismo, «NE» porque no nació en México y «U» porque la segunda letra de su apellido, «Plunkett», es una consonante.
# Además de las excepciones por motivo de ser ofensivo en el idioma español ejemplo: Pulido Torres Amanda su CURP sería ofensiva lo cual se cambia la segunda letra por una X quedando así: PXTA
# 
# En la estructura de la CURP (posiciones 1-4) que en ocasiones forma una palabra cuya pronunciación se considera ofensiva para los patrones socialmente establecidos, en cuyo caso la letra de la segunda posición se sustituye por una 'X'.
# 
# Ejemplo: Si el nombre de una persona es Édgar Patricio Rodríguez Cano, 
# si es de sexo masculino y nació el 31 de enero del 2000 en el estado de 
# Nuevo León, su CURP será: ROCE000131HNLDNDA9.

# In[29]:


import curp_functions as curpf
from random import randint


# In[48]:



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


# In[31]:


nombre = input("Nombre(s): ").upper()


# In[32]:


apellido_paterno = input("Apellido paterno: ").upper()


# In[33]:


apellido_materno = input("Apellido materno: ").upper()


# In[34]:


ano_nacimiento = input("Año de nacimiento: ")


# In[35]:


mes_nacimiento = input("Mes de nacimiento (numero 01-12): ")


# In[36]:


dia_nacimiento = input("Dia de nacimiento (01-31): ")


# In[37]:


genero = input("Sexo: Mujer(M)/Hombre(H): ").upper()


# In[38]:


entidad = input("Entidad federativa de nacimiento: ").upper()


# In[49]:


curp += curpf.curp_1_2(apellido_paterno) + curpf.curp_3(apellido_materno)


# In[50]:


curp += curpf.curp_4(nombre)


# In[51]:


curp += curpf.curp_5to10(ano_nacimiento, mes_nacimiento, dia_nacimiento)


# In[52]:


curp += genero + entidades[entidad] 


# In[53]:


curp += curpf.curp_14(apellido_paterno) + curpf.curp_15(apellido_materno) + curpf.curp_16(curpf.name_list(nombre))


# In[54]:


if int(ano_nacimiento) <= 1999:
    ch17 = str(randint(0,9))
else:
    ch17 = alfabeto[randint(0, len(alfabeto)-1)]


# In[55]:


ch18 = str(randint(0,9))


# In[56]:


curp += ch17 + ch18


# In[57]:


print(curp)


# In[ ]:




