from .musical_notes import MusicalNotes

""" Nota Do """
class PianoDo(MusicalNotes):

    __DO_FREQUENCIES = {
        "C0": 16.3516,
        "C1": 32.7032,
        "C2": 65.4064,
        "C3": 130.813,
        "C4": 261.626,
        "C5": 523.251,
        "C6": 1046.50,
        "C7": 2093.00,
        "C8": 4186.01,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__DO_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None
    
""" Nota Do# / Reb"""
class PianoDoSostenidoReb(MusicalNotes):

    __DO_SOSTENIDO_REB_FREQUENCIES = {
        "C#0": 17.3239,
        "C#1": 34.6478,
        "C#2": 69.2957,
        "C#3": 138.591,
        "C#4": 277.183,
        "C#5": 554.365,
        "C#6": 1108.73,
        "C#7": 2217.46,
        "C#8": 4434.92,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__DO_SOSTENIDO_REB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Re """
class PianoRe(MusicalNotes):

    __RE_FREQUENCIES = {
        "D0": 18.3540,
        "D1": 36.7081,
        "D2": 73.4162,
        "D3": 146.832,
        "D4": 293.665,
        "D5": 587.330,
        "D6": 1174.66,
        "D7": 2349.32,
        "D8": 4698.63,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__RE_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Re# / Mib """
class PianoReSostenidoMib(MusicalNotes):

    __RE_SOSTENIDO_MIB_FREQUENCIES = {
        "D#0": 19.4454,
        "D#1": 38.8909,
        "D#2": 77.7817,
        "D#3": 155.563,
        "D#4": 311.127,
        "D#5": 622.254,
        "D#6": 1244.51,
        "D#7": 2489.02,
        "D#8": 4978.03,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__RE_SOSTENIDO_MIB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Mi """
class PianoMi(MusicalNotes):

    __MI_FREQUENCIES = {
        "E0": 20.6017,
        "E1": 41.2034,
        "E2": 82.4069,
        "E3": 164.814,
        "E4": 329.628,
        "E5": 659.255,
        "E6": 1318.51,
        "E7": 2637.02,
        "E8": 5274.04,
    }

    def __init__(self):
        super().__init__()
    
    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__MI_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Fa """
class PianoFa(MusicalNotes):

    __FA_FREQUENCIES = {
        "F0": 21.8268,
        "F1": 43.6535,
        "F2": 87.3071,
        "F3": 174.614,
        "F4": 349.228,
        "F5": 698.456,
        "F6": 1396.91,
        "F7": 2793.83,
        "F8": 5587.65,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__FA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Fa# / Solb """
class PianoFaSostenidoSolb(MusicalNotes):

    __FA_SOSTENIDO_SOLB_FREQUENCIES = {
        "F#0": 23.1247,
        "F#1": 46.2493,
        "F#2": 92.4986,
        "F#3": 184.997,
        "F#4": 369.994,
        "F#5": 739.989,
        "F#6": 1479.98,
        "F#7": 2959.96,
        "F#8": 5919.91,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__FA_SOSTENIDO_SOLB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Sol """
class PianoSol(MusicalNotes):
    
    __SOL_FREQUENCIES = {
        "G0": 24.5000,
        "G1": 49.0000,
        "G2": 98.0000,
        "G3": 196.000,
        "G4": 392.000,
        "G5": 783.991,
        "G6": 1568.00,
        "G7": 3136.00,
        "G8": 6272.00,
    }

    def is_note(self, frequency, tolerance=5):
        for octave, freq in self.__SOL_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota Sol# / Lab """
class PianoSolSostenidoLab(MusicalNotes):

    __SOL_SOSTENIDO_LAB_FREQUENCIES = {
        "G#0": 25.9565,
        "G#1": 51.9131,
        "G#2": 103.826,
        "G#3": 207.652,
        "G#4": 415.305,
        "G#5": 830.609,
        "G#6": 1661.22,
        "G#7": 3322.44,
        "G#8": 6644.88,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SOL_SOSTENIDO_LAB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota La """
class PianoLa(MusicalNotes):

    __LA_FREQUENCIES = {
        "A0": 27.5000,
        "A1": 55.0000,
        "A2": 110.000,
        "A3": 220.000,
        "A4": 440.000,
        "A5": 880.000,
        "A6": 1760.00,
        "A7": 3520.00,
        "A8": 7040.00,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__LA_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None

""" Nota La# / Sib """
class PianoLaSostenidoSib(MusicalNotes):

    __LA_SOSTENIDO_SIB_FREQUENCIES = {
        "A#0": 29.1352,
        "A#1": 58.2705,
        "A#2": 116.541,
        "A#3": 233.082,
        "A#4": 466.164,
        "A#5": 932.328,
        "A#6": 1864.66,
        "A#7": 3729.31,
        "A#8": 7458.62,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__LA_SOSTENIDO_SIB_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None
    
""" Nota Si """
class PianoSi(MusicalNotes):

    __SI_FREQUENCIES = {
        "B0": 30.8677,
        "B1": 61.7354,
        "B2": 123.471,
        "B3": 246.942,
        "B4": 493.883,
        "B5": 987.767,
        "B6": 1975.53,
        "B7": 3951.07,
        "B8": 7902.13,
    }

    def is_note(self, frequency, tolerance=5):        
        for octave, freq in self.__SI_FREQUENCIES.items():
            if abs(frequency - freq) < tolerance:
                return octave
        return None
    