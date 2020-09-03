'''
Classes from the 'AXSpeechAssetServices' framework.
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

    
AXSettingsVoiceAssetManager = _Class('AXSettingsVoiceAssetManager')
AXSpeechAssetMonitorHelper = _Class('AXSpeechAssetMonitorHelper')
AXSpeechPronunciationHelper = _Class('AXSpeechPronunciationHelper')
AXSpeechPronunciationOptions = _Class('AXSpeechPronunciationOptions')
