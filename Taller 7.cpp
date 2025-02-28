#include <iostream>
#include <bitset>
#include <string>

using namespace std;
//Variables iniciales
int Num1;
int Num2;
//Definir la cantidad de bits
const int Bits = 16;
//Funcion para obtener el valor de un binario con la cantidad de bits definida
string ComplementoDos(int n){
    bitset<Bits> bin(n);
    return bin.to_string();
}

int main()
{
    //Menu
    cout << "Bienvenido" << endl;
    do{
        cout << "Inserta un numero (-32768 a 32767): "; cin >> Num1;
        cout << "Inserta otro numero (-32768 a 32767): "; cin >> Num2;
        if (Num1 < -32768 || Num1 > 32767 || Num2 < -32768 || Num2 > 32767){
            cout << "Error, el numero debe estar entre -32768 y 32767" << endl;
        } else{
            break;
        }
    } while (true);
    //Operaciones
    string Bin1 = ComplementoDos(Num1);
    string Bin2 = ComplementoDos(Num2);
    string BinSuma = ComplementoDos(Num1+Num2);
    //Imprimir salida
    cout << "Numero 1 en binario: " << Bin1 << endl;
    cout << "Numero 2 en binario: " << Bin2 << endl;
    cout << "La suma de los dos numeros en binario es: " << BinSuma << endl;
    return 0;
}
