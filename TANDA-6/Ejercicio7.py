import json

with open('empleados.json', 'r') as archivo:
    empleados = json.load(archivo)

departamentos = {}

for empleado in empleados:
    departamento = empleado['departamento']
    salario = empleado['salario']
    
    if departamento not in departamentos:
        departamentos[departamento] = {'suma_salarios': 0, 'conteo': 0}
    
    departamentos[departamento]['suma_salarios'] += salario
    departamentos[departamento]['conteo'] += 1

resumen = {}
for departamento, datos in departamentos.items():
    salario_medio = datos['suma_salarios'] / datos['conteo']
    resumen[departamento] = salario_medio

with open('resumen_departamentos.json', 'w') as archivo_resumen:
    json.dump(resumen, archivo_resumen, indent=4)

print("El resumen ha sido guardado en 'resumen_departamentos.json'.")