# Convertidor de PDF a Imágenes

Una aplicación en Python que convierte archivos PDF en imágenes utilizando las bibliotecas PyMuPDF (`fitz`) y Pillow (`PIL`). La aplicación incluye una interfaz gráfica de usuario (GUI) construida con Tkinter para facilitar su uso. Además, permite procesar automáticamente todos los archivos PDF en una carpeta definida en la configuración.

## Características
- Convierte páginas de archivos PDF a imágenes.
- Procesa automáticamente todos los archivos PDF en una carpeta configurada.
- Interfaz gráfica amigable con un área de texto desplazable para mostrar mensajes o registros.
- Sistema de registro (logging) para rastrear las actividades de conversión.
- Distribuida como un ejecutable (`main.exe`) para facilitar su uso sin necesidad de instalar Python.

## Requisitos
- Sistema operativo Windows.
- No se requiere instalación de Python ni dependencias adicionales, ya que la aplicación está empaquetada como un ejecutable.

## Instalación
1. Descarga el archivo ZIP desde el repositorio o la página de distribución.
2. Extrae el contenido del archivo ZIP en una carpeta de tu elección.

## Uso
1. Navega a la carpeta donde extrajiste el contenido del ZIP.
2. Ejecuta el archivo `main.exe` haciendo doble clic.
3. La aplicación procesará automáticamente todos los archivos PDF que se encuentren en la carpeta definida en el archivo de configuración (`config`).
4. Los resultados de la conversión se guardarán en la carpeta de salida especificada en la configuración.

### Manejo de errores y éxitos
- Si un archivo PDF se procesa correctamente, se registrará como un éxito en el archivo `conversion.log`.
- Si ocurre un error durante el procesamiento de un archivo, el error también se registrará en `conversion.log` para facilitar la depuración.
- Asegúrate de revisar el archivo `conversion.log` para obtener detalles sobre los archivos procesados y cualquier problema encontrado.

## Registro
Los registros de las conversiones se guardan en el archivo `conversion.log` en la misma carpeta donde se encuentra el ejecutable.
