# Obtener la fecha de modificación de un archivo comprimido en formato RAR
Este script de Python se utiliza para obtener la fecha de modificación de todos los archivos contenidos en un archivo comprimido en formato RAR. El script utiliza la biblioteca `rarfile` de Python para acceder a los archivos en el archivo RAR y la biblioteca time de Python para convertir la marca de tiempo en un formato.

## Requisitos previos
Antes de ejecutar este script, asegúrate de tener Python 3 instalado en tu computadora. También necesitarás instalar la biblioteca rarfile de Python utilizando el siguiente comando:

`pip install rarfile`

## Uso
Para utilizar este script, sigue estos pasos:

1. Abre una ventana de terminal o consola de comandos.
2. Navega hasta el directorio que contiene el archivo RAR cuya fecha de modificación deseas obtener.
3. Ejecuta el siguiente comando en la terminal:
`python modification_date_rar.py`
4. El script imprimirá una lista de todos los archivos en el archivo RAR junto con su fecha de modificación, en formato "YYYY-MM-DD HH:MM:SS".

## Limitaciones
Este script solo funciona con archivos comprimidos en formato RAR. Si deseas obtener la fecha de modificación de archivos en otros formatos de archivo, deberás modificar el script para trabajar con esas bibliotecas específicas.
Si el archivo RAR está protegido por contraseña, deberás proporcionar la contraseña en el script antes de ejecutarlo.
## Contribuciones
Si deseas contribuir a este proyecto, ¡eres bienvenido! Puedes enviar pull requests o abrir problemas en el repositorio de GitHub.
