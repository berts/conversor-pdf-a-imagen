# Convertidor de PDF a Imágenes

Aplicación de escritorio en Windows para la conversión de archivos PDF a imágenes, desarrollada en Python y empaquetada como ejecutable autónomo. Utiliza las bibliotecas PyMuPDF (`fitz`) y Pillow (`PIL`), con una interfaz gráfica basada en Tkinter.

## Funcionalidades principales

- Conversión automática de todas las páginas de archivos PDF a imágenes.
- Procesamiento en lote de todos los documentos ubicados en una carpeta definida por el usuario.
- Interfaz gráfica con área de registros en tiempo real.
- Registro detallado de actividad (`conversion.log`), con información sobre archivos procesados y errores detectados.
- Compatible con formatos de imagen comunes: PNG, JPG, TIFF, BMP, entre otros.
- No requiere instalación de Python ni dependencias en el equipo del usuario final.

## Requisitos del sistema

- Sistema operativo: Windows 10 o superior.
- No se requiere instalación previa de Python ni bibliotecas externas.  
  La aplicación se distribuye como ejecutable (`main.exe`) listo para su uso.

## Instalación

1. Descargue el archivo `.zip` desde el sitio de distribución.
2. Extraiga el contenido en una carpeta de su elección.
3. Asegúrese de contar con permisos de escritura en la carpeta de salida definida en el archivo `config.ini`.

## Uso

1. Ejecute `main.exe` mediante doble clic.
2. La aplicación leerá automáticamente el archivo `config.ini`, que debe contener al menos las siguientes rutas:
   ```
   [RUTAS]
   entrada = ./pdfs
   salida = ./imagenes

   [OPCIONES]
   formato_salida = PNG
   carpeta_errores = ./errores
   ```
3. Todos los archivos PDF ubicados en la carpeta definida en `entrada` serán procesados automáticamente.
4. Las imágenes generadas se guardarán en la ruta definida en `salida`.  
   Los archivos que no puedan ser procesados serán movidos a `carpeta_errores`.

## Gestión de errores

- Los errores de conversión se registran en el archivo `conversion.log`.
- En caso de error en un archivo PDF concreto, se intentará mover el documento a la carpeta definida como `carpeta_errores` para su posterior análisis.

## Consideraciones especiales

### Archivos con múltiples páginas
Cada página del PDF se convierte en una imagen independiente.  
El nombre del archivo generado sigue la convención:  
`nombre_del_pdf_p1.png`, `nombre_del_pdf_p2.png`, etc.

### Archivos protegidos con contraseña
La aplicación **no puede procesar archivos PDF protegidos con contraseña**.  
Si se detecta uno, el sistema lo considera como error y mueve el archivo a la carpeta de errores, registrando el incidente en `conversion.log`.

## Registro de actividad

La aplicación genera un archivo de log (`conversion.log`) en el mismo directorio que el ejecutable, con información de diagnóstico y seguimiento de cada conversión realizada.
