#!/usr/bin/env python3

'''
Speech to text transcription, from your microphone, in real-time, using IBM Watson.
'''

import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from gtts import gTTS
from playsound import playsound

directory='/home/tianyiz/Desktop/workdirectory/digitalWellness/'

authenticator = IAMAuthenticator('THEmPUglWCGy0SfdtveG6L6ST5sncDy1GeiYpnhL5_xz')
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url('https://stream.watsonplatform.net/speech-to-text/api')

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        if 'results' in data and data['results'][0]['final']==True:
            speech = data['results'][0]['alternatives'][0]['transcript']
            print ("\n\nUser response:", speech,"\n\n")
        #with open('transcript_result.json', 'w') as fp:
        #    json.dump(data,fp,indent=2)

    def on_error(self, error):
        #print('Error received: {}'.format(error))
        print("Nothing")

    def on_inactivity_timeout(self, error):
        #print('Inactivity timeout: {}'.format(error))
        print("Nothing")

myRecognizeCallback = MyRecognizeCallback()

from ibm_watson import ApiException
from pygame import mixer  # Load the popular external library

questions=['\nYour current health status: in general would you say it is\n',
           '\nHow many cups of fruits do you eat daily\n',
           '\nHow many cups of vegetable do you eat daily\n']

questionsAudio=['q1.mp3',
                'q2.mp3',
                'q3.mp3']
t=0

while(t<3):
    playsound(directory + questionsAudio[t])
    close()
    #mixer.init()
    #mixer.music.load(directory+questionsAudio[t])
    #mixer.music.play()
    name=input(questions[t])

    audio_file = open(name, "rb")
    try:
        audio_source = AudioSource(audio_file)
        result = stt.recognize_using_websocket(
                    audio=audio_source,
                    content_type='audio/mp3',
                    recognize_callback=myRecognizeCallback,
                    model='en-US_BroadbandModel',
                    #keywords=['colorado', 'tornado', 'tornadoes'],
                    #keywords_threshold=0.5,
                    max_alternatives=3)
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~`",result)

    except ApiException as ex:
        print("Nothing")
        #print("Method failed with status code ", str(ex.code), ": ", ex.messag)
    t=t+1


'''
import argparse
import time

import watson_streaming
import watson_streaming.utilities
import slu

import fluteline


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('credentials', help='path to credentials.json')
    return parser.parse_args()


def main():
    #args = parse_arguments()
    settings = {
        'inactivity_timeout': -1,  # Don't kill me after 30 seconds
        'interim_results': True,
    }

    nodes = [
        watson_streaming.utilities.MicAudioGen(),
        watson_streaming.Transcriber(settings, '/home/tianyiz/Desktop/workdirectory/digitalWellness/credential.json'),
        slu.Interpret(),
    ]

    fluteline.connect(nodes)
    fluteline.start(nodes)

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        pass
    finally:
        fluteline.stop(nodes)


if __name__ == '__main__':
    main()
'''
