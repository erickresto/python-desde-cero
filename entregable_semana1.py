# Entrada
cliente = input("Nombre del Cliente: ")
monto = float(input("Monto del trato: "))
porcentaje_comision = float(input("Cual es el porcentaje de comision: "))

# Calculos
comision = monto * porcentaje_comision / 100
neto_empresa = monto - comision

# Salida
print("=" * 30)
print(f"{'Reporte':^30}") 
print("=" * 30)
print("Cliente:", cliente)
print(f"Monto: ${monto:,.2f}")
print(f"Comision: ${comision:,.2f}")
print(f"Neto Empresa: ${neto_empresa:,.2f}")