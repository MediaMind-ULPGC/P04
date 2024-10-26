import numpy as np
import matplotlib.pyplot as plt
from dominant_frequency import DominantFrequency
from scipy.io import wavfile
from scipy.signal import find_peaks
from collections import Counter

class ScaleIdentifier:
    
    def identify_scale_from_audio(self, audio_file, identifier, window_size=4096, overlap=2048, tolerance=5, num_frequencies=3, timestep=0.1, n=5):
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
                    octava, note = identifier.identify_note_from_frequency(dominant_frequency, tolerance)
                    if note:
                        identified_notes.append([note[n:]])
                        identified_octaves.append([octava])
                        dominant_frequencies.append([dominant_frequency])
                        time_stamps.append(time_stamp)

        return identified_notes, identified_octaves, dominant_frequencies, time_stamps
    
    def plot_scale_over_time(self, notes, frequencies, time_stamps, min_scale=0, max_scale=4000):
        if len(frequencies) == len(time_stamps):
            plt.figure(figsize=(12, 6))
            
            frequency_count = Counter(freq for sublist in frequencies for freq in sublist)

            labeled_notes = {}

            for i, (time, freq_list, note_list) in enumerate(zip(time_stamps, frequencies, notes)):
                for freq, note in zip(freq_list, note_list):
                    if frequency_count[freq] >= 3:
                        plt.scatter(time, freq, c='blue')
                        
                        if freq not in labeled_notes:
                            plt.annotate(note, (time, freq), textcoords="offset points", xytext=(0,10), ha='center')
                            labeled_notes[freq] = note

            plt.ylim(min_scale, max_scale)
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Frecuencia (Hz)')
            plt.title('Frecuencias de las notas en la escala a lo largo del tiempo')
            plt.grid(True)
            plt.show()

        else:
            print("Error: Las longitudes de las frecuencias y las marcas de tiempo no coinciden.")
    
    note_positions = {
        'Do': -1,
        'Re': -0.5,
        'Mi': 0,
        'Fa': 0.5,
        'Sol': 1, 
        'La': 1.5,
        'Si': 2,
        'Do^': 2.5
    }

    colours = {
        'Do': 'blue',
        'DoSostenidoReb': 'lightblue',
        'Re': 'green',
        'ReSostenidoMib': 'lightgreen',
        'Mi': 'red',
        'Fa': 'purple',
        'FaSostenidoSolb': 'violet',
        'Sol': 'orange',
        'SolSostenidoLab': 'gold',
        'La': 'brown',
        'LaSostenidoSib': 'sienna',
        'Si': 'pink',
        'Do^': 'black'
    }

    def plot_notes_on_staff(self, notes, octaves, time_stamps, start=4):
        plt.figure(figsize=(12, 6))

        for i in range(0, 3):
            plt.axhline(i, color='black', lw=1)
        for i in np.arange(-0.5, 3, 0.5):
            plt.axhline(i, color='black', lw=1, ls='--')
        
        for note_list, octave_list, time in zip(notes, octaves, time_stamps):
            for note, octave in zip(note_list, octave_list):
                position, colour = self._position_colour(note, octave, start)
                plt.scatter(time, position, c=colour, s=100)
        
        plt.yticks(list(self.note_positions.values()), list(self.note_positions.keys()))
        plt.ylim(-2, 3)
        plt.xticks([])
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Notas en el pentagrama')
        plt.title('Notas identificadas en el pentagrama a lo largo del tiempo')
        plt.show()

    def _position_colour(self, note, octave, start=4):
        if note == 'Do' and int(octave[-1]) == start + 1:
            return self.note_positions['Do^'], self.colours['Do^']
        elif note == 'Do' and int(octave[-1]) == start:
            return self.note_positions['Do'] , self.colours['Do']
        elif note in self.note_positions:
            return self.note_positions[note], self.colours[note]
        else:
            return None, None