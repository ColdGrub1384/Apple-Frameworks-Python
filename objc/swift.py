
'''
Classes from the 'swift' framework.
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
    
    
Swift.__stdlib_AtomicInt = _Class('Swift.__stdlib_AtomicInt')
Swift.__stdlib_ReturnAutoreleasedDummy = _Class('Swift.__stdlib_ReturnAutoreleasedDummy')
CoreMedia.BoxedError = _Class('CoreMedia.BoxedError')
Dispatch._DispatchWorkItem = _Class('Dispatch._DispatchWorkItem')
Foundation.__NSErrorRecoveryAttempter = _Class('Foundation.__NSErrorRecoveryAttempter')
Foundation._PropertyListDecoder = _Class('Foundation._PropertyListDecoder')
Foundation._PropertyListEncoder = _Class('Foundation._PropertyListEncoder')
Swift._KeyedEncodingContainerBase = _Class('Swift._KeyedEncodingContainerBase')
Foundation.__JSONEncoder = _Class('Foundation.__JSONEncoder')
Swift.__BridgingBufferStorage = _Class('Swift.__BridgingBufferStorage')
Swift._AnyKeyPath = _Class('Swift._AnyKeyPath')
Swift._KeyedDecodingContainerBase = _Class('Swift._KeyedDecodingContainerBase')
Foundation.__JSONDecoder = _Class('Foundation.__JSONDecoder')
Swift.__BridgingHashBuffer = _Class('Swift.__BridgingHashBuffer')
Swift._StringBreadcrumbs = _Class('Swift._StringBreadcrumbs')
Foundation.__DataStorage = _Class('Foundation.__DataStorage')
Swift.__VaListBuilder = _Class('Swift.__VaListBuilder')
Swift.__SwiftNativeNSEnumerator = _Class('Swift.__SwiftNativeNSEnumerator')
Swift.__SwiftEmptyNSEnumerator = _Class('Swift.__SwiftEmptyNSEnumerator')
Swift.__SwiftNativeNSString = _Class('Swift.__SwiftNativeNSString')
Swift.__SharedStringStorage = _Class('Swift.__SharedStringStorage')
Swift.__StringStorage = _Class('Swift.__StringStorage')
Swift.__SwiftNativeNSSet = _Class('Swift.__SwiftNativeNSSet')
Swift.__RawSetStorage = _Class('Swift.__RawSetStorage')
Swift.__EmptySetSingleton = _Class('Swift.__EmptySetSingleton')
Swift.__SwiftNativeNSDictionary = _Class('Swift.__SwiftNativeNSDictionary')
Swift.__RawDictionaryStorage = _Class('Swift.__RawDictionaryStorage')
Swift.__EmptyDictionarySingleton = _Class('Swift.__EmptyDictionarySingleton')
Foundation.__NSSwiftData = _Class('Foundation.__NSSwiftData')
Swift.__SwiftNativeNSArray = _Class('Swift.__SwiftNativeNSArray')
Swift.__SwiftNativeNSArrayWithContiguousStorage = _Class('Swift.__SwiftNativeNSArrayWithContiguousStorage')
Swift.__SwiftDeferredNSArray = _Class('Swift.__SwiftDeferredNSArray')
Swift.__ContiguousArrayStorageBase = _Class('Swift.__ContiguousArrayStorageBase')
Swift.__EmptyArrayStorage = _Class('Swift.__EmptyArrayStorage')
Swift._SwiftNativeNSMutableArray = _Class('Swift._SwiftNativeNSMutableArray')
Swift._SwiftNSMutableArray = _Class('Swift._SwiftNSMutableArray')