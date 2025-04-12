import tkinter as tk
from tkinter import messagebox
import math

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar_rec(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar_rec(nodo.der, valor)

    def limpiar(self):
        self.raiz = None

    def recorrido_inorden(self, nodo):
        if nodo is None:
            return []
        return self.recorrido_inorden(nodo.izq) + [nodo] + self.recorrido_inorden(nodo.der)

    def recorrido_preorden(self, nodo):
        if nodo is None:
            return []
        return [nodo] + self.recorrido_preorden(nodo.izq) + self.recorrido_preorden(nodo.der)

    def recorrido_postorden(self, nodo):
        if nodo is None:
            return []
        return self.recorrido_postorden(nodo.izq) + self.recorrido_postorden(nodo.der) + [nodo]

class AplicacionArbol:
    def __init__(self, root):
        self.root = root
        self.root.title("Árbol Binario - Recorridos")
        self.arbol = ArbolBinario()
        self.nodos_graficos = {}

        self.bg_color = "#1e1e1e"
        self.fg_color = "#ffffff"
        self.accent_color = "#4caf50"
        self.entry_bg = "#2d2d2d"
        self.btn_bg = "#333333"

        self.root.configure(bg=self.bg_color)
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="Valor:", bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0)
        self.entry_valor = tk.Entry(self.root, bg=self.entry_bg, fg=self.fg_color)
        self.entry_valor.grid(row=0, column=1)

        tk.Button(self.root, text="Insertar nodo", command=self.insertar, bg=self.btn_bg, fg=self.fg_color).grid(row=0, column=2)
        tk.Button(self.root, text="Limpiar árbol", command=self.limpiar_arbol, bg="#ff4444", fg="white").grid(row=0, column=3)

        tk.Button(self.root, text="Inorden", command=lambda: self.animar_recorrido("inorden"), bg=self.btn_bg, fg=self.fg_color).grid(row=1, column=0)
        tk.Button(self.root, text="Preorden", command=lambda: self.animar_recorrido("preorden"), bg=self.btn_bg, fg=self.fg_color).grid(row=1, column=1)
        tk.Button(self.root, text="Postorden", command=lambda: self.animar_recorrido("postorden"), bg=self.btn_bg, fg=self.fg_color).grid(row=1, column=2)

        self.canvas = tk.Canvas(self.root, width=900, height=500, bg=self.bg_color, highlightthickness=0)
        self.canvas.grid(row=2, column=0, columnspan=4, pady=10)

        self.label_recorrido = tk.Label(self.root, text="", bg=self.bg_color, fg=self.fg_color, font=("Arial", 12, "bold"))
        self.label_recorrido.grid(row=3, column=0, columnspan=4, pady=(0, 10))

    def insertar(self):
        try:
            valor = int(self.entry_valor.get())
            self.arbol.insertar(valor)
            self.entry_valor.delete(0, tk.END)
            self.dibujar_arbol()
        except ValueError:
            messagebox.showwarning("Valor inválido", "Ingresa un número entero")

    def limpiar_arbol(self):
        self.arbol.limpiar()
        self.canvas.delete("all")
        self.nodos_graficos = {}
        self.label_recorrido.config(text="")

    def dibujar_arbol(self):
        self.canvas.delete("all")
        self.nodos_graficos = {}
        if self.arbol.raiz:
            self._dibujar_nodo(self.arbol.raiz, 450, 30, 200)

    def _dibujar_nodo(self, nodo, x, y, espacio):
        r = 20
        nodo_id = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.accent_color, outline="")
        text_id = self.canvas.create_text(x, y, text=str(nodo.valor), fill="white")
        self.nodos_graficos[nodo] = (x, y, r, nodo_id, text_id)

        if nodo.izq:
            nuevo_x = x - espacio
            nuevo_y = y + 90
            self.canvas.create_line(x, y + r, nuevo_x, nuevo_y - r, fill=self.fg_color)
            self._dibujar_nodo(nodo.izq, nuevo_x, nuevo_y, espacio // 2)

        if nodo.der:
            nuevo_x = x + espacio
            nuevo_y = y + 90
            self.canvas.create_line(x, y + r, nuevo_x, nuevo_y - r, fill=self.fg_color)
            self._dibujar_nodo(nodo.der, nuevo_x, nuevo_y, espacio // 2)

    def animar_recorrido(self, tipo):
        colores = {
            "inorden": "#2196f3",
            "preorden": "#f44336",
            "postorden": "#ffeb3b"
        }

        if tipo == "inorden":
            recorrido = self.arbol.recorrido_inorden(self.arbol.raiz)
        elif tipo == "preorden":
            recorrido = self.arbol.recorrido_preorden(self.arbol.raiz)
        elif tipo == "postorden":
            recorrido = self.arbol.recorrido_postorden(self.arbol.raiz)
        else:
            recorrido = []

        self.ultimo_tipo = tipo
        self.ultimo_recorrido = recorrido
        color = colores.get(tipo, "#2196f3")
        self.dibujar_arbol()
        self._animar_pasos(recorrido, 0, color)

    def _animar_pasos(self, recorrido, indice, color):
        if indice >= len(recorrido):
            self.mostrar_recorrido()
            return

        nodo = recorrido[indice]
        x, y, r, nodo_id, text_id = self.nodos_graficos[nodo]

        self.canvas.itemconfig(nodo_id, fill=color)
        self.canvas.itemconfig(text_id, fill="black" if color == "#ffeb3b" else "white")

        if indice > 0:
            prev_nodo = recorrido[indice - 1]
            px, py, _, _, _ = self.nodos_graficos[prev_nodo]

            dx = x - px
            dy = y - py
            dist = math.hypot(dx, dy)
            offset = 20

            if dist > 0:
                ux = dx / dist
                uy = dy / dist
                x2 = x - ux * offset
                y2 = y - uy * offset
            else:
                x2, y2 = x, y

            self.canvas.create_line(
                px, py, x2, y2,
                arrow=tk.LAST,
                arrowshape=(16, 20, 8),
                fill=color,
                width=2
            )

            mx = (px + x2) // 2
            my = (py + y2) // 2
            self.canvas.create_text(mx, my - 10, text=str(indice + 1), fill=color, font=("Arial", 10, "bold"))

        self.root.after(1000, lambda: self._animar_pasos(recorrido, indice + 1, color))

    def mostrar_recorrido(self):
        texto = f"{self.ultimo_tipo.capitalize()}: " + " → ".join(str(n.valor) for n in self.ultimo_recorrido)
        self.label_recorrido.config(text=texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionArbol(root)
    root.mainloop()
