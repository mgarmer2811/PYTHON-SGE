horas = input("Bro dime cuantas horas has currao\n")
costeHora = input("Ahora dime cuanto te pagan por hora\n")
porcentajeImpuestos = input("Y cual es el porcentaje de impuestos que pagas?{Mete el numero}\n")

porcentajeImpuestos = float(porcentajeImpuestos)
costeHora = float(costeHora)
horas = float(horas)

def sueldoBruto(horas,costeHora):
    return horas * costeHora
    
def impuestos(porcentajeImpuestos,sueldoBruto):
    return (porcentajeImpuestos * sueldoBruto) / 100
    
def sueldoNeto(sueldoBruto,impuestos):
    return sueldoBruto - impuestos

sBruto = sueldoBruto(horas,costeHora)
imp = impuestos(porcentajeImpuestos,sBruto)
sNeto = sueldoNeto(sBruto,imp)

print("Tu sueldo bruto es: ",sBruto)
print("Los impuestos que te corresponden son: ",imp)
print("Finalmente tu sueldo neto es: ",sNeto)