from .piano_identifier import PianoIdentifier
from .guitar_identifier import GuitarIdentifier
from .trumpet_identifier import TrumpetIdentifier

class IdentifierFactory:

    __identifiers = {
        'Piano': PianoIdentifier(),
        'Guitar': GuitarIdentifier(),
        'Trumpet': TrumpetIdentifier()
    }

    @staticmethod
    def initialize_identifier(key):
        identifier_class = IdentifierFactory.__identifiers.get(key)
        if identifier_class is not None:
            return identifier_class
        return None

    