def KeysAndValues(Objeto):
    matriz1= []
    matriz2 =[]
    bandera = 0 
    for indice in diccionario:
        if(len(matriz1)==0): #Si es el primer valor que se ingresa, solo debe agregarlo a ambas matrices
            matriz1.append(indice)
            matriz2.append(diccionario[indice])
    
        else:
            for iterador in range(len(matriz1)):
                if(matriz1[iterador]>indice): #Si el elemento de la matriz (la cadena) es "mayor" alfabeticamente que el que está ingresando
                    matriz1.insert(iterador,indice) #insertara el valor que ingresa en su posición y al hacer esto se correra en la matriz automaticamente
                    matriz2.insert(iterador,diccionario[indice]) #Lo mismo sucede en la otra matriz
                    bandera = 0
                    break
                else:
                    bandera =1

        if(bandera==1): #Si el valor ingresado es mayor que todos los  que hay en la matriz se agrega al final 
            matriz1.append(indice)
            matriz2.append(diccionario[indice])

    print(matriz1)
    print(matriz2)

diccionario = {'Key4':"Dior", 'Key1':"Apple", 'Key5':"Esika", 'Key2':"Bimbo",'Key3':"Calvin Klein" }

KeysAndValues(diccionario)

