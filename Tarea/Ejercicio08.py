def Ejercicio08():
  print("Calificacion que debe tener")
  calificaciones = ["F","D","C","B","A"]
  calificacion = 0
  nota=int(input("Ingrese la nota: "))
  if nota>=0 and nota<=10:
    if 0<=nota<=5:
      print("\nsu calificacion es calificacion es F")
    elif 6<=nota<=7:
      print("\nsu calificacion es D")
    elif nota==8:
      print("\nsu calificacion es C")
    elif nota==9:
      print("\nsu calificacion es B")
    elif nota==10:
      print("\nsu calificacion es A")
  else:
    print("\nerror, ingrese correctamente las notas")
Ejercicio08()