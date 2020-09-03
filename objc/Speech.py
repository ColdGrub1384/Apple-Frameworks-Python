
'''
Classes from the 'Speech' framework.
'''
    
try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None
        
def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None
    
    
SFSpeechAssetManager = _Class('SFSpeechAssetManager')
SFTranscription = _Class('SFTranscription')
SFSpeechRecognitionRequest = _Class('SFSpeechRecognitionRequest')
SFSpeechAudioBufferRecognitionRequest = _Class('SFSpeechAudioBufferRecognitionRequest')
SFSpeechURLRecognitionRequest = _Class('SFSpeechURLRecognitionRequest')
SFUtilities = _Class('SFUtilities')
SFTranscriptionSegment = _Class('SFTranscriptionSegment')
SFSpeechRecognizer = _Class('SFSpeechRecognizer')
SFSpeechRecognitionResult = _Class('SFSpeechRecognitionResult')
SFSpeechLanguageModel = _Class('SFSpeechLanguageModel')
SFSpeechRecognitionTask = _Class('SFSpeechRecognitionTask')
SFVoiceAnalytics = _Class('SFVoiceAnalytics')
SFAcousticFeature = _Class('SFAcousticFeature')