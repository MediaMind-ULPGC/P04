from .musical_notes import MusicalNotes

""" Nota Do (en diferentes cuerdas de la guitarra) """
class GuitarDo(MusicalNotes):

    __DO_FREQUENCIES = {
        "C2": 65.4064,   
        "C3": 130.813,
        "C4": 261.626,  
        "C5": 523.251
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__DO_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Do# / Reb"""
class GuitarDoSostenidoReb(MusicalNotes):

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
class GuitarRe(MusicalNotes):
    
    __RE_FREQUENCIES = {
        "D2": 73.4162,
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
class GuitarReSostenidoMib(MusicalNotes):

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
class GuitarMi(MusicalNotes):

    __MI_FREQUENCIES = {
        "E2": 82.4069,
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
class GuitarFa(MusicalNotes):

    __FA_FREQUENCIES = {
        "F2": 87.3071,
        "F3": 174.614,
        "F4": 349.228
    }

    def is_note(self, frequency, tolerance=5):   
        for octave, freq in self.__FA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Fa# / Solb """
class GuitarFaSostenidoSolb(MusicalNotes):

    __FA_SOSTENIDO_SOLB_FREQUENCIES = {
        "F#2": 92.4986,
        "F#3": 184.997,
        "F#4": 369.994
    }

    def is_note(self, frequency, tolerance=5):   
        for octave, freq in self.__FA_SOSTENIDO_SOLB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Sol """
class GuitarSol(MusicalNotes):

    __SOL_FREQUENCIES = {
        "G2": 97.9989,
        "G3": 195.998,
        "G4": 391.995
    }

    def is_note(self, frequency, tolerance=5):   
        for octave, freq in self.__SOL_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Sol# / Lab """
class GuitarSolSostenidoLab(MusicalNotes):

    __SOL_SOSTENIDO_LAB_FREQUENCIES = {
        "G#2": 103.826,
        "G#3": 207.652,
        "G#4": 415.305
    }

    def is_note(self, frequency, tolerance=5):   
        for octave, freq in self.__SOL_SOSTENIDO_LAB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota La """
class GuitarLa(MusicalNotes):

    __LA_FREQUENCIES = {
        "A2": 110.000,
        "A3": 220.000,
        "A4": 440.000
    }

    def is_note(self, frequency, tolerance=5):   
        for octave, freq in self.__LA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota La# / Sib """
class GuitarLaSostenidoSib(MusicalNotes):

    __LA_SOSTENIDO_SIB_FREQUENCIES = {
        "A#2": 116.541,
        "A#3": 233.082,
        "A#4": 466.164
    }

    def is_note(self, frequency, tolerance=5):   
        for octave, freq in self.__LA_SOSTENIDO_SIB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Si """
class GuitarSi(MusicalNotes):

    __SI_FREQUENCIES = {
        "B2": 123.471,
        "B3": 246.942,
        "B4": 493.883
    }

    def is_note(self, frequency, tolerance=5):   
        for octave, freq in self.__SI_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None