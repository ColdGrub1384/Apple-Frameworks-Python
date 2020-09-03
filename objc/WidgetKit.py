'''
Classes from the 'WidgetKit' framework.
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
    
    
WidgetURLHandler = _Class('WidgetKit.WidgetURLHandler')
UnfairLock = _Class('WidgetKit.UnfairLock')
BaseEntryProviderBox = _Class('WidgetKit.BaseEntryProviderBox')
WidgetPreviewAgent = _Class('WidgetKit.WidgetPreviewAgent')
_WidgetExtensionSession = _Class('WidgetKit._WidgetExtensionSession')
_RunningBoardInterface = _Class('WidgetKit._RunningBoardInterface')
WidgetExtensionSessionFactory = _Class('WidgetKit.WidgetExtensionSessionFactory')
OptionalLocalizationsWrapper = _Class('WidgetKit.OptionalLocalizationsWrapper')
WidgetHost = _Class('WidgetKit.WidgetHost')
ResolvedWidgetBundleHost = _Class('WidgetKit.ResolvedWidgetBundleHost')
WidgetArchiver = _Class('WidgetKit.WidgetArchiver')
WidgetLocalizations = _Class('WidgetKit.WidgetLocalizations')
WGAutoreleasePool = _Class('WidgetKit.WGAutoreleasePool')
_TimelineArchivedViewCollection = _Class('WidgetKit._TimelineArchivedViewCollection')
WidgetCenter = _Class('WidgetKit.WidgetCenter')
Dates = _Class('WidgetKit.Dates')
WidgetViewCollection = _Class('WidgetKit.WidgetViewCollection')
CHKWidgetPersonality = _Class('CHKWidgetPersonality')
CHKWidgetEnvironment = _Class('CHKWidgetEnvironment')
WidgetExtensionChecker = _Class('WidgetExtensionChecker')
_AvocadoExtensionBaseContext = _Class('WidgetKit._AvocadoExtensionBaseContext')
WidgetExtensionContext = _Class('WidgetKit.WidgetExtensionContext')
WidgetHostContext = _Class('WidgetKit.WidgetHostContext')