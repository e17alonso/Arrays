
debitos=[]
creditos=[]
i=0
contcredito=0
contdebito=0
cont=0
print("1. Ingresar debito")
print("2. Ingresar credito")
print("3. Calcular total de debitos")
print("4. Calcular total de creditos")
print("5. Calcular Saldo")
print("6. Calcular promedio de debitos")
print("7. Calcular promedio de creditos")
print("8. Mostrar monto de debitos mas grande")
print("9. Conteo de operaciones de credito y debito")
print("10. Mostrar todos los creditos y debitos")
print("11. Eliminar creditos")
print("12. Salir")  
while i != 12:
    i=int(input("Ingrese la opción a realizar "))
    if i==1:
        debitos.append(int(input("Ingrese el debito ")))
        contdebito=contdebito+1
    if i==2:
        creditos.append(int(input("Ingrese el credito ")))
        contcredito=contcredito+1
    if i==3:
        acu=0
        for j in debitos:
            acu=acu+j
        print(acu)
    if i==4:
        acu=0
        for j in creditos:
            acu=acu+j
        print(acu)
    if i==5:
        acu=0
        for j in creditos:
            acu=acu+j
        for j in debitos:
            acu=acu-j
        print(acu)
    if i==6:
        cont=0
        acu=0
        for j in debitos:
            acu=acu+j
            cont=cont+1
        promedio=acu/cont
        print(promedio)
    if i ==7:
        cont=0
        acu=0
        for j in creditos:
            acu=acu+j
            cont=cont+1
        promedio=acu/cont
        print(promedio)
    if i ==8:
        acu=0
        for j in debitos:
            if j > acu:
                acu=j
        print(acu)
    if i==9:
        print("Conteo de debitos",contdebito)
        print("Conteo de creditos",contcredito)
    if i==10:
        print("Debitos: ")
        for j in debitos:
            print(j)
        print("Creditos: ")
        for j in creditos:
            print(j)
    if i==11:
        creditos.clear()