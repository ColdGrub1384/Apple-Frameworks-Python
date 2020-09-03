
'''
Classes from the 'CoreSuggestionsML' framework.
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
    
    
SGQuickResponsesDatabase = _Class('SGQuickResponsesDatabase')
SGQuickResponsesCategoryScore = _Class('SGQuickResponsesCategoryScore')
SGQuickResponsesClassScore = _Class('SGQuickResponsesClassScore')
SGQuickResponsesDistributingCount = _Class('SGQuickResponsesDistributingCount')
SGQuickResponsesScoring = _Class('SGQuickResponsesScoring')
SGQuickResponsesRanking = _Class('SGQuickResponsesRanking')
SGSelectiveTransformer = _Class('SGSelectiveTransformer')
SGTokenJoiningTransformer = _Class('SGTokenJoiningTransformer')
SGRandomization = _Class('SGRandomization')
SGModelFeatures = _Class('SGModelFeatures')
SGModelSource = _Class('SGModelSource')
SGMessagePairIterator = _Class('SGMessagePairIterator')
SGMessagePair = _Class('SGMessagePair')
SGDefaultAssets = _Class('SGDefaultAssets')
SGTextLabelTransformer = _Class('SGTextLabelTransformer')
SGStringLabelingTransformer = _Class('SGStringLabelingTransformer')
SGConversationTurn = _Class('SGConversationTurn')
SGConversationTracker = _Class('SGConversationTracker')
SGLazyInit = _Class('SGLazyInit')
SGQuickResponsesEngagementDeltas = _Class('SGQuickResponsesEngagementDeltas')
SGQuickResponsesReplyRecord = _Class('SGQuickResponsesReplyRecord')
SGQuickResponsesRecords = _Class('SGQuickResponsesRecords')
SGQuickResponsesStore = _Class('SGQuickResponsesStore')
SGQuickResponsesModelRules = _Class('SGQuickResponsesModelRules')
SGQuickResponsesTransformerInstance = _Class('SGQuickResponsesTransformerInstance')
SGModelSampler = _Class('SGModelSampler')
SGQuickResponsesModel = _Class('SGQuickResponsesModel')
SGQuickResponsesClassificationModel = _Class('SGQuickResponsesClassificationModel')
SGQuickResponsesInference = _Class('SGQuickResponsesInference')
SGQuickResponse = _Class('SGQuickResponse')
SGPipelineTransformer = _Class('SGPipelineTransformer')
SGStringPreprocessor = _Class('SGStringPreprocessor')
SGStringPreprocessingTransformer = _Class('SGStringPreprocessingTransformer')
SGQuickResponsesPersonalization = _Class('SGQuickResponsesPersonalization')
SGQuickResponsesReplyOption = _Class('SGQuickResponsesReplyOption')
SGNestedArray = _Class('SGNestedArray')
SGModelAsset = _Class('SGModelAsset')
SGQuickResponsesConfig = _Class('SGQuickResponsesConfig')
SGCustomResponsesParameters = _Class('SGCustomResponsesParameters')
SGQuickResponsesReplies = _Class('SGQuickResponsesReplies')
SGQuickResponsesReplyModel = _Class('SGQuickResponsesReplyModel')
SGQuickResponsesPredictionParameters = _Class('SGQuickResponsesPredictionParameters')
SGQuickResponsesClassificationParameters = _Class('SGQuickResponsesClassificationParameters')
SGModelHyperparameters = _Class('SGModelHyperparameters')
SGLanguageDetection = _Class('SGLanguageDetection')