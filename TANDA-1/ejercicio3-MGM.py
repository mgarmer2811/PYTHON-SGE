texto = 'Sistemas de Gestion Empresarial'

print('Primera palabra:',texto.split()[0])
print('Segunda palabra:',texto.split()[1])
print('Texto en mayusculas:',texto.upper())
print('Texto sin espacios: ',(texto.replace(' ','')))
print(len(texto.split()[0]),' ',len(texto.split()[1]),' ',len(texto),' ',len(texto.split()))
