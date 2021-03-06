'''
Classes from the 'CoreSpeech' framework.
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

    
CSKeywordDetector = _Class('CSKeywordDetector')
CSOSTransaction = _Class('CSOSTransaction')
NviContext = _Class('NviContext')
CSVoiceProfileContext = _Class('CSVoiceProfileContext')
CSCommandControlBehaviorMonitor = _Class('CSCommandControlBehaviorMonitor')
CSVTSecondPassScorer = _Class('CSVTSecondPassScorer')
CSVTSecondPassPhraseScore = _Class('CSVTSecondPassPhraseScore')
CSUserIdentityClassifier = _Class('CSUserIdentityClassifier')
CSGestureDropEvent = _Class('CSGestureDropEvent')
CSSelfTriggerDetector = _Class('CSSelfTriggerDetector')
CSAudioInjectionServices = _Class('CSAudioInjectionServices')
CSAudioConverter = _Class('CSAudioConverter')
CSAsset = _Class('CSAsset')
CSOpportuneSpeakListnerTestService = _Class('CSOpportuneSpeakListnerTestService')
CSAudioRecordDeviceInfo = _Class('CSAudioRecordDeviceInfo')
CSKeywordAnalyzerQuasar = _Class('CSKeywordAnalyzerQuasar')
CSVoiceTriggerXPCClient = _Class('CSVoiceTriggerXPCClient')
CSStartOfSpeechDetector = _Class('CSStartOfSpeechDetector')
CSTrialAssetManager = _Class('CSTrialAssetManager')
CSLanguageDetectorOption = _Class('CSLanguageDetectorOption')
CSSPGEndpointAnalyzer = _Class('CSSPGEndpointAnalyzer')
CSFallbackAudioSessionReleaseProvider = _Class('CSFallbackAudioSessionReleaseProvider')
CSVoiceTriggerInfo = _Class('CSVoiceTriggerInfo')
CSVoiceTriggerAlwaysOnProcessor = _Class('CSVoiceTriggerAlwaysOnProcessor')
CSVoiceIdXPCConnection = _Class('CSVoiceIdXPCConnection')
CSAudioPowerMeter = _Class('CSAudioPowerMeter')
CSCATAssetManager = _Class('CSCATAssetManager')
CSVoiceTriggerStatistics = _Class('CSVoiceTriggerStatistics')
CSEndpointerProxy = _Class('CSEndpointerProxy')
CSAudioSessionInfoProvider = _Class('CSAudioSessionInfoProvider')
CSAudioInjectionDevice = _Class('CSAudioInjectionDevice')
CSOpportuneSpeakListenerOption = _Class('CSOpportuneSpeakListenerOption')
CSHybridEndpointAnalyzer = _Class('CSHybridEndpointAnalyzer')
CSAdBlockerAssetDecoderV1 = _Class('CSAdBlockerAssetDecoderV1')
CSNovDetector = _Class('CSNovDetector')
CSNovDetectorResult = _Class('CSNovDetectorResult')
CSAudioChunk = _Class('CSAudioChunk')
CSAdBlockerAssetDecoderFactory = _Class('CSAdBlockerAssetDecoderFactory')
CSAudioProvider = _Class('CSAudioProvider')
CoreSpeechXPC = _Class('CoreSpeechXPC')
CSActivationEventNotificationHandler = _Class('CSActivationEventNotificationHandler')
CSServerEndpointFeatures = _Class('CSServerEndpointFeatures')
CSAudioStream = _Class('CSAudioStream')
CSRemoteVADCircularBuffer = _Class('CSRemoteVADCircularBuffer')
CSDarkWakePowerAssertionMac = _Class('CSDarkWakePowerAssertionMac')
SSREnrollmentDataManager = _Class('SSREnrollmentDataManager')
CSAudioCircularBuffer = _Class('CSAudioCircularBuffer')
CSVoiceTriggerAOPModeEnabledPolicyFactory = _Class('CSVoiceTriggerAOPModeEnabledPolicyFactory')
CSAudioZeroFilter = _Class('CSAudioZeroFilter')
CSVoiceTriggerEventNotifier = _Class('CSVoiceTriggerEventNotifier')
CSActivationEventNotifier = _Class('CSActivationEventNotifier')
CSShadowMicScoreCreator = _Class('CSShadowMicScoreCreator')
RMSSample = _Class('RMSSample')
CSVoiceTriggerSecondPass = _Class('CSVoiceTriggerSecondPass')
CSBuiltInVoiceTrigger = _Class('CSBuiltInVoiceTrigger')
CSAudioInjectionEngineFactory = _Class('CSAudioInjectionEngineFactory')
CSBeepCanceller = _Class('CSBeepCanceller')
CSAlertBehaviorPredictor = _Class('CSAlertBehaviorPredictor')
NviCSAudioDataSource = _Class('NviCSAudioDataSource')
CSRemoteRecordClient = _Class('CSRemoteRecordClient')
CSVTUIAudioSessionRecorder = _Class('CSVTUIAudioSessionRecorder')
CSVoiceProfileRetrainManager = _Class('CSVoiceProfileRetrainManager')
CSVoiceTriggerRTModel = _Class('CSVoiceTriggerRTModel')
CSRemoteControlClient = _Class('CSRemoteControlClient')
CSSmartSiriVolume = _Class('CSSmartSiriVolume')
CSEndpointerMetrics = _Class('CSEndpointerMetrics')
NviSignalData = _Class('NviSignalData')
NviDirectionalitySignalData = _Class('NviDirectionalitySignalData')
CSKeywordAnalyzerNDAPI = _Class('CSKeywordAnalyzerNDAPI')
CSKeywordAnalyzerNDAPIResult = _Class('CSKeywordAnalyzerNDAPIResult')
CSContinuousAudioFingerprintProvider = _Class('CSContinuousAudioFingerprintProvider')
CSDiagnosticReporter = _Class('CSDiagnosticReporter')
CSPostBuildInstallService = _Class('CSPostBuildInstallService')
CSUtils = _Class('CSUtils')
CSVoiceTriggerAwareZeroFilter = _Class('CSVoiceTriggerAwareZeroFilter')
CSP2PService = _Class('CSP2PService')
CSBluetoothDeviceInfo = _Class('CSBluetoothDeviceInfo')
CSSmartSiriVolumeController = _Class('CSSmartSiriVolumeController')
CSDispatchGroup = _Class('CSDispatchGroup')
CSVoiceTriggerXPCServiceProxy = _Class('CSVoiceTriggerXPCServiceProxy')
CSAssetControllerFactory = _Class('CSAssetControllerFactory')
CSAudioStartStreamOption = _Class('CSAudioStartStreamOption')
CSVoiceTriggerFidesClient = _Class('CSVoiceTriggerFidesClient')
NviUtils = _Class('NviUtils')
CSVoiceTriggerEventInfoProvider = _Class('CSVoiceTriggerEventInfoProvider')
NviConstants = _Class('NviConstants')
CSMyriadPHash = _Class('CSMyriadPHash')
CSOpportuneSpeakBehaviorMonitor = _Class('CSOpportuneSpeakBehaviorMonitor')
CSVoiceTriggerStatAggregator = _Class('CSVoiceTriggerStatAggregator')
CSSmartSiriVolumeEstimate = _Class('CSSmartSiriVolumeEstimate')
CSSiriClientBehaviorMonitor = _Class('CSSiriClientBehaviorMonitor')
NviAudioFileWriter = _Class('NviAudioFileWriter')
CSVoiceTriggerAssetChangeMonitor = _Class('CSVoiceTriggerAssetChangeMonitor')
CSSiriLauncher = _Class('CSSiriLauncher')
CSAudioDecoder = _Class('CSAudioDecoder')
CSSyncKeywordAnalyzerQuasar = _Class('CSSyncKeywordAnalyzerQuasar')
CSAssetController = _Class('CSAssetController')
CSActivationEvent = _Class('CSActivationEvent')
CSAudioStreamRequest = _Class('CSAudioStreamRequest')
CSVoiceTriggerFileLogger = _Class('CSVoiceTriggerFileLogger')
CSAudioFileLog = _Class('CSAudioFileLog')
CSVoiceTriggerDataCollector = _Class('CSVoiceTriggerDataCollector')
CSSmartSiriVolumeManager = _Class('CSSmartSiriVolumeManager')
CSAudioChunkForTV = _Class('CSAudioChunkForTV')
CSPlainAudioFileWriter = _Class('CSPlainAudioFileWriter')
CSStateMachine = _Class('CSStateMachine')
CSXPCClient = _Class('CSXPCClient')
CSVoiceTriggerFirstPassHearstAP = _Class('CSVoiceTriggerFirstPassHearstAP')
NviSignalProvidersController = _Class('NviSignalProvidersController')
SSRAESKeyManager = _Class('SSRAESKeyManager')
CSAudioTimeConverter = _Class('CSAudioTimeConverter')
CSPreferences = _Class('CSPreferences')
SpeechModelTrainingClient = _Class('SpeechModelTrainingClient')
CSSpeechController = _Class('CSSpeechController')
CSKeywordAnalyzerNDEAPI = _Class('CSKeywordAnalyzerNDEAPI')
CSKeywordAnalyzerNDEAPIResult = _Class('CSKeywordAnalyzerNDEAPIResult')
CSAudioRecorderFactory = _Class('CSAudioRecorderFactory')
SSRTriggerPhraseDetectorNDAPIResult = _Class('SSRTriggerPhraseDetectorNDAPIResult')
SSRTriggerPhraseDetectorNDAPI = _Class('SSRTriggerPhraseDetectorNDAPI')
NviDirectionalitySignalProvider = _Class('NviDirectionalitySignalProvider')
CSAssetManager = _Class('CSAssetManager')
CSCommandControlListener = _Class('CSCommandControlListener')
CSSpeechEndHostTimeEstimator = _Class('CSSpeechEndHostTimeEstimator')
CSSpeechManager = _Class('CSSpeechManager')
CSConfig = _Class('CSConfig')
CSAVVoiceTriggerClientManager = _Class('CSAVVoiceTriggerClientManager')
CSOpportuneSpeakListenerDeviceManager = _Class('CSOpportuneSpeakListenerDeviceManager')
CSCoreSpeechServices = _Class('CSCoreSpeechServices')
CSSelectiveChannelAudioFileWriter = _Class('CSSelectiveChannelAudioFileWriter')
CSMyriadSelfTriggerCoordinator = _Class('CSMyriadSelfTriggerCoordinator')
CSStopRecordingOptions = _Class('CSStopRecordingOptions')
CSAudioRecordContext = _Class('CSAudioRecordContext')
CSLanguageDetector = _Class('CSLanguageDetector')
CSActivationXPCClient = _Class('CSActivationXPCClient')
CSBuiltInVoiceTriggerEnabledPolicy = _Class('CSBuiltInVoiceTriggerEnabledPolicy')
CSNNVADEndpointAnalyzer = _Class('CSNNVADEndpointAnalyzer')
CSVoiceTriggerHeartBeatMetricsProvider = _Class('CSVoiceTriggerHeartBeatMetricsProvider')
CSPolicy = _Class('CSPolicy')
CSVoiceTriggerEnabledPolicyHorseman = _Class('CSVoiceTriggerEnabledPolicyHorseman')
CSVoiceTriggerEnabledPolicyMac = _Class('CSVoiceTriggerEnabledPolicyMac')
CSVoiceTriggerEnabledPolicyAOP = _Class('CSVoiceTriggerEnabledPolicyAOP')
CSListeningEnabledPolicyWatch = _Class('CSListeningEnabledPolicyWatch')
CSAlwaysEnabledPolicy = _Class('CSAlwaysEnabledPolicy')
CSAssetManagerEnablePolicy = _Class('CSAssetManagerEnablePolicy')
CSAlwaysDisabledPolicy = _Class('CSAlwaysDisabledPolicy')
CSSelfTriggerDetectorEnabledPolicyIOS = _Class('CSSelfTriggerDetectorEnabledPolicyIOS')
CSVoiceTriggerAOPModeEnabledPolicyIOS = _Class('CSVoiceTriggerAOPModeEnabledPolicyIOS')
CSVoiceTriggerEnabledPolicyNonAOP = _Class('CSVoiceTriggerEnabledPolicyNonAOP')
CSSmartSiriVolumeEnablePolicy = _Class('CSSmartSiriVolumeEnablePolicy')
CSSelfTriggerDetectorEnabledPolicyFactory = _Class('CSSelfTriggerDetectorEnabledPolicyFactory')
CSSelfTriggerDetectorEnabledPolicyGibraltar = _Class('CSSelfTriggerDetectorEnabledPolicyGibraltar')
CSVoiceTriggerFirstPassJarvis = _Class('CSVoiceTriggerFirstPassJarvis')
CSVoiceIdXPCClient = _Class('CSVoiceIdXPCClient')
CSOpportuneSpeakListener = _Class('CSOpportuneSpeakListener')
CSAudioRecorder = _Class('CSAudioRecorder')
CSAudioInjectionProvider = _Class('CSAudioInjectionProvider')
CSSmartSiriVolumeClient = _Class('CSSmartSiriVolumeClient')
CSLanguageDetectorAssetMonitor = _Class('CSLanguageDetectorAssetMonitor')
CSAudioSampleRateConverter = _Class('CSAudioSampleRateConverter')
CSVoiceTriggerFirstPassHearst = _Class('CSVoiceTriggerFirstPassHearst')
CSHearstSecondPassRequest = _Class('CSHearstSecondPassRequest')
CSContinuousVoiceTrigger = _Class('CSContinuousVoiceTrigger')
CSAudioFileReader = _Class('CSAudioFileReader')
CSPowerAssertionMac = _Class('CSPowerAssertionMac')
CSVoiceTriggerFirstPassRemora = _Class('CSVoiceTriggerFirstPassRemora')
CSRemoraSecondPassRequest = _Class('CSRemoraSecondPassRequest')
CSBluetoothManager = _Class('CSBluetoothManager')
CSAssetDownloadingOption = _Class('CSAssetDownloadingOption')
CSAudioPreprocessor = _Class('CSAudioPreprocessor')
CSAudioFileManager = _Class('CSAudioFileManager')
CSVoiceTriggerXPCService = _Class('CSVoiceTriggerXPCService')
CSAudioZeroCounter = _Class('CSAudioZeroCounter')
CSAssetManagerEnablePolicyFactory = _Class('CSAssetManagerEnablePolicyFactory')
CSAudioStreamHolding = _Class('CSAudioStreamHolding')
CSMSNExceptionManager = _Class('CSMSNExceptionManager')
CSAudioInjectionFileOption = _Class('CSAudioInjectionFileOption')
CSCommandControlListenerOption = _Class('CSCommandControlListenerOption')
CSSiriDebugConnection = _Class('CSSiriDebugConnection')
CSAudioSessionController = _Class('CSAudioSessionController')
CSVoiceTriggerAssetHandler = _Class('CSVoiceTriggerAssetHandler')
CSVoiceTriggerAssetHandlerMac = _Class('CSVoiceTriggerAssetHandlerMac')
NviDataLogger = _Class('NviDataLogger')
CSAudioInjectionEngine = _Class('CSAudioInjectionEngine')
CSAudioInjectionRemoraEngine = _Class('CSAudioInjectionRemoraEngine')
CSAudioInjectionTvRemoteEngine = _Class('CSAudioInjectionTvRemoteEngine')
CSAudioInjectionHearstEngine = _Class('CSAudioInjectionHearstEngine')
CSAudioInjectionBuiltInEngine = _Class('CSAudioInjectionBuiltInEngine')
CSBluetoothWirelessSplitterInfo = _Class('CSBluetoothWirelessSplitterInfo')
CSEventMonitor = _Class('CSEventMonitor')
CSSRFUserSettingMonitor = _Class('CSSRFUserSettingMonitor')
CSOpportuneSpeakEventMonitor = _Class('CSOpportuneSpeakEventMonitor')
CSJarvisTriggerModeMonitor = _Class('CSJarvisTriggerModeMonitor')
CSLanguageCodeUpdateMonitor = _Class('CSLanguageCodeUpdateMonitor')
CSSpeechDetectionDevicePresentMonitor = _Class('CSSpeechDetectionDevicePresentMonitor')
CSNetworkAvailabilityMonitor = _Class('CSNetworkAvailabilityMonitor')
CSCoreSpeechDaemonStateMonitor = _Class('CSCoreSpeechDaemonStateMonitor')
CSAudioServerCrashMonitor = _Class('CSAudioServerCrashMonitor')
CSPhraseSpotterEnabledMonitor = _Class('CSPhraseSpotterEnabledMonitor')
CSFirstUnlockMonitor = _Class('CSFirstUnlockMonitor')
CSTrialAssetDownloadMonitor = _Class('CSTrialAssetDownloadMonitor')
CSUserSessionActiveMonitor = _Class('CSUserSessionActiveMonitor')
CSAlwaysOnProcessorStateMonitor = _Class('CSAlwaysOnProcessorStateMonitor')
CSSpringboardStartMonitor = _Class('CSSpringboardStartMonitor')
CSSiriRestrictionOnLockScreenMonitor = _Class('CSSiriRestrictionOnLockScreenMonitor')
CSAdBlockerAssetMetaUpdateMonitor = _Class('CSAdBlockerAssetMetaUpdateMonitor')
CSVoiceTriggerAssetMetaUpdateMonitor = _Class('CSVoiceTriggerAssetMetaUpdateMonitor')
CSBatteryMonitor = _Class('CSBatteryMonitor')
CSSoftwareUpdateCheckingMonitor = _Class('CSSoftwareUpdateCheckingMonitor')
CSSiriEnabledMonitor = _Class('CSSiriEnabledMonitor')
CSVoiceTriggerEnabledMonitor = _Class('CSVoiceTriggerEnabledMonitor')
CSSpeakerRecognitionAssetMetaUpdateMonitor = _Class('CSSpeakerRecognitionAssetMetaUpdateMonitor')
CSSACInfoMonitor = _Class('CSSACInfoMonitor')
CSBuiltinSpeakerStateMonitor = _Class('CSBuiltinSpeakerStateMonitor')
CSHostPowerSourceMonitor = _Class('CSHostPowerSourceMonitor')
CSSpeechEndpointAssetMetaUpdateMonitor = _Class('CSSpeechEndpointAssetMetaUpdateMonitor')
CSBluetoothWirelessSplitterMonitor = _Class('CSBluetoothWirelessSplitterMonitor')
CSScreenLockMonitor = _Class('CSScreenLockMonitor')
CSClamshellStateMonitor = _Class('CSClamshellStateMonitor')
CSAudioSessionMonitor = _Class('CSAudioSessionMonitor')
CSAVVCRecordingClientMonitor = _Class('CSAVVCRecordingClientMonitor')
CSCommandControlStreamEventMonitor = _Class('CSCommandControlStreamEventMonitor')
CSMacWakeSleepMonitor = _Class('CSMacWakeSleepMonitor')
CSAudioRouteChangeMonitor = _Class('CSAudioRouteChangeMonitor')
CSAudioRouteChangeMonitorImpl = _Class('CSAudioRouteChangeMonitorImpl')
CSAudioRouteChangeMonitorImplWatch = _Class('CSAudioRouteChangeMonitorImplWatch')
CSAdBlockerAssetDownloadMonitor = _Class('CSAdBlockerAssetDownloadMonitor')
CSSpeakerRecognitionAssetDownloadMonitor = _Class('CSSpeakerRecognitionAssetDownloadMonitor')
CSSiriAssertionMonitor = _Class('CSSiriAssertionMonitor')
CSVoiceTriggerAssetDownloadMonitor = _Class('CSVoiceTriggerAssetDownloadMonitor')
CSBiometricMatchMonitor = _Class('CSBiometricMatchMonitor')
CSAlarmMonitor = _Class('CSAlarmMonitor')
CSTimerMonitor = _Class('CSTimerMonitor')
CSVolumeMonitor = _Class('CSVolumeMonitor')
CSMediaPlayingMonitor = _Class('CSMediaPlayingMonitor')
CSPhoneCallStateMonitor = _Class('CSPhoneCallStateMonitor')
CSGestureMonitor = _Class('CSGestureMonitor')
CSGestureMonitorPhone = _Class('CSGestureMonitorPhone')
CSDispatchGroup = _Class('CSDispatchGroup')
CSConfig = _Class('CSConfig')
SSRAESKeyManager = _Class('SSRAESKeyManager')
CSUtils = _Class('CSUtils')
SSREnrollmentDataManager = _Class('SSREnrollmentDataManager')
CSAudioDecoder = _Class('CSAudioDecoder')
CSSelectiveChannelAudioFileWriter = _Class('CSSelectiveChannelAudioFileWriter')
CSAudioRecordContext = _Class('CSAudioRecordContext')
CSNNVADEndpointAnalyzer = _Class('CSNNVADEndpointAnalyzer')
CSAudioZeroFilter = _Class('CSAudioZeroFilter')
CSAudioCircularBuffer = _Class('CSAudioCircularBuffer')
CSVoiceTriggerEventInfoProvider = _Class('CSVoiceTriggerEventInfoProvider')
CSAudioTimeConverter = _Class('CSAudioTimeConverter')
CSAVVoiceTriggerClientManager = _Class('CSAVVoiceTriggerClientManager')
CSServerEndpointFeatures = _Class('CSServerEndpointFeatures')
CSDiagnosticReporter = _Class('CSDiagnosticReporter')
CSVoiceIdXPCClient = _Class('CSVoiceIdXPCClient')
CSRemoteRecordClient = _Class('CSRemoteRecordClient')
CSPolicy = _Class('CSPolicy')
CSAsset = _Class('CSAsset')
CSAudioRecorder = _Class('CSAudioRecorder')
CSRemoteControlClient = _Class('CSRemoteControlClient')
CSVTUIAudioSessionRecorder = _Class('CSVTUIAudioSessionRecorder')
CSAudioRecordDeviceInfo = _Class('CSAudioRecordDeviceInfo')
CSOSTransaction = _Class('CSOSTransaction')
CSAudioStreamRequest = _Class('CSAudioStreamRequest')
SSRTriggerPhraseDetectorNDAPIResult = _Class('SSRTriggerPhraseDetectorNDAPIResult')
SSRTriggerPhraseDetectorNDAPI = _Class('SSRTriggerPhraseDetectorNDAPI')
CSAudioPowerMeter = _Class('CSAudioPowerMeter')
CSAudioStartStreamOption = _Class('CSAudioStartStreamOption')
CSAudioChunk = _Class('CSAudioChunk')
CSAudioFileManager = _Class('CSAudioFileManager')
CSAudioFileReader = _Class('CSAudioFileReader')
CSPreferences = _Class('CSPreferences')
CSPlainAudioFileWriter = _Class('CSPlainAudioFileWriter')
CSAudioChunkForTV = _Class('CSAudioChunkForTV')
