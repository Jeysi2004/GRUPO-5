precio= input("PRECIOS UNITARIOS: \n 1-Rock=63.00"
                 "\n 4-Salsa=56.00"
                 "\n 3-Pop=87.00"
                 "\n 5-Folclore=120.50")
marca=input("Compra(Salsa, Rock, Pop, Folclore): ")
costo=float(input("Precio Unitario: "))
cant=int(input("Cantidad de discos: "))


if cant==4:
    if marca=="Salsa" or "Folclore" or "Pop" or "Rock":
        xdes=costo*cant-(costo*0.06)
        print("Recibe un descuento de 6%, el TOTAL a pagar es:",xdes)

elif marca== "Pop":
    if cant>=6 and cant<=10:
        fdes=costo*cant-(costo*0.08)
        print ("Recibe un descuento de 8%, de obsequio un POSTER y el TOTAL a pagar es: ",fdes)
    elif cant>10:
        gdes=costo*cant-(costo*0.102)
        print("Recibe un descuento de 10.2%, de obsequio un POSTER y el TOTAL a pagar es: ",gdes)

elif marca== "Rock":
    if cant>=6 and cant<=10:
        cdes=costo*cant-(costo*0.08)
        print ("Recibe un descuento de 8%, de obsequio un POSTER y el TOTAL a pagar es: ",cdes)
    elif cant>10:
        ggdes=costo*cant-(costo*0.102)
        print("Recibe un descuento de 10.2%, de obsequio un POSTER y el TOTAL a pagar es: ",ggdes)

    
elif cant>=5 and cant<10:
    if marca=="Salsa" or "Folclore":
        xxdes=costo*cant-(costo*0.08)
        print("Recibe un descuento de 8%, el TOTAL a pagar es:",xxdes)


elif cant>10:
    if marca=="Salsa" or "Folclore":
        ffdes=costo*cant-(costo*0.102)
        print("Recibe un descuento de 10%, el TOTAL a pagar es:",ffdes)



    








    

    
     


