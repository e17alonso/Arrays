prendas=[['Bufanda',1,25],['Lentes',2,20],['Botas',3,100],['Pantalon',4,150],['Sueter',5,125]]
pagos=[]
compras=[]
deuda=0
contcom=0
contpag=0
caro=0
cont=0
print("1. Ingresar items de compra")
print("2. Ingresar pagos")
print("3. Mostrar recibo de compra")
print("4. Mostrar total de pagos")
print("5. Mostrar saldo pendiente a pagar")
print("6. Mostrar promedio de precios")
print("7. Mostrar producto mas caro")
print("8. Mostrar recibo de compra con pagos")
opcion=0
while opcion != 8:
    opcion=int(input("Ingrese la opcion a realizar"))
    if opcion==1:
        id=int(input("Ingrese el ID del producto"))
        for i in range(len(prendas)):
            if prendas[i][1]==id:
                deuda=deuda+prendas[i][2]
                contcom=contcom+1
                compras.append(prendas[i][0])
                if prendas[i][2]> caro:
                    caro=prendas[i][2]
                print("Producto añadido exitosamente")
    if opcion==2:
        pago=int(input("Ingrese el dinero a pagar"))
        pagos.append(pago)
        contpag=contpag+1
        cont=cont+pago
        if cont>deuda:
            print("Deuda saldada")
    if opcion==3:
        print("Los items comprados son ")
        print(compras)
        print("El total a pagar es ",deuda)
    if opcion==4:
        print("Los pagos hechos son ", pagos)
    if opcion==5:
        print("El saldo a pagar es de ", deuda-cont)
    if opcion==6:
        print("El promedio es de ", deuda/contcom)
    if opcion==7:
        print("El precio del producto mas caro es ", caro)
    if opcion==8:
        print("Los items comprados son ",compras)
        print("El total a pagar es ",deuda)
        print("Los pagos hechos son", pagos)
