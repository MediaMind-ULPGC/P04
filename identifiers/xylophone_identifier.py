from dominant_frequency import DominantFrequency
from musical_notes.xylophone_musical_notes import XylophoneDo, XylophoneRe, XylophoneMi, XylophoneFa, XylophoneSol
from musical_notes.xylophone_musical_notes import XylophoneLa, XylophoneSi

class XylophoneIdentifier:

    def __init__(self):
        self.notes = [
            XylophoneDo(),
            XylophoneRe(),
            XylophoneMi(),
            XylophoneFa(),
            XylophoneSol(),
            XylophoneLa(),
            XylophoneSi()
        ]
    
    def identify_note_from_audio(self, audio_file, tolerance=5):
        dominant_frequency = DominantFrequency().get_dominant_frequency(audio_file)
        print("Frecuencia dominante:", dominant_frequency)
        for note in self.notes:
            result = note.is_note(dominant_frequency, tolerance)
            if result:
                return f"Nota identificada: {note.__class__.__name__[9:]} en la octava {result}"

        return "No se pudo identificar la nota."
