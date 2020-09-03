
'''
Classes from the 'PeopleSuggester' framework.
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
    
    
PSDESPlugin = _Class('PSDESPlugin')
scoredRule = _Class('scoredRule')
FeatureVectorCoordinates = _Class('FeatureVectorCoordinates')
ContactEmbeddingAnalysisPETNeuralNetEmbedding = _Class('ContactEmbeddingAnalysisPETNeuralNetEmbedding')
CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent = _Class('CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent')
ContactEmbeddingAnalysisPETContactEmbeddingAnalysisEvent = _Class('ContactEmbeddingAnalysisPETContactEmbeddingAnalysisEvent')
ContactEmbeddingAnalysisPETContactEmbeddingArrayEvent = _Class('ContactEmbeddingAnalysisPETContactEmbeddingArrayEvent')