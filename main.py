#---------------------------------------------------
# Universidad Autónoma Metropolitana unidad Lerma
#---------------------------------------------------
# Código principal del proyecto de Eje integrador II
# Comparación de diferentes formatos de audio (AAC)
# Diego Cantoral González
#---------------------------------------------------

# Este código contiene la implementación de las funciones creadas para leer, graficar y obtener
# el espectro de los archivos de audio FLAC y AAC con el fin de comparar y apreciar la compresión
# que realiza el formato AAC.


from Original import leerDatosOriginal
from Comprimido import leerDatosComprimido
import matplotlib.pyplot as plt

cancion = "SeizetheDay"  # Se define variable que almacenará nombre de la canción (debe compartir el mismo
# directorio que el código)

nfft = 2 ** 14  # Es el número de muestras que se desea rescatar y distrubuir de la FFT
archivoWAV = cancion + ".wav"  # añade extensión .wav al nombre de la canción
fourierWAV, Hz1, senalWAV, tiempoWAV = leerDatosOriginal(archivoWAV, nfft)  # llama la función que trabaja con el archivo WAV

archivoAAC = cancion + ".aac"  # añade extensión .aac al nombre de la canción
fourierAAC, Hz2, senalAAC, tiempoAAC = leerDatosComprimido(archivoAAC, nfft)  # llama la función que trabaja con el archivo AAC

# Grafica los espectros, añade títulos, leyenda, colores y etiquetas a los ejes
plt.figure()
plt.title("Comparación de espectros")
plt.plot(Hz1, fourierWAV, color='purple', label='Archivo WAV')
plt.plot(Hz2, fourierAAC, color='orange', label='Archivo AAC')
#plt.xlim([-10000, 10000])
plt.xlabel("Frecuencias [Hz]")
plt.ylabel("Amplitud")
plt.legend(fontsize="15")
plt.show()
