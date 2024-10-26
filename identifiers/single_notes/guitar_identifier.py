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
        for note in self.notes:
            result = note.is_note(dominant_frequency, tolerance)
            if result:
                return note.__class__.__name__[6:], result[-1], dominant_frequency

        return None, None, dominant_frequency

    def identify_note_from_frequency(self, frequency, tolerance=5):
        for note in self.notes:
            result = note.is_note(frequency, tolerance)
            if result:
                return result, note.__class__.__name__

        return None, None
