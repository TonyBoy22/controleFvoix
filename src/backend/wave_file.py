'''
class around Wave files
'''

from pydub import AudioSegment

class WaveFile(object):
    def __init__(self, filename_path):
        self.filename = filename_path
        self.duration = None
        self.byterate = None
        self.audio_data = None

    def get_wave_bytes(self):
        wave_file = AudioSegment.from_file(self.filename)
        self.byterate = wave_file.frame_rate
        self.duration = wave_file.duration_seconds
        self.audio_data = wave_file.get_array_of_samples()

    def get_wave_duration(self):
        self.duration = len(self.audio_data) / self.byterate
