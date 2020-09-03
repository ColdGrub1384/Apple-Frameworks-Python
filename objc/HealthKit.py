
'''
Classes from the 'HealthKit' framework.
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
    
    
HKInspectableValueInRange = _Class('HKInspectableValueInRange')
HKGymKitMetricsDataSource = _Class('HKGymKitMetricsDataSource')
HKMedicalCoding = _Class('HKMedicalCoding')
HKOAuth2TokenSession = _Class('HKOAuth2TokenSession')
HKECGOnboardingVersion = _Class('HKECGOnboardingVersion')
HKSourceRevision = _Class('HKSourceRevision')
HKMobileCountryCode = _Class('HKMobileCountryCode')
HKMobileCountryCodeManager = _Class('HKMobileCountryCodeManager')
HKHealthServicesManager = _Class('HKHealthServicesManager')
HKConceptRelationship = _Class('HKConceptRelationship')
HKBackgroundObservationExtension = _Class('HKBackgroundObservationExtension')
HKHeartRateVariabilityUtilities = _Class('HKHeartRateVariabilityUtilities')
HKBeatToBeatInstantaneousBPM = _Class('HKBeatToBeatInstantaneousBPM')
HKCalendarCache = _Class('HKCalendarCache')
HKHeartRateSummaryStatistics = _Class('HKHeartRateSummaryStatistics')
HKHeartRateSummaryBreatheStatistics = _Class('HKHeartRateSummaryBreatheStatistics')
HKHeartRateSummaryWorkoutRecoveryStatistics = _Class('HKHeartRateSummaryWorkoutRecoveryStatistics')
HKHeartRateSummaryWorkoutStatistics = _Class('HKHeartRateSummaryWorkoutStatistics')
HKMedicalDateInterval = _Class('HKMedicalDateInterval')
HKSleepQuery = _Class('HKSleepQuery')
HKHeartRateSummary = _Class('HKHeartRateSummary')
HKNanoSyncPairedDeviceInfo = _Class('HKNanoSyncPairedDeviceInfo')
HKNanoSyncPairedDevicesSnapshot = _Class('HKNanoSyncPairedDevicesSnapshot')
HKJSONVisitor = _Class('HKJSONVisitor')
HKRemoteFeatureAvailabilityRuleSet = _Class('HKRemoteFeatureAvailabilityRuleSet')
HKSleepDay = _Class('HKSleepDay')
HKSleepPeriod = _Class('HKSleepPeriod')
HKSleepPeriodSegment = _Class('HKSleepPeriodSegment')
HKNotificationStore = _Class('HKNotificationStore')
HKDiagnosticStore = _Class('HKDiagnosticStore')
HKSampleTypeChange = _Class('HKSampleTypeChange')
HKOAuth2Credential = _Class('HKOAuth2Credential')
HKWorkoutEvent = _Class('HKWorkoutEvent')
HKCoverageClassification = _Class('HKCoverageClassification')
HKTableFormatter = _Class('HKTableFormatter')
HKFHIRVersion = _Class('HKFHIRVersion')
HKClinicalProvider = _Class('HKClinicalProvider')
HKProfileStore = _Class('HKProfileStore')
HKClinicalAccountLoginCompletionState = _Class('HKClinicalAccountLoginCompletionState')
HKClinicalAccount = _Class('HKClinicalAccount')
HKConceptSynthesizer = _Class('HKConceptSynthesizer')
HKAudioExposureUtilities = _Class('HKAudioExposureUtilities')
HKAudioExposureValue = _Class('HKAudioExposureValue')
HKStatisticsCollection = _Class('HKStatisticsCollection')
HKGPXExporter = _Class('HKGPXExporter')
HKHealthWrapEncryptor = _Class('HKHealthWrapEncryptor')
HKSortedQueryAnchor = _Class('HKSortedQueryAnchor')
HKInspectableValueCollection = _Class('HKInspectableValueCollection')
HKAllergyReaction = _Class('HKAllergyReaction')
HKProfileIdentifier = _Class('HKProfileIdentifier')
HKPPT = _Class('HKPPT')
HKPPTPluginManager = _Class('HKPPTPluginManager')
HKHeartRhythmAvailability = _Class('HKHeartRhythmAvailability')
HKUnit = _Class('HKUnit')
HKBaseUnit = _Class('HKBaseUnit')
HKDecibelHearingLevelUnit = _Class('HKDecibelHearingLevelUnit')
HKTiterUnit = _Class('HKTiterUnit')
HKPotentiallyNonConvertibleMassUnit = _Class('HKPotentiallyNonConvertibleMassUnit')
HKMoleUnit = _Class('HKMoleUnit')
HKEquivalentsUnit = _Class('HKEquivalentsUnit')
HKNonConvertibleIUUnit = _Class('HKNonConvertibleIUUnit')
HKScalarUnit = _Class('HKScalarUnit')
HKFrequencyUnit = _Class('HKFrequencyUnit')
HKElectricPotentialDifferenceUnit = _Class('HKElectricPotentialDifferenceUnit')
HKConductanceUnit = _Class('HKConductanceUnit')
HKTemperatureUnit = _Class('HKTemperatureUnit')
HKEnergyUnit = _Class('HKEnergyUnit')
HKTimeUnit = _Class('HKTimeUnit')
HKDecibelAWeightedSoundPressureLevelUnit = _Class('HKDecibelAWeightedSoundPressureLevelUnit')
HKPressureUnit = _Class('HKPressureUnit')
HKVolumeUnit = _Class('HKVolumeUnit')
HKLengthUnit = _Class('HKLengthUnit')
HKMassUnit = _Class('HKMassUnit')
HKXPCEventObserver = _Class('HKXPCEventObserver')
HKWorkoutRouteDataSource = _Class('HKWorkoutRouteDataSource')
HKActivitySummary = _Class('HKActivitySummary')
HKFeatureAvailabilityStore = _Class('HKFeatureAvailabilityStore')
HKCurrentActivityCacheQueryResult = _Class('HKCurrentActivityCacheQueryResult')
HKWatchAppAvailability = _Class('HKWatchAppAvailability')
HKHealthRecordsIngestionOutcome = _Class('HKHealthRecordsIngestionOutcome')
HKRegionAvailabilityMask = _Class('HKRegionAvailabilityMask')
HKEADFFileParser = _Class('HKEADFFileParser')
HKFHIRResource = _Class('HKFHIRResource')
HKEntitlementStore = _Class('HKEntitlementStore')
HKHeartRateSummaryStatisticsBucket = _Class('HKHeartRateSummaryStatisticsBucket')
HKQuantitySeriesSampleEditor = _Class('HKQuantitySeriesSampleEditor')
HKSampleListDataProviderFilter = _Class('HKSampleListDataProviderFilter')
HKDataCollectorCollectionConfiguration = _Class('HKDataCollectorCollectionConfiguration')
HKDataCollector = _Class('HKDataCollector')
HKAudiogramSensitivityPoint = _Class('HKAudiogramSensitivityPoint')
HKChartableCodedQuantitySet = _Class('HKChartableCodedQuantitySet')
HKMedicalDate = _Class('HKMedicalDate')
HKQuantityDatum = _Class('HKQuantityDatum')
HKKeyValueDomain = _Class('HKKeyValueDomain')
HKClinicalProviderSearchResultsPage = _Class('HKClinicalProviderSearchResultsPage')
HKDataFlowLink = _Class('HKDataFlowLink')
HKCloudSyncControl = _Class('HKCloudSyncControl')
HKStatistics = _Class('HKStatistics')
HKWorkoutSession = _Class('HKWorkoutSession')
HKMultiTypeSampleIterator = _Class('HKMultiTypeSampleIterator')
HKContributor = _Class('HKContributor')
HKLiveWorkoutDataSource = _Class('HKLiveWorkoutDataSource')
HKMedicationDosage = _Class('HKMedicationDosage')
HKSampleQueryDescription = _Class('HKSampleQueryDescription')
HKCSVParser = _Class('HKCSVParser')
HKJSONValidator = _Class('HKJSONValidator')
HKRegionAvailabilityMasks = _Class('HKRegionAvailabilityMasks')
HKAvailableRegions = _Class('HKAvailableRegions')
HKHealthRecordsAccountInfoStore = _Class('HKHealthRecordsAccountInfoStore')
HKHealthStoreProvider = _Class('HKHealthStoreProvider')
HKHealthServiceSession = _Class('HKHealthServiceSession')
HKHealthServiceDiscovery = _Class('HKHealthServiceDiscovery')
HKElectrocardiogramSessionConfiguration = _Class('HKElectrocardiogramSessionConfiguration')
HKElectrocardiogramSession = _Class('HKElectrocardiogramSession')
HKIndexableObject = _Class('HKIndexableObject')
HKConceptIndexUtilities = _Class('HKConceptIndexUtilities')
HKConceptIndexKeyPath = _Class('HKConceptIndexKeyPath')
HKActiveWatchRemoteFeatureAvailabilityDataSource = _Class('HKActiveWatchRemoteFeatureAvailabilityDataSource')
HKSemanticDate = _Class('HKSemanticDate')
HKMedicalIDStore = _Class('HKMedicalIDStore')
HKElectrocardiogramVoltageMeasurement = _Class('HKElectrocardiogramVoltageMeasurement')
HKChartableCodedQuantity = _Class('HKChartableCodedQuantity')
HKRemoteFeatureAvailabilityAlwaysFalseRule = _Class('HKRemoteFeatureAvailabilityAlwaysFalseRule')
HKRemoteFeatureAvailabilityAlwaysTrueRule = _Class('HKRemoteFeatureAvailabilityAlwaysTrueRule')
HKClinicalBrand = _Class('HKClinicalBrand')
HKDeviceStore = _Class('HKDeviceStore')
HKDateInterval = _Class('HKDateInterval')
HKHealthRecordsIngestionPerAccountOutcome = _Class('HKHealthRecordsIngestionPerAccountOutcome')
HKWorkoutConfiguration = _Class('HKWorkoutConfiguration')
HKStateMachine = _Class('HKStateMachine')
HKStateMachineTransition = _Class('HKStateMachineTransition')
HKStateMachineState = _Class('HKStateMachineState')
HKStateMachinePendingEvent = _Class('HKStateMachinePendingEvent')
HKUCUMUnitDisplayConverter = _Class('HKUCUMUnitDisplayConverter')
HKSourceStore = _Class('HKSourceStore')
HKNonMPNDeviceRegionFeatureSupportedStateProvider = _Class('HKNonMPNDeviceRegionFeatureSupportedStateProvider')
HKStaticSyncControl = _Class('HKStaticSyncControl')
HKQueryAnchor = _Class('HKQueryAnchor')
HKElectrocardiogramBuilder = _Class('HKElectrocardiogramBuilder')
HKMultiTypeQueryCursor = _Class('HKMultiTypeQueryCursor')
HKDatabaseControl = _Class('HKDatabaseControl')
HKWorkoutCondenserControl = _Class('HKWorkoutCondenserControl')
HKHealthRecordsStore = _Class('HKHealthRecordsStore')
HKInspectableValue = _Class('HKInspectableValue')
HKRatioValue = _Class('HKRatioValue')
HKMetadataValidationUtilities = _Class('HKMetadataValidationUtilities')
HKSleepAnalysisUtilities = _Class('HKSleepAnalysisUtilities')
HKClinicalProviderSearchResult = _Class('HKClinicalProviderSearchResult')
HKDateIntervalTree = _Class('HKDateIntervalTree')
HKAuthorizationRequestRecord = _Class('HKAuthorizationRequestRecord')
HKAuthorizationPresentationRequest = _Class('HKAuthorizationPresentationRequest')
HKProductVersions = _Class('HKProductVersions')
HKElectrocardiogramActiveAlgorithmVersion = _Class('HKElectrocardiogramActiveAlgorithmVersion')
HKNanoRegistryDeviceUtility = _Class('HKNanoRegistryDeviceUtility')
HKMPNDeviceRegionFeatureSupportedStateProvider = _Class('HKMPNDeviceRegionFeatureSupportedStateProvider')
HKReferenceRange = _Class('HKReferenceRange')
HKSource = _Class('HKSource')
HKMedicalRecordsStore = _Class('HKMedicalRecordsStore')
HKHealthWrapMessage = _Class('HKHealthWrapMessage')
HKHealthWrapMessageConfiguration = _Class('HKHealthWrapMessageConfiguration')
HKWorkoutControl = _Class('HKWorkoutControl')
HKQuerySortConstraint = _Class('HKQuerySortConstraint')
HKCDADocument = _Class('HKCDADocument')
HKCloudSyncObserver = _Class('HKCloudSyncObserver')
HKCloudSyncObserverStatus = _Class('HKCloudSyncObserverStatus')
HKWorkoutDataSource = _Class('HKWorkoutDataSource')
HKDaemonTransaction = _Class('HKDaemonTransaction')
HKCardioFitnessMedicationsUseObject = _Class('HKCardioFitnessMedicationsUseObject')
HKWheelchairUseObject = _Class('HKWheelchairUseObject')
HKFitzpatrickSkinTypeObject = _Class('HKFitzpatrickSkinTypeObject')
HKBiologicalSexObject = _Class('HKBiologicalSexObject')
HKBloodTypeObject = _Class('HKBloodTypeObject')
HKHealthService = _Class('HKHealthService')
HKFHIRIdentifier = _Class('HKFHIRIdentifier')
HKQuantitySeriesSampleBuilder = _Class('HKQuantitySeriesSampleBuilder')
HKPersistentTimer = _Class('HKPersistentTimer')
HKObjectAuthorizationPromptSession = _Class('HKObjectAuthorizationPromptSession')
HKAuthorizationStore = _Class('HKAuthorizationStore')
HKConceptAttribute = _Class('HKConceptAttribute')
HKTokenKeychainItem = _Class('HKTokenKeychainItem')
HKSleepAnalysis = _Class('HKSleepAnalysis')
HKMedicalCodingCollection = _Class('HKMedicalCodingCollection')
HKDevice = _Class('HKDevice')
HKBadge = _Class('HKBadge')
HKSeriesBuilder = _Class('HKSeriesBuilder')
HKWorkoutRouteBuilder = _Class('HKWorkoutRouteBuilder')
HKHeartbeatSeriesBuilder = _Class('HKHeartbeatSeriesBuilder')
HKCodedValueCollection = _Class('HKCodedValueCollection')
HKHeartRateSummaryReading = _Class('HKHeartRateSummaryReading')
HKOnboardingCompletion = _Class('HKOnboardingCompletion')
HKConceptStore = _Class('HKConceptStore')
HKRetryableOperation = _Class('HKRetryableOperation')
HKPendingOperationRecord = _Class('HKPendingOperationRecord')
HKQuantity = _Class('HKQuantity')
HKGymKitDataSource = _Class('HKGymKitDataSource')
HKHealthStoreIdentifier = _Class('HKHealthStoreIdentifier')
HKSynchronousObserverSet = _Class('HKSynchronousObserverSet')
HKProxyProvider = _Class('HKProxyProvider')
HKPluginProxyProvider = _Class('HKPluginProxyProvider')
HKTaskServerProxyProvider = _Class('HKTaskServerProxyProvider')
HKQueryServerProxyProvider = _Class('HKQueryServerProxyProvider')
HKConcept = _Class('HKConcept')
HKSortedSampleArray = _Class('HKSortedSampleArray')
HKObjectType = _Class('HKObjectType')
HKActivitySummaryType = _Class('HKActivitySummaryType')
HKCharacteristicType = _Class('HKCharacteristicType')
HKSampleType = _Class('HKSampleType')
HKClinicalType = _Class('HKClinicalType')
HKHeartbeatSequenceSampleType = _Class('HKHeartbeatSequenceSampleType')
HKElectrocardiogramType = _Class('HKElectrocardiogramType')
HKAudiogramSampleType = _Class('HKAudiogramSampleType')
HKSeriesType = _Class('HKSeriesType')
HKWorkoutType = _Class('HKWorkoutType')
HKDocumentType = _Class('HKDocumentType')
HKCorrelationType = _Class('HKCorrelationType')
HKCategoryType = _Class('HKCategoryType')
HKQuantityType = _Class('HKQuantityType')
HKMedicalType = _Class('HKMedicalType')
HKMedicationRecordType = _Class('HKMedicationRecordType')
HKVaccinationRecordType = _Class('HKVaccinationRecordType')
HKCoverageRecordType = _Class('HKCoverageRecordType')
HKDiagnosticTestReportType = _Class('HKDiagnosticTestReportType')
HKMedicationDispenseRecordType = _Class('HKMedicationDispenseRecordType')
HKConditionRecordType = _Class('HKConditionRecordType')
HKDiagnosticTestResultType = _Class('HKDiagnosticTestResultType')
HKProcedureRecordType = _Class('HKProcedureRecordType')
HKAccountOwnerType = _Class('HKAccountOwnerType')
HKAllergyRecordType = _Class('HKAllergyRecordType')
HKMedicationOrderType = _Class('HKMedicationOrderType')
HKUnknownRecordType = _Class('HKUnknownRecordType')
HKHealthStore = _Class('HKHealthStore')
HKNanoSyncControl = _Class('HKNanoSyncControl')
HKQuery = _Class('HKQuery')
HKDocumentQuery = _Class('HKDocumentQuery')
HKDeviceQuery = _Class('HKDeviceQuery')
HKSampleCountQuery = _Class('HKSampleCountQuery')
HKCorrelationQuery = _Class('HKCorrelationQuery')
HKMultiTypeSampleQuery = _Class('HKMultiTypeSampleQuery')
HKStatisticsCollectionQuery = _Class('HKStatisticsCollectionQuery')
HKSourceQuery = _Class('HKSourceQuery')
HKElectrocardiogramQuery = _Class('HKElectrocardiogramQuery')
HKWorkoutBuilderSampleQuery = _Class('HKWorkoutBuilderSampleQuery')
HKActivitySummaryQuery = _Class('HKActivitySummaryQuery')
HKAnchoredObjectQuery = _Class('HKAnchoredObjectQuery')
HKQuantitySeriesSampleQuery = _Class('HKQuantitySeriesSampleQuery')
HKWorkoutRouteQuery = _Class('HKWorkoutRouteQuery')
HKStatisticsQuery = _Class('HKStatisticsQuery')
HKObserverQuery = _Class('HKObserverQuery')
HKSampleQuery = _Class('HKSampleQuery')
HKHeartbeatSeriesQuery = _Class('HKHeartbeatSeriesQuery')
HKCurrentActivityCacheQuery = _Class('HKCurrentActivityCacheQuery')
HKHeartRateSummaryQuery = _Class('HKHeartRateSummaryQuery')
HKCodedQuantity = _Class('HKCodedQuantity')
HKMedicalCodingSystem = _Class('HKMedicalCodingSystem')
HKHealthStoreConfiguration = _Class('HKHealthStoreConfiguration')
HKPluginLoader = _Class('HKPluginLoader')
HKObserverSet = _Class('HKObserverSet')
HKDeletedObject = _Class('HKDeletedObject')
HKRemoteFeatureAvailabilityBaseRule = _Class('HKRemoteFeatureAvailabilityBaseRule')
HKRemoteFeatureAvailabilityActiveWatchAtrialFibrillationDetectionVersionEqualsRule = _Class('HKRemoteFeatureAvailabilityActiveWatchAtrialFibrillationDetectionVersionEqualsRule')
HKRemoteFeatureAvailabilityActiveWatchElectrocardiogramVersionLessThanRule = _Class('HKRemoteFeatureAvailabilityActiveWatchElectrocardiogramVersionLessThanRule')
HKRemoteFeatureAvailabilityWatchOSVersionLessThanRule = _Class('HKRemoteFeatureAvailabilityWatchOSVersionLessThanRule')
HKRemoteFeatureAvailabilityActiveWatchElectrocardiogramVersionEqualsRule = _Class('HKRemoteFeatureAvailabilityActiveWatchElectrocardiogramVersionEqualsRule')
HKRemoteFeatureAvailabilityWatchBuildTypeEqualsRule = _Class('HKRemoteFeatureAvailabilityWatchBuildTypeEqualsRule')
HKRemoteFeatureAvailabilityWatchCompanionDevicePlatformEqualsRule = _Class('HKRemoteFeatureAvailabilityWatchCompanionDevicePlatformEqualsRule')
HKRemoteFeatureAvailabilityWatchOSBuildVersionLessThanRule = _Class('HKRemoteFeatureAvailabilityWatchOSBuildVersionLessThanRule')
HKRemoteFeatureAvailabilityWatchModelNumberHasPrefixRule = _Class('HKRemoteFeatureAvailabilityWatchModelNumberHasPrefixRule')
HKRemoteFeatureAvailabilityWatchOSBuildVersionGreaterThanRule = _Class('HKRemoteFeatureAvailabilityWatchOSBuildVersionGreaterThanRule')
HKRemoteFeatureAvailabilityActiveWatchAtrialFibrillationDetectionVersionLessThanRule = _Class('HKRemoteFeatureAvailabilityActiveWatchAtrialFibrillationDetectionVersionLessThanRule')
HKRemoteFeatureAvailabilityAtrialFibrillationOnboardingCountryCodeRule = _Class('HKRemoteFeatureAvailabilityAtrialFibrillationOnboardingCountryCodeRule')
HKRemoteFeatureAvailabilityWatchOSVersionEqualsRule = _Class('HKRemoteFeatureAvailabilityWatchOSVersionEqualsRule')
HKRemoteFeatureAvailabilityWatchRegionEqualsRule = _Class('HKRemoteFeatureAvailabilityWatchRegionEqualsRule')
HKRemoteFeatureAvailabilityActiveWatchAtrialFibrillationDetectionVersionGreaterThanRule = _Class('HKRemoteFeatureAvailabilityActiveWatchAtrialFibrillationDetectionVersionGreaterThanRule')
HKRemoteFeatureAvailabilityCompoundRule = _Class('HKRemoteFeatureAvailabilityCompoundRule')
HKRemoteFeatureAvailabilityWatchOSVersionGreaterThanRule = _Class('HKRemoteFeatureAvailabilityWatchOSVersionGreaterThanRule')
HKRemoteFeatureAvailabilityElectrocardiogramOnboardingCountryCodeRule = _Class('HKRemoteFeatureAvailabilityElectrocardiogramOnboardingCountryCodeRule')
HKRemoteFeatureAvailabilityWatchOSBuildVersionEqualsRule = _Class('HKRemoteFeatureAvailabilityWatchOSBuildVersionEqualsRule')
HKRemoteFeatureAvailabilityActiveWatchElectrocardiogramVersionGreaterThanRule = _Class('HKRemoteFeatureAvailabilityActiveWatchElectrocardiogramVersionGreaterThanRule')
HKRemoteFeatureAvailabilityWatchProductTypeHasPrefixRule = _Class('HKRemoteFeatureAvailabilityWatchProductTypeHasPrefixRule')
HKObject = _Class('HKObject')
HKSample = _Class('HKSample')
HKElectrocardiogram = _Class('HKElectrocardiogram')
HKCategorySample = _Class('HKCategorySample')
HKWorkout = _Class('HKWorkout')
HKCorrelation = _Class('HKCorrelation')
HKActivityCache = _Class('HKActivityCache')
HKAudiogramSample = _Class('HKAudiogramSample')
HKDocumentSample = _Class('HKDocumentSample')
HKCDADocumentSample = _Class('HKCDADocumentSample')
HKClinicalRecord = _Class('HKClinicalRecord')
HKSleepSchedule = _Class('HKSleepSchedule')
HKQuantitySample = _Class('HKQuantitySample')
HKDiscreteQuantitySample = _Class('HKDiscreteQuantitySample')
HKCumulativeQuantitySample = _Class('HKCumulativeQuantitySample')
HKCumulativeQuantitySeriesSample = _Class('HKCumulativeQuantitySeriesSample')
HKSeriesSample = _Class('HKSeriesSample')
HKHeartbeatSeriesSample = _Class('HKHeartbeatSeriesSample')
HKHeartbeatSequenceSample = _Class('HKHeartbeatSequenceSample')
HKWorkoutRoute = _Class('HKWorkoutRoute')
HKMedicalRecord = _Class('HKMedicalRecord')
HKVaccinationRecord = _Class('HKVaccinationRecord')
HKAllergyRecord = _Class('HKAllergyRecord')
HKUnknownRecord = _Class('HKUnknownRecord')
HKProcedureRecord = _Class('HKProcedureRecord')
HKConditionRecord = _Class('HKConditionRecord')
HKMedicationRecord = _Class('HKMedicationRecord')
HKCoverageRecord = _Class('HKCoverageRecord')
HKDiagnosticTestReport = _Class('HKDiagnosticTestReport')
HKDiagnosticTestResult = _Class('HKDiagnosticTestResult')
HKAccountOwner = _Class('HKAccountOwner')
HKMedicationOrder = _Class('HKMedicationOrder')
HKMedicationDispenseRecord = _Class('HKMedicationDispenseRecord')
HKClinicalGateway = _Class('HKClinicalGateway')
HKCodedValue = _Class('HKCodedValue')
HKFeatureAvailabilityDatabaseInaccessibilityCache = _Class('HKFeatureAvailabilityDatabaseInaccessibilityCache')
HKWorkoutBuilder = _Class('HKWorkoutBuilder')
HKLiveWorkoutBuilder = _Class('HKLiveWorkoutBuilder')
HKTaskConfiguration = _Class('HKTaskConfiguration')
HKQuantitySeriesSampleEditorTaskServerConfiguration = _Class('HKQuantitySeriesSampleEditorTaskServerConfiguration')
HKDataCollectorTaskServerConfiguration = _Class('HKDataCollectorTaskServerConfiguration')
HKSeriesBuilderConfiguration = _Class('HKSeriesBuilderConfiguration')
HKKeyValueDomainServerConfiguration = _Class('HKKeyValueDomainServerConfiguration')
HKWorkoutSessionTaskConfiguration = _Class('HKWorkoutSessionTaskConfiguration')
HKFeatureAvailabilityStoreServerConfiguration = _Class('HKFeatureAvailabilityStoreServerConfiguration')
HKElectrocardiogramSessionTaskConfiguration = _Class('HKElectrocardiogramSessionTaskConfiguration')
HKWorkoutDataSourceConfiguration = _Class('HKWorkoutDataSourceConfiguration')
HKQuantitySeriesSampleBuilderTaskServerConfiguration = _Class('HKQuantitySeriesSampleBuilderTaskServerConfiguration')
HKConceptStoreServerConfiguration = _Class('HKConceptStoreServerConfiguration')
HKQueryServerConfiguration = _Class('HKQueryServerConfiguration')
HKActivitySummaryQueryServerConfiguration = _Class('HKActivitySummaryQueryServerConfiguration')
HKCurrentActivityCacheQueryServerConfiguration = _Class('HKCurrentActivityCacheQueryServerConfiguration')
HKWorkoutBuilderConfiguration = _Class('HKWorkoutBuilderConfiguration')
HKConceptIdentifier = _Class('HKConceptIdentifier')
HKHealthWrapCodableValue = _Class('HKHealthWrapCodableValue')
HKHealthWrapCodableKeyValue = _Class('HKHealthWrapCodableKeyValue')
HKCodableCondensedWorkout = _Class('HKCodableCondensedWorkout')
HKHealthWrapCodablePayloadHeader = _Class('HKHealthWrapCodablePayloadHeader')
HKCodableQuantitySeriesEnumerationResult = _Class('HKCodableQuantitySeriesEnumerationResult')
HKCodableQuantitySeriesDatum = _Class('HKCodableQuantitySeriesDatum')
HKHealthWrapCodableMessageHeader = _Class('HKHealthWrapCodableMessageHeader')
HKHealthWrapCodableMessageKey = _Class('HKHealthWrapCodableMessageKey')
HKCodableQuantitySeriesEnumerationResultCollection = _Class('HKCodableQuantitySeriesEnumerationResultCollection')
HKCodableQuantitySeries = _Class('HKCodableQuantitySeries')
HKCodableCondensedWorkoutCollection = _Class('HKCodableCondensedWorkoutCollection')