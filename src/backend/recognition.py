'''
A tool to read a wav file and to give the text with timestamp.

@author Antoine Marion, Yannick Bellerose
@version 2.0.0
'''
import os
from wave_file import WaveFile
from helpers import get_start_and_end_indexes_per_segment, get_timestamp
import constants as c
import numpy as np
from deepspeech_model import DeepSpeechModel
import time
from tqdm import tqdm

class Recognizer(object):
    
    def __init__(self):
        self.input = None
        self.text_register = []
        self.timestamps_list = []
        self.deepspeech_model = None

    def set_model(self):
        """
        Set the deep speech model to be used.
        """
        self.deepspeech_model = DeepSpeechModel(
            "./src/backend/deepspeech-0.9.3-models.pbmm",
            "./src/backend/deepspeech-0.9.3-models.scorer"
            )
        self.deepspeech_model.set_model()

    def recognize(self, user_input, filename):
        '''
        Recognize an input in a given audio file
        '''
        assert(os.path.exists(filename))
        
        wave_file = WaveFile(filename)
        wave_file.get_wave_bytes()

        self.speech_to_text(wave_file)
        timestamp_list = get_timestamp(self.text_register, user_input)
        return timestamp_list

    def speech_to_text(self, WaveFile):
        '''
        Uses the deep speech engine to convert the wave file to text
        '''
        self.set_model()
        number_of_segments = int(WaveFile.duration / (c.STEP)) + 1
        index_list = np.zeros((number_of_segments, 2), dtype=np.int16)

        start = time.perf_counter()
        for i in tqdm(range(number_of_segments)):
            start_index, end_index = get_start_and_end_indexes_per_segment(len(WaveFile.audio_data), i, WaveFile.byterate)
            index_list[i][0] = start_index
            index_list[i][1] = end_index
            translated_string = self.deepspeech_model.translate_wave_segment(WaveFile.audio_data, start_index, end_index)
            self.text_register.append([i, translated_string])

        finish = time.perf_counter()
        print(f'Finished translation in {round(finish - start, 2)} seconds')