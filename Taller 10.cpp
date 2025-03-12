#include <iostream>
#include <cmath>

using namespace std;

// Definición de la función 1
double f1(double x) {
    return 0.3 * pow(x, 3) - 1.8 * pow(x, 2) + 2.5 * x - 1;
}
// Derivada de la función
double f1_prima(double x) {
    return 0.9 * pow(x, 2) - 3.6 * x + 2.5;
}
double f1_doble_prima(double x) {
    return 1.8 * x - 3.6;
}
double f1_triple_prima() {
    return 1.8;
}

// Definición de la función 2
double f2(double x) {
    return 1.4 * exp(x) - 3.2 * x + 2.4;
}
double f2_prima(double x) {
    return 1.4 * exp(x) - 3.2;
}
double f2_doble_prima(double x) {
    return 1.4 * exp(x);
}
double f2_triple_prima(double x) {
    return 1.4 * exp(x);
}



int main() {
    bool l=true;                
    double x0;
    double a;  
    double f_x0;
    double f_prima_x0;
    double f_doble_prima_x0;
    double f_triple_prima_x0;
    double serie_taylor;
    do{
        
        cout<<"Bienvenido"<<endl;
        cout<<"Que Ejercicio quieres ver?"<<endl;
        cout<<"1. Ejercicio 1"<<endl;
        cout<<"2. Ejercicio 2"<<endl;
        cout<<"3. Cerrar"<<endl;
        int opcion;
        cin>>opcion;
        switch(opcion){
            case 1:
                cout<<"Ejercicio 1"<<endl;
                x0 = 0.4;
                a = 0.5;  
                f_x0 = f1(x0);
                f_prima_x0 = f1_prima(x0);
                f_doble_prima_x0 = f1_doble_prima(x0);
                f_triple_prima_x0 = f1_triple_prima();
                // Expansión de la serie de Taylor
                serie_taylor = f_x0 + f_prima_x0 * (a - x0) + (f_doble_prima_x0 / 2) * pow(a - x0, 2)  + (f_triple_prima_x0 / 6) * pow(a - x0, 3);
                cout << "El valor predicho de f(0.5) usando la expansion de la serie de Taylor es: " << serie_taylor << endl;
                system("PAUSE");
                break;
            case 2:
                cout<<"Ejercicio 2"<<endl;
                x0 = 0.6;
                a = 0.65;  
                f_x0 = f2(x0);
                f_prima_x0 = f2_prima(x0);
                f_doble_prima_x0 = f2_doble_prima(x0);
                f_triple_prima_x0 = f2_triple_prima(x0);
                // Expansión de la serie de Taylor
                serie_taylor = f_x0 + f_prima_x0 * (a - x0) + (f_doble_prima_x0 / 2) * pow(a - x0, 2)  + (f_triple_prima_x0 / 6) * pow(a - x0, 3);
                cout << "El valor predicho de f(0.5) usando la expansion de la serie de Taylor es: " << serie_taylor << endl;
                system("PAUSE");
                break;
            default:
            cout<<"Adios"<<endl;
            system("PAUSE");
            l=false;
            break;
        }
    } while (l);
    return 0;
    }
