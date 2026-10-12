#entrada
cliente = input("Nombre del cliente: ")
monto = float(input("Monto del trato: "))
#calculo
comision = (monto * 0.10)
#salida
print("Cliente:", cliente)
print("Monto: $", monto)
print("Comision: $", comision)