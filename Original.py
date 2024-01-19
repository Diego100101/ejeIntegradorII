#---------------------------------------------------
# Universidad Autónoma Metropolitana unidad Lerma
#---------------------------------------------------
# Eje integrador II
# Comparación de diferentes formatos de audio (AAC)
# Diego Cantoral González
#---------------------------------------------------

# Este código crea la función que trabaja los archivos de formato WAV para obtener sus muestras, vector de tiempo,
# la duración total, el espectro y el vector de frecuencias para poder graficar correctamente el espectro.


import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

def leerDatosOriginal(archivoWAV, nfft):
    fs, data = wavfile.read(archivoWAV)  # Lee archivo WAV
    muestras = (data[:, 0] + data[:, 1])  # Convierte el audio a mono, junta ambos canales
    N = len(data)  # Número de muestas

    # Tiempo de intervalo entre las muestras
    # fs = 1 / Ts --> Ts = 1 / fs
    Ts = 1 / fs
    tiempo = Ts * N  # Tiempo en segundos de la canción
    t = np.linspace(0, tiempo, N)  # vector de tiempo

    print(f"Duración de la canción: {tiempo:.2f} segundos.")  # Duración total en segundos de la canción

    # Transformada Fourier
    fourier = fft(muestras, nfft)
    frecuencias = fftfreq(nfft, Ts)  # retorna frecuencias del espectro para la ventana
    fourier = fourier[np.argsort(frecuencias)]  # ordena componentes
    frecuencias.sort()  # ordena frecuencias
    fourier = (1/nfft) * np.abs(fourier)  # normaliza
    return fourier, frecuencias, muestras, t

