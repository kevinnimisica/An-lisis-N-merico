#include <bits/stdc++.h> 
using namespace std;

double funcion(double x);
double biseccion(double a,double b,int it,double tolerancia);
int main () { 
    
    int a, b;
    cout<<"Ingrese el intervalo [a,b]"<<endl;
    cout<<"a:"<<endl;
    cin>>a;
    cout<<"b:"<<endl;
    cin>>b;
    cout<<"Con una tolerancia de 0.01 se encuentra la maxima raiz aproximada en:"<< biseccion(a,b,100,0.01); 
    return 0; 
}
double funcion(double x){     
    return cos(3*x) + exp(x);
} 
double biseccion(double a,double b,int it,double tolerancia){ 
    int cont=1; 
    double c; 
    double fc; 
    while(cont<it){ 
        c=(a+b)/2; 
        fc=funcion(c); 
        if(abs(b-a)<tolerancia) 
            return c; 
        if(funcion(a)*fc<0) 
            b=c; 
        if(fc*funcion(b)<0) 
            a=c; 
        cont=cont+1;
    } 
    return c;
} 
