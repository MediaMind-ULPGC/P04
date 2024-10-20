from musical_notes.trumpet_musical_notes import TrumpetDo, TrumpetDoSostenidoReb, TrumpetRe, TrumpetReSostenidoMib, TrumpetMi, TrumpetFa
from musical_notes.trumpet_musical_notes import TrumpetFaSostenidoSolb, TrumpetSol, TrumpetSolSostenidoLab, TrumpetLa, TrumpetLaSostenidoSib, TrumpetSi
from dominant_frequency import DominantFrequency

class TrumpetIdentifier:

    def __init__(self):
        self.notes = [
            TrumpetDo(),
            TrumpetDoSostenidoReb(),
            TrumpetRe(),
            TrumpetReSostenidoMib(),
            TrumpetMi(),
            TrumpetFa(),
            TrumpetFaSostenidoSolb(),
            TrumpetSol(),
            TrumpetSolSostenidoLab(),
            TrumpetLa(),
            TrumpetLaSostenidoSib(),
            TrumpetSi()
        ]
    
    def identify_note_from_audio(self, audio_file, tolerance=5):
        dominant_frequency = DominantFrequency().get_dominant_frequency(audio_file)
        print("Frecuencia dominante:", dominant_frequency)
        for note in self.notes:
            result = note.is_note(dominant_frequency, tolerance)
            if result:
                return f"Nota identificada: {note.__class__.__name__[7:]} en la octava {result}"

        return "No se pudo identificar la nota."