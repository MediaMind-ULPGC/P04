from .piano_identifier import PianoIdentifier
from .guitar_identifier import GuitarIdentifier
from .trumpet_identifier import TrumpetIdentifier
from .xylophone_identifier import XylophoneIdentifier
from .violin_identifier import ViolinIdentifier


class IdentifierFactory:

    __identifiers = {
        'Piano': PianoIdentifier(),
        'Guitar': GuitarIdentifier(),
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

    