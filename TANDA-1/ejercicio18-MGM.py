diccionario = {
    'numeros' : list(range(1,6))
}

diccionario.get('numeros').append(7)
diccionario.get('numeros')[0] = 0

print('Contenido diccionario: ',diccionario.get('numeros'))