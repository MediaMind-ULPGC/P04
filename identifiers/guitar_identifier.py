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
        'Sol Mayor': ['G', 'B', 'D']
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
        
        identified_chord = self._match_chord(identified_notes)

        if identified_chord:
            chord_notes = self._CHORDS[identified_chord]
            real_names = [self._notes_names_inverse.get(note, note)[6:] for note in chord_notes]

            return f"Acorde identificado de la guitarra: {identified_chord} compuesto por las notas {', '.join(real_names)}"
        else:
            return f"No se pudo identificar el acorde con las notas {identified_notes}."
        

    def _match_chord(self, notes):
        for chord, notes_chord in self._CHORDS.items():
            if all(note in notes for note in notes_chord):
                return chord
        
        return None