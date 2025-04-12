import tkinter as tk
from tkinter import messagebox

# --------- ESTRUCTURAS DE DATOS ---------
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return elementos

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def eliminar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def mostrar_adelante(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return elementos

    def mostrar_atras(self):
        elementos = []
        actual = self.cola
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.anterior
        return elementos

# --------- INTERFAZ GRÁFICA ---------
class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Listas Enlazadas - GUI")
        self.es_doble = tk.BooleanVar()
        self.lista = ListaSimple()

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="Dato:").grid(row=0, column=0)
        self.entry_dato = tk.Entry(self.root)
        self.entry_dato.grid(row=0, column=1)

        tk.Checkbutton(self.root, text="Lista doble", variable=self.es_doble, command=self.cambiar_lista).grid(row=0, column=2)

        tk.Button(self.root, text="Insertar al inicio", command=self.insertar_inicio).grid(row=1, column=0)
        tk.Button(self.root, text="Insertar al final", command=self.insertar_final).grid(row=1, column=1)
        tk.Button(self.root, text="Eliminar", command=self.eliminar).grid(row=1, column=2)

        tk.Button(self.root, text="Mostrar", command=self.mostrar).grid(row=2, column=0)
        self.btn_atras = tk.Button(self.root, text="Mostrar atrás", command=self.mostrar_atras, state=tk.DISABLED)
        self.btn_atras.grid(row=2, column=1)

        self.resultado = tk.Text(self.root, width=40, height=10)
        self.resultado.grid(row=3, column=0, columnspan=3)

    def cambiar_lista(self):
        self.lista = ListaDoble() if self.es_doble.get() else ListaSimple()
        estado = tk.NORMAL if self.es_doble.get() else tk.DISABLED
        self.btn_atras.config(state=estado)
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, "Lista cambiada a " + ("doble" if self.es_doble.get() else "simple") + "\n")

    def insertar_inicio(self):
        dato = self.entry_dato.get()
        if dato:
            self.lista.insertar_inicio(dato)
            self.resultado.insert(tk.END, f"Insertado al inicio: {dato}\n")
        else:
            messagebox.showwarning("Dato vacío", "Por favor ingresa un dato")

    def insertar_final(self):
        dato = self.entry_dato.get()
        if dato:
            self.lista.insertar_final(dato)
            self.resultado.insert(tk.END, f"Insertado al final: {dato}\n")
        else:
            messagebox.showwarning("Dato vacío", "Por favor ingresa un dato")

    def eliminar(self):
        dato = self.entry_dato.get()
        if dato:
            eliminado = self.lista.eliminar(dato)
            if eliminado:
                self.resultado.insert(tk.END, f"Eliminado: {dato}\n")
            else:
                self.resultado.insert(tk.END, f"No encontrado: {dato}\n")
        else:
            messagebox.showwarning("Dato vacío", "Por favor ingresa un dato")

    def mostrar(self):
        if self.es_doble.get():
            datos = self.lista.mostrar_adelante()
        else:
            datos = self.lista.mostrar()
        self.resultado.insert(tk.END, "Lista: " + " -> ".join(datos) + "\n")

    def mostrar_atras(self):
        if self.es_doble.get():
            datos = self.lista.mostrar_atras()
            self.resultado.insert(tk.END, "Atrás: " + " <- ".join(datos) + "\n")

# --------- EJECUCIÓN ---------
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
