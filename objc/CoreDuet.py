
'''
Classes from the 'CoreDuet' framework.
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
    
    
CDBudget = _Class('CDBudget')
CDAttribute = _Class('CDAttribute')
CDAttributeOccurrence = _Class('CDAttributeOccurrence')
CDSession = _Class('CDSession')
CDGlanceLingerEvent = _Class('CDGlanceLingerEvent')
CDMonitorManager = _Class('CDMonitorManager')
CDTrendLogic = _Class('CDTrendLogic')
CDDevice = _Class('CDDevice')
HomeControlAnalysisPETCoreBehaviorAnalysisEvent = _Class('HomeControlAnalysisPETCoreBehaviorAnalysisEvent')
InteractionAnalysisPETInteractionEvents = _Class('InteractionAnalysisPETInteractionEvents')
CloudFamilyAnalysisPETContactEvent = _Class('CloudFamilyAnalysisPETContactEvent')
CloudFamilyAnalysisPETContactEvents = _Class('CloudFamilyAnalysisPETContactEvents')
InteractionAnalysisPETInteractionEvent = _Class('InteractionAnalysisPETInteractionEvent')
CloudFamilyAnalysisPETCloudFamilyAnalysisEvent = _Class('CloudFamilyAnalysisPETCloudFamilyAnalysisEvent')