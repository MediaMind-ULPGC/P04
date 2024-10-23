from dominant_frequency import DominantFrequency
from musical_notes.violin_musical_notes import ViolinDo, ViolinDoSostenidoReb, ViolinRe, ViolinReSostenidoMib, ViolinMi, ViolinFa
from musical_notes.violin_musical_notes import ViolinFaSostenidoSolb, ViolinSol, ViolinSolSostenidoLab, ViolinLa, ViolinLaSostenidoSib, ViolinSi

class ViolinIdentifier:

    def __init__(self):
        self.notes = [
            ViolinDo(),
            ViolinDoSostenidoReb(),
            ViolinRe(),
            ViolinReSostenidoMib(),
            ViolinMi(),
            ViolinFa(),
            ViolinFaSostenidoSolb(),
            ViolinSol(),
            ViolinSolSostenidoLab(),
            ViolinLa(),
            ViolinLaSostenidoSib(),
            ViolinSi()
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
                return result, note.__class__.__name__

        return None, None

