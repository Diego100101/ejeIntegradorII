#---------------------------------------------------
# Universidad Autónoma Metropolitana unidad Lerma
#---------------------------------------------------
# Eje integrador II
# Comparación de diferentes formatos de audio (AAC)
# Diego Cantoral González
#---------------------------------------------------

# Este código implementa las funciones creadas para comprimir los archivos de FLAC a WAC y de FLAC a AAC, y
# generar un archivo con extensión .wav y otro con extensión .aac.

from FLAC2AAC import flac2aac
from FLAC2WAV import flac2wav

# entrada de terminal
archivo = input("Ingresa la ruta o nombre de la canción en formato .flac\n")

# llama a las funciones
flac2wav(archivo)
flac2aac(archivo)