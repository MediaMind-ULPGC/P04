from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt

class DominantFrequency:

    def __init__(self):
        pass

    @staticmethod
    def _get_frequencies(sr, data):
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

        return fourier, freqs

    @staticmethod
    def get_dominant_frequency(audio_file):
        sr, data = wavfile.read(audio_file)

        if len(data.shape) > 1:
            data = np.mean(data, axis=1)

        fourier, freqs = DominantFrequency()._get_frequencies(sr, data)
        
        return freqs[np.argmax(fourier)]
    
    @staticmethod
    def get_dominant_frequencies(audio_file, num_frequencies=3, min_distance=5):
        sr, data = wavfile.read(audio_file)

        if len(data.shape) > 1:
            data = np.mean(data, axis=1)

        fourier, freqs = DominantFrequency._get_frequencies(sr, data)

        # Encontrar los picos de las frecuencias
        peaks, _ = find_peaks(fourier, height=0)

        # Ordenar los picos de mayor a menor
        sorted_peaks = np.argsort(fourier[peaks])[::-1]

        # Lista para almacenar las frecuencias dominantes finales
        dominant_frequencies = []

        for peak in sorted_peaks:
            freq = freqs[peaks][peak]

            if all(abs(freq - existing_freq) > min_distance for existing_freq in dominant_frequencies):
                dominant_frequencies.append(freq)

            if len(dominant_frequencies) >= num_frequencies:
                break

        return dominant_frequencies
        

    @staticmethod
    def plot_frequencies(frequencies, sr, window_size, overlap):
        time_axis = np.arange(len(frequencies)) * (window_size - overlap) / sr
        plt.plot(time_axis, frequencies)
        plt.xlabel("Time (seconds)")
        plt.ylabel("Frequency (Hz)")
        plt.title("Dominant Frequencies Over Time")
        plt.show()