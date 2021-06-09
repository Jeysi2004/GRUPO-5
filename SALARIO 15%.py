nombre= input("Ingrese su nombre:")
horash= int(input("Ingreese sus horas de trabajo: "))
salarioh= int(input("Ingrese el salario por hora: "))


print(f"su nombre es {nombre}, su tiempo laboral es de {horash} horas, y su salario por hora es de {salarioh} soles" )

sueldo= (horash * salarioh)
print(f"Su sueldo final es de {sueldo} soles")

incremento= sueldo *0.15
dinero_final = sueldo + incremento
print(f"su sueldo incrementado es de {dinero_final:.2f} soles")
