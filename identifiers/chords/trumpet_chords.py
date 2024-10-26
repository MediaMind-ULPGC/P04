from identifiers.chords.chord_identifier import ChordIdentifier
from identifiers.single_notes.trumpet_identifier import TrumpetIdentifier

class TrumpetChordsIdentifier(ChordIdentifier):

    __notes_names = {
        'TrumpetDo': 'C', 'TrumperRe': 'D', 'TrumpetMi': 'E', 'TrumpetFa': 'F',
        'TrumpetSol': 'G', 'TrumpetLa': 'A', 'TrumpetSi': 'B', 'TrumpetDoSostenidoReb': 'C#',
        'TrumpetReSostenidoMib': 'D#', 'TrumpetFaSostenidoSolb': 'F#', 'TrumpetSolSostenidoLab': 'G#',
        'TrumpetLaSostenidoSib': 'A#'
    }

    def identify_chord_from_audio(self, audio_file, tolerance=5):
        return super().identify_chord_from_audio(audio_file, self.__notes_names, TrumpetIdentifier(), 7, tolerance)