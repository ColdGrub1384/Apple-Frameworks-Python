'''
Classes from the 'TextToSpeech' framework.
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

    
TTSSpeechVoice = _Class('TTSSpeechVoice')
TTSSpeechRequestOwner = _Class('TTSSpeechRequestOwner')
TTSAudioSessionChannel = _Class('TTSAudioSessionChannel')
TTSSpeechSynthesizer = _Class('TTSSpeechSynthesizer')
TTSSpeechRequest = _Class('TTSSpeechRequest')
TTSSpeechChannel = _Class('TTSSpeechChannel')
TTSFormatArgument = _Class('TTSFormatArgument')
TTSAudioSession = _Class('TTSAudioSession')
TTSAssetBase = _Class('TTSAssetBase')
TTSVoiceAsset = _Class('TTSVoiceAsset')
TTSVoiceResourceAsset = _Class('TTSVoiceResourceAsset')
TTSSubstitution = _Class('TTSSubstitution')
