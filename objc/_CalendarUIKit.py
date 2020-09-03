'''
Classes from the 'CalendarUIKit' framework.
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

    
CUIKTravelAdvisoryUtilities = _Class('CUIKTravelAdvisoryUtilities')
CUIKLocationDescriptionGenerator = _Class('CUIKLocationDescriptionGenerator')
CUIKSuggestionDescriptionGenerator = _Class('CUIKSuggestionDescriptionGenerator')
CUIKSuggestionCoalescedInfo = _Class('CUIKSuggestionCoalescedInfo')
CUIKEditingManager = _Class('CUIKEditingManager')
CUIKDateStrings = _Class('CUIKDateStrings')
CUIKOverlayCalendar = _Class('CUIKOverlayCalendar')
CUIKAvailabilityDescriptionGenerator = _Class('CUIKAvailabilityDescriptionGenerator')
CUIKApplicationIconUtilities = _Class('CUIKApplicationIconUtilities')
CUIKTravelAdvisoryDescriptionUtilities = _Class('CUIKTravelAdvisoryDescriptionUtilities')
CUIKDefaultIconGenerator = _Class('CUIKDefaultIconGenerator')
CUIKIconDrawObject = _Class('CUIKIconDrawObject')
CUIKAttendeeHeuristics = _Class('CUIKAttendeeHeuristics')
CUIKDefaultAlarmPreferences = _Class('CUIKDefaultAlarmPreferences')
CUIKInviteeDescriptionGenerator = _Class('CUIKInviteeDescriptionGenerator')
CUIKiCloudKVStore = _Class('CUIKiCloudKVStore')
EKUndoSliceOutcome = _Class('EKUndoSliceOutcome')
EKSliceDescription = _Class('EKSliceDescription')
EKPostSliceDescription = _Class('EKPostSliceDescription')
EKSeriesDetails = _Class('EKSeriesDetails')
CUIKTimeToLeaveDescriptionGenerator = _Class('CUIKTimeToLeaveDescriptionGenerator')
CUIKSplashScreenStrings = _Class('CUIKSplashScreenStrings')
CUIKEventHeuristics = _Class('CUIKEventHeuristics')
CUIKSingleDayTimelineLayoutPartition = _Class('CUIKSingleDayTimelineLayoutPartition')
CUIKEventTimeDetector = _Class('CUIKEventTimeDetector')
CUIKSingleDayTimelineOccurrenceBucket = _Class('CUIKSingleDayTimelineOccurrenceBucket')
CUIKEditingContextGroup = _Class('CUIKEditingContextGroup')
CUIKTTLDescriptionGeneratorUtilities = _Class('CUIKTTLDescriptionGeneratorUtilities')
CUIKEventSuggestionGenerator = _Class('CUIKEventSuggestionGenerator')
CUIKCalendarApplicationIcon = _Class('CUIKCalendarApplicationIcon')
CUIKIconDrawingObject = _Class('CUIKIconDrawingObject')
CUIKEditingContext = _Class('CUIKEditingContext')
CUIKDescriptionGenerator = _Class('CUIKDescriptionGenerator')
CUIKNotificationDescriptionGenerator = _Class('CUIKNotificationDescriptionGenerator')
CUIKEventDescriptionGenerator = _Class('CUIKEventDescriptionGenerator')
CUIKRecurrenceRuleDescriptionGenerator = _Class('CUIKRecurrenceRuleDescriptionGenerator')
CUIKContactDescriptionGenerator = _Class('CUIKContactDescriptionGenerator')
CUIKAttendeeDescriptionGenerator = _Class('CUIKAttendeeDescriptionGenerator')
CUIKDateDescriptionGenerator = _Class('CUIKDateDescriptionGenerator')
CUIKPhoneNumberDescriptionGenerator = _Class('CUIKPhoneNumberDescriptionGenerator')
CUIKMessageStrings = _Class('CUIKMessageStrings')
CUIKSingleDayTimelineLayout = _Class('CUIKSingleDayTimelineLayout')
CUIKCalendarDescriptionGenerator = _Class('CUIKCalendarDescriptionGenerator')
CUIKRecents = _Class('CUIKRecents')
CUIKUserActivity = _Class('CUIKUserActivity')
CUIKUserActivityRemindersListDate = _Class('CUIKUserActivityRemindersListDate')
CUIKUserActivityRemindersListScheduled = _Class('CUIKUserActivityRemindersListScheduled')
CUIKUserActivityNewEvent = _Class('CUIKUserActivityNewEvent')
CUIKUserActivityCalendarDate = _Class('CUIKUserActivityCalendarDate')
CUIKUserActivityTomorrow = _Class('CUIKUserActivityTomorrow')
CUIKUserActivityWithSource = _Class('CUIKUserActivityWithSource')
CUIKUserActivityRemindersListSharedInvitation = _Class('CUIKUserActivityRemindersListSharedInvitation')
CUIKUserActivityRemindersListCategory = _Class('CUIKUserActivityRemindersListCategory')
CUIKUserActivityCalendarEvent = _Class('CUIKUserActivityCalendarEvent')
CUIKUserOperation = _Class('CUIKUserOperation')
CUIKCreateOperation = _Class('CUIKCreateOperation')
CUIKUndeleteFutureOperation = _Class('CUIKUndeleteFutureOperation')
CUIKSaveOperation = _Class('CUIKSaveOperation')
CUIKUnsliceOperation = _Class('CUIKUnsliceOperation')
CUIKResliceOperation = _Class('CUIKResliceOperation')
CUIKRevertOperation = _Class('CUIKRevertOperation')
CUIKUnrevertOperation = _Class('CUIKUnrevertOperation')
CUIKDeleteOperation = _Class('CUIKDeleteOperation')
CUIKObjectGroup = _Class('CUIKObjectGroup')
CUIKIcon = _Class('CUIKIcon')
CUIKUndoManager = _Class('CUIKUndoManager')
