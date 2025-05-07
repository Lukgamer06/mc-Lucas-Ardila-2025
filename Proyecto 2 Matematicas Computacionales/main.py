import tkinter as tk
from tkinter import messagebox
from regresion import realizar_regresion
from graficador import graficar_resultados

def calcular_regresion():
    try:
        puntos = []
        for i in range(6):
            x = float(entry_x[i].get())
            y = float(entry_y[i].get())
            puntos.append((x, y))
        
        # Separar las coordenadas x e y
        x = [p[0] for p in puntos]
        y = [p[1] for p in puntos]
        
        # Llamar a realizar_regresion con x e y por separado
        resultados = realizar_regresion(x, y)  # resultados es una lista de tuplas (grado, coeficientes, r2)
        
        # Tomar el último resultado (el que cumple con R² >= 0.95)
        grado, coeficientes, r2 = resultados[-1]
        
        # Graficar los resultados
        graficar_resultados(x, y, coeficientes, grado, r2)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
    except IndexError:
        messagebox.showerror("Error", "La función realizar_regresion no devolvió los resultados esperados.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Regresión Polinomial")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="x").grid(row=0, column=0)
tk.Label(frame, text="y").grid(row=0, column=1)

entry_x = []
entry_y = []

for i in range(6):
    tk.Label(frame, text=f"Punto {i+1}").grid(row=i+1, column=0)
    x_entry = tk.Entry(frame)
    y_entry = tk.Entry(frame)
    x_entry.grid(row=i+1, column=1)
    y_entry.grid(row=i+1, column=2)
    entry_x.append(x_entry)
    entry_y.append(y_entry)

btn_calcular = tk.Button(root, text="Calcular Regresión", command=calcular_regresion)
btn_calcular.pack(pady=10)

root.mainloop()