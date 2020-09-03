
'''
Classes from the 'AppleMediaServices' framework.
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
    
    
wumZ2SSA5KbWdu7E = _Class('wumZ2SSA5KbWdu7E')
cBEET4QRedIfcDrp = _Class('cBEET4QRedIfcDrp')
CerKRQOmMu7LBUoc = _Class('CerKRQOmMu7LBUoc')
RvCyrXrrh7eJhtzx = _Class('RvCyrXrrh7eJhtzx')
RJ39VdykGnvJIRpv = _Class('RJ39VdykGnvJIRpv')
n4cyKQis9m01XZsR = _Class('n4cyKQis9m01XZsR')
ktSeAkOyXkmyQNgH = _Class('ktSeAkOyXkmyQNgH')
AMSXDMessage = _Class('AMSXDMessage')
AMSXDDevice = _Class('AMSXDDevice')
AMSVersionComparator = _Class('AMSVersionComparator')
AMSUserNotificationCenter = _Class('AMSUserNotificationCenter')
AMSUserNotificationAction = _Class('AMSUserNotificationAction')
AMSUserNotification = _Class('AMSUserNotification')
AMSUserAgent = _Class('AMSUserAgent')
AMSURLTaskInfo = _Class('AMSURLTaskInfo')
AMSURLSecurityPolicy = _Class('AMSURLSecurityPolicy')
AMSURLResponseDecoder = _Class('AMSURLResponseDecoder')
AMSURLRequestProperties = _Class('AMSURLRequestProperties')
AMSURLParser = _Class('AMSURLParser')
AMSURLAction = _Class('AMSURLAction')
AMSURLDelegateProxy = _Class('AMSURLDelegateProxy')
AMSUNUserNotificationStrategy = _Class('AMSUNUserNotificationStrategy')
AMSUnitTests = _Class('AMSUnitTests')
AMSUniqueExecutionQueue = _Class('AMSUniqueExecutionQueue')
AMSThreadSafeSet = _Class('AMSThreadSafeSet')
AMSThreadSafeObject = _Class('AMSThreadSafeObject')
AMSThreadSafeDictionary = _Class('AMSThreadSafeDictionary')
AMSSyncPasswordSettingsResult = _Class('AMSSyncPasswordSettingsResult')
AMSSubscriptionEntitlementsResult = _Class('AMSSubscriptionEntitlementsResult')
AMSSubscriptionEntitlement = _Class('AMSSubscriptionEntitlement')
AMSSQLiteStatement = _Class('AMSSQLiteStatement')
AMSSQLiteSchemaMigration = _Class('AMSSQLiteSchemaMigration')
AMSSQLiteSchema = _Class('AMSSQLiteSchema')
AMSSQLiteQueryResults = _Class('AMSSQLiteQueryResults')
AMSSQLiteQueryDescriptor = _Class('AMSSQLiteQueryDescriptor')
AMSSQLiteQuery = _Class('AMSSQLiteQuery')
AMSSQLitePreparedStatement = _Class('AMSSQLitePreparedStatement')
AMSSQLitePredicate = _Class('AMSSQLitePredicate')
AMSSQLiteCompoundPredicate = _Class('AMSSQLiteCompoundPredicate')
AMSSQLitePropertyPredicate = _Class('AMSSQLitePropertyPredicate')
AMSSQLiteNullPredicate = _Class('AMSSQLiteNullPredicate')
AMSSQLiteContainsPredicate = _Class('AMSSQLiteContainsPredicate')
AMSSQLiteComparisonPredicate = _Class('AMSSQLiteComparisonPredicate')
AMSSQLiteMemoryEntity = _Class('AMSSQLiteMemoryEntity')
AMSSQLiteEntity = _Class('AMSSQLiteEntity')
AMSSQLiteCursor = _Class('AMSSQLiteCursor')
AMSSQLiteConnectionOptions = _Class('AMSSQLiteConnectionOptions')
AMSSQLiteConnection = _Class('AMSSQLiteConnection')
AMSSnapshotBagBuilder = _Class('AMSSnapshotBagBuilder')
AMSSnapshotBag = _Class('AMSSnapshotBag')
AMSSimulatedCrash = _Class('AMSSimulatedCrash')
AMSSigningSecurityService = _Class('AMSSigningSecurityService')
AMSSignInContext = _Class('AMSSignInContext')
AMSRestrictions = _Class('AMSRestrictions')
AMSRemoteNotification = _Class('AMSRemoteNotification')
AMSRatingSystem = _Class('AMSRatingSystem')
AMSRatingsStoreFront = _Class('AMSRatingsStoreFront')
AMSRatingsProviderResult = _Class('AMSRatingsProviderResult')
AMSPushPayload = _Class('AMSPushPayload')
AMSPushParsableRichNotification = _Class('AMSPushParsableRichNotification')
AMSPushParsableGenericNotification = _Class('AMSPushParsableGenericNotification')
AMSPushParsableFollowUp = _Class('AMSPushParsableFollowUp')
AMSPushParsableEngagementEvent = _Class('AMSPushParsableEngagementEvent')
AMSPushParsableBadging = _Class('AMSPushParsableBadging')
AMSPushNotificationService = _Class('AMSPushNotificationService')
AMSPushHandler = _Class('AMSPushHandler')
AMSPushConfiguration = _Class('AMSPushConfiguration')
AMSPurchaseResult = _Class('AMSPurchaseResult')
AMSURLRequestEncoder = _Class('AMSURLRequestEncoder')
AMSPurchaseRequestEncoder = _Class('AMSPurchaseRequestEncoder')
AMSPurchaseQueueConfiguration = _Class('AMSPurchaseQueueConfiguration')
AMSPurchaseInfo = _Class('AMSPurchaseInfo')
AMSPurchaseBagConsumer = _Class('AMSPurchaseBagConsumer')
AMSPurchase = _Class('AMSPurchase')
AMSPurchaseBatch = _Class('AMSPurchaseBatch')
AMSPromiseResult = _Class('AMSPromiseResult')
AMSPromiseCompletionBlocks = _Class('AMSPromiseCompletionBlocks')
AMSProcessInfo = _Class('AMSProcessInfo')
AMSPaymentSheetResult = _Class('AMSPaymentSheetResult')
AMSPaymentSheetRequest = _Class('AMSPaymentSheetRequest')
AMSPaymentSheetAssetCache = _Class('AMSPaymentSheetAssetCache')
AMSPaymentSheetRatingImage = _Class('AMSPaymentSheetRatingImage')
AMSPaymentSheetPriceSectionItem = _Class('AMSPaymentSheetPriceSectionItem')
AMSPaymentSetupFeatureVerification = _Class('AMSPaymentSetupFeatureVerification')
AMSPair = _Class('AMSPair')
AMSOptional = _Class('AMSOptional')
AMSOpenURL = _Class('AMSOpenURL')
URLTarget = _Class('URLTarget')
AMSObserver = _Class('AMSObserver')
AMSObservable = _Class('AMSObservable')
AMSNotificationSettingsSection = _Class('AMSNotificationSettingsSection')
AMSNotificationSettingsResult = _Class('AMSNotificationSettingsResult')
AMSNotificationSettingsItem = _Class('AMSNotificationSettingsItem')
AMSNetworkQualityInquiry = _Class('AMSNetworkQualityInquiry')
AMSNetworkConstraints = _Class('AMSNetworkConstraints')
AMSMultiUserService = _Class('AMSMultiUserService')
AMSURLSession = _Class('AMSURLSession')
AMSMockURLSession = _Class('AMSMockURLSession')
AMSMockURLResponse = _Class('AMSMockURLResponse')
AMSMockURLRequestComparator = _Class('AMSMockURLRequestComparator')
AMSMockURLOverride = _Class('AMSMockURLOverride')
AMSPurchaseQueue = _Class('AMSPurchaseQueue')
AMSMockPurchaseQueue = _Class('AMSMockPurchaseQueue')
AMSMetricsMemoryDataSource = _Class('AMSMetricsMemoryDataSource')
AMSMetricsLoadURLContext = _Class('AMSMetricsLoadURLContext')
AMSMetricsBatch = _Class('AMSMetricsBatch')
AMSMetricsFigaroEventModifier = _Class('AMSMetricsFigaroEventModifier')
AMSMetricsFigaroBagConfguration = _Class('AMSMetricsFigaroBagConfguration')
AMSMetricsDatabaseSchema = _Class('AMSMetricsDatabaseSchema')
AMSMetricsDatabaseDataSource = _Class('AMSMetricsDatabaseDataSource')
AMSMetricsDatabase = _Class('AMSMetricsDatabase')
AMSMetricsIdentifier = _Class('AMSMetricsIdentifier')
AMSMetricsClientIdentifier = _Class('AMSMetricsClientIdentifier')
AMSMetrics = _Class('AMSMetrics')
AMSMescalSession = _Class('AMSMescalSession')
AMSMescalFairPlay = _Class('AMSMescalFairPlay')
AMSMescal = _Class('AMSMescal')
AMSMemoryPressure = _Class('AMSMemoryPressure')
AMSMediaVideo = _Class('AMSMediaVideo')
AMSMediaURLBuilderUtility = _Class('AMSMediaURLBuilderUtility')
AMSMediaTokenServiceUserDefaultsStore = _Class('AMSMediaTokenServiceUserDefaultsStore')
AMSMediaTokenServiceThrottler = _Class('AMSMediaTokenServiceThrottler')
AMSMediaTokenServiceStore = _Class('AMSMediaTokenServiceStore')
AMSMediaTokenServiceKeychainStore = _Class('AMSMediaTokenServiceKeychainStore')
AMSMediaTokenServiceDeserializer = _Class('AMSMediaTokenServiceDeserializer')
AMSMediaTokenService = _Class('AMSMediaTokenService')
AMSMediaToken = _Class('AMSMediaToken')
AMSMediaTaskURLBuilder = _Class('AMSMediaTaskURLBuilder')
AMSMediaTaskTypeConfig = _Class('AMSMediaTaskTypeConfig')
AMSMediaSharedProperties = _Class('AMSMediaSharedProperties')
AMSMediaResponseDecoder = _Class('AMSMediaResponseDecoder')
AMSMediaRequestEncoder = _Class('AMSMediaRequestEncoder')
AMSMediaArtwork = _Class('AMSMediaArtwork')
AMSMarketingItemTaskURLBuilder = _Class('AMSMarketingItemTaskURLBuilder')
AMSMarketingItemStub = _Class('AMSMarketingItemStub')
AMSMarketingItemParser = _Class('AMSMarketingItemParser')
AMSMarketingItemActionComponent = _Class('AMSMarketingItemActionComponent')
AMSMarketingItemAction = _Class('AMSMarketingItemAction')
AMSMarketingItem = _Class('AMSMarketingItem')
AMSMappedBundleInfo = _Class('AMSMappedBundleInfo')
AMSLRUCache = _Class('AMSLRUCache')
AMSURLResult = _Class('AMSURLResult')
AMSMediaResult = _Class('AMSMediaResult')
AMSLookupResult = _Class('AMSLookupResult')
AMSLookupItemOffer = _Class('AMSLookupItemOffer')
AMSLookupItemArtwork = _Class('AMSLookupItemArtwork')
AMSLookupItemArtworkColor = _Class('AMSLookupItemArtworkColor')
AMSLookupItem = _Class('AMSLookupItem')
AMSLookupDecoder = _Class('AMSLookupDecoder')
AMSLogConfig = _Class('AMSLogConfig')
AMSMutableLogConfig = _Class('AMSMutableLogConfig')
AMSKeychainOptions = _Class('AMSKeychainOptions')
AMSKeychain = _Class('AMSKeychain')
AMSKeybag = _Class('AMSKeybag')
AMSKeepAlive = _Class('AMSKeepAlive')
AMSInlineDelegate = _Class('AMSInlineDelegate')
AMSHTTPArchiveController = _Class('AMSHTTPArchiveController')
AMSHTTPArchive = _Class('AMSHTTPArchive')
AMSMetricsEvent = _Class('AMSMetricsEvent')
AMSUserNotificationMetricsEvent = _Class('AMSUserNotificationMetricsEvent')
AMSPaymentSheetMetricsEvent = _Class('AMSPaymentSheetMetricsEvent')
AMSMetricsLoadURLEvent = _Class('AMSMetricsLoadURLEvent')
AMSFollowUpMetricsEvent = _Class('AMSFollowUpMetricsEvent')
AMSFollowUpItem = _Class('AMSFollowUpItem')
AMSFollowUpAction = _Class('AMSFollowUpAction')
AMSFollowUp = _Class('AMSFollowUp')
AMSFinanceVerifyPurchaseResponse = _Class('AMSFinanceVerifyPurchaseResponse')
AMSFinanceResponse = _Class('AMSFinanceResponse')
AMSFinancePaymentSheetResponse = _Class('AMSFinancePaymentSheetResponse')
AMSFinanceDialogResponse = _Class('AMSFinanceDialogResponse')
AMSFinanceAuthenticateResponse = _Class('AMSFinanceAuthenticateResponse')
AMSFinanceActionResponse = _Class('AMSFinanceActionResponse')
AMSFeatureFlag = _Class('AMSFeatureFlag')
AMSFeatureEnabler = _Class('AMSFeatureEnabler')
AMSFamilyMember = _Class('AMSFamilyMember')
AMSFamilyInfoLookupResult = _Class('AMSFamilyInfoLookupResult')
AMSFamilyAccountPair = _Class('AMSFamilyAccountPair')
AMSFamilyContentDeletionEvent = _Class('AMSFamilyContentDeletionEvent')
AMSEphemeralDefaults = _Class('AMSEphemeralDefaults')
AMSEngagementSyncResult = _Class('AMSEngagementSyncResult')
AMSEngagementSyncRequest = _Class('AMSEngagementSyncRequest')
AMSEngagementEnqueueResult = _Class('AMSEngagementEnqueueResult')
AMSEngagementEnqueueRequest = _Class('AMSEngagementEnqueueRequest')
AMSEngagementDestination = _Class('AMSEngagementDestination')
AMSEngagementConnection = _Class('AMSEngagementConnection')
AMSEngagementClientData = _Class('AMSEngagementClientData')
AMSEngagementAppWhitelistModel = _Class('AMSEngagementAppWhitelistModel')
AMSEngagementAppResponseModel = _Class('AMSEngagementAppResponseModel')
AMSEngagementAppData = _Class('AMSEngagementAppData')
AMSEngagement = _Class('AMSEngagement')
AMSDoubleLinkedListNode = _Class('AMSDoubleLinkedListNode')
AMSLRUCacheItem = _Class('AMSLRUCacheItem')
AMSDoubleLinkedList = _Class('AMSDoubleLinkedList')
AMSDialogTextField = _Class('AMSDialogTextField')
AMSDialogButton = _Class('AMSDialogButton')
AMSDialogAction = _Class('AMSDialogAction')
AMSDialog = _Class('AMSDialog')
AMSDeviceOffersStore = _Class('AMSDeviceOffersStore')
AMSDeviceOfferMigrator = _Class('AMSDeviceOfferMigrator')
AMSDeviceOffer = _Class('AMSDeviceOffer')
AMSDeviceMessengerFilter = _Class('AMSDeviceMessengerFilter')
AMSDeviceMessenger = _Class('AMSDeviceMessenger')
AMSDeviceUpdateHandlerInfo = _Class('AMSDeviceUpdateHandlerInfo')
AMSDevice = _Class('AMSDevice')
AMSDeprecatedBagContract = _Class('AMSDeprecatedBagContract')
AMSDefaults = _Class('AMSDefaults')
AMSDataMigratorOptions = _Class('AMSDataMigratorOptions')
AMSDataMigrator = _Class('AMSDataMigrator')
AMSData = _Class('AMSData')
AMSDaemonConnectionInterface = _Class('AMSDaemonConnectionInterface')
AMSDaemonConnection = _Class('AMSDaemonConnection')
AMSConnectionDelegateProxy = _Class('AMSConnectionDelegateProxy')
AMSContractBagShim = _Class('AMSContractBagShim')
AMSContentRating = _Class('AMSContentRating')
AMSCommerceService = _Class('AMSCommerceService')
AMSCommerceMigrator = _Class('AMSCommerceMigrator')
AMSCircularBuffer = _Class('AMSCircularBuffer')
AMSCardRegistrationResult = _Class('AMSCardRegistrationResult')
AMSCardMetadataRegistrationResult = _Class('AMSCardMetadataRegistrationResult')
AMSCardEnrollment = _Class('AMSCardEnrollment')
AMSCardAutoEnrollment = _Class('AMSCardAutoEnrollment')
AMSBuyParams = _Class('AMSBuyParams')
AMSBiometricsSignatureResult = _Class('AMSBiometricsSignatureResult')
AMSBiometricsSignatureRequest = _Class('AMSBiometricsSignatureRequest')
AMSBiometricsSecurityService = _Class('AMSBiometricsSecurityService')
AMSBiometricsPresentationProxy = _Class('AMSBiometricsPresentationProxy')
AMSBiometricsMigrator = _Class('AMSBiometricsMigrator')
AMSBiometrics = _Class('AMSBiometrics')
AMSBinaryPromise = _Class('AMSBinaryPromise')
AMSBagValue = _Class('AMSBagValue')
AMSFrozenBagValue = _Class('AMSFrozenBagValue')
AMSFailingBagValue = _Class('AMSFailingBagValue')
AMSBridgedBagValue = _Class('AMSBridgedBagValue')
AMSBagURLParser = _Class('AMSBagURLParser')
AMSBagNetworkTaskResult = _Class('AMSBagNetworkTaskResult')
AMSBagNetworkDataSource = _Class('AMSBagNetworkDataSource')
AMSBagKeySetAggregator = _Class('AMSBagKeySetAggregator')
AMSBagKeySet = _Class('AMSBagKeySet')
AMSMutableBagKeySet = _Class('AMSMutableBagKeySet')
AMSBagKeyInfo = _Class('AMSBagKeyInfo')
AMSBagFrozenDataSourceBuilder = _Class('AMSBagFrozenDataSourceBuilder')
AMSBagFrozenDataSource = _Class('AMSBagFrozenDataSource')
AMSBag = _Class('AMSBag')
AMSAutomaticDownloadKindsResult = _Class('AMSAutomaticDownloadKindsResult')
AMSAuthKitUpdateResult = _Class('AMSAuthKitUpdateResult')
AMSAuthenticateOptions = _Class('AMSAuthenticateOptions')
AMSAttestation = _Class('AMSAttestation')
AMSApplePayClassic = _Class('AMSApplePayClassic')
AMSURLProtocolHandler = _Class('AMSURLProtocolHandler')
AMSPurchaseProtocolHandler = _Class('AMSPurchaseProtocolHandler')
AMSMediaProtocolHandler = _Class('AMSMediaProtocolHandler')
AMSAppleCardSilentEnrollmentProtocolHandler = _Class('AMSAppleCardSilentEnrollmentProtocolHandler')
AMSAppleCardSilentEnrollment = _Class('AMSAppleCardSilentEnrollment')
AMSAnisette = _Class('AMSAnisette')
AMSAccountStoreCache = _Class('AMSAccountStoreCache')
AMSAccountsChangedResult = _Class('AMSAccountsChangedResult')
AMSAccountsChangedObservable = _Class('AMSAccountsChangedObservable')
AMSAbsintheSession = _Class('AMSAbsintheSession')
AMSAbsintheSignature = _Class('AMSAbsintheSignature')
AMSAbsinthe = _Class('AMSAbsinthe')
AMSPromise = _Class('AMSPromise')
AMSLazyPromise = _Class('AMSLazyPromise')
AMSTask = _Class('AMSTask')
AMSSyncPasswordSettingsTask = _Class('AMSSyncPasswordSettingsTask')
AMSSubscriptionEntitlementsTask = _Class('AMSSubscriptionEntitlementsTask')
AMSSystemAlertDialogTask = _Class('AMSSystemAlertDialogTask')
AMSQRCodeDialogTask = _Class('AMSQRCodeDialogTask')
AMSSignOutTask = _Class('AMSSignOutTask')
AMSSetDemoAccountTask = _Class('AMSSetDemoAccountTask')
AMSRatingsProviderTask = _Class('AMSRatingsProviderTask')
AMSPurchaseTask = _Class('AMSPurchaseTask')
AMSPaymentSheetTask = _Class('AMSPaymentSheetTask')
AMSNotificationSettingsTask = _Class('AMSNotificationSettingsTask')
AMSMetricsFigaroFlushTask = _Class('AMSMetricsFigaroFlushTask')
AMSMediaTask = _Class('AMSMediaTask')
AMSMarketingItemTask = _Class('AMSMarketingItemTask')
AMSHandleDialogResultTask = _Class('AMSHandleDialogResultTask')
AMSGenerateFraudScoreTask = _Class('AMSGenerateFraudScoreTask')
AMSFamilyInfoLookupTask = _Class('AMSFamilyInfoLookupTask')
AMSDeviceOfferRegistrationTask = _Class('AMSDeviceOfferRegistrationTask')
AMSCommandLineDialogTask = _Class('AMSCommandLineDialogTask')
AMSClientCertificateTask = _Class('AMSClientCertificateTask')
AMSCardRegistrationTask = _Class('AMSCardRegistrationTask')
AMSCardEnrollmentVerificationTask = _Class('AMSCardEnrollmentVerificationTask')
AMSCardEnrollmentPaymentSessionTask = _Class('AMSCardEnrollmentPaymentSessionTask')
AMSCardEnrollmentEligibilityTask = _Class('AMSCardEnrollmentEligibilityTask')
AMSCardAuthorizationTask = _Class('AMSCardAuthorizationTask')
AMSBiometricsTokenUpdateTask = _Class('AMSBiometricsTokenUpdateTask')
AMSBiometricsSignatureTask = _Class('AMSBiometricsSignatureTask')
AMSBiometricsDisableTask = _Class('AMSBiometricsDisableTask')
AMSBagNetworkTask = _Class('AMSBagNetworkTask')
AMSAutomaticDownloadKindsSetTask = _Class('AMSAutomaticDownloadKindsSetTask')
AMSAutomaticDownloadKindsFetchTask = _Class('AMSAutomaticDownloadKindsFetchTask')
AMSAuthKitUpdateTask = _Class('AMSAuthKitUpdateTask')
AMSAuthenticateTask = _Class('AMSAuthenticateTask')
AMSAnisetteSyncTask = _Class('AMSAnisetteSyncTask')
AMSAnisetteProvisionTask = _Class('AMSAnisetteProvisionTask')
AMSAcknowledgePrivacyTask = _Class('AMSAcknowledgePrivacyTask')
AMSLookup = _Class('AMSLookup')
AMSXDProtoMessage = _Class('AMSXDProtoMessage')
AMSURLRequest = _Class('AMSURLRequest')
AMSMockNetworkProxy = _Class('AMSMockNetworkProxy')
AMSBKSProcessAssertion = _Class('AMSBKSProcessAssertion')
AMSEngagementResult = _Class('AMSEngagementResult')
AMSEngagementRequest = _Class('AMSEngagementRequest')
AMSDialogResult = _Class('AMSDialogResult')
AMSDialogRequest = _Class('AMSDialogRequest')
AMSAuthenticateResult = _Class('AMSAuthenticateResult')
AMSAuthenticateRequest = _Class('AMSAuthenticateRequest')
AMSOperation = _Class('AMSOperation')