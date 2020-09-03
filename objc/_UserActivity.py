'''
Classes from the 'UserActivity' framework.
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

    
UASharedPasteboard = _Class('UASharedPasteboard')
UABestAppSuggestion = _Class('UABestAppSuggestion')
UAPBIRIdentityConverter = _Class('UAPBIRIdentityConverter')
UABestAppSuggestionManagerProxy = _Class('UABestAppSuggestionManagerProxy')
UABestAppSuggestionManager = _Class('UABestAppSuggestionManager')
UAPBIRFileURLConverter = _Class('UAPBIRFileURLConverter')
UASharedPasteboardIRManager = _Class('UASharedPasteboardIRManager')
UAPasteboardGeneration = _Class('UAPasteboardGeneration')
UAPasteboardDataProvider = _Class('UAPasteboardDataProvider')
UAPasteboardFileItemProvider = _Class('UAPasteboardFileItemProvider')
UAUserActivityManager = _Class('UAUserActivityManager')
UASharedPasteboardManager = _Class('UASharedPasteboardManager')
UASharedPasteboardTypeInfo = _Class('UASharedPasteboardTypeInfo')
UASharedPasteboardItemInfo = _Class('UASharedPasteboardItemInfo')
UASharedPasteboardInfo = _Class('UASharedPasteboardInfo')
UAResumableActivitiesControlManager = _Class('UAResumableActivitiesControlManager')
UAUserActivityInfo = _Class('UAUserActivityInfo')
UAPasteboardItem = _Class('UAPasteboardItem')
UAPasteboardFileChunkItemProvider = _Class('UAPasteboardFileChunkItemProvider')
UAUserActivityProxy = _Class('UAUserActivityProxy')
UAPBIRSandboxExtConverter = _Class('UAPBIRSandboxExtConverter')
UAUserActivity = _Class('UAUserActivity')
UAPBIRPublicURLConverter = _Class('UAPBIRPublicURLConverter')
UAFileChunkInputStream = _Class('UAFileChunkInputStream')
