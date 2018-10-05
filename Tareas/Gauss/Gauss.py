
def imprimir(matriz, filas):
    for i in range(filas):
            print(matriz[i])


def main():

    print ("METODO DE GAUSS-JORDAN\n")
    filas = int(input("Ingrese el numero de filas de la matriz: "))
    columnas = int (input("Ingrese el numero de columnas de la matriz: "))
    matrisinia = []
    a = ""
    if filas < columnas:
        print("El sistema no tiene solución.")
        return 0
    for i in range (filas):
        matrisinia.append([])
        for j in range(columnas):
            matrisinia[i].append(int(input("Ingrese el dato en la posición "+str(i)+","+str(j)+": ")))
    if(filas == columnas):
        for i in range (filas):
            matrisinia[i].append(0)

    imprimir(matrisinia, filas)

    print ("Matriz Triagular Inferior: ")
    for k in range (0, filas):
        valor = matrisinia[k][k]
        for i in range (k, filas):
            for j in range (k,columnas):
                if(k!= i):
                    aux = -valor/matrisinia[i][k]
                    dato = matrisinia[i][j]
                    matrisinia[i][j] = -valor/matrisinia[i][k] + matrisinia[i][j]
                else:
                    break
    imprimir(matrisinia, filas)
    
main()
    
