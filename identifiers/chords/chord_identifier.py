from dominant_frequency import DominantFrequency

class ChordIdentifier:
    
    __CHORDS = {
        'Do Mayor': ['C', 'E', 'G'],
        'Do Menor (Cm)': ['C', 'D#', 'G'],
        'Do Sostenido Mayor (C#)': ['C#', 'F', 'G#'],
        'Do Sostenido Menor (C#m)': ['C#', 'E', 'G#'],
        'Re Mayor': ['D', 'F#', 'A'],
        'Re Menor (Dm)': ['D', 'F', 'A'],
        'Re Sostenido Mayor (D#)': ['D#', 'G', 'A#'],
        'Re Sostenido Menor (D#m)': ['D#', 'F#', 'A#'],
        'Mi Mayor': ['E', 'G#', 'B'],
        'Mi Menor (Em)': ['E', 'G', 'B'],
        'Fa Mayor': ['F', 'A', 'C'],
        'Fa Menor (Fm)': ['F', 'G#', 'C'],
        'Fa Sostenido Mayor (F#)': ['F#', 'A#', 'C#'],
        'Fa Sostenido Menor (F#m)': ['F#', 'A', 'C#'],
        'Sol Mayor': ['G', 'B', 'D'],
        'Sol Menor (Gm)': ['G', 'A#', 'D'],
        'Sol Sostenido Mayor (G#)': ['G#', 'C', 'D#'],
        'Sol Sostenido Menor (G#m)': ['G#', 'B', 'D#'],
        'Si Mayor': ['B', 'D#', 'F#'],
        'Si Menor (Bm)': ['B', 'D', 'F#'],
        'La Mayor': ['A', 'C#', 'E'],
        'La Menor (Am)': ['A', 'C', 'E'],
        'La Sostenido Mayor (A#)': ['A#', 'D', 'F'],
        'La Sostenido Menor (A#m)': ['A#', 'C#', 'F']
    }

    def identify_chord_from_audio(self, audio_file, notes_names, instrument_class, n, tolerance=5):
        notes_names_inverse = {v: k for k, v in notes_names.items()}

        dominant_frequencies = DominantFrequency().get_dominant_frequencies(audio_file)

        identified_notes = []
        for frequency in dominant_frequencies:
            _, note_class = instrument_class.identify_note_from_frequency(frequency, tolerance)
            if note_class:
                note_name = notes_names.get(note_class, None)
                if note_name and note_name not in identified_notes:
                    identified_notes.append(note_name)
        
        matches = self._match_chord(identified_notes)
        
        # Si encontramos un acorde exacto
        if len(matches) == 1 and matches[0][1] == 3:
            identified_chord, _ = matches[0]
            if identified_chord is None:
                return None, None, None, None
            chord_notes = self.__CHORDS[identified_chord]
            real_names = [notes_names_inverse.get(note, note)[n:] for note in chord_notes]
            return identified_chord, real_names, [round(freq, 2) for freq in dominant_frequencies], True

        # Si hay aproximaciones
        elif len(matches) > 0:
            identified_chords_approx = []
            notes_approx = []

            for identified_chord, match_score in matches:
                if identified_chord is None:
                    None, None, None, None
                chord_notes = self.__CHORDS[identified_chord]
                real_names = [notes_names_inverse.get(note, note)[n:] for note in chord_notes]

                # Notas coincidentes
                matching_notes = [note for note in identified_notes if note in chord_notes]
                matching_real_names = [notes_names_inverse.get(note, note)[n:] for note in matching_notes]

                identified_chords_approx.append(identified_chord)
                notes_approx.append((real_names, matching_real_names))

            return identified_chords_approx, notes_approx, [round(freq, 2) for freq in dominant_frequencies], False
        else:
            return None, identified_notes, [round(freq, 2) for freq in dominant_frequencies],  None
    

    def _match_chord(self, notes):
        exact_match = None
        approximations = []
        
        for chord, notes_chord in self.__CHORDS.items():
            match_score = sum(1 for note in notes if note in notes_chord)

            # Si encontramos un acorde con todas las notas, devolvemos ese acorde y su puntaje
            if match_score == 3:
                exact_match = (chord, match_score)
                break 

            if match_score == 2:
                approximations.append((chord, match_score))

        # Si encontramos una coincidencia exacta, la devolvemos
        if exact_match:
            return [exact_match]
        
        # Si no hay una coincidencia exacta, devolvemos todas las aproximaciones
        return approximations if approximations else [(None, 0)]