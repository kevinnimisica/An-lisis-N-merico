def imprimir(matriz, filas):
    for i in range(filas):
            print(matriz[i])

def divFilaAbajo (matriz, indice):
    for i in range (indice, len(matriz)):
        valor = matriz[i][indice]
        for j in range(indice,len(matriz[i])):
            matriz[i][j] = matriz[i][j]/valor

            
def multiYsum (matriz, indice):
    for i in range(indice+1, len(matriz)):
        for j in range(indice, len(matriz[i])):
            matriz[i][j]+= matriz[indice][j]*(-1)


def divAlRevez(matriz, indice):
    print ("VALOR DE I E INDICE = "+str(indice)+" ")
    for i in range(len(matriz)-1, indice, -1):
        valor = matriz[i][indice]   
        for j in range(len(matriz[i])-1, indice, -1):
            if valor != 0:
                matriz[i][j] = matriz[i][j]/valor 


def main():

    print ("METODO DE GAUSS-JORDAN\n")
    filas = 3
    columnas = 4
    matrisinia = []
    for i in range (filas):
        matrisinia.append([])
        for j in range(columnas):
            if j == 3:
                matrisinia[i].append(2*i+1)
            else:
                matrisinia[i].append(i+1/(i+1+j+1))
    imprimir(matrisinia, filas)

   
    


    for i in range(filas):
        for j in range (filas):
            if matrisinia[i][0]< matrisinia[j][0]:
                aux = matrisinia[i]
                matrisinia[i] = matrisinia [j]
                matrisinia[j] = aux
    ##print ("Matriz ordenada: ")
    ##imprimir(matrisinia, filas)
    
    for i in range (filas):
        divFilaAbajo(matrisinia,i)
        ##print("MATRIZ DIVIDIDA HACIA ABAJO, DEBE HABER FILA DE UNOS: ")
        ##imprimir(matrisinia, filas)
        multiYsum(matrisinia, i)
        ##print("MULTIPLICACIÓN Y SUMA DE FILAS: ")
        ##imprimir(matrisinia, filas)
        ##print("\n\n\n")
        
    for i in range(filas, -1, -1):
        ##print("VALOR DE I ANTES DELA FUNCION = "+str(i))
        divAlRevez(matrisinia, i)
        ##print("SALE DE LA FUNCION")

    for i in range(0,filas):
        for j in range(i, (columnas -1)):
            if(j != i):
                matrisinia[i][3] = matrisinia[i][3] - matrisinia[i][j]
                matrisinia[i][j] = 0
    print("Solución:")
    imprimir(matrisinia, filas)

            
    
main()