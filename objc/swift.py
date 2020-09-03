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

    
__stdlib_AtomicInt = _Class('Swift.__stdlib_AtomicInt')
__stdlib_ReturnAutoreleasedDummy = _Class('Swift.__stdlib_ReturnAutoreleasedDummy')
BoxedError = _Class('CoreMedia.BoxedError')
_DispatchWorkItem = _Class('Dispatch._DispatchWorkItem')
__NSErrorRecoveryAttempter = _Class('Foundation.__NSErrorRecoveryAttempter')
_PropertyListDecoder = _Class('Foundation._PropertyListDecoder')
_PropertyListEncoder = _Class('Foundation._PropertyListEncoder')
_KeyedEncodingContainerBase = _Class('Swift._KeyedEncodingContainerBase')
__JSONEncoder = _Class('Foundation.__JSONEncoder')
__BridgingBufferStorage = _Class('Swift.__BridgingBufferStorage')
_KeyedDecodingContainerBase = _Class('Swift._KeyedDecodingContainerBase')
__JSONDecoder = _Class('Foundation.__JSONDecoder')
_AnyKeyPath = _Class('Swift._AnyKeyPath')
__BridgingHashBuffer = _Class('Swift.__BridgingHashBuffer')
_StringBreadcrumbs = _Class('Swift._StringBreadcrumbs')
__DataStorage = _Class('Foundation.__DataStorage')
__VaListBuilder = _Class('Swift.__VaListBuilder')
__SwiftNativeNSEnumerator = _Class('Swift.__SwiftNativeNSEnumerator')
__SwiftEmptyNSEnumerator = _Class('Swift.__SwiftEmptyNSEnumerator')
__SwiftNativeNSString = _Class('Swift.__SwiftNativeNSString')
__SharedStringStorage = _Class('Swift.__SharedStringStorage')
__StringStorage = _Class('Swift.__StringStorage')
__SwiftNativeNSSet = _Class('Swift.__SwiftNativeNSSet')
__RawSetStorage = _Class('Swift.__RawSetStorage')
__EmptySetSingleton = _Class('Swift.__EmptySetSingleton')
__SwiftNativeNSDictionary = _Class('Swift.__SwiftNativeNSDictionary')
__RawDictionaryStorage = _Class('Swift.__RawDictionaryStorage')
__EmptyDictionarySingleton = _Class('Swift.__EmptyDictionarySingleton')
__NSSwiftData = _Class('Foundation.__NSSwiftData')
__SwiftNativeNSArray = _Class('Swift.__SwiftNativeNSArray')
__SwiftNativeNSArrayWithContiguousStorage = _Class('Swift.__SwiftNativeNSArrayWithContiguousStorage')
__SwiftDeferredNSArray = _Class('Swift.__SwiftDeferredNSArray')
__ContiguousArrayStorageBase = _Class('Swift.__ContiguousArrayStorageBase')
__EmptyArrayStorage = _Class('Swift.__EmptyArrayStorage')
_SwiftNativeNSMutableArray = _Class('Swift._SwiftNativeNSMutableArray')
_SwiftNSMutableArray = _Class('Swift._SwiftNSMutableArray')
