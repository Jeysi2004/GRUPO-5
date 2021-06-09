dni=int(input("Ingrese su número de DNI: "))
cont=len(str(dni))

if cont==8:
    print ("El número ingresado tiene", cont, "digitos")
else:
    print ("El número ingresado no tiene 8 dígitos")
    
