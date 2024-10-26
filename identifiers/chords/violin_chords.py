from identifiers.chords.chord_identifier import ChordIdentifier
from identifiers.single_notes.violin_identifier import ViolinIdentifier

class ChordViolinIdentifier(ChordIdentifier):

    __notes_names = {
        'ViolinDo': 'C', 'ViolinDoSostenidoReb': 'C#', 'ViolinRe': 'D', 'ViolinReSostenidoMib': 'D#', 'ViolinMi': 'E', 'ViolinFa': 'F',
        'ViolinFaSostenidoSolb': 'F#', 'ViolinSol': 'G', 'ViolinSolSostenidoLab': 'G#', 'ViolinLa': 'A', 'ViolinLaSostenidoSib': 'A#', 'ViolinSi': 'B'
    }

    def identify_chord_from_audio(self, audio_file, tolerance=5):
        return super().identify_chord_from_audio(audio_file, self.__notes_names, ViolinIdentifier(), 6, tolerance)
            