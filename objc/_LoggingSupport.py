'''
Classes from the 'LoggingSupport' framework.
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

    
OSLogEventStore = _Class('OSLogEventStore')
OSLogEventLocalStore = _Class('OSLogEventLocalStore')
OSLogDecomposedMessageSegment = _Class('OSLogDecomposedMessageSegment')
OSLogEventSerializer = _Class('OSLogEventSerializer')
OSLogPreferencesCategory = _Class('OSLogPreferencesCategory')
OSLogPreferencesSubsystem = _Class('OSLogPreferencesSubsystem')
OSLogPreferencesProcess = _Class('OSLogPreferencesProcess')
OSLogPreferencesManager = _Class('OSLogPreferencesManager')
OSLogEventSource = _Class('OSLogEventSource')
LoggingSupport_OSLogCoder = _Class('LoggingSupport_OSLogCoder')
OSLogEventStreamPosition = _Class('OSLogEventStreamPosition')
OSLogEventLiveStore = _Class('OSLogEventLiveStore')
OSLogTermDumper = _Class('OSLogTermDumper')
OSLogEventStreamBase = _Class('OSLogEventStreamBase')
OSLogDeserializedEventStream = _Class('OSLogDeserializedEventStream')
OSLogEventStream = _Class('OSLogEventStream')
OSLogEventLiveStream = _Class('OSLogEventLiveStream')
OSLogPersistence = _Class('OSLogPersistence')
OSLogEventLiveSource = _Class('OSLogEventLiveSource')
OSActivityEvent = _Class('OSActivityEvent')
OSActivityLossEvent = _Class('OSActivityLossEvent')
OSActivityTimesyncEvent = _Class('OSActivityTimesyncEvent')
OSActivityStatedumpEvent = _Class('OSActivityStatedumpEvent')
OSActivityTransitionEvent = _Class('OSActivityTransitionEvent')
OSActivityUserActionEvent = _Class('OSActivityUserActionEvent')
OSActivityEventMessage = _Class('OSActivityEventMessage')
OSActivityLogMessageEvent = _Class('OSActivityLogMessageEvent')
OSActivitySignpostEvent = _Class('OSActivitySignpostEvent')
OSActivityTraceMessageEvent = _Class('OSActivityTraceMessageEvent')
OSActivityCreateEvent = _Class('OSActivityCreateEvent')
OSActivityStream = _Class('OSActivityStream')
OSLogDevice = _Class('OSLogDevice')
OSLogEventBacktrace = _Class('OSLogEventBacktrace')
OSLogEventBacktraceFrame = _Class('OSLogEventBacktraceFrame')
OSLogEventMessageArgument = _Class('OSLogEventMessageArgument')
OSLogDeserializedEventMessageArgument = _Class('OSLogDeserializedEventMessageArgument')
OSLogMessagePlaceholder = _Class('OSLogMessagePlaceholder')
OSLogDeserializedMessagePlaceholder = _Class('OSLogDeserializedMessagePlaceholder')
OSLogEventDecomposedMessage = _Class('OSLogEventDecomposedMessage')
OSLogDeserializedEventDecomposedMessage = _Class('OSLogDeserializedEventDecomposedMessage')
OSLogEventProxy = _Class('OSLogEventProxy')
