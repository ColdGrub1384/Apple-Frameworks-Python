
'''
Classes from the 'ProactiveInputPredictions' framework.
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
    
    
PSGUtilities = _Class('PSGUtilities')
PSGStructuredInfoSuggestion = _Class('PSGStructuredInfoSuggestion')
PSGStructuredInfoSuggestionCache = _Class('PSGStructuredInfoSuggestionCache')
PSGOperationalPredictedItem = _Class('PSGOperationalPredictedItem')
PSGInputSuggesterClient = _Class('PSGInputSuggesterClient')
PSGProactiveTrigger = _Class('PSGProactiveTrigger')
PSGInputSuggestionsResponseItem = _Class('PSGInputSuggestionsResponseItem')
PSGNameMentionsHandler = _Class('PSGNameMentionsHandler')
PSGProactiveTriggerHandler = _Class('PSGProactiveTriggerHandler')
PSGInputSuggestionsResponse = _Class('PSGInputSuggestionsResponse')
PSGTextualResponseSuggestion = _Class('PSGTextualResponseSuggestion')
PSGInputSuggestionsExplanationSet = _Class('PSGInputSuggestionsExplanationSet')
PSGInputSuggestionsExplanationSetGuardedData = _Class('PSGInputSuggestionsExplanationSetGuardedData')
PSGInputSuggestionsRequest = _Class('PSGInputSuggestionsRequest')
PSGInternalClient = _Class('PSGInternalClient')
PSGInputSuggester = _Class('PSGInputSuggester')
PSGWordBoundaryFSTGrammar = _Class('PSGWordBoundaryFSTGrammar')
PSGLMWrapper = _Class('PSGLMWrapper')
PSGDiagnostics = _Class('PSGDiagnostics')