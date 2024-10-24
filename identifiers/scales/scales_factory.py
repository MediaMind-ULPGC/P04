from identifiers.scales.piano_scale import PianoScaleIdentifier
from identifiers.scales.guitar_scale import GuitarScaleIdentifier

class ScalesIdentifierFactory:

    __identifier = {
        'Piano': PianoScaleIdentifier(),
        'Guitar': GuitarScaleIdentifier()
    }

    @staticmethod
    def initialize_identifier(key):
        identifier_class = ScalesIdentifierFactory.__identifier.get(key)
        if identifier_class is not None:
            return identifier_class
        return None