from identifiers.scales.scale_identifier import ScaleIdentifier
from identifiers.single_notes.guitar_identifier import GuitarIdentifier

class GuitarScaleIdentifier(ScaleIdentifier):

    __guitar_identifier = GuitarIdentifier()

    def identify_scale_from_audio(self, audio_file, window_size=4096, overlap=2048, tolerance=5, num_frequencies=3, timestep=0.1):
        return super().identify_scale_from_audio(audio_file, self.__guitar_identifier, window_size, overlap, tolerance, num_frequencies, timestep, 6)
    
    def plot_scale_over_time(self, notes, frequencies, time_stamps, min_scale=0, max_scale=4000):
        return super().plot_scale_over_time(notes, frequencies, time_stamps, min_scale, max_scale)
    
    def plot_scale_over_time(self, notes, frequencies, time_stamps, min_scale=0, max_scale=4000):
        return super().plot_scale_over_time(notes, frequencies, time_stamps, min_scale, max_scale)