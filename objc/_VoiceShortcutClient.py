'''
Classes from the 'VoiceShortcutClient' framework.
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

    
VCWidgetWorkflow = _Class('VCWidgetWorkflow')
WFSingleConnectionXPCListener = _Class('WFSingleConnectionXPCListener')
VCInteractionDonation = _Class('VCInteractionDonation')
WFCoreDataChangeNotification = _Class('WFCoreDataChangeNotification')
WFCoreDataObjectChange = _Class('WFCoreDataObjectChange')
WFObservableResult = _Class('WFObservableResult')
WFObservableObjectResult = _Class('WFObservableObjectResult')
WFObservableArrayResult = _Class('WFObservableArrayResult')
WFColor = _Class('WFColor')
WFWorkflowRunDescriptor = _Class('WFWorkflowRunDescriptor')
WFINShortcutRunDescriptor = _Class('WFINShortcutRunDescriptor')
WFWorkflowDatabaseRunDescriptor = _Class('WFWorkflowDatabaseRunDescriptor')
VCActionDonationFetcher = _Class('VCActionDonationFetcher')
VCUserActivityDonationFetcher = _Class('VCUserActivityDonationFetcher')
VCInteractionDonationFetcher = _Class('VCInteractionDonationFetcher')
VCUserActivityDonation = _Class('VCUserActivityDonation')
WFGradient = _Class('WFGradient')
WFWorkflowRunnerClient = _Class('WFWorkflowRunnerClient')
WFActionExtensionWorkflowRunnerClient = _Class('WFActionExtensionWorkflowRunnerClient')
WFAccessibilityWorkflowRunnerClient = _Class('WFAccessibilityWorkflowRunnerClient')
WFWidgetWorkflowRunnerClient = _Class('WFWidgetWorkflowRunnerClient')
WFSleepWorkflowRunnerClient = _Class('WFSleepWorkflowRunnerClient')
WFSuggestionsWorkflowRunnerClient = _Class('WFSuggestionsWorkflowRunnerClient')
VCAccessSpecifier = _Class('VCAccessSpecifier')
VCSleepAction = _Class('VCSleepAction')
VCSleepDonationAction = _Class('VCSleepDonationAction')
VCSleepOpenAppAction = _Class('VCSleepOpenAppAction')
VCSleepHomeAccessoryAction = _Class('VCSleepHomeAccessoryAction')
WFShareSheetWorkflow = _Class('WFShareSheetWorkflow')
WFRemoteImageDrawingContext = _Class('WFRemoteImageDrawingContext')
VCConfiguredSleepWorkflow = _Class('VCConfiguredSleepWorkflow')
VCSleepWorkflow = _Class('VCSleepWorkflow')
WFDatabaseObjectDescriptor = _Class('WFDatabaseObjectDescriptor')
WFWorkflowDescriptor = _Class('WFWorkflowDescriptor')
WFAccessibilityWorkflow = _Class('WFAccessibilityWorkflow')
WFCoreDataResultState = _Class('WFCoreDataResultState')
WFWorkflowQuery = _Class('WFWorkflowQuery')
VCVoiceShortcut = _Class('VCVoiceShortcut')
WFWorkflowRunningContext = _Class('WFWorkflowRunningContext')
WFWorkflowRunRequest = _Class('WFWorkflowRunRequest')
VCVoiceShortcutClient = _Class('VCVoiceShortcutClient')
