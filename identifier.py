from musical_notes.piano_musical_notes import PianoDo, PianoDoSostenidoReb, PianoRe, PianoReSostenidoMib, PianoMi, PianoFa,PianoFaSostenidoSolb
from musical_notes.piano_musical_notes import PianoSol, PianoSolSostenidoLab,PianoLa, PianoLaSostenidoSib, PianoSi

class Identifier:

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

    def identify_note(self, dominant_frequency, tolerance=5):
        for note in self.notes:
            result = note.is_note(dominant_frequency, tolerance)
            if result:
                return f"Nota identificada: {note.__class__.__name__[5:]} en la octava {result}"

        return "No se pudo identificar la nota."

class ChordIdentifier(Identifier):

    CHORDS = {
        'C Major': ['C', 'E', 'G'],
        'C Minor': ['C', 'D#', 'G'],
        'D Major': ['D', 'F#', 'A'],
        'D Minor': ['D', 'F', 'A'],
        'E Major': ['E', 'G#', 'B'],
        'E Minor': ['E', 'G', 'B'],
    }

    def identify_chord(self, frequencies, tolerance=5):
        identified_notes = []
        
        for frequency in frequencies:
            note = self.identify_note(frequency, tolerance)
            if note:
                identified_notes.append(note.split()[2])
        
        if not identified_notes:
            return "No se identificaron notas para formar un acorde."

        for chord_name, chord_notes in self.CHORDS.items():
            if all(note in identified_notes for note in chord_notes):
                return f"Acorde identificado: {chord_name}"

        return "No se pudo identificar el acorde."