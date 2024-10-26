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

""" Nota Do# / Reb"""
class TrumpetDoSostenidoReb(MusicalNotes):

    __DO_SOSTENIDO_REB_FREQUENCIES = {
        "C#3": 138.591,
        "C#4": 277.183,
        "C#5": 554.365
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__DO_SOSTENIDO_REB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Re """
class TrumpetRe(MusicalNotes):

    __RE_FREQUENCIES = {
        "D3": 146.832,
        "D4": 293.665,
        "D5": 587.330
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__RE_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Re# / Mib """
class TrumpetReSostenidoMib(MusicalNotes):

    __RE_SOSTENIDO_MIB_FREQUENCIES = {
        "D#3": 155.563,
        "D#4": 311.127,
        "D#5": 622.254
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__RE_SOSTENIDO_MIB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Mi """
class TrumpetMi(MusicalNotes):

    __MI_FREQUENCIES = {
        "E3": 164.814,
        "E4": 329.628,
        "E5": 659.255
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__MI_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Fa """
class TrumpetFa(MusicalNotes):

    __FA_FREQUENCIES = {
        "F3": 174.614,
        "F4": 349.228,
        "F5": 698.456
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__FA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Fa# / Solb """
class TrumpetFaSostenidoSolb(MusicalNotes):

    __FA_SOSTENIDO_SOLB_FREQUENCIES = {
        "F#3": 184.997,
        "F#4": 369.994,
        "F#5": 739.989
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__FA_SOSTENIDO_SOLB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Sol """
class TrumpetSol(MusicalNotes):

    __SOL_FREQUENCIES = {
        "G3": 195.998,
        "G4": 391.995,
        "G5": 783.991
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SOL_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Sol# / Lab """
class TrumpetSolSostenidoLab(MusicalNotes):

    __SOL_SOSTENIDO_LAB_FREQUENCIES = {
        "G#3": 207.652,
        "G#4": 415.305,
        "G#5": 830.609
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SOL_SOSTENIDO_LAB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota La """
class TrumpetLa(MusicalNotes):

    __LA_FREQUENCIES = {
        "A3": 220.000,
        "A4": 440.000,
        "A5": 880.000
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__LA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota La# / Sib """
class TrumpetLaSostenidoSib(MusicalNotes):

    __LA_SOSTENIDO_SIB_FREQUENCIES = {
        "A#3": 233.082,
        "A#4": 466.164,
        "A#5": 932.328
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__LA_SOSTENIDO_SIB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Si """
class TrumpetSi(MusicalNotes):

    __SI_FREQUENCIES = {
        "B3": 246.942,
        "B4": 493.883,
        "B5": 987.767
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SI_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None
    