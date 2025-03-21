#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// Función para calcular el factorial de un número
double factorial(int n) {
    if (n == 0 || n == 1) return 1.0;
    double fact = 1.0;
    for (int i = 2; i <= n; ++i) {
        fact *= i;
    }
    return fact;
}

// Función para calcular la serie de Taylor de e^(-x) alrededor de x0 = 0.8
double SerieTaylor(double x, double x0, int orden) {
    double sum = 0.0;
    for (int n = 0; n <= orden; ++n) {
        double term = (pow(-1, n) * pow(x - x0, n)) / factorial(n);
        sum += term;
    }
    return sum * exp(-x0); // Multiplicamos por e^(-x0) para centrar la serie en x0
}

// Función para calcular el error aproximado relativo porcentual
double errorRelativo(double current, double previous) {
    if (previous == 0.0) return 0.0; // Evitar división por cero
    return fabs((current - previous) / current) * 100.0;
}

int main() {
    double x0 = 0.8; // Punto base
    double x = 0.805; // Punto donde queremos estimar la función
    int maxorden = 15; // Máximo orden de la serie de Taylor

    double previousEstimation = 0.0;
    double currentEstimation = 0.0;

    cout << "Orden\tEstimacion\tError Relativo %" << endl;
    cout << "----------------------------------------" << endl;

    for (int orden = 0; orden <= maxorden; ++orden) {
        currentEstimation = SerieTaylor(x, x0, orden);
        double error = errorRelativo(currentEstimation, previousEstimation);

        cout << orden << "\t" << scientific << setprecision(10) << currentEstimation << "\t" << error << endl;

        previousEstimation = currentEstimation;
    }

    return 0;
}
