# ---------------------------------------------------
# Universidad Autónoma Metropolitana unidad Lerma
# ---------------------------------------------------
# Eje integrador II
# Comparación de diferentes formatos de audio (AAC)
# Diego Cantoral González
# ---------------------------------------------------

# Este código crea la función que comprime un archivo FLAC a AAC Genera un archivo con extensión .aac.

from pydub import AudioSegment


def flac2aac(archivo):
    ruta = "/home/diego/EjeIntegradorII/"
    nombre = archivo.split('.')[0]  # rescata el nombre sin extensión del archivo
    archivo = ruta + archivo  # une ruta y nombre del archivo
    flac = AudioSegment.from_file(archivo, format="flac")  # lee archivo formato FLAC

    salida = ruta + nombre + '.aac'  # genera nuevo nombre con extensión .aac
    flac.export(salida, format="adts", codec='aac', bitrate='256k')  # comprime
