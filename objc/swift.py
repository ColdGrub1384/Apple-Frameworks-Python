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

    
_TtCs12_SwiftObject = _Class('_TtCs12_SwiftObject')
_TtCE8CoreMIDIVSo14MIDIPacketList7Builder = _Class('_TtCE8CoreMIDIVSo14MIDIPacketList7Builder')
_TtCE8CoreMIDIVSo10MIDIPacket7Builder = _Class('_TtCE8CoreMIDIVSo10MIDIPacket7Builder')
_TtCE8CoreMIDIVSo13MIDIEventList7Builder = _Class('_TtCE8CoreMIDIVSo13MIDIEventList7Builder')
_TtCE8CoreMIDIVSo15MIDIEventPacket7Builder = _Class('_TtCE8CoreMIDIVSo15MIDIEventPacket7Builder')
__stdlib_AtomicInt = _Class('Swift.__stdlib_AtomicInt')
_TtCVVs10__CocoaSet5Index7Storage = _Class('_TtCVVs10__CocoaSet5Index7Storage')
__stdlib_ReturnAutoreleasedDummy = _Class('Swift.__stdlib_ReturnAutoreleasedDummy')
_TtCVs17__CocoaDictionary8Iterator = _Class('_TtCVs17__CocoaDictionary8Iterator')
_TtCVVs17__CocoaDictionary5Index7Storage = _Class('_TtCVVs17__CocoaDictionary5Index7Storage')
_TtCV9CoreAudio25ManagedAudioChannelLayoutP33_429D68E17F2C221C283DB52CAE70232C7Storage = _Class('_TtCV9CoreAudio25ManagedAudioChannelLayoutP33_429D68E17F2C221C283DB52CAE70232C7Storage')
_TtCVE9CoreMediaaSo22CMFormatDescriptionRef22ParameterSetCollectionP33_B5107634416AF8266ECF5CD01992F6B819CachedParameterSets = _Class('_TtCVE9CoreMediaaSo22CMFormatDescriptionRef22ParameterSetCollectionP33_B5107634416AF8266ECF5CD01992F6B819CachedParameterSets')
BoxedError = _Class('CoreMedia.BoxedError')
_DispatchWorkItem = _Class('Dispatch._DispatchWorkItem')
__NSErrorRecoveryAttempter = _Class('Foundation.__NSErrorRecoveryAttempter')
_TtCCE10FoundationCSo16NSOperationQueueP33_0ECEE0A75E2DD5EDFED9A6FEB26D5D3219DelayReadyOperation19CancellationContext = _Class('_TtCCE10FoundationCSo16NSOperationQueueP33_0ECEE0A75E2DD5EDFED9A6FEB26D5D3219DelayReadyOperation19CancellationContext')
_TtCV10Foundation4Data14RangeReference = _Class('_TtCV10Foundation4Data14RangeReference')
_TtC10FoundationP33_5692656F4C05BA2A580AE9322E9FB0A614__PlistDecoder = _Class('_TtC10FoundationP33_5692656F4C05BA2A580AE9322E9FB0A614__PlistDecoder')
_PropertyListDecoder = _Class('Foundation._PropertyListDecoder')
_TtC10FoundationP33_5692656F4C05BA2A580AE9322E9FB0A614__PlistEncoder = _Class('_TtC10FoundationP33_5692656F4C05BA2A580AE9322E9FB0A614__PlistEncoder')
_TtC10FoundationP33_5692656F4C05BA2A580AE9322E9FB0A625__PlistReferencingEncoder = _Class('_TtC10FoundationP33_5692656F4C05BA2A580AE9322E9FB0A625__PlistReferencingEncoder')
_PropertyListEncoder = _Class('Foundation._PropertyListEncoder')
_TtCE10FoundationCSo7NSTimer14TimerPublisher = _Class('_TtCE10FoundationCSo7NSTimer14TimerPublisher')
_TtCE10FoundationCSo12NSDictionary9_Iterator = _Class('_TtCE10FoundationCSo12NSDictionary9_Iterator')
_TtCV5UIKit35UICollectionLayoutListConfiguration12_ImplWrapper = _Class('_TtCV5UIKit35UICollectionLayoutListConfiguration12_ImplWrapper')
_TtCV5UIKit25UIBackgroundConfiguration12_ImplWrapper = _Class('_TtCV5UIKit25UIBackgroundConfiguration12_ImplWrapper')
_TtCV5UIKit26UIListContentConfiguration12_ImplWrapper = _Class('_TtCV5UIKit26UIListContentConfiguration12_ImplWrapper')
_TtCVV5UIKit26UIListContentConfiguration14TextProperties12_ImplWrapper = _Class('_TtCVV5UIKit26UIListContentConfiguration14TextProperties12_ImplWrapper')
_TtCVV5UIKit26UIListContentConfiguration15ImageProperties12_ImplWrapper = _Class('_TtCVV5UIKit26UIListContentConfiguration15ImageProperties12_ImplWrapper')
_TtCO10Accelerate4vDSP3DCT = _Class('_TtCO10Accelerate4vDSP3DCT')
_TtCO10Accelerate4BNNS5Layer = _Class('_TtCO10Accelerate4BNNS5Layer')
_TtCO10Accelerate4BNNS9LossLayer = _Class('_TtCO10Accelerate4BNNS9LossLayer')
_TtCO10Accelerate4BNNS21BinaryArithmeticLayer = _Class('_TtCO10Accelerate4BNNS21BinaryArithmeticLayer')
_TtCO10Accelerate4BNNS20UnaryArithmeticLayer = _Class('_TtCO10Accelerate4BNNS20UnaryArithmeticLayer')
_TtCO10Accelerate4BNNS18NormalizationLayer = _Class('_TtCO10Accelerate4BNNS18NormalizationLayer')
_TtCO10Accelerate4BNNS11BinaryLayer = _Class('_TtCO10Accelerate4BNNS11BinaryLayer')
_TtCO10Accelerate4BNNS28BroadcastMatrixMultiplyLayer = _Class('_TtCO10Accelerate4BNNS28BroadcastMatrixMultiplyLayer')
_TtCO10Accelerate4BNNS10FusedLayer = _Class('_TtCO10Accelerate4BNNS10FusedLayer')
_TtCO10Accelerate4BNNS37FusedFullyConnectedNormalizationLayer = _Class('_TtCO10Accelerate4BNNS37FusedFullyConnectedNormalizationLayer')
_TtCO10Accelerate4BNNS34FusedConvolutionNormalizationLayer = _Class('_TtCO10Accelerate4BNNS34FusedConvolutionNormalizationLayer')
_TtCO10Accelerate4BNNS12PoolingLayer = _Class('_TtCO10Accelerate4BNNS12PoolingLayer')
_TtCO10Accelerate4BNNS10UnaryLayer = _Class('_TtCO10Accelerate4BNNS10UnaryLayer')
_TtCO10Accelerate4BNNS12PaddingLayer = _Class('_TtCO10Accelerate4BNNS12PaddingLayer')
_TtCO10Accelerate4BNNS11ResizeLayer = _Class('_TtCO10Accelerate4BNNS11ResizeLayer')
_TtCO10Accelerate4BNNS12DropoutLayer = _Class('_TtCO10Accelerate4BNNS12DropoutLayer')
_TtCO10Accelerate4BNNS14ReductionLayer = _Class('_TtCO10Accelerate4BNNS14ReductionLayer')
_TtCO10Accelerate4BNNS9GramLayer = _Class('_TtCO10Accelerate4BNNS9GramLayer')
_TtCO10Accelerate4BNNS12PermuteLayer = _Class('_TtCO10Accelerate4BNNS12PermuteLayer')
_TtCO10Accelerate4BNNS16ConvolutionLayer = _Class('_TtCO10Accelerate4BNNS16ConvolutionLayer')
_TtCO10Accelerate4BNNS19FullyConnectedLayer = _Class('_TtCO10Accelerate4BNNS19FullyConnectedLayer')
_TtCO10Accelerate4BNNS15ActivationLayer = _Class('_TtCO10Accelerate4BNNS15ActivationLayer')
_KeyedEncodingContainerBase = _Class('Swift._KeyedEncodingContainerBase')
_TtC10FoundationP33_12768CA107A31EF2DCE034FD75B541C913__JSONEncoder = _Class('_TtC10FoundationP33_12768CA107A31EF2DCE034FD75B541C913__JSONEncoder')
_TtC10FoundationP33_12768CA107A31EF2DCE034FD75B541C924__JSONReferencingEncoder = _Class('_TtC10FoundationP33_12768CA107A31EF2DCE034FD75B541C924__JSONReferencingEncoder')
__JSONEncoder = _Class('Foundation.__JSONEncoder')
_TtCVs10__CocoaSet8Iterator = _Class('_TtCVs10__CocoaSet8Iterator')
__BridgingBufferStorage = _Class('Swift.__BridgingBufferStorage')
_TtC10FoundationP33_45BFD3D387700B862E3A7353B97EF7ED21__CharacterSetStorage = _Class('_TtC10FoundationP33_45BFD3D387700B862E3A7353B97EF7ED21__CharacterSetStorage')
_AnyKeyPath = _Class('Swift._AnyKeyPath')
_KeyedDecodingContainerBase = _Class('Swift._KeyedDecodingContainerBase')
_TtC10FoundationP33_12768CA107A31EF2DCE034FD75B541C913__JSONDecoder = _Class('_TtC10FoundationP33_12768CA107A31EF2DCE034FD75B541C913__JSONDecoder')
__JSONDecoder = _Class('Foundation.__JSONDecoder')
__BridgingHashBuffer = _Class('Swift.__BridgingHashBuffer')
_StringBreadcrumbs = _Class('Swift._StringBreadcrumbs')
__DataStorage = _Class('Foundation.__DataStorage')
__VaListBuilder = _Class('Swift.__VaListBuilder')
_UTSwiftOverlayRuntimeIssuesAssistant = _Class('_UTSwiftOverlayRuntimeIssuesAssistant')
__SwiftNull = _Class('__SwiftNull')
_TtC10FoundationP33_AE6BD10245B422606B9EE93C01570D8F21_CombineRunLoopAction = _Class('_TtC10FoundationP33_AE6BD10245B422606B9EE93C01570D8F21_CombineRunLoopAction')
_TtC10FoundationP33_6DA0945A07226B3278459E9368612FF427__KVOKeyPathBridgeMachinery = _Class('_TtC10FoundationP33_6DA0945A07226B3278459E9368612FF427__KVOKeyPathBridgeMachinery')
_TtC5UIKitP33_B626C8241CE05CD32813912C34F02B2229_UICustomContentConfiguration = _Class('_TtC5UIKitP33_B626C8241CE05CD32813912C34F02B2229_UICustomContentConfiguration')
__SwiftNSErrorLayoutStandin = _Class('__SwiftNSErrorLayoutStandin')
_TtCC10FoundationP33_6DA0945A07226B3278459E9368612FF427__KVOKeyPathBridgeMachinery9BridgeKey = _Class('_TtCC10FoundationP33_6DA0945A07226B3278459E9368612FF427__KVOKeyPathBridgeMachinery9BridgeKey')
_TtCC10Foundation21NSKeyValueObservationP33_6DA0945A07226B3278459E9368612FF46Helper = _Class('_TtCC10Foundation21NSKeyValueObservationP33_6DA0945A07226B3278459E9368612FF46Helper')
_NSKeyValueObservation = _Class('_NSKeyValueObservation')
_TtCE10FoundationCSo16NSOperationQueueP33_0ECEE0A75E2DD5EDFED9A6FEB26D5D3219DelayReadyOperation = _Class('_TtCE10FoundationCSo16NSOperationQueueP33_0ECEE0A75E2DD5EDFED9A6FEB26D5D3219DelayReadyOperation')
__SwiftValue = _Class('__SwiftValue')
__SwiftNativeNSEnumeratorBase = _Class('__SwiftNativeNSEnumeratorBase')
__SwiftNativeNSEnumerator = _Class('Swift.__SwiftNativeNSEnumerator')
__SwiftEmptyNSEnumerator = _Class('Swift.__SwiftEmptyNSEnumerator')
__SwiftNativeNSError = _Class('__SwiftNativeNSError')
__SwiftNativeNSStringBase = _Class('__SwiftNativeNSStringBase')
__SwiftNativeNSString = _Class('Swift.__SwiftNativeNSString')
__SharedStringStorage = _Class('Swift.__SharedStringStorage')
__StringStorage = _Class('Swift.__StringStorage')
__SwiftNativeNSSetBase = _Class('__SwiftNativeNSSetBase')
__SwiftNativeNSSet = _Class('Swift.__SwiftNativeNSSet')
__RawSetStorage = _Class('Swift.__RawSetStorage')
__EmptySetSingleton = _Class('Swift.__EmptySetSingleton')
_TtC5UIKitP33_B626C8241CE05CD32813912C34F02B2220_UICustomContentView = _Class('_TtC5UIKitP33_B626C8241CE05CD32813912C34F02B2220_UICustomContentView')
__SwiftNativeNSDictionaryBase = _Class('__SwiftNativeNSDictionaryBase')
__SwiftNativeNSDictionary = _Class('Swift.__SwiftNativeNSDictionary')
__RawDictionaryStorage = _Class('Swift.__RawDictionaryStorage')
__EmptyDictionarySingleton = _Class('Swift.__EmptyDictionarySingleton')
__NSSwiftData = _Class('Foundation.__NSSwiftData')
__SwiftNativeNSArrayBase = _Class('__SwiftNativeNSArrayBase')
__SwiftNativeNSArray = _Class('Swift.__SwiftNativeNSArray')
__SwiftNativeNSArrayWithContiguousStorage = _Class('Swift.__SwiftNativeNSArrayWithContiguousStorage')
__SwiftDeferredNSArray = _Class('Swift.__SwiftDeferredNSArray')
__ContiguousArrayStorageBase = _Class('Swift.__ContiguousArrayStorageBase')
__EmptyArrayStorage = _Class('Swift.__EmptyArrayStorage')
__SwiftNativeNSMutableArrayBase = _Class('__SwiftNativeNSMutableArrayBase')
_SwiftNativeNSMutableArray = _Class('Swift._SwiftNativeNSMutableArray')
_SwiftNSMutableArray = _Class('Swift._SwiftNSMutableArray')
