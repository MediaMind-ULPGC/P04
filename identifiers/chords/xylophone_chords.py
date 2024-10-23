from identifiers.chords.chord_identifier import ChordIdentifier
from identifiers.single_notes.xylophone_identifier import XylophoneIdentifier

class XylophoneChordsIdentifier(ChordIdentifier):

    __notes_names = {
        'XylophoneDo': 'C', 'XylophoneRe': 'D', 'XylophoneMi': 'E', 'XylophoneFa': 'F',
        'XylophoneSol': 'G', 'XylophoneLa': 'A', 'XylophoneSi': 'B', 'XylophoneDoSostenidoReb': 'C#',
        'XylophoneReSostenidoMib': 'D#', 'XylophoneFaSostenidoSolb': 'F#', 'XylophoneSolSostenidoLab': 'G#',
        'XylophoneLaSostenidoSib': 'A#'
    }

    def identify_chord_from_audio(self, audio_file, tolerance=5):
        return super().identify_chord_from_audio(audio_file, self.__notes_names, XylophoneIdentifier(), 8, tolerance)