# main.py

import tkinter as tk
from gui import MalwareCheckerGUI
from url_scanner import UrlScanner
from tkinter import messagebox

def main():
    """
    Función principal para configurar y ejecutar la aplicación.
    """
    # --- CONFIGURACIÓN ---
    # Reemplaza "TU_API_KEY" con tu clave real de la API de Google Safe Browsing.
    API_KEY = "Tu Propia API Key" 
    
    try:
        # Inicializa el escáner de URL con la clave
        scanner = UrlScanner(API_KEY)
        
        # Configura la ventana principal de la GUI
        root = tk.Tk()
        app = MalwareCheckerGUI(root, scanner)
        
        # Inicia el bucle de eventos de la aplicación
        root.mainloop()
        
    except ValueError as e:
        # Muestra un error si la API_KEY no es válida y no inicia la GUI
        messagebox.showerror("Error de Configuración", str(e))
    except Exception as e:
        messagebox.showerror("Error Inesperado", f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    main()