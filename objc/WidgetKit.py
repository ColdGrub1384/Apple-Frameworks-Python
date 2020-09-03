
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
    
    
WidgetKit.WidgetURLHandler = _Class('WidgetKit.WidgetURLHandler')
WidgetKit.UnfairLock = _Class('WidgetKit.UnfairLock')
WidgetKit.BaseEntryProviderBox = _Class('WidgetKit.BaseEntryProviderBox')
WidgetKit.WidgetPreviewAgent = _Class('WidgetKit.WidgetPreviewAgent')
WidgetKit._WidgetExtensionSession = _Class('WidgetKit._WidgetExtensionSession')
WidgetKit._RunningBoardInterface = _Class('WidgetKit._RunningBoardInterface')
WidgetKit.WidgetExtensionSessionFactory = _Class('WidgetKit.WidgetExtensionSessionFactory')
WidgetKit.OptionalLocalizationsWrapper = _Class('WidgetKit.OptionalLocalizationsWrapper')
WidgetKit.WidgetHost = _Class('WidgetKit.WidgetHost')
WidgetKit.ResolvedWidgetBundleHost = _Class('WidgetKit.ResolvedWidgetBundleHost')
WidgetKit.WidgetArchiver = _Class('WidgetKit.WidgetArchiver')
WidgetKit.WidgetLocalizations = _Class('WidgetKit.WidgetLocalizations')
WidgetKit.WGAutoreleasePool = _Class('WidgetKit.WGAutoreleasePool')
WidgetKit._TimelineArchivedViewCollection = _Class('WidgetKit._TimelineArchivedViewCollection')
WidgetKit.WidgetCenter = _Class('WidgetKit.WidgetCenter')
WidgetKit.Dates = _Class('WidgetKit.Dates')
WidgetKit.WidgetViewCollection = _Class('WidgetKit.WidgetViewCollection')
CHKWidgetPersonality = _Class('CHKWidgetPersonality')
CHKWidgetEnvironment = _Class('CHKWidgetEnvironment')
WidgetExtensionChecker = _Class('WidgetExtensionChecker')
WidgetKit._AvocadoExtensionBaseContext = _Class('WidgetKit._AvocadoExtensionBaseContext')
WidgetKit.WidgetExtensionContext = _Class('WidgetKit.WidgetExtensionContext')
WidgetKit.WidgetHostContext = _Class('WidgetKit.WidgetHostContext')