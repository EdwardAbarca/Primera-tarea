def Ejercicio09():
  print("El dia de la semana")
  diassemana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
  ordendeldia=int(input("Ingrese el orden del dia: "))
  if 1<=ordendeldia<=7:
    if ordendeldia==1:
      print("el dia es lunes")
    elif ordendeldia==2:
      print("El dia es martes")
    elif ordendeldia==3:
      print("El dia es miercoles")
    elif ordendeldia==4: 
      print ("el dia es jueves")
    elif ordendeldia==5:
      print("El dia es viernes")
    elif ordendeldia==6:
      print("El dia es sabado")
    elif ordendeldia==7:
      print("El dia es domingo")
  else:
    print("\nIngrese correctamente los datos")
Ejercicio09()