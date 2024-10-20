from scipy.io import wavfile
from scipy.fft import fft
import numpy as np

class DominantFrequency:

    def __init__(self):
        pass

    @staticmethod
    def get_dominant_frequency(audio_file):
        sr, data = wavfile.read(audio_file)

        if len(data.shape) > 1:
            data = np.mean(data, axis=1)

        """
        1. Calcular la transformada de Fourier
        2. Clacular las frecuencias
        3. Filtrar las frecuencias positivas
        4. Encontrar la frecuencia dominante
        """
        fourier = np.abs(fft(data))
        freqs = np.fft.fftfreq(len(fourier), 1/sr)
        
        fourier = fourier[:len(fourier)//2]
        freqs = freqs[:len(freqs)//2]
        
        return freqs[np.argmax(fourier)]