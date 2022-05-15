# -*- coding: utf-8 -*-

vocales = ["A","E","I","O","U"]

consonantes = ["B","C","D","F","G","H","J","K","L",
               "M","N","Ñ","P","Q","R","S","T","V","W","X","Y","Z"]

def name_list(name):
  """
  str -> list of strings

  return a list of strings from one string with white 
  spaces (split string input)
  
  >>> name_list("oscar alan")
  ['oscar', 'alan']
  >>> name_list("oscar alan")
  ['oscar']
  """
  nombre_lista = name.split()
  return nombre_lista

def curp_1_2(lastname1):
  """
  str -> str
  return two first characters from string
  >>> curp_1_2("OROZCO")
  OO
  >>> curp_1_2("SANDERS")
  SA
  """
  n = 0
  ch_1_2 = ""
  ch_1_2 += lastname1[n]
  for ch in lastname1[1:]:
    if ch in vocales:
      ch_1_2 += ch
      break
  return ch_1_2

def curp_3(lastname2):
  """
  str -> str
  return first character from string
  >>> curp_3("GUTIERREZ")
  G
  """
  ch_3 = ""
  ch_3 += lastname2[0]
  return ch_3

def curp_4(nombres):
  # put some .startwith(MARIA) OR .startwith(JOSE)
  # if there are two names
  ch_4 = ""

  ch_4 += nombres[0][0]
  return ch_4

def curp_5to10(year, month, day):
  """
  (str, str, str) -> str
  return one string from three strings
  >>> curp_5to10("1990","12","10")
  """
  ch_5_10 = ""
  ch_5_10 += year[2:] + month + day
  return ch_5_10

def curp_14(lastname1):
  """
  """
  ch_14 = ""
  for ch in lastname1[1:]:
    if ch in consonantes:
      ch_14 += ch
      break
  return ch_14

def curp_15(lastname2):
  """
  """
  ch_15 = ""
  for ch in lastname2[1: len(lastname2)-1]:
    if ch in consonantes:
      ch_15 += ch
      break
  return ch_15

def curp_16(name):
  """
  """
  ch_16 = ""
  for ch in name[0]:
    if ch in consonantes:
      ch_16 += ch
      break
  return ch_16

