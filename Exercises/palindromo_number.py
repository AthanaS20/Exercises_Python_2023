# a cada sequencia de 10 numeros temos um num palindromo
x = 121

lista = []
cont = 11

while cont <= 100:
    lista.append(cont)
    cont += 11
    
print(lista)

if x in lista:
    print(True)

elif x >= 0 and x <= 9:
    print(True)
    
else:
    print(False)


    
   

