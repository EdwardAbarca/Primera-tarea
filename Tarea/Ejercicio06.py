#ejercicio 3.7
def Ejercicio06():
  print("Hola, bienvenido al programa becas del estado")
  edad=int(input("Por favor ingrese su edad:"))
  promedio=float(input("Por favor ingrese su promedio:"))
  bono=0.0
  bono1=2000.0
  bono2=1000.0
  bono3=500.0
  bono4=3000.0
  bono5=2000.0
  bono6=100.0
  recomendacion="Lo sentimos siga intentandolo el proximo año"
  if edad>18 and promedio>=9:
    bono=print("Aprobado, su bono es de", bono1)
  elif edad>18 and promedio>=7.5:
    bono=print("Aprobado, su bono es de", bono2)
  elif edad>18 and promedio<7.5 and promedio>=6:
    bono=print("Aprobado, su bono es de", bono3)
  elif edad>18 and promedio<6:
    bono=print("Rechazado", recomendacion)
  elif edad<=18 and promedio>=9:
    bono=print("Aprobado, su bono es de", bono4)
  elif edad<=18 and promedio<9 and promedio>=8:
    bono=print("Aprobado, su bono es de", bono5)
  elif edad<=18 and promedio<8 and promedio>=6:
    bono=print("Aprobado, su bono es de", bono6)
  elif edad<=18 and promedio<6:
    bono=print("Rechazado", recomendacion)
  (bono)
Ejercicio06()