from .musical_notes import MusicalNotes

""" Nota Do """
class XylophoneDo(MusicalNotes):

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

""" Nota Re """
class XylophoneRe(MusicalNotes):

    __RE_FREQUENCIES = {
        "D3": 146.832,
        "D4": 293.665,
        "D5": 587.330,
        "D6": 1174.66
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__RE_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Mi """
class XylophoneMi(MusicalNotes):

    __MI_FREQUENCIES = {
        "E3": 164.814,
        "E4": 329.628,
        "E5": 659.255,
        "E6": 1318.51
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__MI_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Fa """
class XylophoneFa(MusicalNotes):

    __FA_FREQUENCIES = {
        "F3": 174.614,
        "F4": 349.228,
        "F5": 698.456,
        "F6": 1396.91
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__FA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Sol """
class XylophoneSol(MusicalNotes):

    __SOL_FREQUENCIES = {
        "G3": 195.998,
        "G4": 391.995,
        "G5": 783.991,
        "G6": 1567.98
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SOL_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota La """
class XylophoneLa(MusicalNotes):

    __LA_FREQUENCIES = {
        "A3": 220.000,
        "A4": 440.000,
        "A5": 880.000,
        "A6": 1760.00
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__LA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Si """
class XylophoneSi(MusicalNotes):

    __SI_FREQUENCIES = {
        "B3": 246.942,
        "B4": 493.883,
        "B5": 987.767,
        "B6": 1975.53
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SI_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None