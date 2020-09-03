'''
Classes from the 'CoreServices' framework.
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

    
LSApplicationRestrictionsManager = _Class('LSApplicationRestrictionsManager')
LSAltIconManager = _Class('LSAltIconManager')
LSDatabaseContext = _Class('LSDatabaseContext')
LSClaimBindingConfiguration = _Class('LSClaimBindingConfiguration')
LSClaimBinding = _Class('LSClaimBinding')
LSApplicationWorkspaceObserver = _Class('LSApplicationWorkspaceObserver')
LSInstallProgressObserver = _Class('LSInstallProgressObserver')
LSInstallProgressList = _Class('LSInstallProgressList')
LSProgressNotificationTimer = _Class('LSProgressNotificationTimer')
LSAppLink = _Class('LSAppLink')
LSApplicationWorkspaceRemoteObserver = _Class('LSApplicationWorkspaceRemoteObserver')
LSApplicationWorkspace = _Class('LSApplicationWorkspace')
LSRegistrationInfo = _Class('LSRegistrationInfo')
LSDatabaseBuilder = _Class('LSDatabaseBuilder')
LSRecordBuilder = _Class('LSRecordBuilder')
LSBundleRecordBuilder = _Class('LSBundleRecordBuilder')
LSBundleRecordUpdater = _Class('LSBundleRecordUpdater')
LSAppClipMetadata = _Class('LSAppClipMetadata')
LSiTunesMetadata = _Class('LSiTunesMetadata')
LSPlugInQuery = _Class('LSPlugInQuery')
LSPlugInQueryWithURL = _Class('LSPlugInQueryWithURL')
LSPlugInQueryWithQueryDictionary = _Class('LSPlugInQueryWithQueryDictionary')
LSPlugInQueryWithIdentifier = _Class('LSPlugInQueryWithIdentifier')
LSRecord = _Class('LSRecord')
LSClaimRecord = _Class('LSClaimRecord')
UTTypeRecord = _Class('UTTypeRecord')
LSBundleRecord = _Class('LSBundleRecord')
LSApplicationExtensionRecord = _Class('LSApplicationExtensionRecord')
LSApplicationRecord = _Class('LSApplicationRecord')
LSExtensionPointRecord = _Class('LSExtensionPointRecord')
FSNode = _Class('FSNode')
LSExtensionPoint = _Class('LSExtensionPoint')
LSResourceProxy = _Class('LSResourceProxy')
LSDocumentProxy = _Class('LSDocumentProxy')
LSBundleProxy = _Class('LSBundleProxy')
LSVPNPluginProxy = _Class('LSVPNPluginProxy')
LSPlugInKitProxy = _Class('LSPlugInKitProxy')
LSApplicationProxy = _Class('LSApplicationProxy')
LSEnumerator = _Class('LSEnumerator')
LSPropertyList = _Class('LSPropertyList')
LSBundleInfoCachedValues = _Class('LSBundleInfoCachedValues')
