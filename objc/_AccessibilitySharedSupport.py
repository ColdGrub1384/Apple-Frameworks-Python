'''
Classes from the 'AccessibilitySharedSupport' framework.
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

    
AXSSKeyboardCommandCategory = _Class('AXSSKeyboardCommandCategory')
AXSSInterDeviceCommunicator = _Class('AXSSInterDeviceCommunicator')
AXSSInterDeviceSearchResult = _Class('AXSSInterDeviceSearchResult')
AXSSActionManager = _Class('AXSSActionManager')
AXSSMotionTrackingHIDManager = _Class('AXSSMotionTrackingHIDManager')
AXSSEventManager = _Class('AXSSEventManager')
AXSSMotionTrackingCameraManager = _Class('AXSSMotionTrackingCameraManager')
AXSSKeyboardCommandInfo = _Class('AXSSKeyboardCommandInfo')
AXSSLanguageTagger = _Class('AXSSLanguageTagger')
AXSSWordDescriptionManager = _Class('AXSSWordDescriptionManager')
AXSSWordDescriptionManager_ja = _Class('AXSSWordDescriptionManager_ja')
AXSSWordDescriptionManager_zh = _Class('AXSSWordDescriptionManager_zh')
AXSSPunctuationEntry = _Class('AXSSPunctuationEntry')
AXSSLanguageTag = _Class('AXSSLanguageTag')
AXSSMotionTrackingUtilities = _Class('AXSSMotionTrackingUtilities')
AXSSMotionTrackingInputManager = _Class('AXSSMotionTrackingInputManager')
AXSSMotionTracker = _Class('AXSSMotionTracker')
AXSSKeyboardCommandMap = _Class('AXSSKeyboardCommandMap')
AXSSPunctuationGroup = _Class('AXSSPunctuationGroup')
AXSSMotionTrackingState = _Class('AXSSMotionTrackingState')
AXSSCloudKitHelper = _Class('AXSSCloudKitHelper')
AXSSPunctuationEntryCloudKitHelper = _Class('AXSSPunctuationEntryCloudKitHelper')
AXSSPunctuationGroupCloudKitHelper = _Class('AXSSPunctuationGroupCloudKitHelper')
AXSSCloudData = _Class('AXSSCloudData')
AXSSDialectMap = _Class('AXSSDialectMap')
AXSSPronunciationSubstitution = _Class('AXSSPronunciationSubstitution')
AXSSInterDeviceSwitchEvent = _Class('AXSSInterDeviceSwitchEvent')
AXSSSwitchControlSettings = _Class('AXSSSwitchControlSettings')
AXSSLanguageManager = _Class('AXSSLanguageManager')
AXSSKeyboardCommand = _Class('AXSSKeyboardCommand')
AXSSLanguageMap = _Class('AXSSLanguageMap')
AXSSVoiceTagger = _Class('AXSSVoiceTagger')
AXSSMotionTrackingInput = _Class('AXSSMotionTrackingInput')
AXSSMotionTrackingVideoFileInput = _Class('AXSSMotionTrackingVideoFileInput')
AXSSMotionTrackingHIDInput = _Class('AXSSMotionTrackingHIDInput')
AXSSMotionTrackingCameraInput = _Class('AXSSMotionTrackingCameraInput')
AXSSMotionTrackingExpressionConfiguration = _Class('AXSSMotionTrackingExpressionConfiguration')
AXSSMotionTrackingInputConfiguration = _Class('AXSSMotionTrackingInputConfiguration')
AXSSKeyboardEvent = _Class('AXSSKeyboardEvent')
AXSSLanguageLoader = _Class('AXSSLanguageLoader')
AXSSKeyChord = _Class('AXSSKeyChord')
AXSSMotionTrackingVideoFileInputManager = _Class('AXSSMotionTrackingVideoFileInputManager')
AXSSDatabaseManager = _Class('AXSSDatabaseManager')
AXSSPunctuationManager = _Class('AXSSPunctuationManager')
AXSSInterDeviceSecurityHelper = _Class('AXSSInterDeviceSecurityHelper')
AXSSCloudKitHelperManagedObjectContext = _Class('AXSSCloudKitHelperManagedObjectContext')
AXSS_PunctuationGroup = _Class('AXSS_PunctuationGroup')
AXSS_PunctuationEntry = _Class('AXSS_PunctuationEntry')
AXSS_PunctuationContext = _Class('AXSS_PunctuationContext')
AXSS_PunctuationCloudDeletionCache = _Class('AXSS_PunctuationCloudDeletionCache')
VOVoice = _Class('VOVoice')
VOSubstitution = _Class('VOSubstitution')
VOLanguage = _Class('VOLanguage')
VOBundle = _Class('VOBundle')
