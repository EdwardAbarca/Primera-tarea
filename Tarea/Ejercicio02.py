def ejercicio02():
  print ("Pago mensula del trabajador")
  SueldoPagarSem=0
  HosT=int(input("Ingrese horas trabajadas a la semana: "))
  PxH=int(input("Ingrese el pago por hora: "))
  if HosT>40:
    SueldoPagarSem=40*PxH+(HosT-40)*2*PxH
  else:
    SueldoPagarSem=HosT*PxH
  print ("El sueldo a pagar al trabajador es: ", SueldoPagarSem)
ejercicio02()

