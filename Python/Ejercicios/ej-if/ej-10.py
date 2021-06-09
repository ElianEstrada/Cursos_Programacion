nombre = ""
saldo_base = 0.0
no_cuenta = 102535
volver = "s"

while( volver.lower() == "s"):
    print("Bievenidos\n1. Abrir una cuenta\n2. Depositar en una cuenta\n3. Retirar Dinero\n4. Salir")

    opcion = int(input("Ingrese una opción [1-4]: "))

    if (opcion == 1):
        print("\nUsted quiere abrir una cuenta.\n")
        print("No.Cuenta es: " + str(no_cuenta))

        nombre = input("Ingrese su nombre: ")    
        saldo_base = float(input("Ingres su saldo base: "))

        print(nombre + " su número de cuenta es: " + str(no_cuenta) + " y su saldo base es: " + str(saldo_base))

        volver = input("Quiere realizar otra transacción? [S/N]: ")
        
    elif (opcion == 2):
        print("\nUsted quiere depositar dinero a una cuenta")
        cuenta = int(input("Ingrese el número de cuenta: "))

        if (cuenta == no_cuenta):
            dinero_depositado = float(input("Ingrese la cantidad a depositar: "))
            saldo_base = saldo_base + dinero_depositado
        else:
            print("el número de cuenta: " + str(cuenta) + " no existe.")
            
        volver = input("Quiere realizar otra transacción? [S/N]: ")    

    elif (opcion == 3):
        print("\nUsted quiere retirar dinero de una cuenta")
        cuenta = int(input("Ingres el número de cuenta: "))

        if (cuenta == no_cuenta):
            dinero_retirado = float(input("Cuanto dinero quiere retirar"))

            if (dinero_retirado > saldo_base):
                print("Fondos insuficientes")
            else: 
                saldo_base = saldo_base - dinero_retirado
                print("Su saldo disponible es: " + str(saldo_base))

        else: 
            print("El número de cuenta: " + str(cuenta) + " no existe")
        
        volver = input("Quiere realizar otra transacción? [S/N]: ")

    elif (opcion == 4):
        #función exit() -> finaliza el programa
        exit()

    else:
        print("La opcion: " + str(opcion) + " no es valida")
        print("Ingrese una opción valida por favor")
        volver = "s"


