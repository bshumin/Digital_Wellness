#!/usr/bin/env python3
'''
Convenient `fluteline`_ producers and consumers to use with the main
:class:`watson_streaming.Transcriber`.
'''
from gtts import gTTS
from playsound import playsound
import json
import fluteline
import os
from gtts import gTTS
import pyttsx3
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# ID provided by Hudson in email
assistCred = {
  "apikey": "T44GGYi18K6A9i7f7UeZKxfPO41SKBIV6X3Mtp7tjwSj",
  "iam_apikey_description": "Auto-generated for key ad3fda5a-d0e7-48a3-8aeb-9dffb461478d",
  "iam_apikey_name": "Auto-generated service credentials",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/911739c752004265a521eb5f0a2b6e41::serviceid:ServiceId-ee80fbff-8607-4e04-afe4-c65f96406e65",
  "url": "https://api.us-south.assistant.watson.cloud.ibm.com/instances/b5122f34-f675-4fcb-8116-3f3a86d11c82"
}

treeResponses = ['start', 'start', '73', '170', 'white']
intentList = ['start', 'start', 'height', 'weight', 'race']

questionNumber = 0

sessionCreated = False

class Interpret(fluteline.Consumer):
    '''
    Chain consumer to intperet speech results
    '''

    def consume(self, item):
        global directory
        global questionNumber
        speech = ""
        if 'results' in item and item['results'][0]['final'] is True: # changed '=' to 'is'
            # speech = item['results'][0]['alternatives'][0]['transcript']
            speech = treeResponses[questionNumber]  # force speech to be expected response from list
            print("speech before NLP: " + speech)
            # speech = assistant(speech.lower().split())
            response = assistant(speech.lower())

            # print('Assistant spoken response: ' + response['output']['generic'][0]['text'])  # FIXME if added->error
            print('Interpreted user intent: ' + response['output']['intents'][0]['intent'])
            if response['output']['intents'][0]['intent'].lower() == intentList[questionNumber].lower():
                questionNumber += 1
                print("Response matched assistant question")
            print('-----------------------------------------')
            engine = pyttsx3.init()
            engine.say(speech)
            engine.runAndWait()

        # directory = r"C:/Users/Brandon/PycharmProjects/Questionnaire"
        # filename = directory + "/output.mp3"
        #
        # tts = gTTS(text=speech, lang='en')
        #
        # tts.save(filename)
        # playsound(filename)
        # os.remove(filename)
        # # close()
        # print("the dir after removal: %s" %os.listdir(os.getcwd()))

# altered indent to make def work for Interpret class calls
def assistant(speech):
    global sessionCreated
    global session_key
    authenticator = IAMAuthenticator('T44GGYi18K6A9i7f7UeZKxfPO41SKBIV6X3Mtp7tjwSj')
    assistant = AssistantV2(
        version='2020-01-26',
        authenticator=authenticator
    )

    assistant.set_service_url('https://gateway.watsonplatform.net/assistant/api')

    if sessionCreated is False:
        session = assistant.create_session(assistant_id='cb4dacb9-085f-4a99-adfa-96e54d786f90').get_result()
        session_json = json.dumps(session)
        print(session_json)
        session_key = (json.loads(session_json))
        print(session_key["session_id"])
        print('TRIGGERED IF STATEMENT')
        sessionCreated = True

    response = assistant.message(
         assistant_id='cb4dacb9-085f-4a99-adfa-96e54d786f90',
         session_id=session_key["session_id"],
         input={
             'message_type': 'text',
             'text': speech
         }
    ).get_result()
    print(json.dumps(response, indent=2))
    return response
