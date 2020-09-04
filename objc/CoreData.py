'''
Classes from the 'CoreData' framework.
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

    
PFUbiquityContainerMonitor = _Class('PFUbiquityContainerMonitor')
PFUbiquityMigrationAssistant = _Class('PFUbiquityMigrationAssistant')
PFUbiquityRecordsImporterSchedulingContext = _Class('PFUbiquityRecordsImporterSchedulingContext')
PFUbiquitySwitchboardCacheWrapper = _Class('PFUbiquitySwitchboardCacheWrapper')
PFUbiquityGlobalObjectIDCache = _Class('PFUbiquityGlobalObjectIDCache')
PFUbiquityTransactionEntryLight = _Class('PFUbiquityTransactionEntryLight')
PFUbiquityTransactionHistoryCache = _Class('PFUbiquityTransactionHistoryCache')
NSCloudKitMirroringDelegateOptions = _Class('NSCloudKitMirroringDelegateOptions')
_PFChangeInfo = _Class('_PFChangeInfo')
PFUbiquityTransactionLogCache = _Class('PFUbiquityTransactionLogCache')
PFUbiquityMetadataFactoryFilePresenter = _Class('PFUbiquityMetadataFactoryFilePresenter')
NSCloudKitMirroringDelegatePreJazzkonMetadata = _Class('NSCloudKitMirroringDelegatePreJazzkonMetadata')
PFUbiquityPeerRangeReservationContext = _Class('PFUbiquityPeerRangeReservationContext')
PFCloudKitThrottledNotificationObserver = _Class('PFCloudKitThrottledNotificationObserver')
PFUbiquityMetadataFactoryEntry = _Class('PFUbiquityMetadataFactoryEntry')
PFUbiquityMetadataFactory = _Class('PFUbiquityMetadataFactory')
PFUbiquitySQLCorePeerRange = _Class('PFUbiquitySQLCorePeerRange')
PFUbiquityPeerRangeCache = _Class('PFUbiquityPeerRangeCache')
PFUbiquityContainerIdentifier = _Class('PFUbiquityContainerIdentifier')
PFUbiquitySetupAssistant = _Class('PFUbiquitySetupAssistant')
PFUbiquityStoreMetadataMedic = _Class('PFUbiquityStoreMetadataMedic')
PFUbiquityKnowledgeVector = _Class('PFUbiquityKnowledgeVector')
PFUbiquityMigrationManager = _Class('PFUbiquityMigrationManager')
PFCloudKitLogging = _Class('PFCloudKitLogging')
PFUbiquityToManyConflictDiff = _Class('PFUbiquityToManyConflictDiff')
PFCloudKitStoreMonitor = _Class('PFCloudKitStoreMonitor')
PFUbiquityPeerSnapshotCollection = _Class('PFUbiquityPeerSnapshotCollection')
PFUbiquityPeerSnapshot = _Class('PFUbiquityPeerSnapshot')
NSSQLiteIndexTrackingModel = _Class('NSSQLiteIndexTrackingModel')
NSSQLiteIndexStatistics = _Class('NSSQLiteIndexStatistics')
PFCloudKitMetadataModelMigrator = _Class('PFCloudKitMetadataModelMigrator')
PFZipLocalFileHeader = _Class('PFZipLocalFileHeader')
PFZipEndOfCentralDirectoryRecord = _Class('PFZipEndOfCentralDirectoryRecord')
PFZipCentralDirectoryFileHeader = _Class('PFZipCentralDirectoryFileHeader')
_PFZipFileArchive = _Class('_PFZipFileArchive')
_PFUbiquityMigrationContext = _Class('_PFUbiquityMigrationContext')
PFUbiquityTransactionLogMigrator = _Class('PFUbiquityTransactionLogMigrator')
PFHistoryAnalyzerContext = _Class('PFHistoryAnalyzerContext')
PFCloudKitHistoryAnalyzerContext = _Class('PFCloudKitHistoryAnalyzerContext')
PFUbiquityLocation = _Class('PFUbiquityLocation')
PFCloudKitSchemaGenerator = _Class('PFCloudKitSchemaGenerator')
PFUbiquityImportContext = _Class('PFUbiquityImportContext')
_PFFreeMapEntry = _Class('_PFFreeMapEntry')
NSXPCSaveRequestContext = _Class('NSXPCSaveRequestContext')
PFUbiquityTransactionLog = _Class('PFUbiquityTransactionLog')
NSFetchIndexElementDescription = _Class('NSFetchIndexElementDescription')
PFCloudKitStoreComparer = _Class('PFCloudKitStoreComparer')
NSPersistentCloudKitContainerOptions = _Class('NSPersistentCloudKitContainerOptions')
PFUbiquityStoreSaveSnapshot = _Class('PFUbiquityStoreSaveSnapshot')
PFCloudKitExportContext = _Class('PFCloudKitExportContext')
NSSQLSavePlan = _Class('NSSQLSavePlan')
PFUbiquitySaveSnapshot = _Class('PFUbiquitySaveSnapshot')
NSSQLAttributeExtensionFactory = _Class('NSSQLAttributeExtensionFactory')
PFUbiquityGlobalObjectID = _Class('PFUbiquityGlobalObjectID')
PFUbiquityStoreExportContext = _Class('PFUbiquityStoreExportContext')
PFUbiquityExportContext = _Class('PFUbiquityExportContext')
PFUbiquityBaselineMetadata = _Class('PFUbiquityBaselineMetadata')
NSSQLCoreDispatchManager = _Class('NSSQLCoreDispatchManager')
_PFPersistentHistoryFetchModel = _Class('_PFPersistentHistoryFetchModel')
_PFPersistentHistoryModel = _Class('_PFPersistentHistoryModel')
PFUbiquitySafeSaveFile = _Class('PFUbiquitySafeSaveFile')
PFUbiquityPeerReceipt = _Class('PFUbiquityPeerReceipt')
PFUbiquityBaseline = _Class('PFUbiquityBaseline')
NSSQLCorrelationTableUpdateTracker = _Class('NSSQLCorrelationTableUpdateTracker')
PFUbiquitySwitchboardEntryMetadata = _Class('PFUbiquitySwitchboardEntryMetadata')
PFUbiquitySwitchboardEntry = _Class('PFUbiquitySwitchboardEntry')
NSGenerationalRowCache = _Class('NSGenerationalRowCache')
PFUbiquitySwitchboard = _Class('PFUbiquitySwitchboard')
PFUbiquityRecordImportConflict = _Class('PFUbiquityRecordImportConflict')
PFUbiquityFilePresenter = _Class('PFUbiquityFilePresenter')
PFUbiquityEventLogging = _Class('PFUbiquityEventLogging')
PFUBLogEventID = _Class('PFUBLogEventID')
PFUbiquityLogging = _Class('PFUbiquityLogging')
NSCloudKitMirroringDelegateWorkBlockContext = _Class('NSCloudKitMirroringDelegateWorkBlockContext')
NSCloudKitMirroringDelegate = _Class('NSCloudKitMirroringDelegate')
NSSQLEntity_DerivedAttributesExtension = _Class('NSSQLEntity_DerivedAttributesExtension')
PFCloudKitExporterOptions = _Class('PFCloudKitExporterOptions')
PFCloudKitMetadataCache = _Class('PFCloudKitMetadataCache')
NSSQLKeypathTriggerAttributeExtension = _Class('NSSQLKeypathTriggerAttributeExtension')
NSPersistentStoreDescription = _Class('NSPersistentStoreDescription')
NSXPCStoreConnectionManager = _Class('NSXPCStoreConnectionManager')
_PFUbiquityStack = _Class('_PFUbiquityStack')
NSSQLLocationAttributeRTreeExtension = _Class('NSSQLLocationAttributeRTreeExtension')
_PFUbiquityRecordsImporter = _Class('_PFUbiquityRecordsImporter')
_PFUbiquityRecordsExporter = _Class('_PFUbiquityRecordsExporter')
PFCloudKitStoreMonitorProvider = _Class('PFCloudKitStoreMonitorProvider')
_NSFaultingMutableOrderedSetMutationMethods = _Class('_NSFaultingMutableOrderedSetMutationMethods')
NSIncrementalStoreNode = _Class('NSIncrementalStoreNode')
PFCloudKitImportDatabaseContext = _Class('PFCloudKitImportDatabaseContext')
_CDSnapshot = _Class('_CDSnapshot')
PFCloudKitOptionsValidator = _Class('PFCloudKitOptionsValidator')
_NSPropertyDescriptionProxy = _Class('_NSPropertyDescriptionProxy')
_NSPropertyDescriptionProxy2 = _Class('_NSPropertyDescriptionProxy2')
PFCloudKitSerializer = _Class('PFCloudKitSerializer')
_NSSQLiteStoreMigrator = _Class('_NSSQLiteStoreMigrator')
PFCloudKitImporterOptions = _Class('PFCloudKitImporterOptions')
PFMirroredRelationship = _Class('PFMirroredRelationship')
PFMirroredOneToManyRelationship = _Class('PFMirroredOneToManyRelationship')
PFMirroredManyToManyRelationship = _Class('PFMirroredManyToManyRelationship')
PFMirroredManyToManyRelationshipV2 = _Class('PFMirroredManyToManyRelationshipV2')
_NSSQLTableMigrationDescription = _Class('_NSSQLTableMigrationDescription')
NSSQLiteIntarrayTable = _Class('NSSQLiteIntarrayTable')
_NSSQLEntityMigrationDescription = _Class('_NSSQLEntityMigrationDescription')
PFCloudKitBaseMetric = _Class('PFCloudKitBaseMetric')
PFCloudKitSizeMetric = _Class('PFCloudKitSizeMetric')
PFCloudKitFetchedAssetBytesMetric = _Class('PFCloudKitFetchedAssetBytesMetric')
PFCloudKitFetchedRecordBytesMetric = _Class('PFCloudKitFetchedRecordBytesMetric')
PFCloudKitImportedRecordBytesMetric = _Class('PFCloudKitImportedRecordBytesMetric')
PFCloudKitExportedRecordBytesMetric = _Class('PFCloudKitExportedRecordBytesMetric')
PFCloudKitUnhandledPartialErrorMetric = _Class('PFCloudKitUnhandledPartialErrorMetric')
PFCloudKitFatalErrorMetric = _Class('PFCloudKitFatalErrorMetric')
PFCloudKitMetricsClient = _Class('PFCloudKitMetricsClient')
_NSDefaultSectionInfo = _Class('_NSDefaultSectionInfo')
NSManagedImmutableObject = _Class('NSManagedImmutableObject')
NSValidationErrorLocalizationPolicy = _Class('NSValidationErrorLocalizationPolicy')
NSMergedPolicyLocalizationPolicy = _Class('NSMergedPolicyLocalizationPolicy')
_NS128bitWrapper = _Class('_NS128bitWrapper')
NSStoreMigrationPolicy = _Class('NSStoreMigrationPolicy')
NSStoreMappingGenerator = _Class('NSStoreMappingGenerator')
_PFModelMap = _Class('_PFModelMap')
NSSQLSubqueryExpressionIntermediatePredicateVisitor = _Class('NSSQLSubqueryExpressionIntermediatePredicateVisitor')
NSSQLStoreMappingGenerator = _Class('NSSQLStoreMappingGenerator')
_NSCoreDataInternal = _Class('_NSCoreDataInternal')
PFCloudKitExporter = _Class('PFCloudKitExporter')
NSSQLiteStatement = _Class('NSSQLiteStatement')
NSConstraintCache = _Class('NSConstraintCache')
NSConstraintCacheKey = _Class('NSConstraintCacheKey')
NSSQLPredicateAnalyser = _Class('NSSQLPredicateAnalyser')
_PFFetchPlanHeader = _Class('_PFFetchPlanHeader')
PFCloudKitMetadataPurger = _Class('PFCloudKitMetadataPurger')
NSConstraintValidator = _Class('NSConstraintValidator')
NSCloudKitMirroringRequestManager = _Class('NSCloudKitMirroringRequestManager')
PFCloudKitContainerProvider = _Class('PFCloudKitContainerProvider')
NSSQLiteConnection = _Class('NSSQLiteConnection')
_PFSQLiteSnapshotWrapper = _Class('_PFSQLiteSnapshotWrapper')
NSSQLiteAdapter = _Class('NSSQLiteAdapter')
NSPersistentHistoryToken = _Class('NSPersistentHistoryToken')
_NSPersistentHistoryToken = _Class('_NSPersistentHistoryToken')
CDDCloudKitServerConfiguration = _Class('CDDCloudKitServerConfiguration')
PFCloudKitMetadataMigrationContext = _Class('PFCloudKitMetadataMigrationContext')
NSSQLGenerator = _Class('NSSQLGenerator')
NSCloudKitMirroringRequestOptions = _Class('NSCloudKitMirroringRequestOptions')
CDDCloudKitResponse = _Class('CDDCloudKitResponse')
CDDCloudKitClient = _Class('CDDCloudKitClient')
PFCloudKitSetupAssistant = _Class('PFCloudKitSetupAssistant')
PFCloudKitErrorLogEntry = _Class('PFCloudKitErrorLogEntry')
PFCloudKitErrorLog = _Class('PFCloudKitErrorLog')
PFCloudKitImporter = _Class('PFCloudKitImporter')
_NSSQLCoreConnectionObsever = _Class('_NSSQLCoreConnectionObsever')
PFHistoryAnalyzer = _Class('PFHistoryAnalyzer')
PFCloudKitHistoryAnalyzer = _Class('PFCloudKitHistoryAnalyzer')
CDDCloudKitMetadataModel = _Class('CDDCloudKitMetadataModel')
PFUbiquityLocationStatus = _Class('PFUbiquityLocationStatus')
NSSQLBindVariable = _Class('NSSQLBindVariable')
NSSQLProperty = _Class('NSSQLProperty')
NSSQLRelationship = _Class('NSSQLRelationship')
NSSQLToOne = _Class('NSSQLToOne')
NSSQLToMany = _Class('NSSQLToMany')
NSSQLManyToMany = _Class('NSSQLManyToMany')
NSSQLColumn = _Class('NSSQLColumn')
NSSQLForeignOrderKey = _Class('NSSQLForeignOrderKey')
NSSQLPrimaryKey = _Class('NSSQLPrimaryKey')
NSSQLOptLockKey = _Class('NSSQLOptLockKey')
NSSQLForeignKey = _Class('NSSQLForeignKey')
NSSQLForeignEntityKey = _Class('NSSQLForeignEntityKey')
NSSQLEntityKey = _Class('NSSQLEntityKey')
NSSQLAttribute = _Class('NSSQLAttribute')
CDDCloudKitServer = _Class('CDDCloudKitServer')
NSSQLAliasGenerator = _Class('NSSQLAliasGenerator')
NSPropertyTransform = _Class('NSPropertyTransform')
NSPropertyMapping = _Class('NSPropertyMapping')
NSFetchedResultsController = _Class('NSFetchedResultsController')
_PFIndexCacheOffset = _Class('_PFIndexCacheOffset')
_PFRequestExecutor = _Class('_PFRequestExecutor')
NSSQLAttributeTrigger = _Class('NSSQLAttributeTrigger')
PFHistoryAnalyzerDefaultObjectState = _Class('PFHistoryAnalyzerDefaultObjectState')
NSPersistentStoreCoordinator = _Class('NSPersistentStoreCoordinator')
NSPersistentStoreCache = _Class('NSPersistentStoreCache')
NSSQLRowCache = _Class('NSSQLRowCache')
NSSQLiteStatementCache = _Class('NSSQLiteStatementCache')
PFUbiquityBaselineHeuristics = _Class('PFUbiquityBaselineHeuristics')
NSSQLConnectionManager = _Class('NSSQLConnectionManager')
NSSQLUbiquitizedStoreConnectionManager = _Class('NSSQLUbiquitizedStoreConnectionManager')
NSSQLDefaultConnectionManager = _Class('NSSQLDefaultConnectionManager')
NSMigrationManager = _Class('NSMigrationManager')
NSSQLiteInPlaceMigrationManager = _Class('NSSQLiteInPlaceMigrationManager')
NSMigrationContext = _Class('NSMigrationContext')
_PFModelUtilities = _Class('_PFModelUtilities')
NSConstraintConflict = _Class('NSConstraintConflict')
NSMergeConflict = _Class('NSMergeConflict')
PFUbiquityMergeConflict = _Class('PFUbiquityMergeConflict')
NSSQLitePrefetchRequestCache = _Class('NSSQLitePrefetchRequestCache')
NSMappingModel = _Class('NSMappingModel')
NSFetchIndexDescription = _Class('NSFetchIndexDescription')
NSPersistentCloudKitContainerEvent = _Class('NSPersistentCloudKitContainerEvent')
PFStoreComparisonCache = _Class('PFStoreComparisonCache')
PFCloudKitStoreComparisonCache = _Class('PFCloudKitStoreComparisonCache')
NSManagedObjectModelBundle = _Class('NSManagedObjectModelBundle')
NSSQLIntermediate = _Class('NSSQLIntermediate')
NSSQLIndexIntermediate = _Class('NSSQLIndexIntermediate')
NSSQLHavingIntermediate = _Class('NSSQLHavingIntermediate')
NSSQLGroupByIntermediate = _Class('NSSQLGroupByIntermediate')
NSSQLSelectIntermediate = _Class('NSSQLSelectIntermediate')
NSSQLReadOnlySelectIntermediate = _Class('NSSQLReadOnlySelectIntermediate')
NSSQLOrderIntermediate = _Class('NSSQLOrderIntermediate')
NSSQLOffsetIntermediate = _Class('NSSQLOffsetIntermediate')
NSSQLLimitIntermediate = _Class('NSSQLLimitIntermediate')
NSSQLJoinIntermediate = _Class('NSSQLJoinIntermediate')
NSSQLStatementIntermediate = _Class('NSSQLStatementIntermediate')
NSSQLFetchDictionaryCountIntermediate = _Class('NSSQLFetchDictionaryCountIntermediate')
NSSQLUpdateIntermediate = _Class('NSSQLUpdateIntermediate')
NSSQLFetchIntermediate = _Class('NSSQLFetchIntermediate')
NSSQLFetchCountIntermediate = _Class('NSSQLFetchCountIntermediate')
NSSQLExpressionIntermediate = _Class('NSSQLExpressionIntermediate')
NSSQLVariableExpressionIntermediate = _Class('NSSQLVariableExpressionIntermediate')
NSSQLTernaryExpressionIntermediate = _Class('NSSQLTernaryExpressionIntermediate')
NSSQLSubqueryExpressionIntermediate = _Class('NSSQLSubqueryExpressionIntermediate')
NSSQLKeypathExpressionIntermediate = _Class('NSSQLKeypathExpressionIntermediate')
NSSQLFunctionExpressionIntermediate = _Class('NSSQLFunctionExpressionIntermediate')
NSSQLConstantValueIntermediate = _Class('NSSQLConstantValueIntermediate')
NSSQLForeignKeyIntermediate = _Class('NSSQLForeignKeyIntermediate')
NSSQLWhereIntermediate = _Class('NSSQLWhereIntermediate')
NSSQLSimpleWhereIntermediate = _Class('NSSQLSimpleWhereIntermediate')
NSSQLCompoundWhereIntermediate = _Class('NSSQLCompoundWhereIntermediate')
NSSQLRTreeIndexQueryIntermediate = _Class('NSSQLRTreeIndexQueryIntermediate')
NSSQLBoundedByIntermediate = _Class('NSSQLBoundedByIntermediate')
NSSQLUpdateColumnsIntermediate = _Class('NSSQLUpdateColumnsIntermediate')
NSManagedObjectModel = _Class('NSManagedObjectModel')
NSQueryGenerationToken = _Class('NSQueryGenerationToken')
_NSQueryGenerationToken = _Class('_NSQueryGenerationToken')
_NSXPCQueryGenerationToken = _Class('_NSXPCQueryGenerationToken')
_PFTempNestedSnapshot = _Class('_PFTempNestedSnapshot')
_PFManagedObjectReferenceQueue = _Class('_PFManagedObjectReferenceQueue')
_NSManagedObject_st = _Class('_NSManagedObject_st')
PFCloudKitOperationBatch = _Class('PFCloudKitOperationBatch')
_NSOrderedSetDiff = _Class('_NSOrderedSetDiff')
_NSOrderedSetDiffChange = _Class('_NSOrderedSetDiffChange')
_NSOrderedSetDiffMove = _Class('_NSOrderedSetDiffMove')
_NSOrderedSetDiffInsert = _Class('_NSOrderedSetDiffInsert')
_NSOrderedSetDiffDelete = _Class('_NSOrderedSetDiffDelete')
NSKnownKeysMappingStrategy = _Class('NSKnownKeysMappingStrategy')
NSKnownKeysMappingStrategy1 = _Class('NSKnownKeysMappingStrategy1')
NSKnownKeysMappingStrategy2 = _Class('NSKnownKeysMappingStrategy2')
NSJoin = _Class('NSJoin')
NSXPCStoreNotificationObserver = _Class('NSXPCStoreNotificationObserver')
CDDCloudKitMessage = _Class('CDDCloudKitMessage')
CDDCloudKitRegistrationMessage = _Class('CDDCloudKitRegistrationMessage')
CDDCloudKitScheduleActivityMessage = _Class('CDDCloudKitScheduleActivityMessage')
NSXPCStoreMessageContext = _Class('NSXPCStoreMessageContext')
NSSQLIndex = _Class('NSSQLIndex')
NSSQLBinaryIndex = _Class('NSSQLBinaryIndex')
NSSQLRTreeIndex = _Class('NSSQLRTreeIndex')
NSPersistentHistoryChange = _Class('NSPersistentHistoryChange')
_NSPersistentHistoryChange = _Class('_NSPersistentHistoryChange')
NSFaultHandler = _Class('NSFaultHandler')
NSEntityMapping = _Class('NSEntityMapping')
NSEntityDescription = _Class('NSEntityDescription')
NSPersistentStoreMap = _Class('NSPersistentStoreMap')
NSDictionaryStoreMap = _Class('NSDictionaryStoreMap')
NSStoreMapNode = _Class('NSStoreMapNode')
NSDictionaryMapNode = _Class('NSDictionaryMapNode')
NSBinaryObjectStoreFile = _Class('NSBinaryObjectStoreFile')
_NSCoreDataTaggedObjectIDFactory = _Class('_NSCoreDataTaggedObjectIDFactory')
NSManagedObjectID = _Class('NSManagedObjectID')
NSTemporaryObjectID = _Class('NSTemporaryObjectID')
_NSTemporaryObjectID2 = _Class('_NSTemporaryObjectID2')
_NSCoreManagedObjectID = _Class('_NSCoreManagedObjectID')
_NSScalarObjectID = _Class('_NSScalarObjectID')
_NSCoreDataTaggedObjectID = _Class('_NSCoreDataTaggedObjectID')
NSScalarObjectID48 = _Class('NSScalarObjectID48')
NSScalarObjectID64 = _Class('NSScalarObjectID64')
NSBasicObjectID = _Class('NSBasicObjectID')
NSStoreMapping = _Class('NSStoreMapping')
NSSQLModel = _Class('NSSQLModel')
NSSQLEntity = _Class('NSSQLEntity')
NSEntityStoreMapping = _Class('NSEntityStoreMapping')
NSPropertyStoreMapping = _Class('NSPropertyStoreMapping')
NSRelationshipStoreMapping = _Class('NSRelationshipStoreMapping')
NSAttributeStoreMapping = _Class('NSAttributeStoreMapping')
NSPropertyDescription = _Class('NSPropertyDescription')
NSRelationshipDescription = _Class('NSRelationshipDescription')
NSFetchedPropertyDescription = _Class('NSFetchedPropertyDescription')
NSExpressionDescription = _Class('NSExpressionDescription')
NSAttributeDescription = _Class('NSAttributeDescription')
NSDerivedAttributeDescription = _Class('NSDerivedAttributeDescription')
NSAtomicStoreCacheNode = _Class('NSAtomicStoreCacheNode')
_PFAutoreleasePoolThunk = _Class('_PFAutoreleasePoolThunk')
_PFGarbageManager = _Class('_PFGarbageManager')
_PFMutex = _Class('_PFMutex')
_PFLock = _Class('_PFLock')
_PFWeakReference = _Class('_PFWeakReference')
_PFRoutines = _Class('_PFRoutines')
NSPrivateCoreDataClassForFindingBundle = _Class('NSPrivateCoreDataClassForFindingBundle')
_PFTask = _Class('_PFTask')
_PFContextMapTable = _Class('_PFContextMapTable')
_NSSQLGenerator = _Class('_NSSQLGenerator')
_NSPersistenceUtilities = _Class('_NSPersistenceUtilities')
PFCloudKitImporterWorkItem = _Class('PFCloudKitImporterWorkItem')
PFCloudKitImporterZoneDeletedWorkItem = _Class('PFCloudKitImporterZoneDeletedWorkItem')
PFCloudKitImporterZonePurgedWorkItem = _Class('PFCloudKitImporterZonePurgedWorkItem')
PFCloudKitImportRecordsWorkItem = _Class('PFCloudKitImportRecordsWorkItem')
PFCloudKitImporterZoneChangedWorkItem = _Class('PFCloudKitImporterZoneChangedWorkItem')
PFCloudKitImporterFetchRecordsWorkItem = _Class('PFCloudKitImporterFetchRecordsWorkItem')
PFCloudKitCKQueryBackedImportWorkItem = _Class('PFCloudKitCKQueryBackedImportWorkItem')
_PFSpawn = _Class('_PFSpawn')
_NSXPCStorePredicateRemapper = _Class('_NSXPCStorePredicateRemapper')
_NSPersistentHistoryPredicateRemapper = _Class('_NSPersistentHistoryPredicateRemapper')
_NSChildContextPredicateRemapper = _Class('_NSChildContextPredicateRemapper')
_NSMemoryStorePredicateRemapper = _Class('_NSMemoryStorePredicateRemapper')
NSCachedFetchRequestInfo = _Class('NSCachedFetchRequestInfo')
NSCachedFetchRequestThunk = _Class('NSCachedFetchRequestThunk')
NSSQLBindIntarray = _Class('NSSQLBindIntarray')
_NSMappingModelBuilder = _Class('_NSMappingModelBuilder')
_NSFaultingMutableSetMutationMethods = _Class('_NSFaultingMutableSetMutationMethods')
_PFCKInsertedMetadataLink = _Class('_PFCKInsertedMetadataLink')
PFCloudKitImportZoneContext = _Class('PFCloudKitImportZoneContext')
NSSQLDerivedAttributeSQLGenerator = _Class('NSSQLDerivedAttributeSQLGenerator')
PFCloudKitMetadataModel = _Class('PFCloudKitMetadataModel')
NSXPCStoreConnection = _Class('NSXPCStoreConnection')
PFHistoryAnalyzerOptions = _Class('PFHistoryAnalyzerOptions')
PFCloudKitHistoryAnalyzerOptions = _Class('PFCloudKitHistoryAnalyzerOptions')
NSCoreDataXPCMessage = _Class('NSCoreDataXPCMessage')
NSPersistentCacheRow = _Class('NSPersistentCacheRow')
NSSQLRow = _Class('NSSQLRow')
NSXPCRow = _Class('NSXPCRow')
NSXPCStoreServerPerConnectionCache = _Class('NSXPCStoreServerPerConnectionCache')
NSXPCStoreServerConnectionContext = _Class('NSXPCStoreServerConnectionContext')
NSXPCStoreConnectionInfo = _Class('NSXPCStoreConnectionInfo')
NSXPCStoreServer = _Class('NSXPCStoreServer')
PFCloudKitModelValidator = _Class('PFCloudKitModelValidator')
NSPersistentStoreResult = _Class('NSPersistentStoreResult')
NSBatchDeleteResult = _Class('NSBatchDeleteResult')
NSSQLiteIndexStatisticsResult = _Class('NSSQLiteIndexStatisticsResult')
NSBatchUpdateResult = _Class('NSBatchUpdateResult')
NSBatchInsertResult = _Class('NSBatchInsertResult')
NSCloudKitMirroringResult = _Class('NSCloudKitMirroringResult')
NSCloudKitMirroringDelegateSetupResult = _Class('NSCloudKitMirroringDelegateSetupResult')
NSCloudKitMirroringExportProgressResult = _Class('NSCloudKitMirroringExportProgressResult')
NSCloudKitMirroringFetchRecordsResult = _Class('NSCloudKitMirroringFetchRecordsResult')
NSCloudKitMirroringDelegateSerializationRequestResult = _Class('NSCloudKitMirroringDelegateSerializationRequestResult')
NSPersistentCloudKitContainerEventResult = _Class('NSPersistentCloudKitContainerEventResult')
NSPersistentStoreAsynchronousResult = _Class('NSPersistentStoreAsynchronousResult')
NSAsynchronousFetchResult = _Class('NSAsynchronousFetchResult')
NSUnknownRequestTypeResult = _Class('NSUnknownRequestTypeResult')
NSPersistentHistoryResult = _Class('NSPersistentHistoryResult')
NSSQLStoreRequestContext = _Class('NSSQLStoreRequestContext')
NSSQLSaveChangesRequestContext = _Class('NSSQLSaveChangesRequestContext')
NSSQLRelationshipFaultRequestContext = _Class('NSSQLRelationshipFaultRequestContext')
NSSQLGenerateObjectIDRequestContext = _Class('NSSQLGenerateObjectIDRequestContext')
NSSQLFetchRequestContext = _Class('NSSQLFetchRequestContext')
NSSQLObjectIDSetFetchRequestContext = _Class('NSSQLObjectIDSetFetchRequestContext')
NSSQLXPCFetchRequestContext = _Class('NSSQLXPCFetchRequestContext')
NSSQLCountRequestContext = _Class('NSSQLCountRequestContext')
NSSQLPersistentHistoryChangeRequestContext = _Class('NSSQLPersistentHistoryChangeRequestContext')
NSSQLObjectFaultRequestContext = _Class('NSSQLObjectFaultRequestContext')
NSSQLBatchUpdateRequestContext = _Class('NSSQLBatchUpdateRequestContext')
NSSQLBatchInsertRequestContext = _Class('NSSQLBatchInsertRequestContext')
NSSQLBatchDeleteRequestContext = _Class('NSSQLBatchDeleteRequestContext')
NSSQLBlockRequestContext = _Class('NSSQLBlockRequestContext')
NSXPCStoreManagedObjectArchivingToken = _Class('NSXPCStoreManagedObjectArchivingToken')
NSPersistentHistoryTransaction = _Class('NSPersistentHistoryTransaction')
_NSPersistentHistoryTransaction = _Class('_NSPersistentHistoryTransaction')
_NSXPCStoreUtilities = _Class('_NSXPCStoreUtilities')
NSPersistentHistoryChangeRequestToken = _Class('NSPersistentHistoryChangeRequestToken')
NSBatchDeleteRequestEncodingToken = _Class('NSBatchDeleteRequestEncodingToken')
NSBatchUpdateRequestEncodingToken = _Class('NSBatchUpdateRequestEncodingToken')
NSBatchInsertRequestEncodingToken = _Class('NSBatchInsertRequestEncodingToken')
_NSXPCStoreObjectIDArrayConstantValueExpression = _Class('_NSXPCStoreObjectIDArrayConstantValueExpression')
_NSNoChangeToken = _Class('_NSNoChangeToken')
NSPersistentStoreRequest = _Class('NSPersistentStoreRequest')
NSBatchDeleteRequest = _Class('NSBatchDeleteRequest')
NSAsynchronousFetchRequest = _Class('NSAsynchronousFetchRequest')
NSPersistentCloudKitContainerEventRequest = _Class('NSPersistentCloudKitContainerEventRequest')
NSSQLiteIndexStatisticsRequest = _Class('NSSQLiteIndexStatisticsRequest')
NSCloudKitMirroringRequest = _Class('NSCloudKitMirroringRequest')
NSCloudKitMirroringDelegateSetupRequest = _Class('NSCloudKitMirroringDelegateSetupRequest')
NSCloudKitMirroringExportProgressRequest = _Class('NSCloudKitMirroringExportProgressRequest')
NSCloudKitMirroringDelegateSerializationRequest = _Class('NSCloudKitMirroringDelegateSerializationRequest')
NSCloudKitMirroringInitializeSchemaRequest = _Class('NSCloudKitMirroringInitializeSchemaRequest')
NSCloudKitMirroringResetMetadataRequest = _Class('NSCloudKitMirroringResetMetadataRequest')
NSCloudKitMirroringResetZoneRequest = _Class('NSCloudKitMirroringResetZoneRequest')
NSCloudKitMirroringExportRequest = _Class('NSCloudKitMirroringExportRequest')
NSCloudKitMirroringDelegateResetRequest = _Class('NSCloudKitMirroringDelegateResetRequest')
NSCloudKitMirroringImportRequest = _Class('NSCloudKitMirroringImportRequest')
NSCloudKitMirroringFetchRecordsRequest = _Class('NSCloudKitMirroringFetchRecordsRequest')
NSSaveChangesRequest = _Class('NSSaveChangesRequest')
NSBatchUpdateRequest = _Class('NSBatchUpdateRequest')
NSBatchInsertRequest = _Class('NSBatchInsertRequest')
NSPersistentHistoryChangeRequest = _Class('NSPersistentHistoryChangeRequest')
NSFetchRequest = _Class('NSFetchRequest')
NSCachingFetchRequest = _Class('NSCachingFetchRequest')
NSPersistentContainer = _Class('NSPersistentContainer')
NSPersistentCloudKitContainer = _Class('NSPersistentCloudKitContainer')
NSXPCStoreServerRequestHandlingPolicy = _Class('NSXPCStoreServerRequestHandlingPolicy')
NSManagedObjectContext = _Class('NSManagedObjectContext')
NSCoreDataCoreSpotlightDelegate = _Class('NSCoreDataCoreSpotlightDelegate')
NSEntityMigrationPolicy = _Class('NSEntityMigrationPolicy')
NSMergePolicy = _Class('NSMergePolicy')
PFUbiquityMergePolicy = _Class('PFUbiquityMergePolicy')
NSPersistentStore = _Class('NSPersistentStore')
NSSQLCore = _Class('NSSQLCore')
NSMappedObjectStore = _Class('NSMappedObjectStore')
NSMemoryObjectStore = _Class('NSMemoryObjectStore')
NSBinaryObjectStore = _Class('NSBinaryObjectStore')
NSIncrementalStore = _Class('NSIncrementalStore')
NSXPCStore = _Class('NSXPCStore')
NSAtomicStore = _Class('NSAtomicStore')
_NSCoreDataOptimisticLockingException = _Class('_NSCoreDataOptimisticLockingException')
_NSCoreDataConstraintViolationException = _Class('_NSCoreDataConstraintViolationException')
_NSCoreDataException = _Class('_NSCoreDataException')
NSMemoryStoreInPredicateOperator = _Class('NSMemoryStoreInPredicateOperator')
NSMemoryStoreEqualityPredicateOperator = _Class('NSMemoryStoreEqualityPredicateOperator')
NSFetchRequestExpression = _Class('NSFetchRequestExpression')
NSCKRecordZoneQueryCursorTransformer = _Class('NSCKRecordZoneQueryCursorTransformer')
NSCKRecordZoneQueryPredicateTransformer = _Class('NSCKRecordZoneQueryPredicateTransformer')
PFCloudKitMetadataValueTransformer = _Class('PFCloudKitMetadataValueTransformer')
PFUbiquityFileCoordinator = _Class('PFUbiquityFileCoordinator')
NSManagedObject = _Class('NSManagedObject')
NSCKExportOperation = _Class('NSCKExportOperation')
NSCKExportMetadata = _Class('NSCKExportMetadata')
CDDCloudKitRegisteredClient = _Class('CDDCloudKitRegisteredClient')
PFUbiquityPeerRange = _Class('PFUbiquityPeerRange')
PFUbiquityStoreMetadata = _Class('PFUbiquityStoreMetadata')
PFUbiquityTransactionEntry = _Class('PFUbiquityTransactionEntry')
PFUbiquityPeer = _Class('PFUbiquityPeer')
NSCKMirroredRelationship = _Class('NSCKMirroredRelationship')
NSCKRecordZoneQuery = _Class('NSCKRecordZoneQuery')
NSCKImportOperation = _Class('NSCKImportOperation')
NSCKExportedObject = _Class('NSCKExportedObject')
NSCKImportPendingRelationship = _Class('NSCKImportPendingRelationship')
PFUbiquityRemotePeerState = _Class('PFUbiquityRemotePeerState')
CDDCloudKitScheduledActivity = _Class('CDDCloudKitScheduledActivity')
PFUbiquityPeerState = _Class('PFUbiquityPeerState')
NSCKDatabaseMetadata = _Class('NSCKDatabaseMetadata')
NSCKMetadataEntry = _Class('NSCKMetadataEntry')
NSCKHistoryAnalyzerState = _Class('NSCKHistoryAnalyzerState')
NSCKRecordZoneMetadata = _Class('NSCKRecordZoneMetadata')
NSCKEvent = _Class('NSCKEvent')
NSCKRecordMetadata = _Class('NSCKRecordMetadata')
PFUbiquityImportOperation = _Class('PFUbiquityImportOperation')
PFUbiquityBaselineOperation = _Class('PFUbiquityBaselineOperation')
PFUbiquityBaselineRecoveryOperation = _Class('PFUbiquityBaselineRecoveryOperation')
PFUbiquityBaselineRollOperation = _Class('PFUbiquityBaselineRollOperation')
PFUbiquityBaselineRollResponseOperation = _Class('PFUbiquityBaselineRollResponseOperation')
_PFUbiquityRecordImportOperation = _Class('_PFUbiquityRecordImportOperation')
_NSKnownKeysEnumerator = _Class('_NSKnownKeysEnumerator')
_PFResultObjectKeyEnumerator = _Class('_PFResultObjectKeyEnumerator')
_PFAbstractString = _Class('_PFAbstractString')
_PFResultString = _Class('_PFResultString')
_PFResultUniString = _Class('_PFResultUniString')
_PFResultASCIIString = _Class('_PFResultASCIIString')
_PFEncodedString = _Class('_PFEncodedString')
_PFFetchedResultOrderedSetWrapper = _Class('_PFFetchedResultOrderedSetWrapper')
_NSNotifyingWrapperMutableOrderedSet = _Class('_NSNotifyingWrapperMutableOrderedSet')
_NSProxyWrapperMutableOrderedSet = _Class('_NSProxyWrapperMutableOrderedSet')
_NSFaultingMutableOrderedSet = _Class('_NSFaultingMutableOrderedSet')
_NSNotifyingWrapperMutableSet = _Class('_NSNotifyingWrapperMutableSet')
_NSProxyWrapperMutableSet = _Class('_NSProxyWrapperMutableSet')
_NSFaultingMutableSet = _Class('_NSFaultingMutableSet')
_PFResultObject = _Class('_PFResultObject')
NSKnownKeysDictionary = _Class('NSKnownKeysDictionary')
NSKnownKeysDictionary1 = _Class('NSKnownKeysDictionary1')
NSKnownKeysDictionary2 = _Class('NSKnownKeysDictionary2')
_NSDataFileBackedFuture = _Class('_NSDataFileBackedFuture')
_NSCloudKitDataFileBackedFuture = _Class('_NSCloudKitDataFileBackedFuture')
_PFExternalReferenceData = _Class('_PFExternalReferenceData')
_PFResultData = _Class('_PFResultData')
_PFEncodedData = _Class('_PFEncodedData')
_PFEvanescentData = _Class('_PFEvanescentData')
_PFVMData = _Class('_PFVMData')
_PFCachedNumber = _Class('_PFCachedNumber')
_PFEncodedArray = _Class('_PFEncodedArray')
_PFBatchFaultingArray = _Class('_PFBatchFaultingArray')
_PFBatchHistoryFaultingArray = _Class('_PFBatchHistoryFaultingArray')
_PFArray = _Class('_PFArray')
_PFResultArray = _Class('_PFResultArray')
_PFMutableProxyArray = _Class('_PFMutableProxyArray')
_NSFaultingMutableArray = _Class('_NSFaultingMutableArray')
