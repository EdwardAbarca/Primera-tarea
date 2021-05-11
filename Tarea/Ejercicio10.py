def Ejercicio10():
  print("costo del pasaje por alumno")
  cantdalumnos=int(input("Ingrese la cantidad de alumnos: "))
  if cantdalumnos>100:
    print("El costo del pasaje por alumno sera de 20 $")
  elif 50<=cantdalumnos<=100:
    print("el costo del pasaje por alumno sera de 35 $")
  elif 20<=cantdalumnos<=49:
    print("el costo del pasaje por alumno sera de 40 $")
  elif cantdalumnos<20:
    print("el costo del pasaje por alumno sera de 70 $")
Ejercicio10()