
'''
Classes from the 'CoreSuggestionsInternals' framework.
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
    
    
SGDatabaseJournal = _Class('SGDatabaseJournal')
SGCachedResult = _Class('SGCachedResult')
SGLazyResult = _Class('SGLazyResult')
SGLazyPurgeableResult = _Class('SGLazyPurgeableResult')
SGLazyImmortalResult = _Class('SGLazyImmortalResult')
SGEKCalendarAdapter = _Class('SGEKCalendarAdapter')
SGContactSharingTransformer = _Class('SGContactSharingTransformer')
SGMicrodataParserStackItem = _Class('SGMicrodataParserStackItem')
SGDPLogging = _Class('SGDPLogging')
SGPortraitUtils = _Class('SGPortraitUtils')
SGSpotlightContactsAdapter = _Class('SGSpotlightContactsAdapter')
SGSchemaKeys = _Class('SGSchemaKeys')
SGXpcTransaction = _Class('SGXpcTransaction')
SGDNotificationBroadcaster = _Class('SGDNotificationBroadcaster')
SGCuratedEventKey = _Class('SGCuratedEventKey')
SGTopicExtractionPlugin = _Class('SGTopicExtractionPlugin')
SGLevenshtein = _Class('SGLevenshtein')
SGSeekableData = _Class('SGSeekableData')
SGDatabaseMigratorEntities = _Class('SGDatabaseMigratorEntities')
SGNameDetector = _Class('SGNameDetector')
SGContactAggregator = _Class('SGContactAggregator')
SGStringDonationHandler = _Class('SGStringDonationHandler')
SGFoundInAppsStrings = _Class('SGFoundInAppsStrings')
SGMailClientUtil = _Class('SGMailClientUtil')
SGDuplicateKey = _Class('SGDuplicateKey')
SGDSpotlightCommander = _Class('SGDSpotlightCommander')
SGMicrodataParser = _Class('SGMicrodataParser')
SGContentAdmission = _Class('SGContentAdmission')
SGContentAdmissionKVOObserver = _Class('SGContentAdmissionKVOObserver')
SGMicrodataItemProp = _Class('SGMicrodataItemProp')
SGIdentityKey = _Class('SGIdentityKey')
SGPlainTextContentCursor = _Class('SGPlainTextContentCursor')
SGRe2 = _Class('SGRe2')
SGRe2Lazy = _Class('SGRe2Lazy')
SGRe2Subregexps = _Class('SGRe2Subregexps')
SGRe2Basic = _Class('SGRe2Basic')
SGDetectedAttributeML = _Class('SGDetectedAttributeML')
SGContactDetailSupervision = _Class('SGContactDetailSupervision')
SGSelfIDSupervision = _Class('SGSelfIDSupervision')
SGEntityMatchingTransformer = _Class('SGEntityMatchingTransformer')
SGTokenizerMappingTransformer = _Class('SGTokenizerMappingTransformer')
SGPortraitRequestHandler = _Class('SGPortraitRequestHandler')
SGPortraitRequestServerDelegate = _Class('SGPortraitRequestServerDelegate')
SGPortraitRequestServerHandlerCache = _Class('SGPortraitRequestServerHandlerCache')
SGNameInversionPredictor = _Class('SGNameInversionPredictor')
SGCuratedContactMatcher = _Class('SGCuratedContactMatcher')
SGContactPipelineHelper = _Class('SGContactPipelineHelper')
SGDSpotlightReceiver = _Class('SGDSpotlightReceiver')
SGStorageEvent = _Class('SGStorageEvent')
SGMailAttachment = _Class('SGMailAttachment')
SGPseudoContactKey = _Class('SGPseudoContactKey')
SGContactDetailKey = _Class('SGContactDetailKey')
SGPaths = _Class('SGPaths')
SGPOSTagger = _Class('SGPOSTagger')
SGPipeline = _Class('SGPipeline')
SGDOMParserResult = _Class('SGDOMParserResult')
SGRawKey = _Class('SGRawKey')
SGJournal = _Class('SGJournal')
SGStructuredEventClassification = _Class('SGStructuredEventClassification')
SGDSqlHarvestQueueStore = _Class('SGDSqlHarvestQueueStore')
SGIdentityName = _Class('SGIdentityName')
SGDeliveryKey = _Class('SGDeliveryKey')
SGURLContainer = _Class('SGURLContainer')
SGMetricsHelper = _Class('SGMetricsHelper')
SGAppLaunchHistory = _Class('SGAppLaunchHistory')
SGDataNormalization = _Class('SGDataNormalization')
SGPseudoReminderKey = _Class('SGPseudoReminderKey')
SGReverseTemplatesJSDataDetectors = _Class('SGReverseTemplatesJSDataDetectors')
SGServiceContext = _Class('SGServiceContext')
SGOutput = _Class('SGOutput')
SGSqlEntityStore = _Class('SGSqlEntityStore')
SGCustomResponseHarvester = _Class('SGCustomResponseHarvester')
SGSGtoCNContactsCacheUpdateAdapter = _Class('SGSGtoCNContactsCacheUpdateAdapter')
SGContactDetail = _Class('SGContactDetail')
SGTaggedCharacterRange = _Class('SGTaggedCharacterRange')
SGAggregateLogging = _Class('SGAggregateLogging')
SGPortraitRequestClient = _Class('SGPortraitRequestClient')
SGPortraitExtractionContainer = _Class('SGPortraitExtractionContainer')
SGMailPatterns = _Class('SGMailPatterns')
SGXPCServer = _Class('SGXPCServer')
SGExtractionModelCoreMLFeatureWrapper = _Class('SGExtractionModelCoreMLFeatureWrapper')
SGHKHealthStore = _Class('SGHKHealthStore')
SGTokenizer = _Class('SGTokenizer')
SGReminderTrialClientWrapperGuardedData = _Class('SGReminderTrialClientWrapperGuardedData')
SGMailQuoteParser = _Class('SGMailQuoteParser')
SGPseudoEventKey = _Class('SGPseudoEventKey')
SGMeContact = _Class('SGMeContact')
SGSlice = _Class('SGSlice')
SGHtmlEntities = _Class('SGHtmlEntities')
SGModelMappingHelper = _Class('SGModelMappingHelper')
SGPostalAddressExtraction = _Class('SGPostalAddressExtraction')
SGCoalescingDropBox = _Class('SGCoalescingDropBox')
SGStringMappingTransformer = _Class('SGStringMappingTransformer')
SGDPWatchMetricsCollector = _Class('SGDPWatchMetricsCollector')
SGJournalEntry = _Class('SGJournalEntry')
SGTokenDistanceMappingTransformer = _Class('SGTokenDistanceMappingTransformer')
SGStructuredEventCoreMLOutputWrapper = _Class('SGStructuredEventCoreMLOutputWrapper')
SGLabeledValue = _Class('SGLabeledValue')
SGCNContactIdentifierCollection = _Class('SGCNContactIdentifierCollection')
SGDetection = _Class('SGDetection')
SGChatLengthEstimator = _Class('SGChatLengthEstimator')
SGReminderDueLocation = _Class('SGReminderDueLocation')
SGCuratedChangeNotifications = _Class('SGCuratedChangeNotifications')
SGCuratedChangeNotificationsBaseListener = _Class('SGCuratedChangeNotificationsBaseListener')
SGCuratedChangeNotificationsCalendarListener = _Class('SGCuratedChangeNotificationsCalendarListener')
SGCuratedChangeNotificationsAddressBookListener = _Class('SGCuratedChangeNotificationsAddressBookListener')
SGDCloudKitSyncObserver = _Class('SGDCloudKitSyncObserver')
SGDCloudKitSync = _Class('SGDCloudKitSync')
SGStorageLocation = _Class('SGStorageLocation')
SGDOMParser = _Class('SGDOMParser')
SGNames = _Class('SGNames')
SGAhoCorasick = _Class('SGAhoCorasick')
SGDHarvestQueueFileReader = _Class('SGDHarvestQueueFileReader')
SGDHarvestQueueFileWriter = _Class('SGDHarvestQueueFileWriter')
SGDHarvestQueueFileRegistry = _Class('SGDHarvestQueueFileRegistry')
SGDHarvestQueueItem = _Class('SGDHarvestQueueItem')
SGDHarvestQueueItemInMemory = _Class('SGDHarvestQueueItemInMemory')
SGDHarvestQueueItemLegacy = _Class('SGDHarvestQueueItemLegacy')
SGDHarvestQueueItemOnDisk = _Class('SGDHarvestQueueItemOnDisk')
SGDHarvestQueue = _Class('SGDHarvestQueue')
SGDHarvestQueueNop = _Class('SGDHarvestQueueNop')
SGDHarvestQueueCombo = _Class('SGDHarvestQueueCombo')
SGDHarvestQueueInMemory = _Class('SGDHarvestQueueInMemory')
SGDHarvestQueueLegacy = _Class('SGDHarvestQueueLegacy')
SGDHarvestQueueOnDisk = _Class('SGDHarvestQueueOnDisk')
SGSchemaOrgKey = _Class('SGSchemaOrgKey')
SGMicrodataDocument = _Class('SGMicrodataDocument')
SGSqliteDatabase = _Class('SGSqliteDatabase')
SGSqliteDatabaseSharedLock = _Class('SGSqliteDatabaseSharedLock')
SGTrialClientWrapper = _Class('SGTrialClientWrapper')
SGReminderTrialClientWrapper = _Class('SGReminderTrialClientWrapper')
SGStructuredEventTrialClientWrapper = _Class('SGStructuredEventTrialClientWrapper')
SGStructuredEventTrialClientWrapperGuardedData = _Class('SGStructuredEventTrialClientWrapperGuardedData')
SGContactStoreFactory = _Class('SGContactStoreFactory')
SGReverseTemplateJS = _Class('SGReverseTemplateJS')
SGLongRunningTaskManager = _Class('SGLongRunningTaskManager')
SGLongRunningTask = _Class('SGLongRunningTask')
SGXPCActivityManager = _Class('SGXPCActivityManager')
SGRTCLogging = _Class('SGRTCLogging')
SGStructuredEventCoreMLInputWrapper = _Class('SGStructuredEventCoreMLInputWrapper')
SGRequestContext = _Class('SGRequestContext')
SGDatabaseJournalFile = _Class('SGDatabaseJournalFile')
SGConversationHistory = _Class('SGConversationHistory')
SGTextMessageItem = _Class('SGTextMessageItem')
SGTextMessageConversationTracker = _Class('SGTextMessageConversationTracker')
SGBloomFilterChunkMmap = _Class('SGBloomFilterChunkMmap')
SGBloomFilterChunkInMemorySparse = _Class('SGBloomFilterChunkInMemorySparse')
SGBloomFilterChunkInMemory = _Class('SGBloomFilterChunkInMemory')
SGBloomFilter = _Class('SGBloomFilter')
SGTaggedMallocEmailHtml = _Class('SGTaggedMallocEmailHtml')
SGTaggedMallocLevenshteinDistanceBuffer = _Class('SGTaggedMallocLevenshteinDistanceBuffer')
SGTaggedMallocWorkQueueItemPart = _Class('SGTaggedMallocWorkQueueItemPart')
SGTaggedMallocCompressionBuffer = _Class('SGTaggedMallocCompressionBuffer')
SGFlight = _Class('SGFlight')
SGFlightData = _Class('SGFlightData')
SGOffsetDictionary = _Class('SGOffsetDictionary')
SGSymbolicMappingTransformer = _Class('SGSymbolicMappingTransformer')
SGContactsInterface = _Class('SGContactsInterface')
SGNicknames = _Class('SGNicknames')
SGLexicon = _Class('SGLexicon')
SGLowMemoryContactEnumeration = _Class('SGLowMemoryContactEnumeration')
SGHtmlParser = _Class('SGHtmlParser')
SGQuickResponsesML = _Class('SGQuickResponsesML')
SGDPStringRecorder = _Class('SGDPStringRecorder')
SGNamedEntityExtractionPlugin = _Class('SGNamedEntityExtractionPlugin')
SGSimpleMailHeaderKeyValue = _Class('SGSimpleMailHeaderKeyValue')
SGPatternDataFile = _Class('SGPatternDataFile')
SGPatterns = _Class('SGPatterns')
SGPatternGlobalData = _Class('SGPatternGlobalData')
SGContactDetailSummary = _Class('SGContactDetailSummary')
SGIdentityEdge = _Class('SGIdentityEdge')
SGInhumans = _Class('SGInhumans')
SGThreadParser = _Class('SGThreadParser')
SGDataDetectorMatch = _Class('SGDataDetectorMatch')
SGAddressCoalescingState = _Class('SGAddressCoalescingState')
SGDataDetectorMatchesWithSignatureRange = _Class('SGDataDetectorMatchesWithSignatureRange')
SGWords = _Class('SGWords')
SGKeyValueCacheManager = _Class('SGKeyValueCacheManager')
SGSuggestHistory = _Class('SGSuggestHistory')
SGHistorySharedData = _Class('SGHistorySharedData')
SGEntity = _Class('SGEntity')
SGContactEntity = _Class('SGContactEntity')
SGPipelineEnrichment = _Class('SGPipelineEnrichment')
SGPipelineEntity = _Class('SGPipelineEntity')
SGSearchableItemIdTriple = _Class('SGSearchableItemIdTriple')
SGNamedEntityDissectorGuardedData = _Class('SGNamedEntityDissectorGuardedData')
SGNLPDetection = _Class('SGNLPDetection')
SGSelfIdentificationDetection = _Class('SGSelfIdentificationDetection')
SGSelfIdentification = _Class('SGSelfIdentification')
SGNameMappingTransformer = _Class('SGNameMappingTransformer')
SGRemindersAdapter = _Class('SGRemindersAdapter')
SGInMemoryAdapter = _Class('SGInMemoryAdapter')
SGAccountsAdapter = _Class('SGAccountsAdapter')
SGContextKitResultContainer = _Class('SGContextKitResultContainer')
SGDPluginManager = _Class('SGDPluginManager')
SGDatabaseMigratorSnippets = _Class('SGDatabaseMigratorSnippets')
SGStorageContact = _Class('SGStorageContact')
SGContactDetailsHolder = _Class('SGContactDetailsHolder')
SGTopicDissectorGuardedData = _Class('SGTopicDissectorGuardedData')
SGDeduper = _Class('SGDeduper')
SGDManagerForCTS = _Class('SGDManagerForCTS')
SGRe2PrefilterTree = _Class('SGRe2PrefilterTree')
SGDPowerBudgetThrottlingState = _Class('SGDPowerBudgetThrottlingState')
SGDPowerBudget = _Class('SGDPowerBudget')
SGExtractionModel = _Class('SGExtractionModel')
SGReminderExtractionModel = _Class('SGReminderExtractionModel')
SGStructuredEventExtractionModel = _Class('SGStructuredEventExtractionModel')
SGDWorkQueueName = _Class('SGDWorkQueueName')
SGDWorkQueueItem = _Class('SGDWorkQueueItem')
SGDWorkQueue = _Class('SGDWorkQueue')
SGDWorkQueueFile = _Class('SGDWorkQueueFile')
SGEntityMappingTransformer = _Class('SGEntityMappingTransformer')
SGDSuggestManager = _Class('SGDSuggestManager')
SGEKEventStoreProvider = _Class('SGEKEventStoreProvider')
SGRealtimeSuggestionsTuple = _Class('SGRealtimeSuggestionsTuple')
SGHistoryObserver = _Class('SGHistoryObserver')
SGRealtimeEventResponse = _Class('SGRealtimeEventResponse')
SGDPowerLog = _Class('SGDPowerLog')
SGMessageKey = _Class('SGMessageKey')
SGWebPageKey = _Class('SGWebPageKey')
SGEmailKey = _Class('SGEmailKey')
SGInteractionKey = _Class('SGInteractionKey')
SGTextMessageKey = _Class('SGTextMessageKey')
SGDetectedAttributeMetrics = _Class('SGDetectedAttributeMetrics')
SGMonochrome = _Class('SGMonochrome')
SGMicrodataItemScope = _Class('SGMicrodataItemScope')
SGMicrodataItem = _Class('SGMicrodataItem')
SGURLPlugin = _Class('SGURLPlugin')
SGPipelineDissector = _Class('SGPipelineDissector')
SGDonatedContactDissector = _Class('SGDonatedContactDissector')
SGNaturalLanguageDissector = _Class('SGNaturalLanguageDissector')
SGURLDissector = _Class('SGURLDissector')
SGExtractionDissector = _Class('SGExtractionDissector')
SGDetectedAttributeDissector = _Class('SGDetectedAttributeDissector')
SGMetricsDissector = _Class('SGMetricsDissector')
SGSignatureDissector = _Class('SGSignatureDissector')
SGStructuredEventDissector = _Class('SGStructuredEventDissector')
SGMeCardDissector = _Class('SGMeCardDissector')
SGNamedEntityDissector = _Class('SGNamedEntityDissector')
SGCalendarAttachmentDissector = _Class('SGCalendarAttachmentDissector')
SGTopicDissector = _Class('SGTopicDissector')
SGDeliveryDissector = _Class('SGDeliveryDissector')
SGReminderDissector = _Class('SGReminderDissector')
SGExtractionDocument = _Class('SGExtractionDocument')
SGReminderMessage = _Class('SGReminderMessage')
SGStructuredEventDocument = _Class('SGStructuredEventDocument')
SGWordBoundaryQuickTypeInference = _Class('SGWordBoundaryQuickTypeInference')
SGModelRules = _Class('SGModelRules')
SGTransformerInstance = _Class('SGTransformerInstance')
SGModel = _Class('SGModel')
SGEspressoModel = _Class('SGEspressoModel')
SGContactSharingModel = _Class('SGContactSharingModel')
SGBinaryClassificationModel = _Class('SGBinaryClassificationModel')
SGSignificantAddressModelForIMessage = _Class('SGSignificantAddressModelForIMessage')
SGSignificantAddressModel = _Class('SGSignificantAddressModel')
SGTextMessageBirthdayCongratsModel = _Class('SGTextMessageBirthdayCongratsModel')
SGSignificantPhonenumberModel = _Class('SGSignificantPhonenumberModel')
SGSelfIdentificationModel = _Class('SGSelfIdentificationModel')
SGSignificantEmailAddressModel = _Class('SGSignificantEmailAddressModel')
SGSignificantEmailAddressModelForIMessage = _Class('SGSignificantEmailAddressModelForIMessage')
SGMicrodataToJsonParser = _Class('SGMicrodataToJsonParser')
SGConversationFlatteningTransformer = _Class('SGConversationFlatteningTransformer')
SGMessage = _Class('SGMessage')
SGSimpleMailMessage = _Class('SGSimpleMailMessage')
SGTextMessage = _Class('SGTextMessage')
SGAsset = _Class('SGAsset')
SGStorageReminder = _Class('SGStorageReminder')
SGSqliteDatabaseImpl = _Class('SGSqliteDatabaseImpl')
SGJSBurstTrie = _Class('SGJSBurstTrie')
SGSqliteExitOnDeviceLockErrorHandler = _Class('SGSqliteExitOnDeviceLockErrorHandler')
SGDCKTimeRange = _Class('SGDCKTimeRange')
SGDCKEvent = _Class('SGDCKEvent')
SGM2BirthdayExtractionWithSupervision = _Class('SGM2BirthdayExtractionWithSupervision')
SGDCKInteractionInfo = _Class('SGDCKInteractionInfo')
SGDCKLocation = _Class('SGDCKLocation')
SGM2CustomResponsesHarvest = _Class('SGM2CustomResponsesHarvest')
SGM2PerfXPCLatency = _Class('SGM2PerfXPCLatency')
SGM2UnknownContactInformationShown = _Class('SGM2UnknownContactInformationShown')
SGM2SuggestedContactDetailUsed = _Class('SGM2SuggestedContactDetailUsed')
SGM2SuggestedContactDetailShown = _Class('SGM2SuggestedContactDetailShown')
SGM2SqliteErrors = _Class('SGM2SqliteErrors')
SGM2SerializedContactsCacheHit = _Class('SGM2SerializedContactsCacheHit')
SGM2SearchResultsUserSelectedContact = _Class('SGM2SearchResultsUserSelectedContact')
SGM2SearchResultsIncludedPureSuggestion = _Class('SGM2SearchResultsIncludedPureSuggestion')
SGM2FoundInMailModelScore = _Class('SGM2FoundInMailModelScore')
SGM2ContactsInterfaceCacheHit = _Class('SGM2ContactsInterfaceCacheHit')
SGM2ContactsInterfaceCacheCount = _Class('SGM2ContactsInterfaceCacheCount')
SGM2ContactDetailSent = _Class('SGM2ContactDetailSent')
SGM2ContactDetailExtraction = _Class('SGM2ContactDetailExtraction')
SGM2ContactCreated = _Class('SGM2ContactCreated')
SGM2BundleIdsTrackedAsOther = _Class('SGM2BundleIdsTrackedAsOther')
SGM2AutocompleteUserSelectedContact = _Class('SGM2AutocompleteUserSelectedContact')
SGM2SuggestdExitReason = _Class('SGM2SuggestdExitReason')
SGM2SelfIdModelScore = _Class('SGM2SelfIdModelScore')
SGNoCloudNSUbiquitousKeyValueStore = _Class('SGNoCloudNSUbiquitousKeyValueStore')
SGTokenString = _Class('SGTokenString')
SGBigUTF8String = _Class('SGBigUTF8String')