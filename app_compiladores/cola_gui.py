import tkinter as tk
from tkinter import messagebox, filedialog
import platform
import os

# --------- LÓGICA DE COLA ---------
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def frente(self):
        return self.items[0] if not self.esta_vacia() else None

    def final(self):
        return self.items[-1] if not self.esta_vacia() else None

    def mostrar(self):
        return self.items

# --------- SONIDO ---------
def reproducir_sonido():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(800, 200)
    else:
        os.system('printf "\\a"')

# --------- INTERFAZ GRÁFICA ---------
class AplicacionCola:
    def __init__(self, root):
        self.root = root
        self.root.title("Colas - GUI Pro")
        self.cola = Cola()

        self.colores()
        self.crear_widgets()
        self.actualizar_visual()

    def colores(self):
        self.bg_color = "#1e1e1e"
        self.fg_color = "#ffffff"
        self.accent_color = "#4caf50"
        self.entry_bg = "#2d2d2d"
        self.btn_bg = "#333333"

        self.root.configure(bg=self.bg_color)

    def crear_widgets(self):
        tk.Label(self.root, text="Elemento:", fg=self.fg_color, bg=self.bg_color).grid(row=0, column=0)
        self.entry_item = tk.Entry(self.root, bg=self.entry_bg, fg=self.fg_color)
        self.entry_item.grid(row=0, column=1)

        tk.Button(self.root, text="Encolar", command=self.encolar, bg=self.btn_bg, fg=self.fg_color).grid(row=1, column=0)
        tk.Button(self.root, text="Desencolar", command=self.desencolar, bg=self.btn_bg, fg=self.fg_color).grid(row=1, column=1)
        tk.Button(self.root, text="Ver frente", command=self.ver_frente, bg=self.btn_bg, fg=self.fg_color).grid(row=1, column=2)
        tk.Button(self.root, text="Ver final", command=self.ver_final, bg=self.btn_bg, fg=self.fg_color).grid(row=2, column=0)
        tk.Button(self.root, text="Mostrar cola", command=self.mostrar_cola, bg=self.btn_bg, fg=self.fg_color).grid(row=2, column=1)
        self.visual = tk.Canvas(self.root, width=600, height=100, bg=self.bg_color, highlightthickness=0)
        self.visual.grid(row=3, column=0, columnspan=3, pady=10)

        self.resultado = tk.Text(self.root, width=60, height=10, bg=self.entry_bg, fg=self.fg_color)
        self.resultado.grid(row=4, column=0, columnspan=3, pady=10)

    def encolar(self):
        item = self.entry_item.get()
        if item:
            self.cola.encolar(item)
            self.resultado.insert(tk.END, f"Encolado: {item}\n")
            self.entry_item.delete(0, tk.END)
            self.actualizar_visual()
        else:
            messagebox.showwarning("Dato vacío", "Por favor ingresa un elemento")

    def desencolar(self):
        item = self.cola.desencolar()
        if item is not None:
            self.resultado.insert(tk.END, f"Desencolado: {item}\n")
            reproducir_sonido()
        else:
            self.resultado.insert(tk.END, "La cola está vacía\n")
        self.actualizar_visual()

    def ver_frente(self):
        item = self.cola.frente()
        if item is not None:
            self.resultado.insert(tk.END, f"Frente: {item}\n")
        else:
            self.resultado.insert(tk.END, "La cola está vacía\n")

    def ver_final(self):
        item = self.cola.final()
        if item is not None:
            self.resultado.insert(tk.END, f"Final: {item}\n")
        else:
            self.resultado.insert(tk.END, "La cola está vacía\n")

    def mostrar_cola(self):
        elementos = self.cola.mostrar()
        if elementos:
            self.resultado.insert(tk.END, "Cola (frente → final):\n")
            for e in elementos:
                self.resultado.insert(tk.END, f" - {e}\n")
        else:
            self.resultado.insert(tk.END, "La cola está vacía\n")

    def actualizar_visual(self):
        self.visual.delete("all")
        elementos = self.cola.mostrar()
        x = 10
        for item in elementos:
            self.visual.create_rectangle(x, 30, x+80, 80, fill=self.accent_color)
            self.visual.create_text(x+40, 55, text=str(item), fill="white")
            x += 90

# --------- EJECUCIÓN ---------
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionCola(root)
    root.mainloop()
