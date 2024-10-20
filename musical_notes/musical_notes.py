from abc import ABC, abstractmethod

class MusicalNotes(ABC):

    @abstractmethod
    def is_note(self, frequency, note_frequencies, tolerance=5):
        pass