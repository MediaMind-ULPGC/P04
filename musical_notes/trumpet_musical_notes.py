from .musical_notes import MusicalNotes

""" Nota Do """
class TrumpetDo(MusicalNotes):

    __DO_FREQUENCIES = {
        "C3": 130.813,
        "C4": 261.626,
        "C5": 523.251,
        "C6": 1046.50
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__DO_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None
    