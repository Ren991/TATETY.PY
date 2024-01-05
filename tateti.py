import tkinter as tk
from tkinter import messagebox

class TatetiGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tateti")
        self.jugador_actual = "X"
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]

        # Crear botones para las casillas
        self.botones = [[tk.Button(self.root, text=" ", font=("Helvetica", 24), width=5, height=2, command=lambda r=i, c=j: self.hacer_movimiento(r, c)) for j in range(3)] for i in range(3)]

        # Colocar los botones en la cuadrícula
        for i in range(3):
            for j in range(3):
                self.botones[i][j].grid(row=i, column=j)

    def hacer_movimiento(self, fila, columna):
        if self.tablero[fila][columna] == " ":
            self.tablero[fila][columna] = self.jugador_actual
            self.botones[fila][columna].config(text=self.jugador_actual, state=tk.DISABLED)
            
            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"¡El jugador {self.jugador_actual} ha ganado!")
                self.resetear_juego()
            elif all(self.tablero[i][j] != " " for i in range(3) for j in range(3)):
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.resetear_juego()
            else:
                self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def verificar_ganador(self):
        for i in range(3):
            if all(self.tablero[i][j] == self.jugador_actual for j in range(3)) or all(self.tablero[j][i] == self.jugador_actual for j in range(3)):
                return True

        if all(self.tablero[i][i] == self.jugador_actual for i in range(3)) or all(self.tablero[i][2 - i] == self.jugador_actual for i in range(3)):
            return True

        return False

    def resetear_juego(self):
        for i in range(3):
            for j in range(3):
                self.tablero[i][j] = " "
                self.botones[i][j].config(text=" ", state=tk.NORMAL)

        self.jugador_actual = "X"

if __name__ == "__main__":
    juego = TatetiGUI()
    juego.root.mainloop()