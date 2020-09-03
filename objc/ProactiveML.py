
'''
Classes from the 'ProactiveML' framework.
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
    
    
PMLPassThroughTracker = _Class('PMLPassThroughTracker')
PMLPlistClassWrapper = _Class('PMLPlistClassWrapper')
PMLSparseVector = _Class('PMLSparseVector')
PMLEspressoDataProvider = _Class('PMLEspressoDataProvider')
PMLLogRegEvaluationPlan = _Class('PMLLogRegEvaluationPlan')
PMLLexicon = _Class('PMLLexicon')
PMLTrackerMockAdapter = _Class('PMLTrackerMockAdapter')
PMLTrainingStoredSessionBatch = _Class('PMLTrainingStoredSessionBatch')
PMLModelWeights = _Class('PMLModelWeights')
PMLEspressoTrainingVariables = _Class('PMLEspressoTrainingVariables')
PMLDataChunk = _Class('PMLDataChunk')
PMLDataChunkDenseDoubleVector = _Class('PMLDataChunkDenseDoubleVector')
PMLDataChunkDenseFloatVector = _Class('PMLDataChunkDenseFloatVector')
PMLDataChunkPlist = _Class('PMLDataChunkPlist')
PMLDataChunkRaw = _Class('PMLDataChunkRaw')
PMLMockPlan = _Class('PMLMockPlan')
PMLTraining = _Class('PMLTraining')
PMLSpotlightReference = _Class('PMLSpotlightReference')
PMLSessionDescriptor = _Class('PMLSessionDescriptor')
PMLDenseMatrix = _Class('PMLDenseMatrix')
PMLFidesTracker = _Class('PMLFidesTracker')
PMLHashingVectorizer = _Class('PMLHashingVectorizer')
PMLModelRegressor = _Class('PMLModelRegressor')
PMLGaussianSampler = _Class('PMLGaussianSampler')
PMLLogisticRegressionModel = _Class('PMLLogisticRegressionModel')
PMLNoNoiseStrategy = _Class('PMLNoNoiseStrategy')
PMLTrackerAWDAdapter = _Class('PMLTrackerAWDAdapter')
PMLPlanSerialization = _Class('PMLPlanSerialization')
PMLPlanWrapper = _Class('PMLPlanWrapper')
PMLEspressoTrainingPlan = _Class('PMLEspressoTrainingPlan')
PMLMetaTrainingVariables = _Class('PMLMetaTrainingVariables')
PMLAWDBaseTracker = _Class('PMLAWDBaseTracker')
PMLAWDAvailableSessionsTracker = _Class('PMLAWDAvailableSessionsTracker')
PMLAWDSessionTracker = _Class('PMLAWDSessionTracker')
PMLAWDSessionTrackerMock = _Class('PMLAWDSessionTrackerMock')
PMLSparseMatrix = _Class('PMLSparseMatrix')
PMLTrainingMock = _Class('PMLTrainingMock')
PMLSeparatedDPNoiseStrategy = _Class('PMLSeparatedDPNoiseStrategy')
PMLDenseVector = _Class('PMLDenseVector')
PMLMutableDenseVector = _Class('PMLMutableDenseVector')
PMLTrainingDatabaseMigrations = _Class('PMLTrainingDatabaseMigrations')
PMLProtoBufTracker = _Class('PMLProtoBufTracker')
PMLAWDLogisticRegTrackerMock = _Class('PMLAWDLogisticRegTrackerMock')
PMLAWDEvaluationTrackerMock = _Class('PMLAWDEvaluationTrackerMock')
PMLClassificationEvaluationMetrics = _Class('PMLClassificationEvaluationMetrics')
PMLDiffPrivacyNoiseStrategy = _Class('PMLDiffPrivacyNoiseStrategy')
PMLFastTextVectorizer = _Class('PMLFastTextVectorizer')
PMLMultiLabelLogisticRegressionModel = _Class('PMLMultiLabelLogisticRegressionModel')
PMLPlanDescriptor = _Class('PMLPlanDescriptor')
PMLImmutableLogisticRegressionModel = _Class('PMLImmutableLogisticRegressionModel')
PMLTrainingLogEntry = _Class('PMLTrainingLogEntry')
PMLLaplaceSampler = _Class('PMLLaplaceSampler')
PMLLogRegTrainingPlan = _Class('PMLLogRegTrainingPlan')
PMLLabelLimitRowId = _Class('PMLLabelLimitRowId')
PMLMultiLabelRegressionEvaluationPlan = _Class('PMLMultiLabelRegressionEvaluationPlan')
PMLGradientSolver = _Class('PMLGradientSolver')
PMLTrackerParsecAdapter = _Class('PMLTrackerParsecAdapter')
PMLPlanSimulator = _Class('PMLPlanSimulator')
PMLTrainingStore = _Class('PMLTrainingStore')
PMLInMemoryCachedStore = _Class('PMLInMemoryCachedStore')
PMLMultiLabelEspressoClassifier = _Class('PMLMultiLabelEspressoClassifier')
AWDProactiveModelFittingLogRegGradient = _Class('AWDProactiveModelFittingLogRegGradient')
AWDProactiveModelFittingPrecisionAtKPair = _Class('AWDProactiveModelFittingPrecisionAtKPair')
AWDProactiveModelFittingParsecFeedbackEnvelope = _Class('AWDProactiveModelFittingParsecFeedbackEnvelope')
AWDProactiveModelFittingMinibatchStats = _Class('AWDProactiveModelFittingMinibatchStats')
AWDProactiveModelFittingQuantizedDenseVector = _Class('AWDProactiveModelFittingQuantizedDenseVector')
AWDProactiveModelFittingLabelSupportPair = _Class('AWDProactiveModelFittingLabelSupportPair')
AWDProactiveModelFittingSession = _Class('AWDProactiveModelFittingSession')
AWDProactiveModelFittingEvalMetrics = _Class('AWDProactiveModelFittingEvalMetrics')
AWDProactiveModelFittingModelInfo = _Class('AWDProactiveModelFittingModelInfo')
AWDProactiveModelFittingQuantizedSparseMatrix = _Class('AWDProactiveModelFittingQuantizedSparseMatrix')
AWDProactiveModelFittingSparseFloatMatrix = _Class('AWDProactiveModelFittingSparseFloatMatrix')
AWDProactiveModelFittingSparseFloatVector = _Class('AWDProactiveModelFittingSparseFloatVector')
AWDProactiveModelFittingLinRegFeatureMatrix = _Class('AWDProactiveModelFittingLinRegFeatureMatrix')
AWDProactiveModelFittingModelInfoStatsPair = _Class('AWDProactiveModelFittingModelInfoStatsPair')
AWDProactiveModelFittingQuantizedSparseVector = _Class('AWDProactiveModelFittingQuantizedSparseVector')
AWDProactiveModelFittingLinRegObjectiveFeatures = _Class('AWDProactiveModelFittingLinRegObjectiveFeatures')
AWDProactiveModelFittingLogRegWeights = _Class('AWDProactiveModelFittingLogRegWeights')
AWDProactiveModelFittingEvaluation = _Class('AWDProactiveModelFittingEvaluation')