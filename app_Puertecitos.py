import tkinter as tk
from tkinter import ttk
import random
import threading
import time

class DataSimulator(threading.Thread):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
        self._is_running = True

    def run(self):
        while self._is_running:
            # Simular datos de corriente y voltaje
            current = round(random.uniform(0, 10), 2)  # Simular corriente en Amperios
            voltage = round(random.uniform(0, 5), 2)   # Simular voltaje en Voltios

            # Crear una cadena de datos simulados
            data = f"Corriente: {current} A, Voltaje: {voltage} V"
            self.text_widget.insert(tk.END, data + '\n')
            self.text_widget.yview(tk.END)

            # Esperar un segundo antes de generar nuevos datos
            time.sleep(1)

    def stop(self):
        self._is_running = False

def on_closing():
    data_simulator.stop()
    root.destroy()

root = tk.Tk()
root.title("Sistema de Monitoreo Simulado")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Datos del Sensor:")
label.grid(row=0, column=0, sticky=(tk.W, tk.E))

text_box = tk.Text(frame, height=20, width=50)
text_box.grid(row=1, column=0, sticky=(tk.W, tk.E))

data_simulator = DataSimulator(text_box)
data_simulator.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()


