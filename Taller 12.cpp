#include <iostream>
#include <cmath>

using namespace std;

// Función para calcular la derivada de f(x) = 1.1x^4 - 1.9x^3 + 1.2x^2 - 2x + 4
double derivada_f1(double x) {
    return 4.4 * pow(x, 3) - 5.7 * pow(x, 2) + 2.4 * x - 2;
}

// Función para calcular la derivada de f(x) = cos(x) * ln(2x)
double derivada_f2(double x) {
    return -sin(x) * log(2 * x) + cos(x) / x;
}

int main() {
    // Primer problema
    double x1 = 1.4;
    double delta_x1 = 0.05;
    double error_f1 = derivada_f1(x1) * delta_x1;

    cout << "Error en f(x) para x = 1.4: " << error_f1 << endl;

    // Segundo problema
    double x2 = M_PI / 3;
    double delta_x2 = 0.005;
    double error_f2 = derivada_f2(x2) * delta_x2;

    cout << "Error en f(x) para x = pi/3: " << error_f2 << endl;

    return 0;
}
