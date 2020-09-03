
'''
Classes from the 'Sleep' framework.
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
    
    
HKSPMockUserDefaults = _Class('HKSPMockUserDefaults')
HKSPAgeMonitor = _Class('HKSPAgeMonitor')
HKSPSleepScheduleDayOccurrence = _Class('HKSPSleepScheduleDayOccurrence')
HKSPMutableSleepScheduleDayOccurrence = _Class('HKSPMutableSleepScheduleDayOccurrence')
HKSPHealthStoreProvider = _Class('HKSPHealthStoreProvider')
HKSPAnalyticsOnboardingEvent = _Class('HKSPAnalyticsOnboardingEvent')
HKSPXPCConnectionInfo = _Class('HKSPXPCConnectionInfo')
HKSPSleepEventTimelineResults = _Class('HKSPSleepEventTimelineResults')
HKSPSleepEventTimelineBuilder = _Class('HKSPSleepEventTimelineBuilder')
HKSPXPCConnectionProvider = _Class('HKSPXPCConnectionProvider')
HKSPPropertyModification = _Class('HKSPPropertyModification')
HKSPSleepEventRecord = _Class('HKSPSleepEventRecord')
HKSPMutableSleepEventRecord = _Class('HKSPMutableSleepEventRecord')
HKSPAlarmConfiguration = _Class('HKSPAlarmConfiguration')
HKSPMutableAlarmConfiguration = _Class('HKSPMutableAlarmConfiguration')
HKSPXPCClient = _Class('HKSPXPCClient')
HKSPXPCConnectionListener = _Class('HKSPXPCConnectionListener')
HKSPSleepEventTimeline = _Class('HKSPSleepEventTimeline')
HKSPTestObject = _Class('HKSPTestObject')
HKSPMutableTestObject = _Class('HKSPMutableTestObject')
HKSPProperty = _Class('HKSPProperty')
HKSPSleepStoreCache = _Class('HKSPSleepStoreCache')
HKSPAnalyticsWindDownEventDataWrapper = _Class('HKSPAnalyticsWindDownEventDataWrapper')
HKSPAnalyticsWindDownEventData = _Class('HKSPAnalyticsWindDownEventData')
HKSPResolvedSleepScheduleOccurrence = _Class('HKSPResolvedSleepScheduleOccurrence')
HKSPSleepSettings = _Class('HKSPSleepSettings')
HKSPMutableSleepSettings = _Class('HKSPMutableSleepSettings')
HKSPAnalyticsStore = _Class('HKSPAnalyticsStore')
HKSPSleepStoreExportedObject = _Class('HKSPSleepStoreExportedObject')
HKSPSleepStore = _Class('HKSPSleepStore')
HKSPSleepSchedule = _Class('HKSPSleepSchedule')
HKSPMutableSleepSchedule = _Class('HKSPMutableSleepSchedule')
HKSPSensitiveUIMonitor = _Class('HKSPSensitiveUIMonitor')
HKSPSleepScheduleOccurrence = _Class('HKSPSleepScheduleOccurrence')
HKSPMutableSleepScheduleOccurrence = _Class('HKSPMutableSleepScheduleOccurrence')
HKSPImmediateExecutor = _Class('HKSPImmediateExecutor')
HKSPCoalescingExecutor = _Class('HKSPCoalescingExecutor')
HKSPStateMachineState = _Class('HKSPStateMachineState')
HKSPPersistentStateMachineState = _Class('HKSPPersistentStateMachineState')
HKSPXPCMessage = _Class('HKSPXPCMessage')
HKSPFeatureAvailabilityStore = _Class('HKSPFeatureAvailabilityStore')
HKSPSleepEvent = _Class('HKSPSleepEvent')
HKSPMuteMonitor = _Class('HKSPMuteMonitor')
HKSPAnalyticsSleepScheduleChangeEvent = _Class('HKSPAnalyticsSleepScheduleChangeEvent')
HKSPChangeSet = _Class('HKSPChangeSet')
HKSPObserverSet = _Class('HKSPObserverSet')
HKSPSleepModeButtonModel = _Class('HKSPSleepModeButtonModel')
HKSPAnalyticsManager = _Class('HKSPAnalyticsManager')
HKSPDiagnostics = _Class('HKSPDiagnostics')
HKSPChange = _Class('HKSPChange')
HKSPRelationshipChange = _Class('HKSPRelationshipChange')
HKSPSleepScheduleModel = _Class('HKSPSleepScheduleModel')
HKSPSleepScheduleRange = _Class('HKSPSleepScheduleRange')
HKSPStateMachine = _Class('HKSPStateMachine')
HKSPPersistentStateMachine = _Class('HKSPPersistentStateMachine')
HKSPAnalyticsWindDownEvent = _Class('HKSPAnalyticsWindDownEvent')
HKSPAnalyticsDailyReportEvent = _Class('HKSPAnalyticsDailyReportEvent')
HKSPDictionaryDeserializer = _Class('HKSPDictionaryDeserializer')
HKSPDictionarySerializer = _Class('HKSPDictionarySerializer')