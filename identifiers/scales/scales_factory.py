from identifiers.scales.piano_scale import PianoScaleIdentifier

class ScalesIdentifierFactory:

    __identifier = {
        'Piano': PianoScaleIdentifier()
    }

    @staticmethod
    def initialize_identifier(key):
        identifier_class = ScalesIdentifierFactory.__identifier.get(key)
        if identifier_class is not None:
            return identifier_class
        return None