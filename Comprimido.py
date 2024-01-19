# ---------------------------------------------------
# Universidad Autónoma Metropolitana unidad Lerma
# ---------------------------------------------------
# Eje integrador II
# Comparación de diferentes formatos de audio (AAC)
# Diego Cantoral González
# ---------------------------------------------------

# Este código crea la función que trabaja los archivos de formato AAC para obtener sus muestras, vector de tiempo,
# la duración total, el espectro y el vector de frecuencias para poder graficar correctamente el espectro.

import numpy as np
from pydub import AudioSegment
from scipy.fft import fft, fftfreq


def leerDatosComprimido(archivoAAC, nfft):
    data = AudioSegment.from_file(archivoAAC, format="aac")  # Lee archivo AAC
    canales = data.split_to_mono()  # Divide audio stéreo en dos canales mono
    mono = canales[0] + canales[1]  # Une canal 1 y canal 2
    bytes = mono.raw_data  # Convierte a bytes
    muestras = np.frombuffer(bytes, dtype=np.int16)  # Convierte a arreglo numpy
    N = len(muestras)  # Número de muestras
    fs = data.frame_rate  # Frecuencia de muestreo

    # Tiempo de intervalo entre las muestras
    # fs = 1 / Ts --> Ts = 1 / fs
    Ts = 1 / fs
    tiempo = Ts * N
    t = np.linspace(0, tiempo / 2, N)  # vector de tiempo

    fourier = fft(muestras, nfft)
    frecuencias = fftfreq(nfft, Ts)  # retorna frecuencias del espectro para la ventana
    fourier = fourier[np.argsort(frecuencias)]  # ordena componentes
    frecuencias.sort()  # ordena frecuencias
    fourier = (1 / nfft) * np.abs(fourier)  # normaliza
    return fourier, frecuencias, muestras, t
