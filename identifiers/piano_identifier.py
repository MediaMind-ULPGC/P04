from musical_notes.piano_musical_notes import PianoDo, PianoDoSostenidoReb, PianoRe, PianoReSostenidoMib, PianoMi, PianoFa,PianoFaSostenidoSolb
from musical_notes.piano_musical_notes import PianoSol, PianoSolSostenidoLab,PianoLa, PianoLaSostenidoSib, PianoSi
from dominant_frequency import DominantFrequency

class PianoIdentifier:

    def __init__(self):
        self.notes = [
            PianoDo(),
            PianoDoSostenidoReb(),
            PianoRe(),
            PianoReSostenidoMib(),
            PianoMi(),
            PianoFa(),
            PianoFaSostenidoSolb(),
            PianoSol(),
            PianoSolSostenidoLab(),
            PianoLa(),
            PianoLaSostenidoSib(),
            PianoSi()
        ]

    def identify_note_from_audio(self, audio_file, tolerance=5):
        dominant_frequency = DominantFrequency().get_dominant_frequency(audio_file)
        print("Frecuencia dominante:", dominant_frequency)
        for note in self.notes:
            result = note.is_note(dominant_frequency, tolerance)
            if result:
                return f"Nota identificada: {note.__class__.__name__[5:]} en la octava {result}"

        return "No se pudo identificar la nota."
    
    def identify_note_from_frequency(self, frequency, tolerance=5):
        for note in self.notes:
            result = note.is_note(frequency, tolerance)
            if result:
                return note.__class__.__name__

        return None

class PianoChordIdentifier:

    _CHORDS = {
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

    _notes_names = {
        'PianoDo': 'C', 'PianoRe': 'D', 'PianoMi': 'E', 'PianoFa': 'F',
        'PianoSol': 'G', 'PianoLa': 'A', 'PianoSi': 'B', 'PianoDoSostenidoReb': 'C#',
        'PianoReSostenidoMib': 'D#', 'PianoFaSostenidoSolb': 'F#', 'PianoSolSostenidoLab': 'G#',
        'PianoLaSostenidoSib': 'A#'
    }

    _notes_names_inverse = {v: k for k, v in _notes_names.items()}

    _pianoIdentifier = PianoIdentifier()


    def identify_chord_from_audio(self, audio_file, tolerance=5):

        dominant_frequencies = DominantFrequency().get_dominant_frequencies(audio_file)
        print("Frecuencias dominantes:", dominant_frequencies)

        identified_notes = []
        for frequency in dominant_frequencies:
            note_class = self._pianoIdentifier.identify_note_from_frequency(frequency, tolerance)
            if note_class:
                note_name = self._notes_names.get(note_class, None)
                if note_name and note_name not in identified_notes:
                    identified_notes.append(note_name)
        
        identified_chord = self._match_chord(identified_notes)

        if identified_chord:
            chord_notes = self._CHORDS[identified_chord]
            real_names = [self._notes_names_inverse.get(note, note)[5:] for note in chord_notes]

            print(f"Acorde identificado del piano: {identified_chord} compuesto por las notas {', '.join(real_names)}")
        else:
            return f"No se pudo identificar el acorde con las notas {identified_notes}."
        

    def _match_chord(self, notes):
        for chord, notes_chord in self._CHORDS.items():
            if all(note in notes for note in notes_chord):
                return chord
        
        return None

