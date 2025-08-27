# gui.py

import tkinter as tk
from tkinter import messagebox
from url_scanner import UrlScanner

class MalwareCheckerGUI:
    """
    Clase para la interfaz gráfica de usuario del verificador de malware.
    """
    def __init__(self, master, scanner: UrlScanner):
        """
        Inicializa la GUI.
        
        Args:
            master: La ventana raíz de tkinter.
            scanner (UrlScanner): Una instancia de la clase UrlScanner.
        """
        self.master = master
        self.scanner = scanner
        master.title("Verificador de Malware de URL")
        master.geometry("500x200")
        master.resizable(False, False)

        self.label = tk.Label(master, text="Introduce la URL a verificar:")
        self.label.pack(pady=10)

        self.url_entry = tk.Entry(master, width=60, font=("Arial", 10))
        self.url_entry.pack(pady=5, padx=10)

        self.check_button = tk.Button(master, text="Verificar Sitio", command=self.perform_check)
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 10, "bold"))
        self.result_label.pack(pady=5)

    def perform_check(self):
        """
        Obtiene la URL del campo de entrada y la verifica.
        """
        url = self.url_entry.get()
        if not url.strip():
            messagebox.showwarning("Entrada Vacía", "Por favor, introduce una URL.")
            return

        # Muestra un mensaje de espera
        self.result_label.config(text="Verificando...", fg="blue")
        self.master.update_idletasks()

        result = self.scanner.check_url(url)
        
        # Actualiza el color del texto según el resultado
        if "¡Peligro!" in result:
            self.result_label.config(text=result, fg="red")
        else:
            self.result_label.config(text=result, fg="green")