import math

def funcion1(numero):
    return math.log1p(numero + 2)

def funcion2(numero):
    return math.sin(numero)

def main():
    print ("El punto inicial del intervalo es: -2 ")
    print ("El punto final del intervalo es: -1 ")
    error = (-2-1.6314459)/-1.6314459
    resultado1 = -2
    resultado = -2.0000001
    while error > 10**-7:
        aux = resultado
        resultado = resultado1- funcion2(resultado1)*((resultado-resultado1)/ funcion2(resultado)-funcion2(resultado1))
        resultado1 = aux
        error = (resultado - 1.6314459)
    print ("El resultado es: " + str(resultado))
    print ("El error es: " + str(error))
    print("El intervalo fue escogido gráficamente y el resultado que se considera exacto fue traído de una calculadora online.")
    print("El resultado que se considera exacto es: -1.6314459" )

main()