from identifiers.chords.chord_identifier import ChordIdentifier
from identifiers.single_notes.guitar_identifier import GuitarIdentifier

class ChordGuitarIdentifier(ChordIdentifier):

    __notes_names = {
        'GuitarDo': 'C', 'GuitarDoSostenidoReb': 'C#', 'GuitarRe': 'D', 'GuitarReSostenidoMib': 'D#', 'GuitarMi': 'E', 'GuitarFa': 'F',
        'GuitarFaSostenidoSolb': 'F#', 'GuitarSol': 'G', 'GuitarSolSostenidoLab': 'G#', 'GuitarLa': 'A', 'GuitarLaSostenidoSib': 'A#', 'GuitarSi': 'B'
    }

    def identify_chord_from_audio(self, audio_file, tolerance=5):
        return super().identify_chord_from_audio(audio_file, self.__notes_names,GuitarIdentifier(), 6, tolerance)

