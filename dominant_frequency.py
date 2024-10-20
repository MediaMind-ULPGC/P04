from scipy.io import wavfile
from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt

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

    @staticmethod
    def get_dominant_frequencies(audio_file, window_size=1024, overlap=512):
        sr, data = wavfile.read(audio_file)

        if len(data.shape) > 1:
            data = np.mean(data, axis=1)

        data = data / np.max(np.abs(data))

        step_size = window_size - overlap
        num_windows = (len(data) - window_size) // step_size + 1

        dominant_frequencies = []

        for i in range(num_windows):
            start = i * step_size
            end = start + window_size
            window_data = data[start:end]

            fourier = np.abs(fft(window_data))
            freqs = np.fft.fftfreq(len(fourier), 1/sr)

            fourier = fourier[:len(fourier) // 2]
            freqs = freqs[:len(freqs) // 2]

            dominant_frequency = freqs[np.argmax(fourier)]
            dominant_frequencies.append(dominant_frequency)

        return dominant_frequencies, sr

    @staticmethod
    def plot_frequencies(frequencies, sr, window_size, overlap):
        time_axis = np.arange(len(frequencies)) * (window_size - overlap) / sr
        plt.plot(time_axis, frequencies)
        plt.xlabel("Time (seconds)")
        plt.ylabel("Frequency (Hz)")
        plt.title("Dominant Frequencies Over Time")
        plt.show()