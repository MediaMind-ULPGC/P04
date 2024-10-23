import numpy as np
import matplotlib.pyplot as plt
from identifiers.single_notes.piano_identifier import PianoIdentifier
from dominant_frequency import DominantFrequency
from scipy.io import wavfile
from scipy.signal import find_peaks


class PianoScaleIdentifier:

    __piano_identifier = PianoIdentifier()

    def identify_scale_from_audio(self, audio_file, window_size=4096, overlap=2048, tolerance=10, num_frequencies=3):
        """
        Identificar la escala de un archivo de audio dividiéndolo en ventanas temporales y
        utilizando la clase DominantFrequency para identificar las frecuencias dominantes en cada ventana.
        """
        sr, data = wavfile.read(audio_file)

        if len(data.shape) > 1:
            data = np.mean(data, axis=1)

        identified_notes = []
        dominant_frequencies = []
        time_stamps = []

        # Procesar el audio por ventanas
        for start in range(0, len(data) - window_size, window_size - overlap):
            window_data = data[start:start + window_size]
            
            # Calculamos el tiempo correspondiente al centro de la ventana actual
            time_stamp = (start + window_size / 2) / sr
            # Obtener las frecuencias dominantes de la ventana
            fourier, freqs = DominantFrequency._get_frequencies(sr, window_data)
            peaks, _ = find_peaks(fourier, height=0)
            
            # Ordenar las frecuencias dominantes por magnitud
            sorted_peaks = np.argsort(fourier[peaks])[::-1]
            
            # Capturar las principales frecuencias dominantes
            window_frequencies = []
            window_notes = []
            for peak_index in sorted_peaks[:num_frequencies]:
                dominant_frequency = freqs[peaks][peak_index]

                # Filtrar frecuencias no relevantes
                if 20 < dominant_frequency < 4000:
                    # Identificar la nota correspondiente
                    _, note = self.__piano_identifier.identify_note_from_frequency(dominant_frequency, tolerance)
                    if note:
                        window_notes.append(note[5:])
                        window_frequencies.append(dominant_frequency)

            # Solo añadimos si identificamos al menos una frecuencia
            if window_notes and window_frequencies:
                identified_notes.append(window_notes)
                dominant_frequencies.append(window_frequencies)
                time_stamps.append(time_stamp)

        return identified_notes, dominant_frequencies, time_stamps

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
