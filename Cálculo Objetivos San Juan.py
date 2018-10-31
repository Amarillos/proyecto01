

def precio_hora(lista_obj,facturacion,tipo):
  objs=len(lista_obj[1])
  p_hora=0
  for i in range(objs):
    if facturacion >= lista_obj[1][i] and facturacion < lista_obj[1][i+1]:
      p_hora=lista_obj[tipo][i]
      break
  return p_hora

def tipo_hora(lista_obj):
  print("Ingrese el tipo de hora: ")
  for i in range(2,5):
    print("Opción ", i-1," - ", lista_obj[0][i])
  opc=int(input("Ingrese la opción correcta: "))
  while opc<1 or opc>3:
    opc=int(input("Ingrese una opción correcta: "))
  return opc+1

def facturacion(lista_obj):
  objs=lista_obj[1][len(lista_obj[1])-1]-1
  facturacion=float(input("Ingrese el total de Facturación: "))
  while facturacion < 0 or facturacion > objs:
    print("Ingrese un número mayor que 0 y menor que ",objs)
    facturacion=float(input("Ingrese el total de Facturación: "))
  return facturacion

def tabla(lista_obj):
  objs0=len(lista_obj)
  objs1=len(lista_obj[1])
  objs2=len(lista_obj[0])
  esp1=" "
  for k in range(objs2):
    aux=12
    esp2=aux-len(str(lista_obj[0][k]))
    esp3=esp1*esp2
    print(lista_obj[0][k],end=esp3)
  print()
  for j in range(objs1):
    aux=4
    esp1=" "
    esp2=aux-len(str(j))
    esp3=esp1*esp2
    print(esp3,j,end="")
    for i in range(1,objs0):
      aux=6
      esp2=aux-len(str(lista_obj[i][j]))
      esp3=esp1*esp2
      print("   $",esp3,lista_obj[i][j],end="")
    print()  


"""
Impresión de tabla considerando la distancia a la derecha
def tabla(lista_obj):
  objs0=len(lista_obj)
  objs1=len(lista_obj[0])
  for j in range(objs1):
    aux=6
    esp1=" "
    esp2=aux-len(str(j))
    esp3=esp1*esp2
    print(j,end=esp3)
    for i in range(objs0):
      aux=8
      esp2=aux-len(str(lista_obj[i][j]))
      esp3=esp1*esp2
      print(lista_obj[i][j],end=esp3)
    print()

"""
def lista_objetivos():
  obj_sanjuan=[["Índice", "Ventas", "Día Semana", "Sábado", "Domingo"],[0	,	4000	,	6000	,	8000	,	10000	,	11500	,	13000	,	14500	,	16000	,	17500	,	19000	,	20500	,	22000	,	23500	,	25000	,	26500	,	28000	,	29500	,	31000],[40	,	45	,	50	,	55	,	60	,	65	,	70	,	75	,	80	,	85	,	90	,	95	,	100	,	105	,	110	,	115	,	120	,	125	,	130],[45	,	51	,	56	,	62	,	68	,	73	,	79	,	84	,	90	,	96	,	102	,	108	,	113	,	119	,	124	,	130	,	135	,	141	,	146],[50	,	56	,	63	,	69	,	75	,	81	,	88	,	94	,	100	,	106	,	113	,	119	,	125	,	131	,	137	,	143	,	149	,	155	,	162]]
  return obj_sanjuan

def despedida():
  mensaje="Gracias por usar el programa..."
  print(mensaje)

otra="s"
obj_sanjuan=lista_objetivos()
while otra=="s" or otra=="S":
  tabla(obj_sanjuan)
  print()
  facturac=facturacion(obj_sanjuan)
  print()
  tipo=tipo_hora(obj_sanjuan)
  print()
  cant_horas=float(input("Ingrese la cantidad de horas trabajadas: "))
  while cant_horas<0 or cant_horas>24:
    cant_horas=float(input("Ingrese la cantidad de horas correcta: "))      
  hora=precio_hora(obj_sanjuan,facturac,tipo)
  print()
  print("El precio de la hora es: $",hora)
  print("Corresponde cobrar: $",hora*cant_horas)

  otra=str(input("Ingrese ´s´ si quiere hacer otra consulta: "))

despedida()