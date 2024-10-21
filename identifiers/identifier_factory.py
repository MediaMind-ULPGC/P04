from .piano_identifier import PianoIdentifier, PianoChordIdentifier
from .guitar_identifier import GuitarIdentifier, GuitarChordIdentifier
from .trumpet_identifier import TrumpetIdentifier
from .xylophone_identifier import XylophoneIdentifier
from .violin_identifier import ViolinIdentifier


class IdentifierFactory:

    __identifiers = {
        'Piano': PianoIdentifier(),
        'PianoChords': PianoChordIdentifier(),
        'Guitar': GuitarIdentifier(),
        'GuitarChords': GuitarChordIdentifier(),
        'Trumpet': TrumpetIdentifier(),
        'Xylophone': XylophoneIdentifier(),
        'Violin': ViolinIdentifier(),
    }

    @staticmethod
    def initialize_identifier(key):
        identifier_class = IdentifierFactory.__identifiers.get(key)
        if identifier_class is not None:
            return identifier_class
        return None

    