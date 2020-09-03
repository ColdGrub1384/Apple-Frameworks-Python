'''
Classes from the 'Trial' framework.
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

    
TRIXPCUtils = _Class('TRIXPCUtils')
TRINamespaceDescriptor = _Class('TRINamespaceDescriptor')
TRIVersion = _Class('TRIVersion')
TRINamespaceStatus = _Class('TRINamespaceStatus')
TRIAppContainer = _Class('TRIAppContainer')
TRIClient = _Class('TRIClient')
TRIClientGuardedData = _Class('TRIClientGuardedData')
TRINotificationCallback = _Class('TRINotificationCallback')
TRINamespaceFactorProviderChain = _Class('TRINamespaceFactorProviderChain')
TRISubjectProvider = _Class('TRISubjectProvider')
TRISubjectProviderGuardedData = _Class('TRISubjectProviderGuardedData')
TRISystemConfiguration = _Class('TRISystemConfiguration')
TRISystemInfoGuardedData = _Class('TRISystemInfoGuardedData')
TRIDownloadNotification = _Class('TRIDownloadNotification')
TRITreatmentInfo = _Class('TRITreatmentInfo')
TRIProcessInfo = _Class('TRIProcessInfo')
TRIStopwatch = _Class('TRIStopwatch')
TRIStandardPaths = _Class('TRIStandardPaths')
TRIFactorDownloadValidator = _Class('TRIFactorDownloadValidator')
TRILogger = _Class('TRILogger')
TRIDevLogger = _Class('TRIDevLogger')
TRIPruningFactorLevelCache = _Class('TRIPruningFactorLevelCache')
TRIPruningFactorLevelCacheGuardedData = _Class('TRIPruningFactorLevelCacheGuardedData')
TRINaiveFactorLevelCache = _Class('TRINaiveFactorLevelCache')
TRISystemInfo = _Class('TRISystemInfo')
TRINotificationState = _Class('TRINotificationState')
TRINamespaceUpdateNotification = _Class('TRINamespaceUpdateNotification')
TRIDefaultFactorProvider = _Class('TRIDefaultFactorProvider')
TRIDownloadOptions = _Class('TRIDownloadOptions')
TRILevelChecked = _Class('TRILevelChecked')
TRITrackingId = _Class('TRITrackingId')
TRINamespaceFactorProvider = _Class('TRINamespaceFactorProvider')
TRILogTreatmentReader = _Class('TRILogTreatmentReader')
TRISubjectRotationNotification = _Class('TRISubjectRotationNotification')
TRINamespaceStatusProvider = _Class('TRINamespaceStatusProvider')
TRIEntitlement = _Class('TRIEntitlement')
TRIXPCNamespaceManagementClient = _Class('TRIXPCNamespaceManagementClient')
TRITripersistedNamespaceStatusRoot = _Class('TRITripersistedNamespaceStatusRoot')
TRITripersistedNetworkBehaviorRoot = _Class('TRITripersistedNetworkBehaviorRoot')
TRIPersistedNamespaceStatus = _Class('TRIPersistedNamespaceStatus')
TRIPersistedNetworkBehavior = _Class('TRIPersistedNetworkBehavior')
