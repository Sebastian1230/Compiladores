import tkinter as tk
from tkinter import messagebox

# --------- LÓGICA DE PILA ---------
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def mostrar(self):
        return self.items[::-1]  # Se muestra de arriba hacia abajo

# --------- INTERFAZ GRÁFICA ---------
class AplicacionPila:
    def __init__(self, root):
        self.root = root
        self.root.title("Pilas - GUI")
        self.pila = Pila()

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="Elemento:").grid(row=0, column=0)
        self.entry_item = tk.Entry(self.root)
        self.entry_item.grid(row=0, column=1)

        tk.Button(self.root, text="Apilar (Push)", command=self.apilar).grid(row=1, column=0)
        tk.Button(self.root, text="Desapilar (Pop)", command=self.desapilar).grid(row=1, column=1)
        tk.Button(self.root, text="Ver tope", command=self.ver_tope).grid(row=1, column=2)
        tk.Button(self.root, text="Mostrar pila", command=self.mostrar_pila).grid(row=2, column=0, columnspan=3)

        self.resultado = tk.Text(self.root, width=40, height=10)
        self.resultado.grid(row=3, column=0, columnspan=3)

    def apilar(self):
        item = self.entry_item.get()
        if item:
            self.pila.apilar(item)
            self.resultado.insert(tk.END, f"Apilado: {item}\n")
            self.entry_item.delete(0, tk.END)
        else:
            messagebox.showwarning("Dato vacío", "Por favor ingresa un elemento")

    def desapilar(self):
        item = self.pila.desapilar()
        if item is not None:
            self.resultado.insert(tk.END, f"Desapilado: {item}\n")
        else:
            self.resultado.insert(tk.END, "La pila está vacía\n")

    def ver_tope(self):
        item = self.pila.ver_tope()
        if item is not None:
            self.resultado.insert(tk.END, f"Tope de la pila: {item}\n")
        else:
            self.resultado.insert(tk.END, "La pila está vacía\n")

    def mostrar_pila(self):
        elementos = self.pila.mostrar()
        if elementos:
            self.resultado.insert(tk.END, "Pila (tope abajo):\n")
            for e in elementos:
                self.resultado.insert(tk.END, f" - {e}\n")
        else:
            self.resultado.insert(tk.END, "La pila está vacía\n")

# --------- EJECUCIÓN ---------
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionPila(root)
    root.mainloop()
