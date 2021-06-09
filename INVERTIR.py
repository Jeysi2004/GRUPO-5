persona1=int(input("Ingrese la Primera inversión: "))
persona2=int(input("Ingrese la Segunda inversión : "))
persona3=int(input("Ingrese la Tercera inversión: "))

sumatoria= (persona1+persona2+persona3)
print("La cantidad total sumada de dinero es: "+str(sumatoria))

print("La primera persona invirtio: "+str((persona1/sumatoria)*100)+" %")
print("La segunda persona invirtio: "+str((persona2/sumatoria)*100)+" %")
print("La tercera persona invirtio: "+str((persona3/sumatoria)*100)+" %")
