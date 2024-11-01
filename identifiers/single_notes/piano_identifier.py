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
        for note in self.notes:
            result = note.is_note(dominant_frequency, tolerance)
            if result:
                return note.__class__.__name__[5:], result[-1], dominant_frequency

        return None, None, dominant_frequency
    
    def identify_note_from_frequency(self, frequency, tolerance=5):
        for note in self.notes:
            result = note.is_note(frequency, tolerance)
            if result:
                return result, note.__class__.__name__

        return None, None


