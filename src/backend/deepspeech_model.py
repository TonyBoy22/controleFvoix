'''
class wrapper deepspeech model
'''
import deepspeech


class DeepSpeechModel(object):
    def __init__(self, model_path, scorer_path):
        self.model = None
        self.model_path = model_path
        self.scorer_path = scorer_path
        self.beam_width = 500
        self.lm_alpha = 0.93
        self.lm_beta = 1.18

    def set_hyper_parameters(self, beam_width, lm_alpha, lm_beta):
        self.beam_width = beam_width
        self.lm_alpha = lm_alpha
        self.lm_beta = lm_beta

    def set_model(self):
        self.model = deepspeech.Model(self.model_path)
        self.model.enableExternalScorer(self.scorer_path)
        self.model.setScorerAlphaBeta(self.lm_alpha, self.lm_beta)
        self.model.setBeamWidth(self.beam_width)

    def translate_wave_segment(self, audio_data, start_index, end_index):
        translated_string = self.model.stt(audio_data[start_index:end_index])
        return translated_string
        