#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <algorithm>

using namespace std;

class Nodo {
  public:
      int valor;
      Nodo* izquierdo;
      Nodo* derecho;

      Nodo(int val) : valor(val), izquierdo(nullptr), derecho(nullptr) {}
};

class ArbolBinario {
  private:
      Nodo* raiz;

      void agregarValorRecursivo(int valor, Nodo*& nodo) {
          if (nodo == nullptr) {
              nodo = new Nodo(valor);
          } else if (valor < nodo -> valor) {
              agregarValorRecursivo(valor, nodo -> izquierdo);
          } else if (valor > nodo -> valor) {
              agregarValorRecursivo(valor, nodo -> derecho);
          }
      }

    bool buscarValorRecursivo(int valor, Nodo* nodo) const {
        if (nodo == nullptr) {
            return false;
        }
        if (valor == nodo -> valor) {
            return true;
        } else if (valor < nodo -> valor) {
            return buscarValorRecursivo(valor, nodo->izquierdo);
        } else {
            return buscarValorRecursivo(valor, nodoz->derecho);
        }
    }

    void imprimirEnOrdenRecursivo(Nodo* nodo) const {
        if (nodo != nullptr) {
            imprimirEnOrdenRecursivo(nodo->izquierdo);
            cout << nodo->valor << " ";
            imprimirEnOrdenRecursivo(nodo->derecho);
        }
    }

    void liberarArbol(Nodo* nodo) {
        if (nodo != nullptr) {
            liberarArbol(nodo->izquierdo);
            liberarArbol(nodo->derecho);
            delete nodo;
        }
    }

public:
    ArbolBinario() : raiz(nullptr) {}

    ~ArbolBinario() {
        liberarArbol(raiz);
    }

    void agregarValor(int valor) {
        agregarValorRecursivo(valor, raiz);
    }

    bool buscarValor(int valor) const {
        return buscarValorRecursivo(valor, raiz);
    }

    void imprimirValores() const {
        imprimirEnOrdenRecursivo(raiz);
        cout << endl;
    }
};

vector<int> generarNumerosUnicos(int cantidad, int min, int max) {
    vector<int> numeros;
    for (int i = min; i <= max; ++i) {
        numeros.push_back(i);
    }
    random_shuffle(numeros.begin(), numeros.end());
    numeros.resize(cantidad);
    return numeros;
}

int main() {
    srand(time(nullptr)); // Inicializar semilla para números aleatorios

    // Generar 20 números aleatorios únicos entre 1 y 100
    vector<int> numeros = generarNumerosUnicos(20, 1, 100);
    cout << "Numeros generados: ";
    for (int num : numeros) {
        cout << num << " ";
    }
    cout << endl;

    // Crear el árbol binario de búsqueda
    ArbolBinario arbol;
    for (int num : numeros) {
        arbol.agregarValor(num);
    }

    // Menú interactivo
    while (true) {
        cout << "\n--- Menu ---\n";
        cout << "1. Buscar un numero en el arbol\n";
        cout << "2. Imprimir los numeros en orden ascendente\n";
        cout << "3. Salir\n";
        cout << "Seleccione una opcion: ";

        int opcion;
        cin >> opcion;

        if (cin.fail()) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Por favor ingrese un numero valido.\n";
            continue;
        }

        switch (opcion) {
            case 1: {
                int numBuscar;
                cout << "Ingrese el numero a buscar: ";
                cin >> numBuscar;
                if (cin.fail()) {
                    cin.clear();
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    cout << "Por favor ingrese un numero valido.\n";
                } else {
                    if (arbol.buscarValor(numBuscar)) {
                        cout << "El numero " << numBuscar << " SI esta en el arbol.\n";
                    } else {
                        cout << "El numero " << numBuscar << " NO esta en el arbol.\n";
                    }
                }
                break;
            }
            case 2:
                cout << "Numeros en orden ascendente:\n";
                arbol.imprimirValores();
                break;
            case 3:
                cout << "Saliendo del programa...\n";
                return 0;
            default:
                cout << "Opcion no valida. Por favor seleccione 1, 2 o 3.\n";
        }
    }

    return 0;
}
