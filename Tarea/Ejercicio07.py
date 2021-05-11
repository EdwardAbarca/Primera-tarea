
def Ejercicio07():
  print("Buenos dias")
  saldo=int(input("Cuanto dinero tiene "))
  opciones=""
  if saldo<=10.0:
    opciones="tarjeta"
  elif saldo>=11.0 and saldo<=100.0:
    opciones="tarjeta o chocolate"
  elif saldo>=101.0 and saldo<=250.0:
    opciones="tarjeta, chocolate o flores"
  else:
    opciones="tarjeta, chocolate, flores o un anillo"
  print("puede adquirir los siguientes elementos:", opciones)

  
Ejercicio07()