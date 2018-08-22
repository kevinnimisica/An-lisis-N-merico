def imprimir(matriz, filas):
    for i in range(filas):
            print(matriz[i])

def main():
    numero = int (input("Ingrese el numero de filas y columnas de las matrices: "))
    matriz1 = []
    for i in range (numero):    
        matriz1.append([])
        for j in range(numero):
            matriz1[i].append(int(input("Ingrese el dato en la posición "+str(i)+","+str(j)+" de la matriz 1: ")))
    matriz2 = []
    for i in range (numero):
        matriz2.append([])
        for j in range(numero):
            matriz2[i].append(int(input("Ingrese el dato en la posición "+str(i)+","+str(j)+" de la matriz 2: ")))
    print("Matriz 1: ")
    imprimir(matriz1, numero)
    print("Matriz 2: ")
    imprimir(matriz2, numero)
    for i in range (numero):
        for j in range(numero):
            matriz2[i][j] = matriz1[i][j] + matriz2[i][j]
    print("Matriz 1 + Matriz 2: ")
    imprimir(matriz2, numero)
main()