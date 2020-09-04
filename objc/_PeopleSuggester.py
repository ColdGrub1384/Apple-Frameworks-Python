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

    
_PSBehaviorRuleFeatureExtraction = _Class('_PSBehaviorRuleFeatureExtraction')
_PSInteractionStoreUtils = _Class('_PSInteractionStoreUtils')
_PSMessagesPinningSuggestion = _Class('_PSMessagesPinningSuggestion')
_PSContactEmbeddingFeatureExtractor = _Class('_PSContactEmbeddingFeatureExtractor')
_PS_TPSDiscoverabilitySignal = _Class('_PS_TPSDiscoverabilitySignal')
_PSContactSuggestionHandleAndApp = _Class('_PSContactSuggestionHandleAndApp')
_PSPhotoSuggestions = _Class('_PSPhotoSuggestions')
_PSIMCoreUtils = _Class('_PSIMCoreUtils')
_PSRuleMiningModel = _Class('_PSRuleMiningModel')
_PSSuggestion = _Class('_PSSuggestion')
_PSSuggestionTemplate = _Class('_PSSuggestionTemplate')
_PSSuggestionProxy = _Class('_PSSuggestionProxy')
_PSFeaturizedBehaviorRule = _Class('_PSFeaturizedBehaviorRule')
_PSContactEmbeddingDataCollectionUtilities = _Class('_PSContactEmbeddingDataCollectionUtilities')
_PSRecipient = _Class('_PSRecipient')
_PSSiriHandleRanker = _Class('_PSSiriHandleRanker')
_PSRuleOverlapFeedback = _Class('_PSRuleOverlapFeedback')
PSDESPlugin = _Class('PSDESPlugin')
_PSFeedback = _Class('_PSFeedback')
_PSKNNModel = _Class('_PSKNNModel')
_PSPhotoUtils = _Class('_PSPhotoUtils')
_PSPersonalizationEvaluation = _Class('_PSPersonalizationEvaluation')
scoredRule = _Class('scoredRule')
FeatureVectorCoordinates = _Class('FeatureVectorCoordinates')
_PSBehaviorRuleRankingUtilities = _Class('_PSBehaviorRuleRankingUtilities')
_PSContactEmbedding = _Class('_PSContactEmbedding')
_PSSiriNLLogger = _Class('_PSSiriNLLogger')
_PSContactSuggestion = _Class('_PSContactSuggestion')
_PSSuggesterConfiguration = _Class('_PSSuggesterConfiguration')
_PSMessagesZkwFeedback = _Class('_PSMessagesZkwFeedback')
_PSAppUsageUtilities = _Class('_PSAppUsageUtilities')
_PSMapsPredictionContext = _Class('_PSMapsPredictionContext')
_PSMapsFeedback = _Class('_PSMapsFeedback')
_PSFeedbackAction = _Class('_PSFeedbackAction')
_PSMapsFeedbackAction = _Class('_PSMapsFeedbackAction')
_PSFamilyUtilities = _Class('_PSFamilyUtilities')
_PSShareSheetSuggestLessFeedback = _Class('_PSShareSheetSuggestLessFeedback')
_PSPredictionContext = _Class('_PSPredictionContext')
_PSHeuristics = _Class('_PSHeuristics')
_PSMessagesPinningUtilities = _Class('_PSMessagesPinningUtilities')
_PSFamilyMLPredictionTask = _Class('_PSFamilyMLPredictionTask')
_PSContactResolver = _Class('_PSContactResolver')
_PSInteractionAndContactMonitor = _Class('_PSInteractionAndContactMonitor')
_PSHandleRanker = _Class('_PSHandleRanker')
_PSMessagesPinningSuggester = _Class('_PSMessagesPinningSuggester')
_PSSiriHandleRankerPredictionContext = _Class('_PSSiriHandleRankerPredictionContext')
_PSMapsSuggester = _Class('_PSMapsSuggester')
_PSProximityBooster = _Class('_PSProximityBooster')
_PSAttachment = _Class('_PSAttachment')
_PSFamilyMLModel = _Class('_PSFamilyMLModel')
_PSContactEmbeddingUtilities = _Class('_PSContactEmbeddingUtilities')
_PSSuggester = _Class('_PSSuggester')
_PSMailUtils = _Class('_PSMailUtils')
_PSFamilyRecommender = _Class('_PSFamilyRecommender')
_PSFeedbackUtils = _Class('_PSFeedbackUtils')
_PSSiriNLRankerUtilities = _Class('_PSSiriNLRankerUtilities')
_PSKNNeighbor = _Class('_PSKNNeighbor')
_PSFamilyFeatureExtractor = _Class('_PSFamilyFeatureExtractor')
_PSConstants = _Class('_PSConstants')
_PSEnsembleModel = _Class('_PSEnsembleModel')
_PSContactSuggester = _Class('_PSContactSuggester')
_PSLogging = _Class('_PSLogging')
_PSRuleRankingMLModel = _Class('_PSRuleRankingMLModel')
_PSMessagesPinningFeedback = _Class('_PSMessagesPinningFeedback')
_PSAutocompleteSuggestion = _Class('_PSAutocompleteSuggestion')
ContactEmbeddingAnalysisPETNeuralNetEmbedding = _Class('ContactEmbeddingAnalysisPETNeuralNetEmbedding')
CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent = _Class('CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent')
ContactEmbeddingAnalysisPETContactEmbeddingAnalysisEvent = _Class('ContactEmbeddingAnalysisPETContactEmbeddingAnalysisEvent')
ContactEmbeddingAnalysisPETContactEmbeddingArrayEvent = _Class('ContactEmbeddingAnalysisPETContactEmbeddingArrayEvent')
