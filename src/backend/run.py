'''
test file to run the backend locally
'''
from recognition import Recognizer

def main(user_input, audio_file):
    recognizer = Recognizer()
    timestamp_list = recognizer.recognize('energy', audio_file)
    return f"matches for {user_input} found at seconds {timestamp_list} of file {audio_file}"

if __name__ == '__main__':
    audio_file = "./src/backend/longer_test_file.wav"
    matches = main(audio_file)
    print(matches)