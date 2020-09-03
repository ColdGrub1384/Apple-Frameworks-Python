'''
Classes from the 'ProactiveInputPredictionsInternals' framework.
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

    
PSGResponseSuggestionsExpConfigDefaults = _Class('PSGResponseSuggestionsExpConfigDefaults')
PSGInputSuggesterMetricsLogger = _Class('PSGInputSuggesterMetricsLogger')
PSGResponseSuggestionsExpConfig = _Class('PSGResponseSuggestionsExpConfig')
PSGXPCServer = _Class('PSGXPCServer')
PSGExperimentResolver = _Class('PSGExperimentResolver')
PSGWordBoundarySuggestionsExpConfigGuardedData = _Class('PSGWordBoundarySuggestionsExpConfigGuardedData')
PSGResponseSuggestionsExpConfigGuardedData = _Class('PSGResponseSuggestionsExpConfigGuardedData')
PSGWordBoundarySuggestionsExpConfigDefaults = _Class('PSGWordBoundarySuggestionsExpConfigDefaults')
PSGInternalRequestHandler = _Class('PSGInternalRequestHandler')
PSGWordBoundarySuggestionsExpConfig = _Class('PSGWordBoundarySuggestionsExpConfig')
PSGInternalServerDelegate = _Class('PSGInternalServerDelegate')
PSGInputSuggesterServerRequestHandler = _Class('PSGInputSuggesterServerRequestHandler')
PSGInputSuggesterServerDelegate = _Class('PSGInputSuggesterServerDelegate')
PSGPBTrigger = _Class('PSGPBTrigger')
PSGPBQuery = _Class('PSGPBQuery')
PSGPBEngagement = _Class('PSGPBEngagement')
PSGPBError = _Class('PSGPBError')
PSGPBPrediction = _Class('PSGPBPrediction')
PSGPBImpression = _Class('PSGPBImpression')
PSGPBTypingSpeed = _Class('PSGPBTypingSpeed')
