from musical_notes.piano_musical_notes import PianoDo, PianoDoSostenidoReb, PianoRe, PianoReSostenidoMib, PianoMi, PianoFa,PianoFaSostenidoSolb
from musical_notes.piano_musical_notes import PianoSol, PianoSolSostenidoLab,PianoLa, PianoLaSostenidoSib, PianoSi
from dominant_frequency import DominantFrequency

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

class ChordIdentifier(Identifier):

    CHORDS = {
        'C Major': ['C', 'E', 'G'],
        'C Minor': ['C', 'D#', 'G'],
        'D Major': ['D', 'F#', 'A'],
        'D Minor': ['D', 'F', 'A'],
        'E Major': ['E', 'G#', 'B'],
        'E Minor': ['E', 'G', 'B'],
    }

    notes_names = {
        'PianoDo': 'C',
        'PianoRe': 'D',
        'PianoMi': 'E',
        'PianoFa': 'F',
        'PianoSol': 'G',
        'PianoLa': 'A',
        'PianoSi': 'B',
        'PianoDoSostenidoReb': 'C#',
        'PianoReSostenidoMib': 'D#',
        'PianoFaSostenidoSolb': 'F#',
        'PianoSolSostenidoLab': 'G#',
        'PianoLaSostenidoSib': 'A#'
    }

    def identify_chord_from_audio(self, audio_file, window_size=2048, overlap=1024, tolerance=5):
        dominant_freq = DominantFrequency()
        frequencies, sr = dominant_freq.get_dominant_frequencies(audio_file, window_size, overlap)

        chords_detected = []
        current_window_notes = []

        for frequency in frequencies:
            note = self.identify_note_from_frequency(frequency, tolerance)
            if note:
                note_name = self.notes_names[note]

                if note_name not in current_window_notes:
                    print(f"Identified note: {note_name}")
                    current_window_notes.append(note_name)
            
            if len(current_window_notes) >= 3:
                identified_chord = self.identify_chord(current_window_notes)
                if identified_chord:
                    chords_detected.append(identified_chord)
                current_window_notes = []

        if not chords_detected:
            return "No se identificaron acordes."

        return chords_detected

    def identify_chord(self, notes_in_window):
        for chord_name, chord_notes in self.CHORDS.items():
            if all(note in notes_in_window for note in chord_notes):
                return f"Acorde identificado: {chord_name}"
        return None
