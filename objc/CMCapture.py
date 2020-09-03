
'''
Classes from the 'CMCapture' framework.
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
    
    
BWInferenceDepthScalingProvider = _Class('BWInferenceDepthScalingProvider')
BWPhotoDescriptor = _Class('BWPhotoDescriptor')
BWPhotoManifest = _Class('BWPhotoManifest')
FigCaptureVideoDataSinkPipelineConfiguration = _Class('FigCaptureVideoDataSinkPipelineConfiguration')
BWBracketSettings = _Class('BWBracketSettings')
FigCaptureMicSourcePipelineConfiguration = _Class('FigCaptureMicSourcePipelineConfiguration')
BWVisionInferenceProvider = _Class('BWVisionInferenceProvider')
FigCaptureDepthDataPipelineConfiguration = _Class('FigCaptureDepthDataPipelineConfiguration')
BWBravoPortraitSceneMonitor = _Class('BWBravoPortraitSceneMonitor')
FigDelegateStorage = _Class('FigDelegateStorage')
FigWeakReference = _Class('FigWeakReference')
BWImageControlModeTransitionMonitor = _Class('BWImageControlModeTransitionMonitor')
BWIOSurfaceTracking = _Class('BWIOSurfaceTracking')
BWIOSurfacePoller = _Class('BWIOSurfacePoller')
BWObjectLifetimeTracker = _Class('BWObjectLifetimeTracker')
BWTrackedSurface = _Class('BWTrackedSurface')
BWBoxedOutputDetectionTimingInfo = _Class('BWBoxedOutputDetectionTimingInfo')
FigStateMachine = _Class('FigStateMachine')
BWDeepFusionProcessorRequest = _Class('BWDeepFusionProcessorRequest')
BWPendingIrisRecordingRequest = _Class('BWPendingIrisRecordingRequest')
FigCaptureMetadataSinkPipelineConfiguration = _Class('FigCaptureMetadataSinkPipelineConfiguration')
FigCaptureSystemPressureMonitor = _Class('FigCaptureSystemPressureMonitor')
BWNodeError = _Class('BWNodeError')
BWCameraParameters = _Class('BWCameraParameters')
FigMomentCaptureSettings = _Class('FigMomentCaptureSettings')
BWInferenceScalingRequirement = _Class('BWInferenceScalingRequirement')
BWDeferredProcessorRequest = _Class('BWDeferredProcessorRequest')
FigIrisAutoTrimmer = _Class('FigIrisAutoTrimmer')
BWSensorConfiguration = _Class('BWSensorConfiguration')
BWFigVideoCaptureDevice = _Class('BWFigVideoCaptureDevice')
BWZoomRange = _Class('BWZoomRange')
BWZoomDelayBuffer = _Class('BWZoomDelayBuffer')
BWZoomCommandHandler = _Class('BWZoomCommandHandler')
BWInferenceDependencyProvider = _Class('BWInferenceDependencyProvider')
BWGraph = _Class('BWGraph')
BWNoiseReductionAndSharpeningParameters = _Class('BWNoiseReductionAndSharpeningParameters')
BWInferenceSchedulerScaler = _Class('BWInferenceSchedulerScaler')
BWSingleCameraPortraitSceneMonitor = _Class('BWSingleCameraPortraitSceneMonitor')
BWTrackedFace = _Class('BWTrackedFace')
BWFigCaptureDevice = _Class('BWFigCaptureDevice')
BWDeferredIntermediate = _Class('BWDeferredIntermediate')
BWDeferredDataIntermediate = _Class('BWDeferredDataIntermediate')
BWDeferredDictionaryIntermediate = _Class('BWDeferredDictionaryIntermediate')
BWDeferredMetadataIntermediate = _Class('BWDeferredMetadataIntermediate')
BWDeferredArrayIntermediate = _Class('BWDeferredArrayIntermediate')
BWDeferredBufferIntermediate = _Class('BWDeferredBufferIntermediate')
BWIrisSequenceAdjuster = _Class('BWIrisSequenceAdjuster')
BWIrisDiscontinuity = _Class('BWIrisDiscontinuity')
BWTimeSkew = _Class('BWTimeSkew')
BWCaptureDeferredPhotoProcessor = _Class('BWCaptureDeferredPhotoProcessor')
BWMemoryPool = _Class('BWMemoryPool')
BWInferenceEngine = _Class('BWInferenceEngine')
FigCoreMotionDelegate = _Class('FigCoreMotionDelegate')
BWRenderListProcessor = _Class('BWRenderListProcessor')
BWNodeConnection = _Class('BWNodeConnection')
BWCameraStreamingMonitor = _Class('BWCameraStreamingMonitor')
FigCaptureImageMotionDetector = _Class('FigCaptureImageMotionDetector')
FigCaptureRecordingSettings = _Class('FigCaptureRecordingSettings')
FigCaptureAudioFileRecordingSettings = _Class('FigCaptureAudioFileRecordingSettings')
FigCaptureMovieFileRecordingSettings = _Class('FigCaptureMovieFileRecordingSettings')
BWVisionLandmarkDetector = _Class('BWVisionLandmarkDetector')
FigCaptureSessionServerKeyedUnarchiverDelegate = _Class('FigCaptureSessionServerKeyedUnarchiverDelegate')
BWStillImageSettings = _Class('BWStillImageSettings')
BWInferenceScheduler = _Class('BWInferenceScheduler')
BWCoreImageFilterRenderer = _Class('BWCoreImageFilterRenderer')
BWInferenceSchedulerConnection = _Class('BWInferenceSchedulerConnection')
BWMultiStreamCameraSourceNodeConfiguration = _Class('BWMultiStreamCameraSourceNodeConfiguration')
BWColorLookupCache = _Class('BWColorLookupCache')
BWEspressoInferenceAdapter = _Class('BWEspressoInferenceAdapter')
BWDroppedSample = _Class('BWDroppedSample')
FigCapturePreviewSinkPipelineConfiguration = _Class('FigCapturePreviewSinkPipelineConfiguration')
BWAutoFocusPositionSensorMonitor = _Class('BWAutoFocusPositionSensorMonitor')
BWVideoProcessingInferenceProvider = _Class('BWVideoProcessingInferenceProvider')
BWInferenceSchedulerInference = _Class('BWInferenceSchedulerInference')
FigUtlROIProcessor = _Class('FigUtlROIProcessor')
FigCameraViewfinderServer = _Class('FigCameraViewfinderServer')
BWStreamStartStopSynchronizer = _Class('BWStreamStartStopSynchronizer')
BWStreamStartStopState = _Class('BWStreamStartStopState')
BWEspressoInferenceProvider = _Class('BWEspressoInferenceProvider')
FigIrisAutoTrimmerMotionSample = _Class('FigIrisAutoTrimmerMotionSample')
BWFigCaptureISPProcessingSession = _Class('BWFigCaptureISPProcessingSession')
BWInferenceResultRingBuffers = _Class('BWInferenceResultRingBuffers')
FigCaptureSessionPipelines = _Class('FigCaptureSessionPipelines')
FigCaptureStillImageSinkPipelineSessionStorage = _Class('FigCaptureStillImageSinkPipelineSessionStorage')
FigCaptureSessionPreparedBracket = _Class('FigCaptureSessionPreparedBracket')
BWRenderList = _Class('BWRenderList')
BWObjectRingBuffer = _Class('BWObjectRingBuffer')
BWObjectRingBufferThreadSafe = _Class('BWObjectRingBufferThreadSafe')
BWLivePhotoMovieAnalyticsPayload = _Class('BWLivePhotoMovieAnalyticsPayload')
BWDeferredProcessingAnalyticsPayload = _Class('BWDeferredProcessingAnalyticsPayload')
BWDeferredCaptureAnalyticsPayload = _Class('BWDeferredCaptureAnalyticsPayload')
BWStartupCalibrationAnalyticsPayload = _Class('BWStartupCalibrationAnalyticsPayload')
BWStreamingSessionAnalyticsPayload = _Class('BWStreamingSessionAnalyticsPayload')
BWIOSurfaceCompressionStatisticsAnalyticsPayload = _Class('BWIOSurfaceCompressionStatisticsAnalyticsPayload')
BWMovieFileOutputAnalyticsPayload = _Class('BWMovieFileOutputAnalyticsPayload')
BWStillImageCaptureAnalyticsPayload = _Class('BWStillImageCaptureAnalyticsPayload')
BWCoreAnalyticsReporter = _Class('BWCoreAnalyticsReporter')
BWStillImageProcessorCoordinator = _Class('BWStillImageProcessorCoordinator')
FigCaptureSessionConfigurationKeyedUnarchiverDelegate = _Class('FigCaptureSessionConfigurationKeyedUnarchiverDelegate')
FigCaptureSinkConfiguration = _Class('FigCaptureSinkConfiguration')
FigCaptureCameraCalibrationDataSinkConfiguration = _Class('FigCaptureCameraCalibrationDataSinkConfiguration')
FigCaptureVisionDataSinkConfiguration = _Class('FigCaptureVisionDataSinkConfiguration')
FigCaptureDepthDataSinkConfiguration = _Class('FigCaptureDepthDataSinkConfiguration')
FigCaptureIrisSinkConfiguration = _Class('FigCaptureIrisSinkConfiguration')
FigCapturePointCloudDataSinkConfiguration = _Class('FigCapturePointCloudDataSinkConfiguration')
FigCaptureInternalSinkConfiguration = _Class('FigCaptureInternalSinkConfiguration')
FigCaptureMetadataItemGroupSinkConfiguration = _Class('FigCaptureMetadataItemGroupSinkConfiguration')
FigCaptureMetadataObjectSinkConfiguration = _Class('FigCaptureMetadataObjectSinkConfiguration')
FigCaptureAudioDataSinkConfiguration = _Class('FigCaptureAudioDataSinkConfiguration')
FigCaptureVideoDataSinkConfiguration = _Class('FigCaptureVideoDataSinkConfiguration')
FigCaptureAudioFileSinkConfiguration = _Class('FigCaptureAudioFileSinkConfiguration')
FigCaptureMovieFileSinkConfiguration = _Class('FigCaptureMovieFileSinkConfiguration')
FigCaptureStillImageSinkConfiguration = _Class('FigCaptureStillImageSinkConfiguration')
FigCaptureAudioPreviewSinkConfiguration = _Class('FigCaptureAudioPreviewSinkConfiguration')
FigCaptureVideoThumbnailSinkConfiguration = _Class('FigCaptureVideoThumbnailSinkConfiguration')
FigCaptureVideoPreviewSinkConfiguration = _Class('FigCaptureVideoPreviewSinkConfiguration')
FigCaptureSourceConfiguration = _Class('FigCaptureSourceConfiguration')
FigCaptureConnectionConfiguration = _Class('FigCaptureConnectionConfiguration')
FigCameraCalibrationDataCaptureConnectionConfiguration = _Class('FigCameraCalibrationDataCaptureConnectionConfiguration')
FigMetadataItemCaptureConnectionConfiguration = _Class('FigMetadataItemCaptureConnectionConfiguration')
FigMetadataObjectCaptureConnectionConfiguration = _Class('FigMetadataObjectCaptureConnectionConfiguration')
FigAudioCaptureConnectionConfiguration = _Class('FigAudioCaptureConnectionConfiguration')
FigVideoCaptureConnectionConfiguration = _Class('FigVideoCaptureConnectionConfiguration')
FigPointCloudDataCaptureConnectionConfiguration = _Class('FigPointCloudDataCaptureConnectionConfiguration')
FigVisionDataCaptureConnectionConfiguration = _Class('FigVisionDataCaptureConnectionConfiguration')
FigDepthDataCaptureConnectionConfiguration = _Class('FigDepthDataCaptureConnectionConfiguration')
FigCaptureSessionConfiguration = _Class('FigCaptureSessionConfiguration')
BWDeviceMotionActivityDetector = _Class('BWDeviceMotionActivityDetector')
BWMotionSampleRingBuffer = _Class('BWMotionSampleRingBuffer')
BWRingBuffer = _Class('BWRingBuffer')
BWDeferredContainer = _Class('BWDeferredContainer')
BWDeferredProcessingContainer = _Class('BWDeferredProcessingContainer')
BWDeferredCaptureContainer = _Class('BWDeferredCaptureContainer')
BWStereoDisparityRequest = _Class('BWStereoDisparityRequest')
BWStillImageTimeMachine = _Class('BWStillImageTimeMachine')
BWUBCaptureParameters = _Class('BWUBCaptureParameters')
BWMetalColorCubeRenderer = _Class('BWMetalColorCubeRenderer')
FigCaptureLockScreenPrewarmingMonitor = _Class('FigCaptureLockScreenPrewarmingMonitor')
FigCapturePixelConverter = _Class('FigCapturePixelConverter')
BWSphereModeSelector = _Class('BWSphereModeSelector')
BWFrameStatisticsByPortType = _Class('BWFrameStatisticsByPortType')
BWFrameStatistics = _Class('BWFrameStatistics')
BWRenderListParameters = _Class('BWRenderListParameters')
FigCaptureDisplayLayoutMonitor = _Class('FigCaptureDisplayLayoutMonitor')
FigSmartcamDiagnostics = _Class('FigSmartcamDiagnostics')
BWMattingV2InferenceProvider = _Class('BWMattingV2InferenceProvider')
BWFigCaptureDeviceVendor = _Class('BWFigCaptureDeviceVendor')
BWFigCaptureDeviceClient = _Class('BWFigCaptureDeviceClient')
BWMotionDataPreserver = _Class('BWMotionDataPreserver')
BWInferenceSchedulerJobList = _Class('BWInferenceSchedulerJobList')
BWMotionDataTimeMachine = _Class('BWMotionDataTimeMachine')
FigCaptureMachPortSendRight = _Class('FigCaptureMachPortSendRight')
BWFigCaptureSynchronizedStreamsGroup = _Class('BWFigCaptureSynchronizedStreamsGroup')
BWInferenceDataDependency = _Class('BWInferenceDataDependency')
BWVideoOrientationTimeMachine = _Class('BWVideoOrientationTimeMachine')
BWVideoOrientationTimeMachineItem = _Class('BWVideoOrientationTimeMachineItem')
BWFigCaptureSession = _Class('BWFigCaptureSession')
FigCaptureSessionActiveCameraCaptureSource = _Class('FigCaptureSessionActiveCameraCaptureSource')
BWInferenceSchedulerFramebuffer = _Class('BWInferenceSchedulerFramebuffer')
BWStillImageCaptureStreamFrameCounts = _Class('BWStillImageCaptureStreamFrameCounts')
BWInferenceSchedulerGraph = _Class('BWInferenceSchedulerGraph')
FigMetalTextureStub = _Class('FigMetalTextureStub')
FigMetalAllocator = _Class('FigMetalAllocator')
FigMetalHeapAllocator = _Class('FigMetalHeapAllocator')
FigMetalBufferAllocator = _Class('FigMetalBufferAllocator')
FigMetalNoAliasingAllocator = _Class('FigMetalNoAliasingAllocator')
FigMetalTextureDescriptor = _Class('FigMetalTextureDescriptor')
FigMetalAllocatorDescriptor = _Class('FigMetalAllocatorDescriptor')
FigMetalUtils = _Class('FigMetalUtils')
FigMetalAllocatorMetadata = _Class('FigMetalAllocatorMetadata')
BWFigCaptureStream = _Class('BWFigCaptureStream')
BWMeaningfulSubjectDetectionContext = _Class('BWMeaningfulSubjectDetectionContext')
FigCaptureSessionProxy = _Class('FigCaptureSessionProxy')
FigCaptureSessionObservatory = _Class('FigCaptureSessionObservatory')
FigMetalHistogram = _Class('FigMetalHistogram')
BWEspressoInferenceContext = _Class('BWEspressoInferenceContext')
BWAggdDataReporter = _Class('BWAggdDataReporter')
FigCaptureCameraSourcePipelineConfiguration = _Class('FigCaptureCameraSourcePipelineConfiguration')
BWMattingInferenceProvider = _Class('BWMattingInferenceProvider')
BWNodeOutputMediaProperties = _Class('BWNodeOutputMediaProperties')
BWNodeOutputMediaConfiguration = _Class('BWNodeOutputMediaConfiguration')
BWNodeOutput = _Class('BWNodeOutput')
BWDetectedObjectsInfoRingBuffer = _Class('BWDetectedObjectsInfoRingBuffer')
BWDetectedFacesRingBuffer = _Class('BWDetectedFacesRingBuffer')
BWDeferredMetadataCache = _Class('BWDeferredMetadataCache')
FigCaptureSourceStreamsContainer = _Class('FigCaptureSourceStreamsContainer')
BWStillImageCaptureStreamFrameCounters = _Class('BWStillImageCaptureStreamFrameCounters')
BWStreamingCVAFilterRenderer = _Class('BWStreamingCVAFilterRenderer')
BWStreamingCVAFilterRendererAnimator = _Class('BWStreamingCVAFilterRendererAnimator')
BWStillImageCaptureDelegateCallbackInfo = _Class('BWStillImageCaptureDelegateCallbackInfo')
BWDeferredContainerManagerBase = _Class('BWDeferredContainerManagerBase')
BWDeferredProcessingContainerManager = _Class('BWDeferredProcessingContainerManager')
BWDeferredCaptureContainerManager = _Class('BWDeferredCaptureContainerManager')
BWDeferredContainerPixelBufferPoolWrapper = _Class('BWDeferredContainerPixelBufferPoolWrapper')
BWDeferredContainerPixelBufferWrapper = _Class('BWDeferredContainerPixelBufferWrapper')
BWNRFProcessorRequest = _Class('BWNRFProcessorRequest')
BWNRFProcessorCompletionStatus = _Class('BWNRFProcessorCompletionStatus')
BWNRFSemanticRenderingInput = _Class('BWNRFSemanticRenderingInput')
BWNRFAdaptiveBracketingParameters = _Class('BWNRFAdaptiveBracketingParameters')
BWUBProcessorRequest = _Class('BWUBProcessorRequest')
BWUBSemanticRenderingInput = _Class('BWUBSemanticRenderingInput')
BWUBAdaptiveBracketingParameters = _Class('BWUBAdaptiveBracketingParameters')
BWSpringSimulation = _Class('BWSpringSimulation')
FigCaptureAutoFocusPositionSensorCalibrationIStopZEstimateDeltaHistory = _Class('FigCaptureAutoFocusPositionSensorCalibrationIStopZEstimateDeltaHistory')
FigCaptureClientSessionMonitor = _Class('FigCaptureClientSessionMonitor')
FigCaptureSourceCompanionFormat = _Class('FigCaptureSourceCompanionFormat')
FigCaptureSourceFormat = _Class('FigCaptureSourceFormat')
FigCaptureSourceDepthDataFormat = _Class('FigCaptureSourceDepthDataFormat')
FigCaptureSourceVideoFormat = _Class('FigCaptureSourceVideoFormat')
BWRamp = _Class('BWRamp')
BWNodeInputMediaProperties = _Class('BWNodeInputMediaProperties')
BWNodeInputMediaConfiguration = _Class('BWNodeInputMediaConfiguration')
BWNodeInput = _Class('BWNodeInput')
BWNodeMessage = _Class('BWNodeMessage')
BWNodeStillImagePrewarmMessage = _Class('BWNodeStillImagePrewarmMessage')
BWNodeStillImageReferenceFrameBracketedCaptureSequenceNumberMessage = _Class('BWNodeStillImageReferenceFrameBracketedCaptureSequenceNumberMessage')
BWNodeDroppedSampleMessage = _Class('BWNodeDroppedSampleMessage')
BWNodeErrorMessage = _Class('BWNodeErrorMessage')
BWNodeEndOfDataMessage = _Class('BWNodeEndOfDataMessage')
BWNodeConfigurationLiveMessage = _Class('BWNodeConfigurationLiveMessage')
BWNodeSampleBufferMessage = _Class('BWNodeSampleBufferMessage')
BWFigVideoCaptureStream = _Class('BWFigVideoCaptureStream')
FigWiredMemory = _Class('FigWiredMemory')
FigCaptureDeferredProcessingEngine = _Class('FigCaptureDeferredProcessingEngine')
FigCaptureDeferredProcessingJob = _Class('FigCaptureDeferredProcessingJob')
BWBravoPortraitSceneMonitorV2 = _Class('BWBravoPortraitSceneMonitorV2')
BWInferenceResult = _Class('BWInferenceResult')
FigCaptureCalibrationMonitor = _Class('FigCaptureCalibrationMonitor')
BWIrisMovieInfo = _Class('BWIrisMovieInfo')
BWDataBufferPool = _Class('BWDataBufferPool')
FigCapturePowerMonitor = _Class('FigCapturePowerMonitor')
BWVideoQualityMetrics = _Class('BWVideoQualityMetrics')
BWLimitedGMErrorLogger = _Class('BWLimitedGMErrorLogger')
BWStats = _Class('BWStats')
BWMovingWindowStats = _Class('BWMovingWindowStats')
FigCaptureSessionParsedConfiguration = _Class('FigCaptureSessionParsedConfiguration')
FigCaptureSessionParsedMovieFileSinkConfiguration = _Class('FigCaptureSessionParsedMovieFileSinkConfiguration')
FigCaptureSessionParsedMetadataSinkConfiguration = _Class('FigCaptureSessionParsedMetadataSinkConfiguration')
FigCaptureSessionParsedDepthDataSinkConfiguration = _Class('FigCaptureSessionParsedDepthDataSinkConfiguration')
FigCaptureSessionParsedVisionDataSinkConfiguration = _Class('FigCaptureSessionParsedVisionDataSinkConfiguration')
FigCaptureSessionParsedVideoDataSinkConfiguration = _Class('FigCaptureSessionParsedVideoDataSinkConfiguration')
FigCaptureSessionParsedStillImageSinkConfiguration = _Class('FigCaptureSessionParsedStillImageSinkConfiguration')
FigCaptureSessionParsedPreviewSinkConfiguration = _Class('FigCaptureSessionParsedPreviewSinkConfiguration')
FigCaptureSessionParsedMicSourceConfiguration = _Class('FigCaptureSessionParsedMicSourceConfiguration')
FigCaptureSessionParsedCameraSourceConfiguration = _Class('FigCaptureSessionParsedCameraSourceConfiguration')
BWStillImageConditionalRouterConfiguration = _Class('BWStillImageConditionalRouterConfiguration')
BWStillImageConditionalRouterOverCaptureConfiguration = _Class('BWStillImageConditionalRouterOverCaptureConfiguration')
BWStillImageConditionalRouterInferenceConfiguration = _Class('BWStillImageConditionalRouterInferenceConfiguration')
BWStillImageConditionalRouterUBConfiguration = _Class('BWStillImageConditionalRouterUBConfiguration')
BWStillImageConditionalRouterPersonSegmentationAndMattingConfiguration = _Class('BWStillImageConditionalRouterPersonSegmentationAndMattingConfiguration')
BWStillImageConditionalRouterLandmarksConfiguration = _Class('BWStillImageConditionalRouterLandmarksConfiguration')
BWStillImageProcessingSettings = _Class('BWStillImageProcessingSettings')
BWInferenceSingleBufferPoolProvider = _Class('BWInferenceSingleBufferPoolProvider')
FigCaptureIrisPreparedSettings = _Class('FigCaptureIrisPreparedSettings')
FigCaptureStillImageSettings = _Class('FigCaptureStillImageSettings')
FigCaptureIrisStillImageSettings = _Class('FigCaptureIrisStillImageSettings')
FigCameraUsageListener = _Class('FigCameraUsageListener')
FigCaptureThermalMonitor = _Class('FigCaptureThermalMonitor')
BWMetalColorCubeRendererParameters = _Class('BWMetalColorCubeRendererParameters')
BWStillImageMetalBlurMapRenderer = _Class('BWStillImageMetalBlurMapRenderer')
BWInferenceProviderStorage = _Class('BWInferenceProviderStorage')
BWVisionInferenceStorage = _Class('BWVisionInferenceStorage')
BWEspressoInferenceStorage = _Class('BWEspressoInferenceStorage')
BWVideoProcessingInferenceStorage = _Class('BWVideoProcessingInferenceStorage')
BWMattingInferenceStorage = _Class('BWMattingInferenceStorage')
BWCoreImageFilterRendererParameters = _Class('BWCoreImageFilterRendererParameters')
BWMeaningfulSubjectTracker = _Class('BWMeaningfulSubjectTracker')
BWPipelineStage = _Class('BWPipelineStage')
BWFigVideoCaptureSynchronizedStreamsGroup = _Class('BWFigVideoCaptureSynchronizedStreamsGroup')
CMMTLCommandBuffer = _Class('CMMTLCommandBuffer')
CMMTLCommandQueue = _Class('CMMTLCommandQueue')
CMMTLDevice = _Class('CMMTLDevice')
InterceptConfig = _Class('InterceptConfig')
FigCaptureMovieFileSinkTailPipelineConfiguration = _Class('FigCaptureMovieFileSinkTailPipelineConfiguration')
FigCaptureMovieFileSinkMiddlePipelineConfiguration = _Class('FigCaptureMovieFileSinkMiddlePipelineConfiguration')
FigCapturePipeline = _Class('FigCapturePipeline')
FigCaptureVISPipeline = _Class('FigCaptureVISPipeline')
FigCaptureSourcePipeline = _Class('FigCaptureSourcePipeline')
FigCaptureMicSourcePipeline = _Class('FigCaptureMicSourcePipeline')
FigCaptureMetadataSourcePipeline = _Class('FigCaptureMetadataSourcePipeline')
FigCaptureCameraSourcePipeline = _Class('FigCaptureCameraSourcePipeline')
FigCaptureSinkPipeline = _Class('FigCaptureSinkPipeline')
FigCaptureAudioFileSinkPipeline = _Class('FigCaptureAudioFileSinkPipeline')
FigCapturePreviewSinkPipeline = _Class('FigCapturePreviewSinkPipeline')
FigCaptureSessionPreviewSinkPipeline = _Class('FigCaptureSessionPreviewSinkPipeline')
FigCaptureStillImageSinkPipeline = _Class('FigCaptureStillImageSinkPipeline')
FigCaptureStillImageUnifiedBracketingSinkPipeline = _Class('FigCaptureStillImageUnifiedBracketingSinkPipeline')
FigCaptureVideoThumbnailSinkPipeline = _Class('FigCaptureVideoThumbnailSinkPipeline')
FigCaptureRemoteQueueSinkPipeline = _Class('FigCaptureRemoteQueueSinkPipeline')
FigCaptureAudioDataSinkPipeline = _Class('FigCaptureAudioDataSinkPipeline')
FigCaptureVideoDataSinkPipeline = _Class('FigCaptureVideoDataSinkPipeline')
FigCaptureDepthDataPipeline = _Class('FigCaptureDepthDataPipeline')
FigCaptureMetadataSinkPipeline = _Class('FigCaptureMetadataSinkPipeline')
FigCapturePointCloudDataSinkPipeline = _Class('FigCapturePointCloudDataSinkPipeline')
FigCaptureVisionDataSinkPipeline = _Class('FigCaptureVisionDataSinkPipeline')
FigCaptureCameraCalibrationDataSinkPipeline = _Class('FigCaptureCameraCalibrationDataSinkPipeline')
FigCaptureMovieFileSinkPipeline = _Class('FigCaptureMovieFileSinkPipeline')
FigCaptureSessionMovieFileSinkPipeline = _Class('FigCaptureSessionMovieFileSinkPipeline')
FigCaptureMovieFileSinkTailPipeline = _Class('FigCaptureMovieFileSinkTailPipeline')
FigCaptureMovieFileSinkMiddlePipeline = _Class('FigCaptureMovieFileSinkMiddlePipeline')
FigCaptureMovieFileSinkHeadPipeline = _Class('FigCaptureMovieFileSinkHeadPipeline')
FigCaptureMovieFileSinkHeadPipelineConfiguration = _Class('FigCaptureMovieFileSinkHeadPipelineConfiguration')
FigCaptureMovieFileSinkPipelineConfiguration = _Class('FigCaptureMovieFileSinkPipelineConfiguration')
BWPhotoDecompressor = _Class('BWPhotoDecompressor')
BWVisionInferenceContext = _Class('BWVisionInferenceContext')
FigCameraViewfinderSession = _Class('FigCameraViewfinderSession')
FigCameraViewfinderSessionLocal = _Class('FigCameraViewfinderSessionLocal')
FigCameraViewfinderSessionRemote = _Class('FigCameraViewfinderSessionRemote')
FigCameraViewfinder = _Class('FigCameraViewfinder')
FigCameraViewfinderLocal = _Class('FigCameraViewfinderLocal')
FigCameraViewfinderRemote = _Class('FigCameraViewfinderRemote')
BWFormat = _Class('BWFormat')
BWVideoFormat = _Class('BWVideoFormat')
BWCameraCalibrationDataFormat = _Class('BWCameraCalibrationDataFormat')
BWPointCloudFormat = _Class('BWPointCloudFormat')
BWMetadataFormat = _Class('BWMetadataFormat')
BWAudioFormat = _Class('BWAudioFormat')
BWMetadataObjectFormat = _Class('BWMetadataObjectFormat')
FigCaptureBaseStillImageSinkPipelineConfiguration = _Class('FigCaptureBaseStillImageSinkPipelineConfiguration')
FigCaptureStillImageSinkPipelineConfiguration = _Class('FigCaptureStillImageSinkPipelineConfiguration')
FigCaptureStillImageUnifiedBracketingSinkPipelineConfiguration = _Class('FigCaptureStillImageUnifiedBracketingSinkPipelineConfiguration')
FigCameraViewfinderStream = _Class('FigCameraViewfinderStream')
BWInferenceDataRequirement = _Class('BWInferenceDataRequirement')
BWInferenceMetadataRequirement = _Class('BWInferenceMetadataRequirement')
BWInferenceMediaRequirement = _Class('BWInferenceMediaRequirement')
BWInferenceVideoRequirement = _Class('BWInferenceVideoRequirement')
BWInferenceLazyVideoRequirement = _Class('BWInferenceLazyVideoRequirement')
BWInferenceCompressedVideoRequirement = _Class('BWInferenceCompressedVideoRequirement')
BWInferenceCloneVideoRequirement = _Class('BWInferenceCloneVideoRequirement')
BWAdaptiveBracketingFrameParameters = _Class('BWAdaptiveBracketingFrameParameters')
FigStillImageSharedProcessingResources = _Class('FigStillImageSharedProcessingResources')
BWRedEyeReductionRequest = _Class('BWRedEyeReductionRequest')
BWPixelBufferPool = _Class('BWPixelBufferPool')
BWDeferredContainerPixelBufferPool = _Class('BWDeferredContainerPixelBufferPool')
FigBWNodeRenderObserver = _Class('FigBWNodeRenderObserver')
BWPearlPortraitSceneMonitor = _Class('BWPearlPortraitSceneMonitor')
BWVideoProcessingInferenceAdapter = _Class('BWVideoProcessingInferenceAdapter')
BWMetadataTimeMachine = _Class('BWMetadataTimeMachine')
BWMetadataTimeMachineRequest = _Class('BWMetadataTimeMachineRequest')
BWMetadataTimeMachineWaitRequest = _Class('BWMetadataTimeMachineWaitRequest')
BWMetadataTimeMachineMetadataRequest = _Class('BWMetadataTimeMachineMetadataRequest')
BWIntermediateJPEGCompressor = _Class('BWIntermediateJPEGCompressor')
BWIntermediateJPEGCompressedBufferAssociatedSemaphore = _Class('BWIntermediateJPEGCompressedBufferAssociatedSemaphore')
BWStillImageNodeConfiguration = _Class('BWStillImageNodeConfiguration')
BWRenderListAnimator = _Class('BWRenderListAnimator')
FigUtlFaceDetection = _Class('FigUtlFaceDetection')
FigM2MController = _Class('FigM2MController')
BWInferenceSchedulerGraphInputNode = _Class('BWInferenceSchedulerGraphInputNode')
BWInferenceVideoScalingProvider = _Class('BWInferenceVideoScalingProvider')
FigCaptureDeferredPhotoProcessorRequest = _Class('FigCaptureDeferredPhotoProcessorRequest')
BWBravoStreamSelector = _Class('BWBravoStreamSelector')
BWInferenceVideoFormat = _Class('BWInferenceVideoFormat')
BWFormatRequirements = _Class('BWFormatRequirements')
BWPointCloudFormatRequirements = _Class('BWPointCloudFormatRequirements')
BWVideoFormatRequirements = _Class('BWVideoFormatRequirements')
BWInferenceVideoFormatRequirements = _Class('BWInferenceVideoFormatRequirements')
BWStillImageCaptureMetadata = _Class('BWStillImageCaptureMetadata')
BWStillImageCaptureStreamSettings = _Class('BWStillImageCaptureStreamSettings')
BWStillImageCaptureSettings = _Class('BWStillImageCaptureSettings')
BWInferenceRequirement = _Class('BWInferenceRequirement')
BWColorLookupCacheEntry = _Class('BWColorLookupCacheEntry')
FigCaptureCalibrationContext = _Class('FigCaptureCalibrationContext')
FigCaptureSphereCalibrationContext = _Class('FigCaptureSphereCalibrationContext')
FigCaptureAutoFocusCalibrationContext = _Class('FigCaptureAutoFocusCalibrationContext')
FigCaptureAutoFocusPositionSensorCalibrationContext = _Class('FigCaptureAutoFocusPositionSensorCalibrationContext')
FigCaptureAPSSphereInteractionCalibrationContext = _Class('FigCaptureAPSSphereInteractionCalibrationContext')
FigCaptureSphereEndStopCalibrationContext = _Class('FigCaptureSphereEndStopCalibrationContext')
BWMeaningfulSubjectTrackingContext = _Class('BWMeaningfulSubjectTrackingContext')
BWSimpleCache = _Class('BWSimpleCache')
BWIrisStillImageMovieMetadataCache = _Class('BWIrisStillImageMovieMetadataCache')
BWInferenceSimpleStorage = _Class('BWInferenceSimpleStorage')
BWIrisMovieGenerator = _Class('BWIrisMovieGenerator')
BWIrisMovieInfoAndCallback = _Class('BWIrisMovieInfoAndCallback')
BWInferenceConfiguration = _Class('BWInferenceConfiguration')
BWMattingInferenceConfiguration = _Class('BWMattingInferenceConfiguration')
BWMonocularDepthConfiguration = _Class('BWMonocularDepthConfiguration')
BWMattingV2InferenceConfiguration = _Class('BWMattingV2InferenceConfiguration')
BWPersonSemanticsConfiguration = _Class('BWPersonSemanticsConfiguration')
BWPersonSegmentationConfiguration = _Class('BWPersonSegmentationConfiguration')
BWRGBPersonSegmentationInferenceConfiguration = _Class('BWRGBPersonSegmentationInferenceConfiguration')
BWVisionInferenceConfiguration = _Class('BWVisionInferenceConfiguration')
BWPhotosCurationInferenceConfiguration = _Class('BWPhotosCurationInferenceConfiguration')
BWLandmarksInferenceConfiguration = _Class('BWLandmarksInferenceConfiguration')
BWFaceSegmentsWithLandmarksInferenceConfiguration = _Class('BWFaceSegmentsWithLandmarksInferenceConfiguration')
BWInferenceSchedulerFramebufferBuilder = _Class('BWInferenceSchedulerFramebufferBuilder')
BWVisionInferenceAdapter = _Class('BWVisionInferenceAdapter')
BWInferenceSchedulerResourceCoordinator = _Class('BWInferenceSchedulerResourceCoordinator')
BWStillImageProcessorController = _Class('BWStillImageProcessorController')
BWDeepFusionProcessorController = _Class('BWDeepFusionProcessorController')
BWDeferredProcessorController = _Class('BWDeferredProcessorController')
BWStereoDisparityProcessorController = _Class('BWStereoDisparityProcessorController')
BWNRFProcessorController = _Class('BWNRFProcessorController')
BWUBProcessorController = _Class('BWUBProcessorController')
BWRedEyeReductionController = _Class('BWRedEyeReductionController')
BWUBInferenceController = _Class('BWUBInferenceController')
BWStillImageProcessorInput = _Class('BWStillImageProcessorInput')
BWDeepFusionProcessorInput = _Class('BWDeepFusionProcessorInput')
BWDeferredProcessorControllerInput = _Class('BWDeferredProcessorControllerInput')
BWStereoDisparityProcessorInput = _Class('BWStereoDisparityProcessorInput')
BWNRFProcessorInput = _Class('BWNRFProcessorInput')
BWUBProcessorInput = _Class('BWUBProcessorInput')
BWRedEyeReductionControllerInput = _Class('BWRedEyeReductionControllerInput')
BWUBInferenceControllerInput = _Class('BWUBInferenceControllerInput')
BWStillImageProcessorOutputRouter = _Class('BWStillImageProcessorOutputRouter')
BWStillImageProcessorConfiguration = _Class('BWStillImageProcessorConfiguration')
BWDeepFusionProcessorControllerConfiguration = _Class('BWDeepFusionProcessorControllerConfiguration')
BWStereoDisparityProcessorControllerConfiguration = _Class('BWStereoDisparityProcessorControllerConfiguration')
BWNRFProcessorControllerConfiguration = _Class('BWNRFProcessorControllerConfiguration')
BWUBProcessorControllerConfiguration = _Class('BWUBProcessorControllerConfiguration')
BWUBInferenceControllerConfiguration = _Class('BWUBInferenceControllerConfiguration')
FigMetalContext = _Class('FigMetalContext')
FigMetalExecutionStatus = _Class('FigMetalExecutionStatus')
BWNode = _Class('BWNode')
BWStillImageBravoDisparityNode = _Class('BWStillImageBravoDisparityNode')
BWVideoOrientationMetadataNode = _Class('BWVideoOrientationMetadataNode')
BWFunnelNode = _Class('BWFunnelNode')
BWParallelJoinerNode = _Class('BWParallelJoinerNode')
BWPreviewHistogramNode = _Class('BWPreviewHistogramNode')
BWHDRNode = _Class('BWHDRNode')
BWStillImagePortraitMetadataNode = _Class('BWStillImagePortraitMetadataNode')
BWMeaningfulSubjectTrackingNode = _Class('BWMeaningfulSubjectTrackingNode')
BWFrameRateGovernorNode = _Class('BWFrameRateGovernorNode')
BWDepthConverterNode = _Class('BWDepthConverterNode')
BWSynchronizerNode = _Class('BWSynchronizerNode')
BWInferenceNode = _Class('BWInferenceNode')
BWInferenceBufferingNode = _Class('BWInferenceBufferingNode')
BWVISNode = _Class('BWVISNode')
BWVideoCompressorNode = _Class('BWVideoCompressorNode')
BWVideoDepthNode = _Class('BWVideoDepthNode')
BWSceneClassifierFrameGateNode = _Class('BWSceneClassifierFrameGateNode')
BWDepthSynchronizerNode = _Class('BWDepthSynchronizerNode')
BWCameraInfoMetadataNode = _Class('BWCameraInfoMetadataNode')
BWUBNode = _Class('BWUBNode')
BWSISNode = _Class('BWSISNode')
BWStillImageBufferRouterNode = _Class('BWStillImageBufferRouterNode')
BWStillImageTimeMachineFrameCoordinatorNode = _Class('BWStillImageTimeMachineFrameCoordinatorNode')
BWSlaveFrameSynchronizerNode = _Class('BWSlaveFrameSynchronizerNode')
BWStillImageFilterNode = _Class('BWStillImageFilterNode')
BWCrossoverNode = _Class('BWCrossoverNode')
BWNoiseReducerNode = _Class('BWNoiseReducerNode')
BWRedEyeReducerNode = _Class('BWRedEyeReducerNode')
BWStereoFusionNode = _Class('BWStereoFusionNode')
BWStreamingCameraCalibrationDataNode = _Class('BWStreamingCameraCalibrationDataNode')
BWStillImageDualPhotoFacePropagatorNode = _Class('BWStillImageDualPhotoFacePropagatorNode')
BWMotionAttachmentsNode = _Class('BWMotionAttachmentsNode')
BWDepthRotatorNode = _Class('BWDepthRotatorNode')
BWStillImageFrameCoordinatorNode = _Class('BWStillImageFrameCoordinatorNode')
BWMeteorHeadroomNode = _Class('BWMeteorHeadroomNode')
BWVideoDefringingNode = _Class('BWVideoDefringingNode')
BWStillImageCoordinatorNode = _Class('BWStillImageCoordinatorNode')
BWStillImageTurnstileNode = _Class('BWStillImageTurnstileNode')
BWStillImageCameraCalibrationDataNode = _Class('BWStillImageCameraCalibrationDataNode')
BWMultiFilterThumbnailNode = _Class('BWMultiFilterThumbnailNode')
BWInferenceSynchronizerNode = _Class('BWInferenceSynchronizerNode')
BWAudioConverterNode = _Class('BWAudioConverterNode')
BWStillImageDisparitySplitterNode = _Class('BWStillImageDisparitySplitterNode')
BWIrisStagingNode = _Class('BWIrisStagingNode')
BWFaceTrackingNode = _Class('BWFaceTrackingNode')
BWStillImageMultiCameraDoserNode = _Class('BWStillImageMultiCameraDoserNode')
BWPhotoEncoderNode = _Class('BWPhotoEncoderNode')
BWStreamingFilterNode = _Class('BWStreamingFilterNode')
BWGNRNode = _Class('BWGNRNode')
BWMRCNode = _Class('BWMRCNode')
BWStillImageScalerNode = _Class('BWStillImageScalerNode')
BWSourceNode = _Class('BWSourceNode')
BWCoreMotionMetadataSourceNode = _Class('BWCoreMotionMetadataSourceNode')
BWAudioSourceNode = _Class('BWAudioSourceNode')
BWMetadataSourceNode = _Class('BWMetadataSourceNode')
BWMultiStreamCameraSourceNode = _Class('BWMultiStreamCameraSourceNode')
BWDeferredProcessingSourceNode = _Class('BWDeferredProcessingSourceNode')
BWSinkNode = _Class('BWSinkNode')
BWRemoteQueueSinkNode = _Class('BWRemoteQueueSinkNode')
BWImageQueueSinkNode = _Class('BWImageQueueSinkNode')
BWStillImageSampleBufferSinkNode = _Class('BWStillImageSampleBufferSinkNode')
BWSceneClassifierSinkNode = _Class('BWSceneClassifierSinkNode')
BWFileSinkNode = _Class('BWFileSinkNode')
BWAudioFileSinkNode = _Class('BWAudioFileSinkNode')
BWQuickTimeMovieFileSinkNode = _Class('BWQuickTimeMovieFileSinkNode')
BWPreviewTimeMachineSinkNode = _Class('BWPreviewTimeMachineSinkNode')
BWPreviewStitcherNode = _Class('BWPreviewStitcherNode')
BWFileCoordinatorNode = _Class('BWFileCoordinatorNode')
BWPixelTransferNode = _Class('BWPixelTransferNode')
BWAttachedMediaSwapNode = _Class('BWAttachedMediaSwapNode')
BWMonochromeEffectNode = _Class('BWMonochromeEffectNode')
BWPortraitHDRStagingNode = _Class('BWPortraitHDRStagingNode')
BWFanOutNode = _Class('BWFanOutNode')
BWFaceDetectionNode = _Class('BWFaceDetectionNode')
BWVideoSDOFSplitNode = _Class('BWVideoSDOFSplitNode')
BWStillImageConditionalRouterNode = _Class('BWStillImageConditionalRouterNode')
BWAttachedMediaSplitNode = _Class('BWAttachedMediaSplitNode')
BWOverCaptureAttachedMediaSplitNode = _Class('BWOverCaptureAttachedMediaSplitNode')
BWParallelSplitterNode = _Class('BWParallelSplitterNode')
BWOverCaptureFanOutNode = _Class('BWOverCaptureFanOutNode')
BWStillImageFocusPixelDisparityNode = _Class('BWStillImageFocusPixelDisparityNode')
BWBackPressureNode = _Class('BWBackPressureNode')
BWPhotoDecompressorNode = _Class('BWPhotoDecompressorNode')
BWMatteMediaSuppressionNode = _Class('BWMatteMediaSuppressionNode')
BWStreamingCVAFilterRendererParameters = _Class('BWStreamingCVAFilterRendererParameters')
BWStillImageMetalSDOFRenderer = _Class('BWStillImageMetalSDOFRenderer')
FigNSXPCConnection = _Class('FigNSXPCConnection')
FigFlatToNSDictionaryWrapperKeyEnumerator = _Class('FigFlatToNSDictionaryWrapperKeyEnumerator')
BWNodeEnumerator = _Class('BWNodeEnumerator')
BWReverseBreadthFirstEnumerator = _Class('BWReverseBreadthFirstEnumerator')
BWBreadthFirstEnumerator = _Class('BWBreadthFirstEnumerator')
BWReverseDepthFirstEnumerator = _Class('BWReverseDepthFirstEnumerator')
BWDepthFirstEnumerator = _Class('BWDepthFirstEnumerator')
FigFlatToNSDictionaryWrapper = _Class('FigFlatToNSDictionaryWrapper')
FigIOSurfaceData = _Class('FigIOSurfaceData')