from musical_notes.guitar_musical_notes import GuitarDo, GuitarDoSostenidoReb, GuitarRe, GuitarReSostenidoMib, GuitarMi
from musical_notes.guitar_musical_notes import GuitarFa, GuitarFaSostenidoSolb, GuitarSol, GuitarSolSostenidoLab, GuitarLa, GuitarLaSostenidoSib, GuitarSi
from dominant_frequency import DominantFrequency

class GuitarIdentifier:

    def __init__(self):
        self.notes = [
            GuitarDo(),
            GuitarDoSostenidoReb(),
            GuitarRe(),
            GuitarReSostenidoMib(),
            GuitarMi(),
            GuitarFa(),
            GuitarFaSostenidoSolb(),
            GuitarSol(),
            GuitarSolSostenidoLab(),
            GuitarLa(),
            GuitarLaSostenidoSib(),
            GuitarSi()
        ]

    def identify_note_from_audio(self, audio_file, tolerance=5):
        dominant_frequency = DominantFrequency().get_dominant_frequency(audio_file)
        print("Frecuencia dominante:", dominant_frequency)
        for note in self.notes:
            result = note.is_note(dominant_frequency, tolerance)
            if result:
                return f"Nota identificada: {note.__class__.__name__[6:]} en la octava {result}"

        return "No se pudo identificar la nota."

    def identify_note_from_frequency(self, frequency, tolerance=5):
        for note in self.notes:
            result = note.is_note(frequency, tolerance)
            if result:
                return note.__class__.__name__

        return None

class GuitarChordIdentifier:

    _CHORDS = {
        'Do Mayor': ['C', 'E', 'G'],
        'Do Menor (Cm)': ['C', 'D#', 'G'], 
        'Do Sostenido Mayor (C#)': ['C#', 'F', 'G#'],
        'Do Sostenido Menor (C#m)': ['C#', 'E', 'G#'], # falta
        'Re Mayor': ['D', 'F#', 'A'], 
        'Re Menor (Dm)': ['D', 'F', 'A'], 
        'Re Sostenido Mayor (D#)': ['D#', 'G', 'A#'], # falta
        'Re Sostenido Menor (D#m)': ['D#', 'F#', 'A#'], # falta
        'Mi Mayor': ['E', 'G#', 'B'],
        'Mi Menor (Em)': ['E', 'G', 'B'],
        'Fa Mayor': ['F', 'A', 'C'], # falta
        'Fa Menor (Fm)': ['F', 'G#', 'C'], 
        'Fa Sostenido Mayor (F#)': ['F#', 'A#', 'C#'], # falta
        'Fa Sostenido Menor (F#m)': ['F#', 'A', 'C#'], # falta
        'Sol Mayor': ['G', 'B', 'D'], 
        'Sol Menor (Gm)': ['G', 'A#', 'D'], # falta
        'Sol Sostenido Mayor (G#)': ['G#', 'C', 'D#'], # falta
        'Sol Sostenido Menor (G#m)': ['G#', 'B', 'D#'], # falta
        'La Mayor': ['A', 'C#', 'E'], # falta
        'La Menor (Am)': ['A', 'C', 'E'], 
        'La Sostenido Mayor (A#)': ['A#', 'D', 'F'], # falta
        'La Sostenido Menor (A#m)': ['A#', 'C#', 'F'], # falta
    }


    _notes_names = {
        "GuitarDo": "C", "GuitarDoSostenidoReb": "C#", "GuitarRe": "D", "GuitarReSostenidoMib": "D#",
        "GuitarMi": "E", "GuitarFa": "F", "GuitarFaSostenidoSolb": "F#", "GuitarSol": "G",  "GuitarSolSostenidoLab": "G#",
        "GuitarLa": "A", "GuitarLaSostenidoSib": "A#", "GuitarSi": "B"
    }

    _notes_names_inverse = {v: k for k, v in _notes_names.items()}

    _guitarIdentifier = GuitarIdentifier()

    def identify_chord_from_audio(self, audio_file, tolerance=5):

        dominant_frequencies = DominantFrequency().get_dominant_frequencies(audio_file)
        print("Frecuencias dominantes:", dominant_frequencies)

        identified_notes = []
        for frequency in dominant_frequencies:
            note_class = self._guitarIdentifier.identify_note_from_frequency(frequency, tolerance)
            if note_class:
                note_name = self._notes_names.get(note_class, None)
                if note_name and note_name not in identified_notes:
                    identified_notes.append(note_name)
        
        matches = self._match_chord(identified_notes)

        # Si encontramos un acorde exacto
        if len(matches) == 1 and matches[0][1] == 3:
            identified_chord, _ = matches[0]
            chord_notes = self._CHORDS[identified_chord]
            real_names = [self._notes_names_inverse.get(note, note)[6:] for note in chord_notes]
            return f"Acorde identificado de la guitarra: {identified_chord} compuesto por las notas {', '.join(real_names)}"

        # Si hay aproximaciones
        elif len(matches) > 0:
            approximations_info = []
            for identified_chord, match_score in matches:
                chord_notes = self._CHORDS[identified_chord]
                real_names = [self._notes_names_inverse.get(note, note)[6:] for note in chord_notes]

                # Notas coincidentes
                matching_notes = [note for note in identified_notes if note in chord_notes]
                matching_real_names = [self._notes_names_inverse.get(note, note)[6:] for note in matching_notes]

                approximations_info.append(
                    f"Acorde aproximado: {identified_chord} compuesto por las notas {', '.join(real_names)} "
                    f"(coinciden: {', '.join(matching_real_names)})"
                )

            return "\n".join(approximations_info)
        else:
            return f"No se pudo identificar el acorde con las notas {identified_notes}."
            

    def _match_chord(self, notes):
        exact_match = None
        approximations = []
        
        for chord, notes_chord in self._CHORDS.items():
            match_score = sum(1 for note in notes if note in notes_chord)

            # Si encontramos un acorde con todas las notas, devolvemos ese acorde y su puntaje
            if match_score == 3:
                exact_match = (chord, match_score)
                break  # Detenemos la búsqueda si encontramos un acorde exacto

            # Si hay al menos 2 coincidencias, lo consideramos como una aproximación
            if match_score == 2:
                approximations.append((chord, match_score))

        # Si encontramos una coincidencia exacta, la devolvemos
        if exact_match:
            return [exact_match]
        
        # Si no hay una coincidencia exacta, devolvemos todas las aproximaciones
        return approximations if approximations else [(None, 0)]