'''
unit tests for Recognizer
'''
from recognition import Recognizer

class TestRecognizer(object):
    def test_get_number_of_segment():
        recognizer = Recognizer()
        assert recognizer.get_number_of_segment() == 0