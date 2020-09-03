
'''
Classes from the 'ProactiveExperiments' framework.
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
    
    
PREResponsesClient = _Class('PREResponsesClient')
PREResponsesExperiment = _Class('PREResponsesExperiment')
PREResponseTappedEvent = _Class('PREResponseTappedEvent')
PREResponsesMetricsPET = _Class('PREResponsesMetricsPET')
PREResponsesGeneratedEvent = _Class('PREResponsesGeneratedEvent')
PREXPCClientHelpers = _Class('PREXPCClientHelpers')
PREResponsesTrialSimulator = _Class('PREResponsesTrialSimulator')
PREResponseItem = _Class('PREResponseItem')
PREResponsesTrial = _Class('PREResponsesTrial')
PREUMResponseItem = _Class('PREUMResponseItem')
PREAMResponseItem = _Class('PREAMResponseItem')
PREUMTrialExperiment = _Class('PREUMTrialExperiment')
PREAMResponseListGenerated = _Class('PREAMResponseListGenerated')
PREUMResponseList = _Class('PREUMResponseList')
PREUMMessageMetadata = _Class('PREUMMessageMetadata')
PREAMEngagedResponse = _Class('PREAMEngagedResponse')
PREUMEngagedResponseList = _Class('PREUMEngagedResponseList')