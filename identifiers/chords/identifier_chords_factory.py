from identifiers.chords.piano_chords import ChordPianoIdentifier
from identifiers.chords.guitar_chords import ChordGuitarIdentifier
from identifiers.chords.trumpet_chords import TrumpetChordsIdentifier
from identifiers.chords.xylophone_chords import XylophoneChordsIdentifier
from identifiers.chords.violin_chords import ChordViolinIdentifier


class IdentifierChordsFactory:

    __identifiers = {
        'Piano': ChordPianoIdentifier(),
        'Guitar': ChordGuitarIdentifier(),
        'Trumpet': TrumpetChordsIdentifier(),
        'Xylophone': XylophoneChordsIdentifier(),
        'Violin': ChordViolinIdentifier()
    }

    
    @staticmethod
    def initialize_identifier(key):
        identifier_class = IdentifierChordsFactory.__identifiers.get(key)
        if identifier_class is not None:
            return identifier_class
        return None