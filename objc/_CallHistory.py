'''
Classes from the 'CallHistory' framework.
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

    
CHPluginHelper = _Class('CHPluginHelper')
CallDBMigrator = _Class('CallDBMigrator')
CHMigrator = _Class('CHMigrator')
CHRecentCall = _Class('CHRecentCall')
DeserializedTransaction = _Class('DeserializedTransaction')
CHTransaction = _Class('CHTransaction')
DBMigrationResult = _Class('DBMigrationResult')
CHPhoneBookIOSManager = _Class('CHPhoneBookIOSManager')
CHConfigurationAggregator = _Class('CHConfigurationAggregator')
CallDBMetaInfo = _Class('CallDBMetaInfo')
CallDBManager = _Class('CallDBManager')
CallDBManagerServer = _Class('CallDBManagerServer')
CallDBManagerClient = _Class('CallDBManagerClient')
CHConfiguration = _Class('CHConfiguration')
CHUserConfiguration = _Class('CHUserConfiguration')
CHHandle = _Class('CHHandle')
CHLogger = _Class('CHLogger')
WatchDogTimer = _Class('WatchDogTimer')
AWDLogger = _Class('AWDLogger')
DBManager = _Class('DBManager')
SyncManager = _Class('SyncManager')
CHPhoneNumber = _Class('CHPhoneNumber')
GateKeeper = _Class('GateKeeper')
CallHistoryDBHandle = _Class('CallHistoryDBHandle')
NotificationSender = _Class('NotificationSender')
CHSynchronizedLoggable = _Class('CHSynchronizedLoggable')
TransactionManager = _Class('TransactionManager')
CHSharedAddressBook = _Class('CHSharedAddressBook')
CallHistoryDBClientHandle = _Class('CallHistoryDBClientHandle')
CHManager = _Class('CHManager')
CHDatabaseClientHandleManager = _Class('CHDatabaseClientHandleManager')
CHSynchronizable = _Class('CHSynchronizable')
CHLogServer = _Class('CHLogServer')
CHEntityMigrationPolicy = _Class('CHEntityMigrationPolicy')
CHManagedHandleMigrationPolicy = _Class('CHManagedHandleMigrationPolicy')
EncryptionTransformer = _Class('EncryptionTransformer')
AWDCallHistoryMalformedCloudChangeToken = _Class('AWDCallHistoryMalformedCloudChangeToken')
AWDCallHistoryNilUuid = _Class('AWDCallHistoryNilUuid')
AWDCallHistoryGizmoDatabaseMigrationFailure = _Class('AWDCallHistoryGizmoDatabaseMigrationFailure')
AWDCallHistoryEntitlementRejection = _Class('AWDCallHistoryEntitlementRejection')
AWDCallHistoryErrorReport = _Class('AWDCallHistoryErrorReport')
AWDCallHistorySync = _Class('AWDCallHistorySync')
AWDCallHistorySyncOverLimit = _Class('AWDCallHistorySyncOverLimit')
AWDCallHistoryMissingCloudChangeToken = _Class('AWDCallHistoryMissingCloudChangeToken')
AWDCallHistoryDatabaseMigration = _Class('AWDCallHistoryDatabaseMigration')
AWDCallHistoryUninitializedDatabaseSave = _Class('AWDCallHistoryUninitializedDatabaseSave')
AWDCallHistoryDatabaseSaveError = _Class('AWDCallHistoryDatabaseSaveError')
AWDCallHistoryGizmoBootstrap = _Class('AWDCallHistoryGizmoBootstrap')
AWDCallHistoryCallAddedBeforeUnlock = _Class('AWDCallHistoryCallAddedBeforeUnlock')
AWDCallHistoryDeleteAll = _Class('AWDCallHistoryDeleteAll')
AWDCallHistoryDeviceUnlocked = _Class('AWDCallHistoryDeviceUnlocked')
AWDCallHistoryCommCenterMigration = _Class('AWDCallHistoryCommCenterMigration')
CHManagedHandle = _Class('CHManagedHandle')
CallRecord = _Class('CallRecord')
CallDBProperties = _Class('CallDBProperties')
