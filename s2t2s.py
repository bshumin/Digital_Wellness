# speech to text to speech
from gtts import gTTS
from playsound import playsound
import json
import argparse
import time

import fluteline

import watson_streaming
import watson_streaming.utilities
import slu

directory = r"C:\Users\Brandon\PycharmProjects\Questionnaire\credentials.json"  # FIXME change as needed


# close()
# ----------------------------------------------------------
#!/usr/bin/env python3

'''
Speech to text transcription, from your microphone, in real-time, using IBM Watson.
'''

def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('credentials', help=directory)
    return parser.parse_args()


def main():
    args = directory
    settings = {
        'inactivity_timeout': -1,  # Don't kill me after 30 seconds
        'interim_results': True,
    }

    nodes = [
        watson_streaming.utilities.MicAudioGen(),
        watson_streaming.Transcriber(settings, directory),
        slu.Interpret(),
    ]

    fluteline.connect(nodes)
    fluteline.start(nodes)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        fluteline.stop(nodes)

# tts = gTTS(text='Stopping the car at the nearest safe location', lang='en')
# tts.save(directory + "output.mp3")
# playsound(directory + 'output.mp3')

if __name__ == '__main__':
    main()
