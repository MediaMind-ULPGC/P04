import numpy as np
import matplotlib.pyplot as plt
from identifiers.single_notes.piano_identifier import PianoIdentifier
from dominant_frequency import DominantFrequency
from scipy.io import wavfile
from scipy.signal import find_peaks

class PianoScaleIdentifier:

    __piano_identifier = PianoIdentifier()

    def identify_scale_from_audio(self, audio_file, window_size=4096, overlap=2048, tolerance=10, num_frequencies=3, timestep=0.1):
        """
        Identificar la escala de un archivo de audio dividiéndolo en ventanas temporales y
        utilizando la clase DominantFrequency para identificar las frecuencias dominantes en cada ventana.
        """
        sr, data = wavfile.read(audio_file)

        if len(data.shape) > 1:
            data = np.mean(data, axis=1)

        window_size_seconds = timestep
        window_size = int(sr * window_size_seconds)
        timestep_samples = int(timestep * sr)

        identified_notes = []
        identified_octaves = []
        dominant_frequencies = []
        time_stamps = []

        # Recorremos los datos con un paso de tiempo fijo
        for start in range(0, len(data) - window_size, timestep_samples):
            window_data = data[start:start + window_size]

            time_stamp = (start + window_size / 2) / sr

            fourier, freqs = DominantFrequency._get_frequencies(sr, window_data)
            peaks, _ = find_peaks(fourier, height=0)
            
            if peaks.size > 0:
                sorted_peaks = np.argsort(fourier[peaks])[::-1]
                
                # Capturar solo la frecuencia dominante (la más alta)
                dominant_frequency = freqs[peaks][sorted_peaks[0]]

                if 20 < dominant_frequency < 4000:
                    octava, note = self.__piano_identifier.identify_note_from_frequency(dominant_frequency, tolerance)
                    if note:
                        identified_notes.append([note[5:]])
                        identified_octaves.append([octava])
                        dominant_frequencies.append([dominant_frequency])
                        time_stamps.append(time_stamp)

        return identified_notes, identified_octaves, dominant_frequencies, time_stamps

    def plot_scale_over_time(self, notes, frequencies, time_stamps):
        # Comprobar si el tamaño de time_stamps y frequencies es el mismo
        if len(frequencies) == len(time_stamps):
            plt.figure(figsize=(12, 6))
            
            # Diccionario para almacenar las notas que ya hemos etiquetado para evitar duplicados
            labeled_notes = {}

            for i, (time, freq_list, note_list) in enumerate(zip(time_stamps, frequencies, notes)):
                # Graficar todas las frecuencias
                for freq, note in zip(freq_list, note_list):
                    plt.scatter(time, freq, c='blue')  # Graficar el punto
                    
                    # Etiquetar la nota solo si no ha sido etiquetada aún en esa frecuencia
                    if freq not in labeled_notes:
                        plt.annotate(note, (time, freq), textcoords="offset points", xytext=(0,10), ha='center')  # Etiquetar la nota
                        labeled_notes[freq] = note  # Marcar la frecuencia como etiquetada
                    
            # Etiquetas y leyenda
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Frecuencia (Hz)')
            plt.title('Frecuencias de las notas en la escala a lo largo del tiempo')
            plt.grid(True)
            plt.show()

        else:
            print("Error: Las longitudes de las frecuencias y las marcas de tiempo no coinciden.")
