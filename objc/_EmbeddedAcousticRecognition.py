'''
Classes from the 'EmbeddedAcousticRecognition' framework.
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

    
EARCaesuraSilencePosteriorGenerator = _Class('EARCaesuraSilencePosteriorGenerator')
EARClientSilenceFeatures = _Class('EARClientSilenceFeatures')
EARSyncPSRAudioProcessor = _Class('EARSyncPSRAudioProcessor')
EMTResult = _Class('EMTResult')
EMTTranslator = _Class('EMTTranslator')
EARAudioResultsGenerator = _Class('EARAudioResultsGenerator')
EARAudioResult = _Class('EARAudioResult')
EMTToken = _Class('EMTToken')
EARCSpeechRecognitionResultStreamGlue = _Class('EARCSpeechRecognitionResultStreamGlue')
EARPSRAudioProcessor = _Class('EARPSRAudioProcessor')
EMTTokenizer = _Class('EMTTokenizer')
EARAudioReader = _Class('EARAudioReader')
EARKeywordFinder = _Class('EARKeywordFinder')
EARKeywordFinderResult = _Class('EARKeywordFinderResult')
EARTokenPronounciations = _Class('EARTokenPronounciations')
EARSdapiHelper = _Class('EARSdapiHelper')
