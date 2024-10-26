from identifiers.chords.chord_identifier import ChordIdentifier
from identifiers.single_notes.piano_identifier import PianoIdentifier

class ChordPianoIdentifier(ChordIdentifier):

    __notes_names = {
        'PianoDo': 'C', 'PianoRe': 'D', 'PianoMi': 'E', 'PianoFa': 'F',
        'PianoSol': 'G', 'PianoLa': 'A', 'PianoSi': 'B', 'PianoDoSostenidoReb': 'C#',
        'PianoReSostenidoMib': 'D#', 'PianoFaSostenidoSolb': 'F#', 'PianoSolSostenidoLab': 'G#',
        'PianoLaSostenidoSib': 'A#'
    }

    def identify_chord_from_audio(self, audio_file, tolerance=5):
        return super().identify_chord_from_audio(audio_file, self.__notes_names, PianoIdentifier(), 5, tolerance)