import os
import sys
import subprocess
import configparser
import tkinter as tk
from tkinter import scrolledtext
from pathlib import Path
import shutil
import logging



import fitz  # PyMuPDF
from PIL import Image

# Configuración del log
logging.basicConfig(
    filename="conversion.log",
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PDFtoImageApp:
    def __init__(self, master):
        self.master = master
        master.title("Conversor de PDF a Imágenes (sin Poppler)")

        self.textbox = scrolledtext.ScrolledText(master, width=80, height=20)
        self.textbox.pack(padx=10, pady=10)

        self.boton_iniciar = tk.Button(master, text="Convertir PDFs", command=self.iniciar_conversion)
        self.boton_iniciar.pack(pady=10)

        self.log("Aplicación iniciada correctamente.")

    def log(self, mensaje):
        self.textbox.insert(tk.END, mensaje + "\n")
        self.textbox.see(tk.END)
        self.master.update()
        logging.info(mensaje)

    def log_error(self, mensaje):
        self.textbox.insert(tk.END, "ERROR: " + mensaje + "\n")
        self.textbox.see(tk.END)
        self.master.update()
        logging.error(mensaje)

    def iniciar_conversion(self):
        correctos = 0
        fallidos = 0

        try:
            config = configparser.ConfigParser()
            config.read('config.ini')

            entrada = Path(config['RUTAS']['entrada'])
            salida = Path(config['RUTAS']['salida'])
            carpeta_errores = Path(config['OPCIONES'].get('carpeta_errores', './errores'))

            salida.mkdir(parents=True, exist_ok=True)
            carpeta_errores.mkdir(parents=True, exist_ok=True)

            # Verificación de permisos de escritura
            try:
                test_file = salida / ".test_write"
                with open(test_file, 'w') as f:
                    f.write("test")
                test_file.unlink()
            except Exception as e:
                self.log_error(f"No se puede escribir en la carpeta de salida: {salida}\n{e}")
                return

            formato = config['OPCIONES'].get('formato_salida', 'PNG').upper()
            formatos_validos = ['PNG', 'JPEG', 'JPG', 'TIFF', 'BMP']
            if formato not in formatos_validos:
                self.log_error(f"Formato no válido: {formato}. Se usará PNG por defecto.")
                formato = 'PNG'

            extensiones = {'JPEG': 'jpg', 'JPG': 'jpg', 'PNG': 'png', 'TIFF': 'tiff', 'BMP': 'bmp'}
            extension = extensiones.get(formato, formato.lower())

            pdfs = list(entrada.glob("*.pdf"))
            if not pdfs:
                self.log("No se encontraron archivos PDF en la carpeta de entrada.")
                return

            for pdf in pdfs:
                self.log(f"Procesando: {pdf.name}")
                try:
                    doc = fitz.open(str(pdf))
                    for i, page in enumerate(doc, start=1):
                        pix = page.get_pixmap()
                        nombre_imagen = salida / f"{pdf.stem}_p{i}.{extension}"
                        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                        img.save(nombre_imagen, formato)
                        self.log(f" - Página {i} guardada como {nombre_imagen.name}")
                    doc.close()
                    correctos += 1
                except Exception as e:
                    fallidos += 1
                    self.log_error(f"PDF no procesado: {pdf.name} — {e}")
                    try:
                        destino = carpeta_errores / pdf.name
                        shutil.move(str(pdf), destino)
                        self.log(f"   → Copiado a carpeta de errores: {destino}")
                    except Exception as mover_error:
                        self.log_error(f"No se pudo mover {pdf.name} a 'errores': {mover_error}")
        except Exception as e:
            self.log_error(f"Error general al iniciar la conversión: {e}")

        self.log("Conversión finalizada.")
        self.log(f"Resumen: {correctos} PDF(s) procesados correctamente, {fallidos} con errores.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFtoImageApp(root)
    root.mainloop()
