from .musical_notes import MusicalNotes

""" Nota Do """
class ViolinDo(MusicalNotes):

    __DO_FREQUENCIES = {
        "C3": 130.813,
        "C4": 261.626,
        "C5": 523.251,
        "C6": 1046.50,
        "C7": 2093.00
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__DO_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Do Sostenido """
class ViolinDoSostenidoReb(MusicalNotes):

    __DO_SOSTENIDO_REB_FREQUENCIES = {
        "C#3": 138.591,
        "C#4": 277.183,
        "C#5": 554.365,
        "C#6": 1108.73,
        "C#7": 2217.46
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__DO_SOSTENIDO_REB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None
    
""" Nota Re """
class ViolinRe(MusicalNotes):

    __RE_FREQUENCIES = {
        "D3": 146.832,
        "D4": 293.665,
        "D5": 587.330,
        "D6": 1174.66,
        "D7": 2349.32
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__RE_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Re Sostenido """
class ViolinReSostenidoMib(MusicalNotes):

    __RE_SOSTENIDO_MIB_FREQUENCIES = {
        "D#3": 155.563,
        "D#4": 311.127,
        "D#5": 622.254,
        "D#6": 1244.51,
        "D#7": 2489.02
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__RE_SOSTENIDO_MIB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Mi """
class ViolinMi(MusicalNotes):

    __MI_FREQUENCIES = {
        "E3": 164.814,
        "E4": 329.628,
        "E5": 659.255,
        "E6": 1318.51,
        "E7": 2637.02
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__MI_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Fa """
class ViolinFa(MusicalNotes):

    __FA_FREQUENCIES = {
        "F3": 174.614,
        "F4": 349.228,
        "F5": 698.456,
        "F6": 1396.91,
        "F7": 2793.83
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__FA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Fa Sostenido """
class ViolinFaSostenidoSolb(MusicalNotes):

    __FA_SOSTENIDO_SOLB_FREQUENCIES = {
        "F#3": 185.000,
        "F#4": 369.994,
        "F#5": 739.989,
        "F#6": 1479.98,
        "F#7": 2959.96
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__FA_SOSTENIDO_SOLB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Sol """
class ViolinSol(MusicalNotes):

    __SOL_FREQUENCIES = {
        "G3": 195.998,
        "G4": 391.995,
        "G5": 783.991,
        "G6": 1567.98,
        "G7": 3135.96
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SOL_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Sol Sostenido """
class ViolinSolSostenidoLab(MusicalNotes):

    __SOL_SOSTENIDO_LAB_FREQUENCIES = {
        "G#3": 207.652,
        "G#4": 415.305,
        "G#5": 830.609,
        "G#6": 1661.22,
        "G#7": 3322.44
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SOL_SOSTENIDO_LAB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota La """
class ViolinLa(MusicalNotes):

    __LA_FREQUENCIES = {
        "A3": 220.000,
        "A4": 440.000,
        "A5": 880.000,
        "A6": 1760.00,
        "A7": 3520.00
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__LA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota La Sostenido """
class ViolinLaSostenidoSib(MusicalNotes):

    __LA_SOSTENIDO_SIB_FREQUENCIES = {
        "A#3": 233.082,
        "A#4": 466.164,
        "A#5": 932.328,
        "A#6": 1864.66,
        "A#7": 3729.31
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__LA_SOSTENIDO_SIB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Si """
class ViolinSi(MusicalNotes):

    __SI_FREQUENCIES = {
        "B3": 246.942,
        "B4": 493.883,
        "B5": 987.767,
        "B6": 1975.53,
        "B7": 3951.07
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SI_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None
    