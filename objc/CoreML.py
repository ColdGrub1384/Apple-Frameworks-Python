
'''
Classes from the 'CoreML' framework.
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
    
    
MLBackgroundWatchdog = _Class('MLBackgroundWatchdog')
MLImageSizeConstraint = _Class('MLImageSizeConstraint')
MLMultiArrayConstraint = _Class('MLMultiArrayConstraint')
MLLayerPath = _Class('MLLayerPath')
MLInternalSettings = _Class('MLInternalSettings')
MLAppleWordEmbeddingParameters = _Class('MLAppleWordEmbeddingParameters')
MLFillBrick = _Class('MLFillBrick')
MLModelMetadata = _Class('MLModelMetadata')
MLModelDescriptionUtils = _Class('MLModelDescriptionUtils')
MLFairPlayKeyLoadingSession = _Class('MLFairPlayKeyLoadingSession')
MLSequenceConstraint = _Class('MLSequenceConstraint')
MLModelIOUtils = _Class('MLModelIOUtils')
MLSVMLoader = _Class('MLSVMLoader')
MLConcatNDBrick = _Class('MLConcatNDBrick')
MLIndexedBatchProvider = _Class('MLIndexedBatchProvider')
MLWindowedBatchProvider = _Class('MLWindowedBatchProvider')
MLLazyUnionBatchProvider = _Class('MLLazyUnionBatchProvider')
MLBatchProviderUtils = _Class('MLBatchProviderUtils')
MLAppleWordTaggerParameters = _Class('MLAppleWordTaggerParameters')
MLPredictionOptions = _Class('MLPredictionOptions')
MLSupervisedOnlineUpdateOptions = _Class('MLSupervisedOnlineUpdateOptions')
MLFeatureFlags = _Class('MLFeatureFlags')
MLCloudDeploymentUtils = _Class('MLCloudDeploymentUtils')
MLTask = _Class('MLTask')
MLUpdateTask = _Class('MLUpdateTask')
InternalCustomGatherTree = _Class('InternalCustomGatherTree')
MLClipBrick = _Class('MLClipBrick')
MLNonMaximumSuppressionParameters = _Class('MLNonMaximumSuppressionParameters')
MLDefaultCustomLayerFactory = _Class('MLDefaultCustomLayerFactory')
MLShufflingBatchProvider = _Class('MLShufflingBatchProvider')
MLNearestNeighborsSingleKdTreeIndex = _Class('MLNearestNeighborsSingleKdTreeIndex')
MLPipelineLoader = _Class('MLPipelineLoader')
MLAppleTextClassifierParameters = _Class('MLAppleTextClassifierParameters')
MLNeuralNetworksCompileTimeParams = _Class('MLNeuralNetworksCompileTimeParams')
MLSlidingWindowsBrick = _Class('MLSlidingWindowsBrick')
MLClassifierResult = _Class('MLClassifierResult')
MLKeyManager = _Class('MLKeyManager')
MLDictionaryFeatureProvider = _Class('MLDictionaryFeatureProvider')
MLModelEncryptionUtils = _Class('MLModelEncryptionUtils')
InternalCustomTileLike = _Class('InternalCustomTileLike')
MLNNLayerComputeUnitSelectionUtils = _Class('MLNNLayerComputeUnitSelectionUtils')
MLCloudSession = _Class('MLCloudSession')
MLNumericConstraint = _Class('MLNumericConstraint')
MLFeatureTypeUtils = _Class('MLFeatureTypeUtils')
MLNeuralNetworkUpdateUtils = _Class('MLNeuralNetworkUpdateUtils')
MLDataConversionUtils = _Class('MLDataConversionUtils')
MLRegressorResult = _Class('MLRegressorResult')
MLAppleImageFeatureExtractorParameters = _Class('MLAppleImageFeatureExtractorParameters')
MLAppleImageFeatureExtractorObjectPrintParameters = _Class('MLAppleImageFeatureExtractorObjectPrintParameters')
MLAppleImageFeatureExtractorScenePrintParameters = _Class('MLAppleImageFeatureExtractorScenePrintParameters')
MLModelCollectionEntry = _Class('MLModelCollectionEntry')
MLUpdateProgressHandlers = _Class('MLUpdateProgressHandlers')
MLUpdateProgressHandlersUtils = _Class('MLUpdateProgressHandlersUtils')
MLLogging = _Class('MLLogging')
MLSaver = _Class('MLSaver')
MLCompiler = _Class('MLCompiler')
MLCompilerResult = _Class('MLCompilerResult')
MLCompilerOptions = _Class('MLCompilerOptions')
MLBackgroundRunner = _Class('MLBackgroundRunner')
MLKNearestNeighborsClassifierParameters = _Class('MLKNearestNeighborsClassifierParameters')
MLGeluActivationBrick = _Class('MLGeluActivationBrick')
MLFairPlayDecryptSession = _Class('MLFairPlayDecryptSession')
MLFairPlayDecryptSessionManager = _Class('MLFairPlayDecryptSessionManager')
MLModelInterface = _Class('MLModelInterface')
MLSequence = _Class('MLSequence')
MLSliceNDBrick = _Class('MLSliceNDBrick')
MLReporterUtils = _Class('MLReporterUtils')
MLReporter = _Class('MLReporter')
MLGKDecisionTree = _Class('MLGKDecisionTree')
MLBroadcastToBrick = _Class('MLBroadcastToBrick')
MLGatherBrick = _Class('MLGatherBrick')
MLLoaderEvent = _Class('MLLoaderEvent')
MLModelExecutionSchedule = _Class('MLModelExecutionSchedule')
CoreMLVersion = _Class('CoreMLVersion')
MLModelVisionFeaturePrintInfo = _Class('MLModelVisionFeaturePrintInfo')
MLNearestNeighborsLinearIndex = _Class('MLNearestNeighborsLinearIndex')
MLFeatureDescription = _Class('MLFeatureDescription')
MLCeilBrick = _Class('MLCeilBrick')
MLExpBrick = _Class('MLExpBrick')
MLRangeBrick = _Class('MLRangeBrick')
MLLoader = _Class('MLLoader')
MLArrayDictionaryFeatureProvider = _Class('MLArrayDictionaryFeatureProvider')
CoreMLModelSecurityServiceToClient = _Class('CoreMLModelSecurityServiceToClient')
MLSecureModelDecryptCredential = _Class('MLSecureModelDecryptCredential')
MLModelTypeRegistry = _Class('MLModelTypeRegistry')
MLArchivingUtils = _Class('MLArchivingUtils')
MLPowBroadcastableBrick = _Class('MLPowBroadcastableBrick')
MLDivideBroadcastableBrick = _Class('MLDivideBroadcastableBrick')
MLBatchedMatMulBrick = _Class('MLBatchedMatMulBrick')
MLFeatureValue = _Class('MLFeatureValue')
MLFloorBrick = _Class('MLFloorBrick')
MLModelAsset = _Class('MLModelAsset')
MLImageConstraint = _Class('MLImageConstraint')
MLLazyUnionFeatureProvider = _Class('MLLazyUnionFeatureProvider')
MLFeatureProviderUtils = _Class('MLFeatureProviderUtils')
MLPersistentKeyStorage = _Class('MLPersistentKeyStorage')
MLCustomLayerWrapper = _Class('MLCustomLayerWrapper')
MLSVMEngine = _Class('MLSVMEngine')
MLUpdateContext = _Class('MLUpdateContext')
MLParameterContainer = _Class('MLParameterContainer')
MLVersionInfo = _Class('MLVersionInfo')
MLObjectBoundingBoxOutputDescription = _Class('MLObjectBoundingBoxOutputDescription')
MLErfActivationBrick = _Class('MLErfActivationBrick')
MLMultiArrayShapeConstraint = _Class('MLMultiArrayShapeConstraint')
MLCosineBrick = _Class('MLCosineBrick')
MLModelDescription = _Class('MLModelDescription')
MLMultiplyBroadcastableBrick = _Class('MLMultiplyBroadcastableBrick')
MLArrayBatchProvider = _Class('MLArrayBatchProvider')
MLSineBrick = _Class('MLSineBrick')
MLLayerExecutionSchedule = _Class('MLLayerExecutionSchedule')
MLSVRLoader = _Class('MLSVRLoader')
MLModelConfiguration = _Class('MLModelConfiguration')
MLCustomModelLoader = _Class('MLCustomModelLoader')
MLDefaultCustomModelFactory = _Class('MLDefaultCustomModelFactory')
MLKey = _Class('MLKey')
MLMetricKey = _Class('MLMetricKey')
MLParameterKey = _Class('MLParameterKey')
MLNeuralNetworkContainer = _Class('MLNeuralNetworkContainer')
MLProgramContainer = _Class('MLProgramContainer')
MLModelErrorUtils = _Class('MLModelErrorUtils')
MLSVREngine = _Class('MLSVREngine')
MLParameterDescription = _Class('MLParameterDescription')
MLMultiArray = _Class('MLMultiArray')
MLMultiArrayView = _Class('MLMultiArrayView')
MLMultiArrayUtils = _Class('MLMultiArrayUtils')
MLAppleGazetteerParameters = _Class('MLAppleGazetteerParameters')
MLSoftmaxNDBrick = _Class('MLSoftmaxNDBrick')
MLAddBroadcastableBrick = _Class('MLAddBroadcastableBrick')
MLImageSize = _Class('MLImageSize')
MLStackNDBrick = _Class('MLStackNDBrick')
MLTileBrick = _Class('MLTileBrick')
MLBackgroundTask = _Class('MLBackgroundTask')
MLBackgroundPredictionTask = _Class('MLBackgroundPredictionTask')
MLSplitNDBrick = _Class('MLSplitNDBrick')
MLModelCollection = _Class('MLModelCollection')
MLTransposeBrick = _Class('MLTransposeBrick')
MLSubtractBroadcastableBrick = _Class('MLSubtractBroadcastableBrick')
MLParameterUtils = _Class('MLParameterUtils')
MLDictionaryConstraint = _Class('MLDictionaryConstraint')
MLModel = _Class('MLModel')
MLArrayFeatureExtractor = _Class('MLArrayFeatureExtractor')
MLOneHotEncoder = _Class('MLOneHotEncoder')
MLScaler = _Class('MLScaler')
MLCategoricalMapping = _Class('MLCategoricalMapping')
MLAppleWordEmbedding = _Class('MLAppleWordEmbedding')
MLNormalizer = _Class('MLNormalizer')
MLDictVectorizer = _Class('MLDictVectorizer')
MLFeatureVectorizer = _Class('MLFeatureVectorizer')
MLImputer = _Class('MLImputer')
MLAppleSoundAnalysisPreprocessing = _Class('MLAppleSoundAnalysisPreprocessing')
MLAppleWordTagger = _Class('MLAppleWordTagger')
MLNonMaximumSuppression = _Class('MLNonMaximumSuppression')
MLAppleTextClassifier = _Class('MLAppleTextClassifier')
MLLinkedModel = _Class('MLLinkedModel')
MLAppleImageFeatureExtractor = _Class('MLAppleImageFeatureExtractor')
MLPipeline = _Class('MLPipeline')
MLPipelineUpdateEngine = _Class('MLPipelineUpdateEngine')
MLSecureModel = _Class('MLSecureModel')
MLWrappedModel = _Class('MLWrappedModel')
MLWritableWrappedModel = _Class('MLWritableWrappedModel')
MLRegressor = _Class('MLRegressor')
MLBayesianProbitRegression = _Class('MLBayesianProbitRegression')
MLPipelineRegressor = _Class('MLPipelineRegressor')
MLGLMRegression = _Class('MLGLMRegression')
MLSupportVectorRegressor = _Class('MLSupportVectorRegressor')
MLTreeEnsembleRegressor = _Class('MLTreeEnsembleRegressor')
MLIdentity = _Class('MLIdentity')
MLItemSimilarityRecommender = _Class('MLItemSimilarityRecommender')
MLKNearestNeighborsClassifier = _Class('MLKNearestNeighborsClassifier')
MLCustomModelWrapper = _Class('MLCustomModelWrapper')
MLNeuralNetworkEngine = _Class('MLNeuralNetworkEngine')
MLProgramEngine = _Class('MLProgramEngine')
MLNeuralNetworkUpdateEngine = _Class('MLNeuralNetworkUpdateEngine')
MLNeuralNetworkCompiler = _Class('MLNeuralNetworkCompiler')
MLAppleGazetteer = _Class('MLAppleGazetteer')
MLClassifier = _Class('MLClassifier')
MLGLMClassification = _Class('MLGLMClassification')
MLSupportVectorClassifier = _Class('MLSupportVectorClassifier')
MLTreeEnsembleXGBoostClassifier = _Class('MLTreeEnsembleXGBoostClassifier')
MLTreeEnsembleXGBoostUpdateEngine = _Class('MLTreeEnsembleXGBoostUpdateEngine')
MLTreeEnsembleClassifier = _Class('MLTreeEnsembleClassifier')
MLPipelineClassifier = _Class('MLPipelineClassifier')
MLInt64ProbabilityDictionaryEnumerator = _Class('MLInt64ProbabilityDictionaryEnumerator')
MLStringProbabilityDictionaryEnumerator = _Class('MLStringProbabilityDictionaryEnumerator')
MLProbabilityDictionary = _Class('MLProbabilityDictionary')
MLInt64ProbabilityDictionary = _Class('MLInt64ProbabilityDictionary')
MLStringProbabilityDictionary = _Class('MLStringProbabilityDictionary')
MLSequnceAsFeatureValueArray = _Class('MLSequnceAsFeatureValueArray')
MLMultiArrayAsNSArrayWrapper = _Class('MLMultiArrayAsNSArrayWrapper')