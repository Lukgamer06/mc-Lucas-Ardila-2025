#include <iostream>
#include <wchar.h>
#include <locale.h>
#include <cstdlib>

using namespace std;
//Variables
int opcion;
int rta;
//Funcion para limpiar terminal
void clearScreen() {
    #ifdef _WIN32
        system("cls");  // Comando para Windows
    #elif __linux__
        system("clear");  // Comando para Linux
    #else
        std::cout << "Sistema operativo no compatible para limpiar la pantalla." << std::endl;
    #endif
}

int main()
{
    setlocale(LC_ALL,"");
    do
    {
        //Menu
        cout<<"Bienvenido"<<endl;
        cout<<"Que Ejercicio del taller quieres ver?"<<endl;
        cout<<"1. Ejercicio 1"<<endl;
        cout<<"2. Ejercicio 2"<<endl;
        cout<<"3. Ejercicio 3"<<endl;
        cout<<"4. Ejercicio 4"<<endl;
        cout<<"5. Ejercicio 5"<<endl;
        cout<<"6. Salir"<<endl;
        cin>>opcion;
        clearScreen();
        switch(opcion){
            //Ejercicio 1
            case 1:
            cout<<"La fabrica de automoviles Summer fabrica su popular modelo Sunshine en 3 colores, 5 líneas, 3 tipos de transmision y 2 cilindrajes diferentes."<<endl;
            rta=0;

            cout<<"a. Cuantos tipos diferentes de vehiculos se pueden fabricar?"<<endl;
            rta=0;
            rta=3*5*3*2;
            cout<<"RTA: " << rta << endl;

            cout<<"b. Si ahora se ofrecen en 10 colores diferentes, cuantos tipos se tendran ahora?"<<endl;
            rta=0;
            rta=10*5*3*2;
            cout<<"RTA: "<< rta << endl;
            system("PAUSE");
            break;

            //Ejercicio 2
            case 2:
            cout<<"Las placas de automoviles en Colombia contienen 3 letras seguidas de tres numeros. Entre las letras no se incluye la N."<<endl;
            rta=0;

            cout<<"a. Cuantas placas de automovil diferentes existen?"<<endl;
            rta=0;
            rta=26*26*26*10*10*10;
            cout<<"RTA: "<< rta << endl;

            cout<<"b. Cuantas se podrian hacer si no se aceptan repeticiones de letras o numeros?"<<endl;
            rta=0;
            rta=26*25*24*10*9*8;
            cout<<"RTA: "<< rta << endl;
            system("PAUSE");
            break;

            //Ejercicio 3
            case 3:
            cout<<"De cuantas maneras se puede seleccionar el presidente, vicepresidente, secretario y tesorero de un grupo de 10 personas?"<<endl;
            rta=0;
            rta=10*9*8*7;
            cout<<"RTA: "<< rta << endl;
            system("PAUSE");
            break;

            //Ejercicio 4
            case 4:
            cout<<"Cuantas cadenas de 16 bits comienzan y terminan con numeros 00? Ejemplos: 0010110000101100, 0001010000010100, 0011000000110000"<<endl;
            rta=0;
            rta=1*1*2*2*2*2*2*2*2*2*2*2*2*2*1*1;
            cout<<"RTA: "<< rta << endl;
            system("PAUSE");
            break;

            //Ejercicio 5
            case 5:
            cout<<"Un coleccionista de libros antiguos desea ubicar sus 9 libros mas preciados en una vitrina antirrobos, uno al lado del otro. 4 de los libros estan escritos en griego y los 5 restantes en latin. Cada uno de los libros es diferente de los demas."<<endl;
            rta=0;

            cout<<"a. De cuantas formas se pueden ubicar los libros en la vitrina?"<<endl;
            rta=0;
            rta=9*8*7*6*5*4*3*2*1;
            cout<<"RTA: "<< rta << endl;

            cout<<"b. De cuantas formas se pueden ubicar si todos los libros en latin deben estar uno al lado del otro?"<<endl;
            rta=0;
            rta=5*4*3*2*1;
            cout<<"RTA: "<< rta<<endl;

            cout<<"c. Si desea alternar los libros (latin, griego, latin, griego, etc.), de cuantas formas se pueden ubicar ahora?"<<endl;
            rta=0;
            rta=(5*4*3*2*1)*(4*3*2*1);
            cout<<"RTA: "<< rta << endl;
            system("PAUSE");
            break;
        }
        if (opcion == 6){
            cout<<"Gracias por utilizar el programa"<<endl;
            break;
        }
    } while (true);
    
    return 0;
}
