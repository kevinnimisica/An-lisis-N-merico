#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

float evaluar(float numero);
float nSeccion(float limteInf, float limiteSup, int particiones);

int main()
{
	int particiones;
	float limiteInf, limiteSup, raiz;
	cout<<"\nIngrese el limite inferior: ";
	cin>>limiteInf;
	cout<<"\nIngrese el limite superior: ";
	cin>>limiteSup;
	cout<<"\nIngrese el numero de particiones; ";
	cin>>particiones;
	if(evaluar(limiteInf)*evaluar(limiteSup) > 0)
		cout<<"\nNo hay raiz en el intervalo";
	else
		raiz = nSeccion(limiteInf, limiteSup, particiones);
	cout<<"La raiz es: "<<raiz;
	return 0;
	
}

float evaluar(float numero)
{
	float resultado = (9.8*68.1)*(1-pow(2.71828182846,-(numero/68.1))-40);
	return resultado;
}

float nSeccion(float limteInf, float limiteSup, int paticiones)
{
	float particion = (limiteInf + limiteSup)/particiones;
	for(int i = 1; i <= particiones; i++)
	{
		if(evaluar(particion)== 0)
			return particion;
		if(evaluar(i*particion) * evaluar((i+1)*particion) < 0 )
			return nSeccion(i*particion, (i+1)*particion, particiones);
	} 
}